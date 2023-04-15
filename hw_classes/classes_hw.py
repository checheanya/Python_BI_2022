# Task 1 -----------------------------------------------------------------

class Chat(object):
    '''
    Class for the chat object.
    '''
    def __init__(self, name, messages):
        # stores messages from new to old (inverted order) 
        self.chat_name = name
        self.chat_history = sorted(messages, key=lambda mes: mess.datetime, reverse=True)
    
    def show_last_message(self):
        # prints the last message
        self.chat_history[0].show()
    
    def get_history_from_the_timeperiod(self, start_date=None, end_date=None):
        # returns messages from the given timeframe
        if isinstance(start_date, datetime) and isinstance(end_date, datetime):
            return Chat(f'{self.chat_name}_subchat', [message for message in self.chat_history if (end_date > message.datetime > start_date)])
        else:
            print('Dates should be in the datetime format!')
    
    def show_chat(self):
        print(f'Messages in the {self.chat_name}:')
        for message in self.chat_history[::-1]:
            message.show()
    
    def recieve(self, message_new):
        self.chat_history = [message_new] + self.chat_history

class Message(object):
    def __init__(self, text, usr):
        self.text = text
        self.datetime = None
        try:
            if usr.date_registered:
                self.user = usr
        except AttributeError as ae:
            print('This user does not exist, add user first!')
    
    def show(self):
        print(self.datetime)
        print(self.user.nickname, 'wrote:')
        print('> ', self.text)
        
    def send(self, chat):
        self.datetime = datetime.now()
        chat.recieve(self)


class User(object):
    def __init__(self, nickname, status, phone, share_phone=True):
        self.nickname = nickname
        self.status = status
        self.date_registered = datetime.now()
        if share_phone:
            self.phone = phone
        else:
            self.phone = 'hidden'
    
    def get_info(self):
        print('Name: ', self.nickname, '| Status: ', self.status)
        print('Registered: ', self.date_registered)
        print('Phone number: ', self.phone)
        
        
        
# Task 2 ---------------------------------------------------------------------------------------------------------


class Args:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    def __rlshift__(self, func):
        return func(*self.args, **self.kwargs)

    
# Task 3 ---------------------------------------------------------------------------------------------------------


class StrangeFloat(float):
    def __getattr__(self, name):
        func = f'super(StrangeFloat, self).__{name[:3]}__(float({name[name.find("_")+1:]}))'
        try:
            s = eval(func)
            return StrangeFloat(s)
        except AttributeError as ae:
            for fun in dir(float)[::-1]:
                if name[:3] in fun:
                    f = f'super(StrangeFloat, self).{fun}(float({name[name.find("_")+1:]}))'
                    s = eval(f)
                    return StrangeFloat(s)

                
# Task 4 ---------------------------------------------------------------------------------------------------------
 
    
np = __import__('numpy')

matrix = list.__new__(list)
idx = int.__int__(0)
while idx.__lt__(100):
    matrix.__iadd__([list.__call__(range(idx, idx.__add__(10)))])
    idx = idx.__add__(10)
    
selected_columns_indices = list.__call__((filter(lambda x: x in range(1, 5, 2), range(matrix.__len__()))))
selected_columns = map(lambda x: list.__call__(x.__getitem__(col) for col in selected_columns_indices), matrix)

arr = np.array(list.__call__(selected_columns))

mask = arr[:, 1].__mod__(3).__eq__(0)

new_arr = arr.__getitem__(mask)

product = new_arr.__matmul__(new_arr.T)

if (product.__getitem__(0).__lt__(1000)).all().__and__((product.__getitem__(2).__gt__(1000)).any()):
    print(product.mean().__str__())

    
# Task 5 ---------------------------------------------------------------------------------------------------------
 
    
from abc import ABC, abstractmethod
from Bio.SeqUtils.ProtParam import ProteinAnalysis as PA


class BiologicalSequence(ABC):
    def __init__(self, seq):
        # we will store input sequence as a string
        if isinstance(seq, list):
            self.seq = ''.join(seq).upper()
        else:
            self.seq = seq.upper()
    
    def __len__(self):
        # returns the length of the sequence, call: len()
        return len(self.seq)
        
    def __getitem__(self, slc):
        # returns i-th element of the sequence, call: obj[i] OR
        # slice from start to stop with step=step
            return self.seq[slc]
    
    def __str__(self):
        # returns sequence as a string, call: str()
        # since we're storing seq as a string - just printing it out
        return self.seq
    
    def __repr__(self):
        # prints out info about the sequence
        print('Sequence: ')
        return self.seq
    
    def check_alphabet(self):
        # checking the sequence for the presence of inappropriate letters
        if set(self.seq).issubset(self.letters_set):
            print('Everything is fine!')
        else:
            raise TypeError("Sequence contains invalid letter")

            
    
class NucleotideSequence(BiologicalSequence):
    def __init__(self, seq):
        super().__init__(seq)
        # dict of all allowed letters - DNA by default
        self.letters_set = {'A', 'T', 'G', 'C'}
        # dict of the complementary letters - DNA by default
        self.comp_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    
    def complement(self):
        # returns a complementary sequence
        return type(self)(''.join([self.comp_dict[i] for i in self.seq]))
    
    def gc_content(self):
        # returns a GC-content of the sequence
        return sum([self.seq.count('C'), self.seq.count('G')])/len(self)

class DNASequence(NucleotideSequence):    
    def transcribe(self):
        # returns transcribed sequence of RNA class
        return RNASequence(self.seq.replace('T', 'U'))


class RNASequence(NucleotideSequence):
    def __init__(self, seq):
        super().__init__(seq)
        # dict of all allowed letters - updating
        self.letters_set = {'A', 'T', 'G', 'C'}
        self.letters_set = {'A', 'U', 'G', 'C'}
        self.comp_dict = {'A': 'U', 'G': 'C', 'C': 'G', 'U': 'A'}
        self.translation_dict = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N',
                                 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'AGA': 'R',
                                 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I',
                                 'AUC': 'I', 'AUG': 'M', 'CAA': 'Q', 'CAC': 'H',
                                 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P',
                                 'CCG': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R',
                                 'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L',
                                 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D',
                                 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GGA': 'G',
                                 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
                                 'GUC': 'V', 'GUG': 'V', 'UAA': '-', 'UAC': 'Y',
                                 'UAG': '-', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S',
                                 'UCG': 'S', 'UGA': '-', 'UGC': 'C', 'UGG': 'W',
                                 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L'}
    
    def reverse_transcribe(self):
        # returns reverse-transcribed sequence of DNA class
        return DNASequence(self.seq.replace('U', 'T'))
    
    def translate(self):
        # retuns protein sequence of the class AminoAcidSequence based on RNA
        if self.seq.find("AUG") == -1:
            raise KeyError("No start codons in your sequence")
        else:
            orf_start_pos = self.seq.find('AUG')
            
        orf_end_pos = min(self.seq.find('UAA'), self.seq.find('UAG'), self.seq.find('UGA'))
        gene = self.seq[orf_start_pos:orf_end_pos]
        return AminoAcidSequence(''.join([self.translation_dict[gene[i:i+3]] for i in range(0, len(gene)-3, 3)]))

    
class AminoAcidSequence(BiologicalSequence):
    def __init__(self, seq):
        super().__init__(seq)
        # dict of amino acids molecular weight
        self.aa_weight_dict = {
            'A': 71.03711, 'G': 57.02146, 'M': 131.04049, 'S': 87.03203,
            'C': 103.00919, 'H': 137.05891, 'N': 114.04293, 'T': 101.04768,
            'D': 115.02694, 'I': 113.08406, 'P': 97.05276, 'V': 99.06841,
            'E': 129.04259, 'K': 128.09496, 'Q': 128.05858, 'W': 186.07931,
            'F': 147.06841, 'L': 113.08406, 'R': 156.10111, 'Y': 163.06333
        }
        # tools to work with proteins
        self.tools = PA(self.seq)
        # list of allowed letters
        self.letters_set = self.aa_weight_dict.keys

    def calc_mass(self):
        # retunns a molecular weight of the protein
        s = 0
        for aa in self.seq:
           s += self.aa_weight_dict[aa]
        return s
    
    def calc_isoel_point(self):
        # returns isoelectric point of the protein
        return self.tools.isoelectric_point()
    
    def calc_charge_at_ph(self, ph):
        # returns protein charge at the given ph 
        return self.tools.charge_at_pH(ph)
    
    def check_alphabet(self, letters_set):
        # checking the alphabet of the sequence
        return super().check_alphabet(self, self.letters_set)
 
    
