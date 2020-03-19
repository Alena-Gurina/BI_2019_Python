def valid_seq(seq):
    if len(seq) == 0:
        raise ValueError  # zero-length of sequence
    valid_bases = ("A", "T", "G", "C", "N")
    for base in seq:
        if base not in valid_bases:
            raise ValueError  # not-valid nucleotide
    return True


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


def checking_parametrs(seq, bounds, minimal_len):
    if gc_bounds(seq, bounds) and min_len(seq, minimal_len):
        result = True
    else:
        result = False
    return result


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Fastq filtering")
    parser.add_argument('--min_length', help="minimal length of read",
                        dest="min_length", type=int, action="store", default=1)
    parser.add_argument('--keep_filtered', help="save reads that don`t throw out filter into file",
                        action="store_true", default=False)
    parser.add_argument('--gc_bounds', nargs='*', action="store", default=[0, 100], dest="gc_bounds",
                        help="bounds for GC persentage, 1st arg - lower bound, 2nd (optional) - upper bound",
                        type=int)
    parser.add_argument('--otput_base_name', help="common name`s start for output files",
                        action="store", dest='output_base_name')
    parser.add_argument("file", help="fastq file")

    args = parser.parse_args()


    def writing_results(name_s, seq, chain, quality):
        if valid_seq(seq):
            if args.output_base_name:
                output_name = args.output_base_name
            else:
                output_name = '.'.join(args.file.split('.')[0:-1])
            if checking_parametrs(seq, args.gc_bounds, args.min_length):
                output_name = output_name + "_good_reads.fastq"
                with open(output_name, 'a') as output:
                    output.write(name_s + '\r\n')
                    output.write(seq + '\r\n')
                    output.write(chain + '\r\n')
                    output.write(quality + '\r\n')
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
