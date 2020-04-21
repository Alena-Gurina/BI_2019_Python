import argparse
import os
from bed_copy import bed_sorting

parser = argparse.ArgumentParser(description="bed_tools_copy")
parser.add_argument('--sort', help='sorted bed file', action='store_true', default=False)
parser.add_argument('--merge', help='merge overlapped intervals', action='store_true',
                    default=False)
parser.add_argument('--gap_merged_size', help='size of gap', default=0, type=int, action='store',
                    dest='gap_size')
parser.add_argument('--subtract', help='subtract from file1 file2', action='store_true',
                    default=False)
parser.add_argument('--intersect', help='intersect file1 and file2', action='store_true',
                    default=False)
parser.add_argument('--intersect_type', action='store', default='only_overlapped', dest='intersect_type',
                    help='only_overlapped, whole_interval or not_intersected, depend of type of intersection')
parser.add_argument('--file_to_compare', help='second file for subtract and intersect functions', action='store',
                    default=None, dest="file2")
parser.add_argument('--output_file_name', action='store', dest='out_f', default='bed_copy_output',
                    help='name of output file')
parser.add_argument('file', help='bed file for parsing')

args = parser.parse_args()
intersect_vars = {'only_overlapped', 'whole_interval', 'not_intersected'}
if args.intersect_type not in intersect_vars:
    raise ValueError('variant value could be only only_overlapped, not_intersected, or whole_interval')

if (args.subtract or args.intersect) and args.file2 == 'None':
    raise FileExistsError('you need write path to file in file_to_compare argument')

if args.sort:

    bed_sorting.bed_sorting(args.file, args.out_f)
else:
    bed_sorting.bed_sorting(args.file, 'tmp_sort')
from bed_copy import bed_merge

if args.merge:
    bed_merge.bed_merge('tmp_sort', args.out_f, args.gap_size)
    os.remove('tmp_sort')

if args.subtract or args.intersect:
    bed_sorting.bed_sorting(args.file2, 'tmp_file2_sorted')
    bed_merge.bed_merge('tmp_sort', 'tmp_merged')
    bed_merge.bed_merge('tmp_file2_sorted', 'tmp_file2_merged')
    if args.subtract:
        from bed_copy import bed_subtract

        bed_subtract.subtract('tmp_merged', 'tmp_file2_merged', args.out_f)
    if args.intersect:
        from bed_copy import bed_intersect

        bed_intersect.intersect('tmp_merged', 'tmp_file2_merged', args.out_f, args.intersect_type)
    os.remove('tmp_sort')
    os.remove('tmp_merged')
    os.remove('tmp_file2_sorted')
    os.remove('tmp_file2_merged')
