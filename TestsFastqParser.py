import unittest

from Parse_fastq import gc_bounds
from Parse_fastq import min_len
from Parse_fastq import checking_parametrs
from Parse_fastq import valid_seq


class TestParseFastq(unittest.TestCase):

    def setUp(self):
        self.seq_1 = "AAGGGCTCTGGGGGG"
        self.seq_2 = "AGTC"
        self.seq_3 = 'A'

    def test_empty_string(self):
        self.assertRaises(ValueError, valid_seq, '')

    def test_not_valid_nucl(self):
        self.assertRaises(ValueError, valid_seq, 'AGCU')

    def test_normal_seq(self):
        self.assertTrue(valid_seq(self.seq_1))

    def test_gc_content_more_low_bounds(self):
        self.assertTrue(gc_bounds(self.seq_1, [50]))  # check gc more low bound

    def test_gc_content_not_between_bounds(self):
        self.assertFalse(gc_bounds(self.seq_1, [20, 50]))  # check gc is not between bounds

    def test_gc_content_less_low_bounds(self):
        self.assertFalse(gc_bounds(self.seq_2, [70]))  # check gc is less then low bound

    def test_gc_content_default(self):
        self.assertTrue(gc_bounds(self.seq_3, [0, 100]))  # check default parameters

    def test_min_length_more(self):
        self.assertTrue(min_len(self.seq_1, 10))  # check min length more bounds

    def test_min_length_less(self):
        self.assertFalse(min_len(self.seq_2, 10))  # check min length less bounds

    def test_checking_parameters_all_good(self):
        self.assertTrue(checking_parametrs(self.seq_1, [50], 10))  # all filtered passed

    def test_checking_parameters_gc_failed(self):
        self.assertFalse(checking_parametrs(self.seq_1, [20, 50], 10), False)  # failed gc_bounds filter

    def test_checking_parameters_len_failed(self):
        self.assertFalse(checking_parametrs(self.seq_2, [20, 50], 10), False)  # failed min_length filter

    def test_checking_parameters_all_failed(self):
        self.assertFalse(checking_parametrs(self.seq_2, [50], 10), False)  # failed both filters


if __name__ == "__main__":
    unittest.main()
