
def transcribe(seq):   # DNA --> RNA

    if not(set(seq).issubset(set('ATGCatgc'))):
        return 'Wrong alphabet! Make sure that input = DNA'

    else:
        tr_dict = {
            "A": "A", "a": "a", "T": "U", "t": "u",
            "G": "G", "g": "g", "C": "C", "c": "c"
        }
        return "".join([tr_dict[i] for i in seq])


def rev_transcr(seq):  # RNA --> DNA

    if not(set(seq).issubset(set('AUGCaugc'))):
        return 'Wrong alphabet! Make sure that input = RNA'

    else:
        tr_dict = {
            "A": "A", "a": "a", "U": "T", "u": "t",
            "G": "G", "g": "g", "C": "C", "c": "c"
        }
        return "".join([tr_dict[i] for i in seq])


def reverse(seq):  # input --> reversed sequence

    # check for DNA or RNA alphabet
    if set(seq).issubset(set('ATGCatgc')) or set(seq).issubset(set('AUGCaugc')):
        return seq[::-1]

    else:
        return 'Wrong alphabet!'


def complement(seq):  # DNA/RNA --> complement DNA/RNA

    dict_DNA = {
        "A": "T", "a": "t", "T": "A", "t": "a",
        "G": "C", "g": "c", "C": "G", "c": "g"
    }

    dict_RNA = {
        "A": "T", "a": "t", "T": "A", "t": "a",
        "G": "C", "g": "c", "C": "G", "c": "g"
    }

    if set(seq).issubset(set('ATGCatgc')):  # DNA case
        return "".join([dict_DNA[i] for i in seq])

    elif set(seq).issubset(set('AUGCaugc')):  # RNA case
        return "".join([dict_RNA[i] for i in seq])

    else:
        return 'Wrong alphabet!'


def first_orf(s):  # DNA --> finding the first reading frame

    if not(set(seq).issubset(set('ATGCatgc'))):
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


def translate(seq):  # RNA/DNA --> DNA --> first ORF --> RNA --> protein

    if not (set(seq).issubset(set('AUGCaugc')) or
            set(seq).issubset(set('ATGCatgc'))):
        return 'Wrong alphabet! Try one more time!'

    elif set(seq).issubset(set('AUGCaugc')):  # RNA case
        seq_dna = rev_transcr(seq)

    else:
        seq_dna = seq

    orf = first_orf(seq_dna)  # find the ORF
    orf = orf[:(len(orf) // 3) * 3]  # if the are no stop codons --> cut to :3

    if orf[0] == "N":  # no reading frames :(
        return orf

    rna = transcribe(orf)  # obtain RNA

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


def rev_compl(seq):
    return reverse(complement(seq))


command = input("Enter command: ")

command_dict = {"transcribe": transcribe,
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
        print(command_dict[command](seq))

    command = input("Enter command: ")

print("Good luck, see you later!")
