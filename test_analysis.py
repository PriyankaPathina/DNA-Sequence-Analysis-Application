import unittest
from main import (
    calculate_gc_content,
    calculate_nucleotide_frequencies,
    search_motif
)


class TestDNAAnalysis(unittest.TestCase):

    def test_gc_content(self):
        sequence = "GGCCAA"
        self.assertEqual(calculate_gc_content(sequence), 66.67)

    def test_nucleotide_frequencies(self):
        sequence = "AATTGGCC"
        expected = {"A": 2, "T": 2, "G": 2, "C": 2}
        self.assertEqual(calculate_nucleotide_frequencies(sequence), expected)

    def test_search_motif(self):
        sequence = "TATATATA"
        motif = "TATA"
        expected_positions = [1, 3, 5]
        self.assertEqual(search_motif(sequence, motif), expected_positions)


if __name__ == "__main__":
    unittest.main()