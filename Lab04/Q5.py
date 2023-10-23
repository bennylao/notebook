class DNAStrand:
    def __init__(self, dna):
        self.dna = dna

    def is_valid_DNA(self):
        if set(self.dna) == {"A", "T", "C", "G"}:
            return True
        else:
            return False

    def complement_wc(self):
        temp = self.dna.replace("A", "=")
        temp = temp.replace("T", "A")
        temp = temp.replace("=", "T")
        temp = temp.replace("C", "=")
        temp = temp.replace("G", "C")
        temp = temp.replace("=", "G")
        return temp

    def palindrome_wc(self):
        return self.dna[::-1]

    def contains_sequence(self, seq):
        return seq in self.dna

    def __str__(self):
        return self.dna

    @staticmethod
    def summarise(dna):
        print("Original DNA Sequence: ", dna)

        if dna.is_valid_DNA():
            print("Is valid")
            print("Complement: ", dna.complement_wc())
            print("WC Palindrome: ", dna.palindrome_wc())
        else:
            print("Not Valid DNA")


if __name__ == "__main__":
    d1 = DNAStrand("ATCGGCATG")
    print(d1.is_valid_DNA())
    print(d1.complement_wc())
    print(d1.palindrome_wc())

    print("\nTo summarise:")
    DNAStrand.summarise(d1)
