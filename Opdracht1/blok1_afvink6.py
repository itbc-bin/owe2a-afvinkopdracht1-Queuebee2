# semi-author: Milain Lambers
# Naam: alpacaReader
# Datum: 16 Nov 2017
# Versie: 3 testfase

    
def main(debug=False):
    """
    """
    welcome_user()
    bestand = ask_user_for_file("FASTA filename: ")
    enzym_bestand = ask_user_for_file("enzymes filename: ")
    enzymes = False
    while not enzymes:
        enzymes = get_enzyme_data(enzym_bestand)

    
    headers, seqs = lees_inhoud(bestand) 
    zoekwoord = input("Geef een zoekwoord op: ")


        
    if debug: print(enzymes)
    
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print(headers[i])
            if is_dna(seqs[i]):
                knipt(seqs[i], enzymes)

                


def welcome_user():
    """welcomes the user"""
#!!!Question
#   - wrote this function to remove clutter from main()
#   - is this 'right'?
#   - is printlines() a bad way of printing lines in between actions?
    print("welcome")
    printlines()
    print("To work, I need 2 files:")
    print("FASTA")
    print("\tThis file should contain pure FASTA data.")
    print("enzymes")
    print("\tThis file should contain a list of ")
    print("\tenzyme-names and their 'cut' location line separated.")
    printlines()
    
def printlines():
    print("--------------------------------------------------------")

extentions = ['.fa','.fna','.fasta', '.txt']
def ask_user_for_file(prompt):
    """ask a user for a file (uses promt)
    assuming the file is a textfile...  
    INPUT  (optional) a prompt to display
    OUTPUT file"""
    
    gevonden = False
    
    while not gevonden:
        filename = input(prompt)
        try:
            file = open(filename, 'r')
            if not filename.endswith(tuple(extentions)):
                printlines()
                print("note: this file has an unknown extention,\nit might not work properly.")
                print("known formats are:",extentions)
                printlines()
            gevonden = True
        except IOError or FileNotFoundError:
            printlines()
            print("Couldn't find the file named", filename)
            print("make sure this file is located in the same\ndirectory from which this script is running")
        except TypeError:
            print("Wrong filetype")
        else:
            print("Thanks, found it!")
        finally:
            printlines()
            
    return file
                    

                

def lees_inhoud(bestand):
    """ - takes a FASTA file
        - extracts headers and their sequences
        - closes file
        - returns headers, sequences

        - INPUT  FASTA file type = (_io.TextIOWrapper)
        - OUTPUT headers, sequences
    """
    headers = []
    seqs = []    
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

    bestand.close()
    
    return headers, seqs

    
def is_dna(seq):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    INPUT   indien ja, return True
    OUTPUT  niet, return False
    """    
    for character in seq:
        if character not in ['A','T','C','G','n','N']:
            print('not DNA')
            return False
    return True

def get_enzyme_data(bestand):
    """
    INPUT    a file containing enzyme-names and their 'cut'-location
    OUTPUT   a list of tuples containing enzyme-names and their 'cut'-location
    """
    my_enzymes = []
    for line in bestand:    
        enzyme_name, cut_location = line.split() # split line at space, assign line[0] to name variable, line[1] to cut_location variable.
        my_enzymes.append((enzyme_name, cut_location, cut_location.replace("^",""))) # make a tuple with the data and append it to the my_enzyme list
    bestand.close()
    return my_enzymes
    

def knipt(sequence, list_of_enzymes):
    """
    
    """
    knip = False
    for enzyme in list_of_enzymes:

        if enzyme[2] in sequence:
            alignspot = sequence.find(enzyme[2])
            print(enzyme[0],"cuts at",alignspot)
            knip = True
    print(knip)

       
    
if __name__ == '__main__':
    main()
