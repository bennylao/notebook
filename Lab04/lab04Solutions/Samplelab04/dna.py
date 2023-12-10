class DNAStrand:
    def __init__(self, dna):
        self.dna = dna

    def __str__(self):
        return self.dna

    def is_valid_dna(self):
        letters = ['A', 'T', 'C', 'G']
        for l in self.dna:
            if l not in letters:
                return False
        return True

    def complement_wc(self):
        """
        Returns the Watson Crick complement which is a string representing
        the complimentary strand of DNA.
        """
        complement = ''
        for letter in self.dna:
            if letter == 'A':
                complement += 'T'
            if letter == 'T':
                complement += 'A'
            if letter == 'C':
                complement += 'G'
            if letter == 'G':
                complement += 'C'

        return complement

    def palindrome_wc(self):
        return self.complement_wc()[::-1]

    def contains_sequence(self, seq):
        return seq in self.dna


def summarise(dna):
    print(f'Original DNA sequence: {dna.__str__()}')

    if dna.is_valid_dna():
        print('Is Valid')
        print(f'Complement: {dna.complement_wc()}')
        print(f'WC Palindrome: {dna.palindrome_wc()}')
    else:
        print('Not Valid DNA')


dna1 = DNAStrand('TTACGGCT')
print(dna1.is_valid_dna())
print(dna1.complement_wc())
print(dna1.palindrome_wc())
print(dna1.contains_sequence('GGC'))

summarise(dna1)
