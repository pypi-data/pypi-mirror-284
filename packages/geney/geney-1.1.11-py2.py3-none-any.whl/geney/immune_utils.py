import subprocess
import logging
import tempfile
from geney import config_setup
import pandas as pd


class NetChop(object):
    """
    Wrapper around netChop tool. Assumes netChop is in your PATH.
    """
    def predict_epitopes(self, sequences, threshold=0.5, min_len=8):
        """
        Return netChop predictions for each position in each sequence.

        Parameters
        -----------
        sequences : list of string
            Amino acid sequences to predict cleavage for

        Returns
        -----------
        list of list of float

        The i'th list corresponds to the i'th sequence. Each list gives
        the cleavage probability for each position in the sequence.
        """
        with tempfile.NamedTemporaryFile(dir=config_setup['NETCHOP'], suffix=".fsa", mode="w") as input_fd:
            for (i, sequence) in enumerate(sequences):
                _ = input_fd.write("> %d\n" % i)
                _ = input_fd.write(sequence)
                _ = input_fd.write("\n")
            input_fd.flush()
            try:
                output = subprocess.check_output(["netchop", str(input_fd.name)])
            except subprocess.CalledProcessError as e:
                logging.error("Error calling netChop: %s:\n%s" % (e, e.output))
                raise
        parsed = self.parse_netchop(output)
        return parsed
        #
        # assert len(parsed) == len(sequences), \
        #     "Expected %d results but got %d" % (
        #         len(sequences), len(parsed))
        # assert [len(x) for x in parsed] == [len(x) for x in sequences]
        # filtered_proteosomes = []
        # for scores, seq in list(zip(parsed, sequences)):
        #     proteosome = self.chop_protein(seq, [s > threshold for s in scores])
        #     filtered_proteosomes.append([e for e in proteosome if len(e) > min_len])
        # return filtered_proteosomes
    @staticmethod
    def parse_netchop(netchop_output):
        """
        Parse netChop stdout.
        """
        line_iterator = iter(netchop_output.decode().split("\n"))
        scores = []
        for line in line_iterator:
            if "pos" in line and 'AA' in line and 'score' in line:
                scores.append([])
                if "----" not in next(line_iterator):
                    raise ValueError("Dashes expected")
                line = next(line_iterator)
                while '-------' not in line:
                    score = float(line.split()[3])
                    scores[-1].append(score)
                    line = next(line_iterator)
        return scores
    def chop_protein(self, seq, pos):
        # Generate subsequences using list comprehension and slicing
        start = 0
        subsequences = [seq[start:(start := i+1)] for i, marker in enumerate(pos) if marker == 1]
        # Check if the last part needs to be added
        if start < len(seq):
            subsequences.append(seq[start:])
        return subsequences
    def generate_cut_sequences(self, char_sequence, cut_probabilities):
        """
        Generate all possible cut sequences and their abundance values,
        considering only those sequences where the probabilities of all cut sites
        between the two ends are zero.

        :param char_sequence: A string representing the sequence of characters.
        :param cut_probabilities: A list of probabilities for each position in the sequence.
        :return: A list of tuples, where each tuple contains a cut sequence and its abundance value.
        """
        if len(char_sequence) != len(cut_probabilities):
            raise ValueError("Character sequence and cut probabilities must have the same length.")
        cut_sequences = []
        # Generate all possible cuts
        for i in range(len(char_sequence)):
            for j in range(i + 1, len(char_sequence) + 1):
                # Check if probabilities of all cut sites between i and j are zero
                if sum(cut_probabilities[i + 1:j - 1]) < 1:
                    cut_sequence = char_sequence[i:j]
                    abundance_value = cut_probabilities[i] * cut_probabilities[j - 1] - sum(
                        cut_probabilities[i + 1:j - 1])
                    cut_sequences.append({'seq': cut_sequence, 'abundance': abundance_value})
        return pd.DataFrame(cut_sequences)




from .base_commandline_predictor import BaseCommandlinePredictor
from .parsing import parse_netmhc41_stdout
from functools import partial


class NetMHCpan41(BaseCommandlinePredictor):
    def __init__(
            self,
            alleles,
            default_peptide_lengths=[9],
            program_name="netMHCpan",
            process_limit=-1,
            mode="binding_affinity",
            extra_flags=[]):
        """
        Wrapper for NetMHCpan4.1.

        The mode argument should be one of "binding_affinity" (default) or
        "elution_score".
        """

        # The -BA flag is required to predict binding affinity
        if mode == "binding_affinity":
            flags = ["-BA"]
        elif mode == "elution_score":
            flags = []
        else:
            raise ValueError("Unsupported mode", mode)

        BaseCommandlinePredictor.__init__(
            self,
            program_name=program_name,
            alleles=alleles,
            default_peptide_lengths=default_peptide_lengths,
            parse_output_fn=partial(parse_netmhc41_stdout, mode=mode),
            supported_alleles_flag="-listMHC",
            input_file_flag="-f",
            length_flag="-l",
            allele_flag="-a",
            extra_flags=flags + extra_flags,
            process_limit=process_limit)

class NetMHCpan41_EL(NetMHCpan41):
    """
    Wrapper for NetMHCpan4 when the preferred mode is elution score
    """
    def __init__(
            self,
            alleles,
            default_peptide_lengths=[9],
            program_name="netMHCpan",
            process_limit=-1,
            extra_flags=[]):
        NetMHCpan41.__init__(
            self,
            alleles=alleles,
            default_peptide_lengths=default_peptide_lengths,
            program_name=program_name,
            process_limit=process_limit,
            mode="elution_score",
            extra_flags=extra_flags)


class NetMHCpan41_BA(NetMHCpan41):
    """
    Wrapper for NetMHCpan4 when the preferred mode is binding affinity
    """
    def __init__(
            self,
            alleles,
            default_peptide_lengths=[9],
            program_name="netMHCpan",
            process_limit=-1,
            extra_flags=[]):
        NetMHCpan41.__init__(
            self,
            alleles=alleles,
            default_peptide_lengths=default_peptide_lengths,
            program_name=program_name,
            process_limit=process_limit,
            mode="binding_affinity",
            extra_flags=extra_flags)