def read_from_file(input_fastq):
    """
    :param input_fastq: fastq file with reads
    :return: list length = number of reads, on each position - sublist with information on
    [0] name [1] sequence [2] separator [3] quality
    """
    reads_list = {'name': [], 'sequence': [], 'separator': [], 'quality': []}

    with open(input_fastq, 'r') as file:
        while True:
            if not file.readline().strip():
                break
            reads_list['name'].append(file.readline().strip())
            reads_list['sequence'].append(file.readline().strip())
            reads_list['separator'].append(file.readline().strip())
            reads_list['quality'].append(file.readline().strip())

    return reads_list


def gc_check(read, gc_bounds):
    """
    :param read: the read to be checked for the GC-content
    :param gc_bounds: admissible limits of the GC-content (percentage)
    :return: True if the GC content fits the limits, False if not
    """
    if not isinstance(gc_bounds, tuple):
        gc_bounds = (0, gc_bounds)

    if len(gc_bounds) == 2:
        max_border = gc_bounds[1]
        min_border = gc_bounds[0]
    else:
        max_border = gc_bounds[0]
        min_border = 0

    gc_count = 0
    for letter in read:
        if letter in {'G', 'C'}:
            gc_count += 1

    return max_border >= (100 * (gc_count / len(read))) >= min_border


def length_check(read, length_bounds):
    """
    :param read: the read to be checked for the proper length
    :param length_bounds: admissible limits of length for a read
    :return: True if the length fits the limits, False if not
    """
    if not isinstance(length_bounds, tuple):
        length_bounds = (0, length_bounds)

    if len(length_bounds) == 2:
        max_length = length_bounds[1]
        min_border = length_bounds[0]
    else:
        max_length = length_bounds[0]
        min_border = 0

    return max_length >= len(read) >= min_border


def avg_quality(read_quality):
    """
    :param read_quality: fastq file quality string in the ASCII-code form
    :return: average quality per letter for one read
    """
    bases_quality = []
    for letter in read_quality:
        bases_quality.append(ord(letter) - 33)

    return sum(bases_quality) / len(bases_quality)


def write_to_file(prefix, index, reads):
    """
    :param prefix: prefix of the out file name, prefix_index.fastq
    :param index: index of the out file name
    :param reads: list of reads with all attributes for the fastq file (name, sequence, sepsrator, quality)
    :return: fastq file or the given reads
    """
    with open(f"{prefix}_{index}.fastq", 'w') as out_file:
        final_text = "\n".join(reads)
        out_file.write(final_text)


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100),
         length_bounds=(0, 2 ** 32), quality_threshold=0, save_filtered=False):
    """
    :param input_fastq: a fastq file to process
    :param output_file_prefix: a prefix for the output file(s)
    :param gc_bounds: GC-content limits for each read
    :param length_bounds: length limits for each read
    :param quality_threshold: the minimum average quality of the read (according to phred33 scale)
    :param save_filtered: if True, an additional file with filtered out reads will be returned
    :return: a fastq file with accepted reads ({output_file_prefix}_passed.fastq)
    and a fastq file with removed reads ({output_file_prefix}_failed.fastq) if save_filtered = True
    """

    reads_dict_full = read_from_file(input_fastq)

    passed_reads = []
    failed_reads = []

    for read_no in range(len(reads_dict_full['name'])):
        read = reads_dict_full['name'][read_no]
        quality_check = avg_quality(reads_dict_full['quality'][read_no]) >= quality_threshold

        check_score = (gc_check(read, gc_bounds) and
                       length_check(read, length_bounds) and
                       quality_check)

        if check_score:
            passed_reads += [reads_dict_full[key][read_no] for key in reads_dict_full.keys()]

        else:
            failed_reads += [reads_dict_full[key][read_no] for key in reads_dict_full.keys()]

    write_to_file(output_file_prefix, "passed", passed_reads)

    if save_filtered:
        write_to_file(output_file_prefix, "failed", failed_reads)

