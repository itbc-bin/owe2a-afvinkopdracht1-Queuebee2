# semi-author: Milain Lambers
# Naam: alpacaReader
# Datum: 16 Nov 2017
# Versie: 3 testfase

extentions = ['.fa','.fna','.fasta']
def askUser():
    gevonden = False
    
    while not gevonden:
        try:
            isfasta = False
            while not isfasta:
                filename = input("I'd like a fasta filename right here, with extention:")
                if not filename.endswith(tuple(extentions):
                    print("wrong extention. please input a valid filename")
                else
            
            file = open(filename, 'r')    
            gevonden = True
        except IOError:
            print("File does not exist")
            
    return file
                    
def main(debug=False):
    """
    """

    bestand = "test.fa"
    enzym_bestand = "enzymen.txt"

    
    headers, seqs = lees_inhoud(bestand) 
        
    zoekwoord = input("Geef een zoekwoord op: ")

    enzymes = get_enzyme_data(enzym_bestand)
        
    if debug: print(enzymes)
    
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print(headers[i])
            if is_dna(seqs[i]):
                knipt(seqs[i], enzymes)
                

def lees_inhoud(bestands_naam):
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
    
    thissequence = ''
    for line in bestand:
        if ">" in line:
            if thissequence != '':
                seqs.append(thissequence)
            thissequence = ''
            headers.append(line.strip("\n"))
        else:
            thissequence = thissequence + line.strip("\n")
    seqs.append(thissequence)
    
    return headers, seqs

    
def is_dna(seq):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """    
    for character in seq:
        if character not in ['A','T','C','G','n','N']:
            print('not DNA')
            return False
    return True

def get_enzyme_data(bestand):
    """from afvink4
    """
    my_enzymes = []
    bestand = open(bestand, 'r')
    
    for line in bestand: #iterate over every line in textfile 'bestand'
        #if not line == '': # apparently I didn't even need this5
        enzyme_name, cut_location = line.split() # split line at space, assign line[0] to name variable, line[1] to cut_location variable.
        my_enzymes.append((enzyme_name, cut_location, cut_location.replace("^",""))) # make a tuple with the data and append it to the my_enzyme list
    return my_enzymes
    

def knipt(sequence, list_of_enzymes):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    knip = False
    for enzyme in list_of_enzymes:
        #print("checking for enzyme....",enzyme[0])
        if enzyme[2] in sequence:
            alignspot = sequence.find(enzyme[2])
            print(enzyme[0],"cuts at",alignspot)
            knip = True
            
            #graphical representation in shell (lol)
            #print(sequence)
            #print((alignspot-1)*' ',enzyme[2])
    print(knip)

       
    
if __name__ == '__main__':
    main()
