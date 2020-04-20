import statistics


def valid_seq(seq):
    if len(seq) == 0:
        raise ValueError  # zero-length of sequence
    valid_bases = ("A", "T", "G", "C", "N", 'a', 'g', 'c', 't')
    for base in seq:
        if base not in valid_bases:
            raise ValueError  # not-valid nucleotide
    return True


def headcroping(seq, quality, hcrop):
    if hcrop >= len(seq) - 1:
        return False
    if hcrop ==0:
        return seq, quality
    new_seq = seq[hcrop:]
    new_quality = quality[hcrop:]
    return new_seq, new_quality


def croping(seq, quality, crop):
    if crop < len(seq):
        new_seq = seq[0:crop]
        new_quality = quality[0:crop]
        return new_seq, new_quality
    else:
        return seq, quality


def leading_fun(seq, quality, leading):
    cutting = 0
    nucleotide_number = 0
    while (ord(quality[nucleotide_number]) < leading) and (cutting < len(seq) - 1):
        cutting += 1
        nucleotide_number += 1
    if cutting == len(seq) - 1:
        return False
    new_seq = seq[cutting:]
    new_quality = quality[cutting:]
    return new_seq, new_quality


def trailing_fun(seq, quality, trailing):
    cutting = 0
    nucleotide_number = -1
    while (ord(quality[nucleotide_number]) < trailing) and (cutting < len(seq) - 1):
        cutting += 1
        nucleotide_number -= 1
    if cutting >= len(seq) - 1:
        return False
    new_seq = seq[0:(len(seq) - cutting)]
    new_quality = quality[0:(len(seq) - cutting)]
    return new_seq, new_quality


import statistics


def sliding_window_fun(seq, quality, sliding_window):
    if sliding_window == [0, 0]:
        return seq, quality
    if len(seq) < sliding_window[0]:
        return False
    avr_q = 0
    window_bounds = [len(quality) - sliding_window[0], len(quality) - 1]
    while window_bounds[0] >= sliding_window[0]:
        avr_q = statistics.mean([ord(quality[i]) for i in range(window_bounds[0], window_bounds[1])])
        if avr_q >= sliding_window[1]:
            new_seq = seq[0:(window_bounds[1] + 1)]
            new_quality = quality[0:(window_bounds[1] + 1)]
            return new_seq, new_quality
        else:
            window_bounds = [window_bounds[0] - sliding_window[0], window_bounds[1] - sliding_window[0]]
            if window_bounds[1] < sliding_window[0]:
                return False
    return False


def gc_bounds(seq, bounds):
    seq.upper()
    gc_content = ((seq.count("G") + seq.count("C")) / len(seq)) * 100
    if len(bounds) == 2:
        if bounds[0] <= gc_content <= bounds[1]:
            return True
        else:
            return False
    else:
        if gc_content >= bounds[0]:
            return True
        else:
            return False


def min_len(seq, minimal_len):
    if len(seq) >= minimal_len:
        return True
    else:
        return False


def cutting_sequence(seq, quality, headcrop, leading, trailing, sliding_window, crop):
    new_data = headcroping(seq, quality, headcrop)
    if new_data:
        new_data = leading_fun(new_data[0], new_data[1], leading)
        if new_data:
            new_data = trailing_fun(new_data[0], new_data[1], trailing)
            if new_data:
                new_data = sliding_window_fun(new_data[0], new_data[1], sliding_window)
                if new_data:
                    new_data = croping(new_data[0], new_data[1], crop)
                    return new_data
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False



def checking_parametrs(seq, bounds, minimal_len):
    if gc_bounds(seq, bounds) and min_len(seq, minimal_len):
        result = True
    else:
        result = False
    return result


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Fastq filtering")
    parser.add_argument('--min_length', help="minimal length of read, if you use different cutting function"
                                             "these parameter checked after all cut have be done",
                        dest="min_length", type=int, action="store", default=1)
    parser.add_argument('--keep_filtered', help="save reads that don`t throw out filter into file",
                        action="store_true", default=False)
    parser.add_argument('--gc_bounds', nargs='*', action="store", default=[0, 100], dest="gc_bounds",
                        help="bounds for GC persentage, 1st arg - lower bound, 2nd (optional) - upper bound,"
                             "if you use different cutting function "
                             "these parameter checked after all cut have be done",
                        type=int)
    parser.add_argument('--output_base_name', help="common name`s start for output files",
                        action="store", dest='output_base_name')
    parser.add_argument('--sliding_window', help="two integers, first - window size,"
                                                 "second - minimum of average quality below which, "
                                                 "all nucleotides in window would be cut",
                        nargs=2, default=[0, 0], type=int, action='store', dest='slid_window')
    parser.add_argument('--LEADING', nargs='?', type=int, default=0, action='store', dest='leading',
                        help="Level of quality, below which we cut nucleotides start, default = 0")
    parser.add_argument('--TRAILING', nargs='?', type=int, default=0, action='store', dest='trailing',
                        help="Level of quality, below which we cut nucleotides from end, default = 0")
    parser.add_argument('--CROP', help='Cut the read to a specified length (cut from the end)', action='store',
                        type=int, default=100000000000, dest='crop')
    parser.add_argument('--HEADCROP', help='Cut the specified number of bases from the start of the read',
                        type=int, default=0, action='store', dest='headcrop')
    parser.add_argument("file", help="fastq file")

    args = parser.parse_args()


    def writing_results(name_s, seq, chain, quality):
        if valid_seq(seq):
            if args.output_base_name:
                output_name = args.output_base_name
            else:
                output_name = '.'.join(args.file.split('.')[0:-1])
            new_data = cutting_sequence(seq, quality, args.headcrop, args.leading,
                                        args.trailing, args.slid_window, args.crop)
            if new_data and checking_parametrs(new_data[0], args.gc_bounds, args.min_length):
                output_name = output_name + "_good_reads.fastq"
                with open(output_name, 'a') as output:
                    output.write(name_s + '\r\n')
                    output.write(new_data[0] + '\r\n')
                    output.write(chain + '\r\n')
                    output.write(new_data[1] + '\r\n')
                return
            else:
                if args.keep_filtered:
                    output_name = output_name + "_bad_reads.fastq"
                    with open(output_name, 'a') as output:
                        output.write(name_s + '\r\n')
                        output.write(seq + '\r\n')
                        output.write(chain + '\r\n')
                        output.write(quality + '\r\n')
                    return


    with open(args.file, "r") as in_f:
        for element in in_f:
            name_s = element.rstrip('\n')  # 1
            seq = next(in_f).rstrip('\n')  # 2
            chain = next(in_f).rstrip('\n')
            quality = next(in_f).rstrip('\n')
            writing_results(name_s, seq, chain, quality)
