def bed_sorting(file, output_file, save_header=False):
    chromosome_set = set()
    with open(file, 'r') as input:
        for line in input:
            if line.lstrip().startswith('#') or line.lstrip().startswith('track'):
                if save_header:
                    with open(output_file, 'a') as output:
                        output.write(line)
            else:
                # find all unique chromosomes names for sorting them separately
                chromosome_set.add(line.lstrip()[:line.find('\t')])

    chr_list = sorted(list(chromosome_set))
    # sort chromosomes names

    for chromosome in chr_list:
        bed_part = list()
        with open(file, 'r') as input:
            for line in input:
                if line.lstrip().startswith('#') or line.lstrip().startswith('track'):
                    pass
                else:
                    if line.lstrip()[:line.find('\t')] == chromosome:
                        # read and save all intervals from one chromosome
                        bed_part.append(line.rstrip().split('\t'))
        bed_part.sort(key=lambda i: (i[1], i[2]))
        # sort intervals using first start and then finish of interval

        with open(output_file, 'a') as output:
            # write sorted intervals from one chromosome in file
            for el in bed_part:
                output.write('\t'.join(el) + '\n')

    return


if __name__ == '__main__':
    file = "../BI_2019_Python/bed_copy/lamina.bed"
    output_file = "../BI_2019_Python/bed_copy/tmp_output.bed"
    bed_sorting(file, output_file)
