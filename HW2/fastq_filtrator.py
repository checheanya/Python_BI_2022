def read_from_file(input_fastq):
    """
    :param input_fastq: fastq file with reads
    :return: list length = number of reads, on each position - sublist with information on
    [0] name [1] sequence [2] separator [3] quality
    """
    reads_list = []
    with open(input_fastq, 'r') as file:
        lines = file.readlines()

    for read_no in range((len(lines) // 4)):
        if read_no == (len(lines) // 4) - 1 and lines[read_no * 4 + 3][-1] != "\n":
            reads_list.append([lines[read_no * 4][:-1], lines[read_no * 4 + 1][:-1], lines[read_no * 4 + 2][:-1],
                               lines[read_no * 4 + 3]])
        else:
            reads_list.append([lines[read_no*4][:-1], lines[read_no*4 + 1][:-1], lines[read_no*4 + 2][:-1],
                               lines[read_no*4 + 3][:-1]])

    return reads_list


def GC_check(read, gc_bounds):
    """
    :param read: the read to be checked for the GC-content
    :param gc_bounds: admissible limits of the GC-content (percentage)
    :return: True if the GC content fits the limits, False if not
    """
    if len(gc_bounds) == 2:
        max_border = gc_bounds[1]
        min_border = gc_bounds[0]
    else:
        max_border = gc_bounds[0]
        min_border = 0
    gc_percent = 100 * (read.count("C") + read.count("G")) / len(read)

    return max_border >= gc_percent >= min_border


def length_check(read, length_bounds):
    """
    :param read: the read to be checked for the proper length
    :param length_bounds: admissible limits of length for a read
    :return: True if the length fits the limits, False if not
    """
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

    reads_list_full = read_from_file(input_fastq)

    passed_reads = []
    failed_reads = []

    for read_no in range(len(reads_list_full)):
        read = reads_list_full[read_no][1]
        quality_check = avg_quality(reads_list_full[read_no][3]) >= quality_threshold

        check_score = (GC_check(read, gc_bounds) and
                       length_check(read, length_bounds) and
                       quality_check)

        if check_score:
            passed_reads += reads_list_full[read_no]
        else:
            failed_reads += reads_list_full[read_no]

    write_to_file(output_file_prefix, "passed", passed_reads)

    if save_filtered:
        write_to_file(output_file_prefix, "failed", failed_reads)

