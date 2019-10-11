# ● Visit the website: http://www.cbs.dtu.dk/courses/27619/codon.html

# ● Note the 'SLC' code for each Amino Acid.

# ● Create a program called, ‘SickleCellDisease.py’. You will simulate the effects of the
# Single Nucleotide Polymorphism that leads to this genetic disease.

# ● Write a function called ‘translate’ that, when given a DNA sequence of arbitrary length,
# the program identifies and returns the amino acid sequence of the DNA using the
# amino acid SLC code found in that table.
# E.g DNA Input: ATTATTATT
# Output: III (representing: Isoleucine, Isoleucine, Isoleucine )

# ● There are many different amino acids, so this may get a bit repetitive. Just do the first
# five Amino Acids (i.e I, L, V, F M) and make any other codon be printed as the amino
# acid 'X' . So basically, you would use an if - elif - elif .... else structure to translate each
# codon of DNA into the correct Amino Acid.

# ● Note that the program must be able to handle DNA sequences that are not of a length
# divisible by 3.

# ● Hint:
# len(DNA) - (Will return the length of a String)
# DNA[0:3] - (Will get the first 3 characters of the string stored in DNA num = 3)
# DNA[0:num] - (This will work too!)
########################################################################################################################################

#def translate, takes a codone and translates it by checking in the first 5 amino acids if it appears in there
def translate(codone):

     #list of the SLC codes and the codones which are found in that SLC code
     I = ['ATT', 'ATC', 'ATA']
     L = ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG']
     V = ['GTT', 'GTC', 'GTA', 'GTG']
     F = ['TTT', 'TTC']
     M = ['ATG']

     #checking in the first 5 amino acids if it appears in there
     if codone in I:
          amino = 'I'
     elif codone in L:
          amino = 'L'
     elif codone in V:
          amino = 'V'
     elif codone in F:
          amino = 'F'
     elif codone in M:
          amino = 'M'
     else:
          amino = 'X'

     return amino


#read contents of DNA.txt to detect 'a' (the mutatated neucleotide) and find the position of 'a'
def mutate():
     #contents of file == dna codons
    f = open('DNA.txt', 'r') 
    genome = ""
    letters = []

    for line in f:
     genome += line #genome == a complete set of an organism's DNA 

     for i in range(0,len(genome)): #len because each codone is made up of 3 nucleotides
          letters.append(genome[i])

     f.close()

     return letters.index("a") + 1 ### why do we add the 1 here?  
                                   ### keep getting the error: Exception has occurred: ValueError 'a' is not in list
     
print("The small letter 'a' occurs at position : "+str(mutate()))





#function returns the amino acids in a dna sequence 
#ie. a genome, which is an organism's complete set of DNA by calling the above function translate

def txtTranslate():

     DNA = ''
     mDNA = ''
     sequence = []
     msequence = []

#create normalDNA file
     with open('DNA.txt') as f:
          with open('normalDNA.txt', 'w') as fn:
               for line in f:
                    fn.write(line)


     #contents of the normalDNA file stored in a list, storing the contents 1 by 1
     normalDNA = open('normalDNA.txt', 'r') ### should this .txt file be created? 

     for line in normalDNA:
          DNA += line

     for i in range(0, len(DNA)):
          sequence.append(DNA[i])

     normalDNA.close()

     #create mutatedDNA file
     with open('DNA.txt') as f:
          with open('mutatedDNA.txt', 'w') as fm:
               for line in f:
                    fm.write(line)

     #nucleotides are stored in a list in the file mutatedDNA.txt
     mutatedDNA = open('mutatedDNA.txt', 'r')

     for line in mutatedDNA:
          mDNA += line

     for i in range(0,len(mDNA)):
          msequence = []
          msequence.append(mDNA[i]) ###if i dont place msequence = [] in the for loop then msequence undefined.
                                    ###but shouldn't be so because #msequence.append(mDNA[i]) is indented in the function right?

     mutatedDNA.close()

#use the modulus to calculate the number of codons 
#and translate all codones ignoring the remaining nucleotides
     DNA = ''###if i define DNA here the DNA below is undefined.
                                    ###but shouldn't be so because '#remainder1 = len(DNA)%3 is indented in the function right?

     remainder1 = len(DNA)%3 #normal DNA len
     remainder2 = len(mDNA)%3 #mutated DNA len

     x = len(DNA) - remainder1
     y = len(mDNA) - remainder2

     genome1 = ''
     genome2 = ''

#Then by slicing through the list,
#three nucleotides at a time, 
#codone is translated and added to a string of amino acids
     for i in range(0,x,30):
          codone = DNA[i:i+3]
          genome1 += translate(codone)

     for j in range(0,y,3):
          codone = mDNA[j:j+3]
          genome2 += translate(codone)


     print("The amino acids in the normal sequence of the DNA are :  " + genome1)
     print("The amino acids in the mutated sequence of the DNA are :  " + genome2)

txtTranslate()

# End of code 