
def RNA_DNA_check(seq):

    if set(seq).issubset(set('ATGCatgc')):
        return "DNA"
    elif set(seq).issubset(set('AUGCaugc')):
        return "RNA"
    else:
        return 'Wrong alphabet! Make sure that input is DNA or RNA'


def transcribe(seq, na):   # DNA --> RNA

    if na != "DNA":
        return 'Wrong alphabet! Make sure that input = DNA'

    else:
        tr_dict = {
            "A": "A", "a": "a", "T": "U", "t": "u",
            "G": "G", "g": "g", "C": "C", "c": "c"
        }
        return "".join([tr_dict[i] for i in seq])


def rev_transcr(seq, na):  # RNA --> DNA

    if na != "RNA":
        return 'Wrong alphabet! Make sure that input = RNA'

    else:
        tr_dict_rev = {
            "A": "A", "a": "a", "U": "T", "u": "t",
            "G": "G", "g": "g", "C": "C", "c": "c"
        }
        return "".join([tr_dict_rev[i] for i in seq])


def reverse(seq, na):  # input --> reversed sequence
    return seq[::-1]


def complement(seq, na):  # DNA/RNA --> complement DNA/RNA

    dict_DNA = {
        "A": "T", "a": "t", "T": "A", "t": "a",
        "G": "C", "g": "c", "C": "G", "c": "g"
    }

    dict_RNA = {
        "A": "U", "a": "u", "U": "A", "u": "a",
        "G": "C", "g": "c", "C": "G", "c": "g"
    }

    if na == "DNA":  # DNA case
        return "".join([dict_DNA[i] for i in seq])

    else:  # RNA case
        return "".join([dict_RNA[i] for i in seq])


def first_orf(s, na):  # DNA --> finding the first reading frame

    if na != "DNA":
        return 'Wrong alphabet! Make sure that input = DNA'

    n = len(s)
    i = 0

    # if there are no start codons
    if s.find("ATG") == -1:
        return "No start codons in your sequence"

    # if there are some start codons and some stop codons
    while i + 2 <= n:
        if s[i:i + 3] == 'ATG':
            j = i + 3
            while j + 2 <= n:
                if s[j:j + 3] in {'TAA', 'TAG', 'TGA'}:
                    return s[i:j + 3]
                j = j + 3
        i = i + 1

    # if there is no stop codons --> [from first start till the end]
    return s[s.find("ATG"):]


def translate(seq, na):  # RNA/DNA --> DNA --> first ORF --> RNA --> protein

    if na == "RNA":  # RNA case
        seq_dna = rev_transcr(seq, na)

    else:
        seq_dna = seq

    orf = first_orf(seq_dna, na="DNA")  # find the ORF
    orf = orf[:(len(orf) // 3) * 3]  # if the are no stop codons --> cut to :3

    if orf[0] == "N":  # no reading frames :(
        return orf

    rna = transcribe(orf, na="DNA")  # obtain RNA

    transl_dict = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T',
                   'ACC': 'T', 'ACG': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R',
                   'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'CAA': 'Q',
                   'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P',
                   'CCG': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
                   'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'GAA': 'E', 'GAC': 'D',
                   'GAG': 'E', 'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A',
                   'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
                   'GUC': 'V', 'GUG': 'V', 'UAA': '-', 'UAC': 'Y', 'UAG': '-',
                   'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UGA': '-',
                   'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F',
                   'UUG': 'L'}
    # you might think I typed it in manually, but ofc I didn't!

    length = len(rna)
    pos = 0
    protein = []

    while pos + 3 <= length:
        codon = rna[pos:pos + 3]
        protein.append(transl_dict[codon])
        pos += 3

    return ''.join(protein)


def rev_compl(seq, na):
    return reverse(complement(seq, na), na)


command = input("Enter command: ")

command_dict = {"transcribe": transcribe,
                "reverse transcription": rev_transcr,
                "reverse": reverse,
                "complement": complement,
                "reverse complement": rev_compl,
                "find ORF": first_orf,
                "find orf": first_orf,
                "translate": translate}

while command != "exit":
    if command not in command_dict.keys():
        print("Cannot find this command :( try again!")
    else:
        seq = str(input("Enter sequence: "))
        NA = RNA_DNA_check(seq)

        if NA == "RNA" or NA == "DNA":
            print(command_dict[command](seq, NA))
        else:
            print(NA)

    command = input("Enter command: ")

print("Good luck, see you later!")

