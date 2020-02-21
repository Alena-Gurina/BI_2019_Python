class Rna:
    def __init__(self, *seq):
        seq_rna = list()
        seq_rna.extend(*seq)
        if ((seq_rna.count("G") + seq_rna.count("C") + seq_rna.count("U") + seq_rna.count("A") + seq_rna.count("N")) < len(seq_rna)):
            print("This sequence can`t be Rna, check it!")
        else:
            self.sequence = seq_rna

    def gc_content(self):
        res = (self.sequence.count("G") + self.sequence.count("C")) / len(self.sequence)
        return (res)

    def reverse_complement(self):
        transl_dict_rna = dict(A="U", U="A", G="C", C="G", N="N")
        rev = []
        for i in range(len(self.sequence) - 1, -1, -1):
            rev.append(transl_dict_rna[self.sequence[i]])
        return (rev)

    def __eq__(self, other):
        return isinstance(other, Rna) and self.sequence == other.sequence


class Dna:
    def __init__(self, *seq):
        seq_dna = list()
        seq_dna.extend(*seq)
        if ((seq_dna.count("G") + seq_dna.count("C") + seq_dna.count("T") + seq_dna.count("A") + seq_dna.count("N")) < len(seq_dna)):
            print("This sequence can`t be dna, check it!")
        else:
            self.sequence = seq_dna

    def gc_content(self):
        res = (self.sequence.count("G") + self.sequence.count("C")) / len(self.sequence)
        return (res)

    def reverse_complement(self):
        transl_dict_dna = dict(A="T", T="A", G="C", C="G", N="N")
        rev = []
        for i in range(len(self.sequence) - 1, -1, -1):
            rev.append(transl_dict_dna[self.sequence[i]])
        return (rev)

    def add(self, *seq):
        add_seq = list()
        add_seq.extend(*seq)
        if ((add_seq.count("G") + add_seq.count("C") + add_seq.count("T")
             + add_seq.count("A") + add_seq.count("N")) < len(add_seq)):
            print("This sequence can`t be dna, check it!")
        else:
            self.sequence.extend(add_seq)

    def __eq__(self, other):
        return isinstance(other, Dna) and self.sequence == other.sequence

    def rna_transcript(self):
        transl_dict_rna = dict(A="U", T="A", G="C", C="G", N="N")
        rna = []
        for nucleotid in self.sequence:
            rna.append(transl_dict_rna[nucleotid])
        res = ''.join(rna)
        return (Rna(res))


seq = Dna("AGTC")
a = "".join(seq.sequence)
print(a)
print(*seq.sequence)
print(seq.gc_content())

b = Rna("AGCU")
print(b.sequence)
b = seq.rna_transcript()
print(b.sequence)
seq2 = Dna("AGTC")
print(seq.__eq__(seq2))
