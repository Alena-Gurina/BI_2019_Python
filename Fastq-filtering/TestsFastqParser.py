import unittest

from FastqFiltrator.Parse_fastq import gc_bounds
from FastqFiltrator.Parse_fastq import min_len
from FastqFiltrator.Parse_fastq import checking_parametrs
from FastqFiltrator.Parse_fastq import valid_seq
from FastqFiltrator.Parse_fastq import croping
from FastqFiltrator.Parse_fastq import headcroping
from FastqFiltrator.Parse_fastq import leading_fun
from FastqFiltrator.Parse_fastq import trailing_fun
from FastqFiltrator.Parse_fastq import sliding_window_fun
from FastqFiltrator.Parse_fastq import cutting_sequence


class TestParseFastq(unittest.TestCase):

    def setUp(self):
        self.seq_1 = "AAGGGCTCTGGGGGG"
        self.seq_2 = "AGTC"
        self.seq_3 = 'A'
        self.quality_good = "STS9HJJKL56**+,"
        self.quality_bad_some_nucl = "$TS9HJJKL56**+&"
        self.quality_bad__some_nucl2 = "$%S9HJJKL56**+&"
        self.quality_all_bad = "%'(*(&&%%%$$##'"
        self.quality_bad_slice = "$TS9HJJKL56&&&/"

    def test_empty_string(self):
        self.assertRaises(ValueError, valid_seq, '')

    def test_not_valid_nucl(self):
        self.assertRaises(ValueError, valid_seq, 'AGCU')

    def test_normal_seq(self):
        self.assertTrue(valid_seq(self.seq_1))

    def test_not_cutting_good_read(self):
        self.assertEqual(cutting_sequence(self.seq_1, self.quality_good, 0, 35, 35, [4, 35], 1000),
                         (self.seq_1, self.quality_good))

    def test_head_croping(self):
        self.assertEqual(headcroping(self.seq_1, self.quality_good, 2), (self.seq_1[2:], self.quality_good[2:]))

    def test_large_head_croping(self):
        self.assertFalse(headcroping(self.seq_1, self.quality_good, 15))

    def test_crop_crop_less_len(self):
        self.assertEqual(croping(self.seq_1, self.quality_good, 10), (self.seq_1[:10], self.quality_good[:10]))

    def test_crop_crop_more_than_len(self):
        self.assertEqual(croping(self.seq_1, self.quality_good, 20), (self.seq_1, self.quality_good))

    def test_leading_not_cut(self):
        self.assertEqual(leading_fun(self.seq_1, self.quality_good, 30), (self.seq_1, self.quality_good))

    def test_leading_cut_one(self):
        self.assertEqual(leading_fun(self.seq_1, self.quality_bad_some_nucl, 40),
                         (self.seq_1[1:], self.quality_bad_some_nucl[1:]))

    def test_leading_cut_several(self):
        self.assertEqual(leading_fun(self.seq_1, self.quality_bad__some_nucl2, 40),
                         (self.seq_1[2:], self.quality_bad__some_nucl2[2:]))

    def test_leading_cut_all(self):
        self.assertFalse(leading_fun(self.seq_1, self.quality_all_bad, 45))

    def test_trailing_not_cut(self):
        self.assertEqual(trailing_fun(self.seq_1, self.quality_good, 30), (self.seq_1, self.quality_good))

    def test_trailing_cut_one(self):
        self.assertEqual(trailing_fun(self.seq_1, self.quality_bad_some_nucl, 40),
                         (self.seq_1[:-1], self.quality_bad_some_nucl[:-1]))

    def test_trailing_cut_several(self):
        self.assertEqual(trailing_fun(self.seq_1, self.quality_all_bad, 40),
                         (self.seq_1[:len(self.seq_1)-10], self.quality_all_bad[:len(self.quality_all_bad)-10]))

    def test_trailing_cut_all(self):
        self.assertFalse(trailing_fun(self.seq_1, self.quality_all_bad, 45))

    def test_sliding_window_not_cut(self):
        self.assertEqual(sliding_window_fun(self.seq_1, self.quality_good, [4, 40]),
                         (self.seq_1, self.quality_good))

    def test_sliding_window_not_cut_bad_last_nucl(self):
        self.assertEqual(sliding_window_fun(self.seq_1, self.quality_bad_some_nucl, [4, 40]),
                         (self.seq_1, self.quality_bad_some_nucl))

    def test_sliding_window_cut_one_window(self):
        self.assertEqual(sliding_window_fun(self.seq_1, self.quality_bad_slice, [4, 40]),
                         (self.seq_1[:len(self.seq_1)-4], self.quality_bad_slice[:len(self.quality_bad_slice)-4]))

    def test_slid_cutting_all(self):
        self.assertFalse(sliding_window_fun(self.seq_1, self.quality_all_bad, [4,40]))

    def test_cutting_start(self):
        self.assertEqual(cutting_sequence(self.seq_1, self.quality_bad_some_nucl, 0, 40, 35, [4, 40], 1000),
                         (self.seq_1[1:], self.quality_bad_some_nucl[1:]))

    def test_cutting_end(self):
        self.assertEqual(cutting_sequence(self.seq_1, self.quality_bad_some_nucl, 0, 35, 40, [4, 40], 1000),
                         (self.seq_1[:-1], self.quality_bad_some_nucl[:-1]))

    def test_cutting_start_and_end(self):
        self.assertEqual(cutting_sequence(self.seq_1, self.quality_bad_some_nucl, 0, 40, 40, [4, 40], 1000),
                         (self.seq_1[1:-1], self.quality_bad_some_nucl[1:-1]))

    def test_cutting_slise(self):
        self.assertEqual(cutting_sequence(self.seq_1, self.quality_bad_slice, 0, 30, 40, [4, 40], 1000),
                         (self.seq_1[:len(self.seq_1)-4], self.quality_bad_slice[:len(self.quality_bad_slice)-4]))

    def test_cutting_all_by_leading(self):
        self.assertFalse(cutting_sequence(self.seq_1, self.quality_all_bad, 0, 45, 45, [4, 40], 1000))

    def test_cutting_all_by_slid_window(self):
        self.assertFalse(cutting_sequence(self.seq_1, self.quality_all_bad, 0, 0,0,[4,40], 1000))

    def test_crop_after_cutting(self):
        self.assertEqual(cutting_sequence(self.seq_1, self.quality_good, 0, 40, 40, [4, 40], 10),
                         (self.seq_1[:10], self.quality_good[:10]))

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
