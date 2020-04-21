#!!! warnings! work only with sorted files
def subtract_fun(file1, file2, output_file):
    with open(file1, 'r') as input1:
        with open(file2, 'r') as input2:
            for line in input1:
                if line.lstrip().startswith('#') or line.lstrip().startswith('track'):
                    # rewrite header
                    with open(output_file, 'a') as output:
                        output.write(line)
                else:
                    line = list(line.rstrip().split('\t'))
                    for file2_line in input2:
                        file2_line = list(file2_line.rstrip().split('\t'))
                        if line[0] != file2_line[0]:
                            pass
                        else:
                            if (int(file2_line[1]) <= int(line[1])) and (int(file2_line[2]) >= int(line[1])):
                                # is start of interval from first file in interval from second file?
                                if int(file2_line[2]) >= int(line[2]):
                                    # is end of 1st interval in 2nd interval?
                                    line[1] = line[2]
                                else:
                                    line[1] = file2_line[2]
                            if int(file2_line[1]) > int(line[1]):
                                # if start of 2nd interval more then start of 1st interval
                                if int(file2_line[1]) > int(line[2]):
                                    # if start of 2nd interval not in 1st interval
                                    pass
                                else:
                                    # if start of 2nd interval within of 1st interval
                                    if int(file2_line[2]) >= int(line[2]):
                                        # if end of 2nd interval more then end of 1st interval
                                        line[2] = file2_line[1]
                                        # only start of first interval saved
                                    else:
                                        if int(file2_line[2]) < int(line[2]):
                                            # if all 2nd interval within first interval
                                            line_new = line
                                            line_new[2] = file2_line[1]
                                            # first write start of interval
                                            # (as files sorted none of intervals from 2nd file overlapped it)
                                            with open(output_file, 'a') as output:
                                                output.write('\t'.join(line_new) + '\n')
                                            # rewrite 1st interval as it`s end
                                            line[1] = file2_line[2]
                    if int(line[2]) - int(line[1]) <= 0:
                        # if all interval was overlapped
                        pass
                    else:
                        with open(output_file, 'a') as output:
                            output.write('\t'.join(line) + '\n')


if __name__ == '__main__':
    file1 = "file1.bed"
    file2 = "file2.bed"
    output = "minus_test.bed"
    subtract_fun(file1, file2, output)
