# semi-author: Milain Lambers
# Naam: alpacaReader
# Datum: 16 Nov 2017
# Versie: 3 testfase

    
def main(debug=False):
    """ speaks for itself """
    welcome_user()
 
    file_FASTA = ask_user_for_file("FASTA filename: ")
    if not file_FASTA:
        print("something went terribly wrong")
    else:   
        while True:
            file_ENZYMES = ask_user_for_file("enzymes filename: ")
        
            try:
                enzymes = get_enzyme_data(file_ENZYMES)
                break
            except ValueError:
                print("it seems like that file hasn't got enzymes listed properly.")
                print("make sure enzymes are line separated")
            

        

        headers, seqs = lees_inhoud(file_FASTA)

        count=0
        found = False
        while not found:
            searchterm = input("search term: ")
            if debug: print(enzymes)
            print("searching...")
        
        
        
        
            
            for i in range(len(headers)):
                if searchterm in headers[i]:
                    print(headers[i])
                    if is_dna(seqs[i]):
                        cuts(seqs[i], enzymes)
                        found = True

            if not found:
                print("I couldn't find anything!")
                count +=1
            if count > 10:
                print("I think you wont find anything in this file. try something else.")
                break
    

def cuts(sequence, list_of_enzymes):
    """ docstring lost! """
    cut = False
    for enzyme in list_of_enzymes:
        if enzyme[2] in sequence:
            alignspot = sequence.find(enzyme[2])
            print(enzyme[0],"cuts at",alignspot)
            cut = True                

def welcome_user():
    """welcomes the user"""
#!!!Question
#   - wrote this function to remove clutter from main()
#   - is this 'right'?
#   - is printLines() a bad way of printing lines in between actions?
    print("welcome")
    printLines()
    print("To work, I need 2 files:")
    print("FASTA")
    print("\tThis file should contain pure FASTA data.")
    print("enzymes")
    print("\tThis file should contain a list of ")
    print("\tenzyme-names and their 'cut' location line separated.")
    printLines()
    

def printLines():
    print("-----------------------------------------------------------------------------")

def is_valid(file, filetype):
    try:
        next(file)
        print('file validated')
    except UnicodeDecodeError:
        print("This file is encoded in a way I can't read it!")
        print("make sure the file is a",filetype,"file!")
        printLines()
        return False
    except ValueError:
        print("somehow a valueError appeared, are you sure that is the right file?")
        return False
#!!!QUESTION
#   - should I put this return in the try ?
#   - does it cost extra computing power to 'break' out of try/except when
#     try clausule finises?
    file.seek(0)
    return True
    

extentions = ['.fa','.fna','.fasta', '.txt']
def ask_user_for_file(prompt, inputString=False, filetype='filetype'):
    """ask a user for a file (uses promt). dependend on printLines() function.
    INPUT  (optional) a prompt to display, a filetypename
    OUTPUT file
    """
    sameloop = 0
    gevonden = False
    confirmed = False
    
    while not gevonden:
        if inputString:
            print("I will start using",inputString+", is that correct? (y/n): ")
            choice = input()
            if choice in 'YESyes ':
                filename = inputString
            else:
                print("Change the filename in the script please.")
                filename = None
                inputString = False
        else:
            filename = input(prompt)
        try:
            file = open(filename, 'r')
            next(file)
            file.seek(0)
            if not filename.endswith(tuple(extentions)):
                printLines()
                print("note: this file has an unknown extention,\nit might not work properly.")
                if extentions:
                    print("known formats are:",extentions)
                printLines()
            gevonden = True
        except IOError or FileNotFoundError:
            printLines()
            print("Couldn't find the file named", filename,"\nmake sure this file is located in the same\ndirectory from which this script is running")
        except TypeError:
            print("Wrong filetype")
        except UnicodeDecodeError:
            print("This file is encoded in a way I can't read it!\nmake sure the file is a file of type",filetype)
        else:
            print("Thanks, I found the file and it seems valid.")
        finally:
            printLines()

        sameloop+=1
        if sameloop >10:
            break

    if sameloop:
        return None
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
    


       
   
if __name__ == '__main__':
    """ naim/mane """
    main()
