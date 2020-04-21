def bed_merge(file1, output_file, max_gap_del_size=0):
    with open(file1, 'r') as input:
        line_a = list(input.readline().rstrip().split('\t'))
        while line_a[0].startswith('#') or line_a[0].startswith('track'):
            with open(output_file, 'a') as output:
                output.write('\n'.join(line_a) + '\n')
            line_a = list(input.readline().rstrip().split('\t'))
        line_b = list(input.readline().rstrip().split('\t'))
        counts = 1
        while line_a and line_b:
            if line_a[0] != line_b[0]:
                # check that lines from one chromosome
                with open(output_file, 'a') as output:
                    output.write('\t'.join(line_a[0:3]) + '\t' + str(counts) + '\n')
                counts = 1
                line_a = line_b
                line_b = list(input.readline().rstrip().split('\t'))
                if line_b == ['']:
                    with open(output_file, 'a') as output:
                        output.write('\t'.join(line_a[0:3]) + '\t' + str(counts) + '\n')
                        break
            else:
                if int(line_a[1]) <= int(line_b[1]) <= int(line_a[2]) + max_gap_del_size:
                    counts += 1
                    if int(line_b[2]) <= int(line_a[2]) + max_gap_del_size:
                        line_b = list(input.readline().rstrip().split('\t'))
                        if line_b == ['']:
                            with open(output_file, 'a') as output:
                                output.write('\t'.join(line_a[0:3]) + '\t' + str(counts) + '\n')
                            break
                    # if start of 2nd interval within first interval or with little gap (size set) after it
                    # include 2nd interval into first interval
                    else:
                        line_a[2] = line_b[2]
                        # refresh line_b
                        line_b = list(input.readline().rstrip().split('\t'))
                        if line_b == ['']:
                            with open(output_file, 'a') as output:
                                output.write('\t'.join(line_a[0:3]) + '\t' + str(counts) + '\n')
                            break
                else:
                    # 1st and second interval are not overlapped (and gap between them more set level)
                    # just write 1st interval as it was before
                    with open(output_file, 'a') as output:
                        output.write('\t'.join(line_a[0:3]) + '\t' + str(counts) + '\n')
                    # refresh both intervals
                    line_a = line_b
                    line_b = list(input.readline().rstrip().split('\t'))
                    if line_b == ['']:
                        with open(output_file, 'a') as output:
                            output.write('\t'.join(line_a[0:3]) + '\t' + str(counts) + '\n')
                        break


if __name__ == '__main__':
    file1 = 'bed_file.bed'
    output_file1 = 'merging_test_no_gap.bed'
    output_file2 = 'merging_test_gap2.bed'
    # bed_merge(file1, output_file1)
    bed_merge(file1, output_file2, 3)
