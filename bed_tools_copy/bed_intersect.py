def intersect_fun(file_a, file_b, output_file, variant='only_overlapped'):
    valid_var = {'only_overlapped', 'not_intersected', 'whole_interval'}
    if variant not in valid_var:
        raise ValueError('variant value could be only only_overlapped, not_intersected, or whole_interval')
    with open(file_a, 'r') as base_input:
        for base_line in base_input:
            base = list(base_line.rstrip().split('\t'))
            not_overlapped = True
            with open(file_b, 'r') as add_input:
                for add_line in add_input:
                    add = list(add_line.rstrip().split('\t'))
                    if add[0].strip() != base[0].strip():
                        if add[0].strip() > base[0].strip():
                            if variant == "not_intersected" and not_overlapped:
                                with open(output_file, 'a') as output:
                                    output.write('\t'.join(base[0:3]) + '\n')
                            break
                        else:
                            pass
                    else:
                        if int(add[2]) < int(base[1]):
                            # interval 2 less then interval 1
                            pass
                        if int(add[1]) > int(base[2]):
                            # interval 2 more then interval 1,
                            # as files sorted none of intervals from file2 could intersect these interval
                            if variant == "not_intersected" and not_overlapped:
                                with open(output_file, 'a') as output:
                                    output.write('\t'.join(base[0:3]) + '\n')
                            break
                        if int(add[1]) <= int(base[2]) and int(add[2]) >= int(base[1]):
                            not_overlapped = False
                            # if there is an overlap
                            if variant == 'whole_interval':
                                with open(output_file, 'a') as output:
                                    output.write('\t'.join(base[0:3]) + '\n')
                                break
                            if int(add[1]) <= int(base[1]):
                                # if overlap in left of interval
                                if int(add[2]) <= int(base[2]):
                                    # if it don`t get whole interval
                                    if variant == 'only_overlapped':
                                        with open(output_file, 'a') as output:
                                            output.write(base[0] + '\t' + base[1] + '\t' + add[2] + '\n')
                                if int(add[2]) > int(base[2]):
                                    # if it overlapped whole interval
                                    if variant == 'only_overlapped':
                                        with open(output_file, 'a') as output:
                                            output.write('\t'.join(base[0:3]) + '\n')
                                            break
                            if int(add[1]) > int(base[1]):
                                # if overlapping start within an interval
                                if int(add[2]) >= int(base[2]):
                                    # if it overlapped end of interval
                                    if variant == 'only_overlapped':
                                        with open(output_file, 'a') as output:
                                            output.write(base[0] + '\t' + add[1] + '\t' + base[2] + '\n')
                                            break
                                if int(add[2]) < int(base[2]):
                                    # if whole intersected region lie within interval
                                    if variant == 'only_overlapped':
                                        with open(output_file, 'a') as output:
                                            output.write(base[0] + '\t' + add[1] + '\t' + add[2] + '\n')
        if variant == 'not_intersected' and not_overlapped:
            with open(output_file, 'a') as output:
                output.write('\t'.join(base[0:3]) + '\n')

        return


if __name__ == '__main__':
    file_a = '../BI_2019_Python/bed_copy/bed_1.bed'
    file_b = '../BI_2019_Python/bed_copy/bed_2.bed'
    output = 'intersect1.bed'
    intersect_fun(file_a, file_b, output, variant='not_intersected')
