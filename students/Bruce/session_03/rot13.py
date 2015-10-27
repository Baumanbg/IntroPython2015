#
Capstr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Lwrstr = 'abcdefghijklmnopqrstuvwxyz'
Resultstr = ""

def Rot13(str,Resultstr):
    """Step through string checking each character position; test whether letter is a capital or lower case; record position of matching letter; adjust position to new letter and build new result string."""
    index = 0
    counter = 0
    for i in str:
        letter = str[counter]
        #print(letter)
        if letter in Capstr:
            for i in range(26):
                if letter == Capstr[i]:index = i
            if index > 12: index = index - 13
            else: index = index + 13
            Resultstr = Resultstr + Capstr[index]
        if letter in Lwrstr:
            for i in range(26):
                if letter == Lwrstr[i]:index = i
            if index > 12: index = index - 13
            else: index = index + 13
            Resultstr = Resultstr + Lwrstr[index]
        if not(letter in Capstr) and not(letter in Lwrstr): Resultstr = Resultstr + " "
        counter +=1
    print(Resultstr)
    
string1 = input('Type in the phrase to be encrypted or decrypted. \n')
Rot13(string1,Resultstr)






