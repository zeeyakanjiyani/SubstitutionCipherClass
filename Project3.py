# File: Project3.py
# Student: Zeeya Kanjiyani
# UT EID: zkk83
# Course Name: CS303E
# 
# Date: 11/20/2022
# Description of Program: 

import random
import os

# A global constant defining the alphabet. 
LETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):
    # A key is legal if it has length 26 and contains all letters.
    # from LETTERS.
    key = key.lower()
    return ( len(key) == 26 and all( [ ch in key for ch in LETTERS ] ) )

def makeRandomKey():
    # A legal random key is a permutation of LETTERS.
    lst = list( LETTERS )    # Turn string into list of letters
    random.shuffle( lst )    # Shuffle the list randomly
    return ''.join( lst )    # Assemble them back into a string


def makeConversionDictionary( key1, key2 ):
    d = {}
    for i in range (26):
        d[key1[i]] = key2[i]
    return d
    
    
def convertCharacter( ch, d ):
    if ch.isupper():
        ch = (d[ch.lower()]).upper()
    else:
        ch = d[ch]
    return ch


def convertText( text, d ):
    convertedText = ""
    for ch in text:
        if ch.lower() in d:
            convertedText += convertCharacter(ch, d)
        else: 
            convertedText += ch
    return convertedText

class SubstitutionCipher:
    def __init__ (self, key = makeRandomKey() ):
        """Create an instance of the cipher with stored key, which
        defaults to a randomly generated key."""
        self.key = key

    def getKey( self ):
        """Getter for the stored key."""
        return self.key

    def setKey( self, newKey):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if (isLegalKey(key = newKey)):
            self.key = newKey

    def encryptFile( self, inFile, outFile ):
        """Encrypt the contents of inFile using the stored key
        and write the results into outFile.  Assume inFile exists.
        """
        encryptionComplete = open(outFile, "w")
        for line in inFile:
            convertedLine = convertText(line, makeConversionDictionary(LETTERS, self.key))
            encryptionComplete.write(convertedLine)
        inFile.close()
        encryptionComplete.close()
        print("    The encrypted output filename is " + outFile + "\n")

    def decryptFile( self, inFile, outFile ):
        """Decrypt the contents of inFile using the stored key
        and write the results into outFile.  Assume inFile exists."""
        decryptionComplete = open(outFile, "w")
        for line in inFile:
            convertedLine = convertText(line, makeConversionDictionary(self.key, LETTERS))
            decryptionComplete.write(convertedLine)
        inFile.close()
        decryptionComplete.close()
        print("    The decrypted output filename is " + outFile + "\n")

def main():
        """This implements the top level command loop. It
        creates an instance of the SubstitutionCipher class and allows the user
        to invoke within a loop the following commands: getKey, changeKey,
        encryptFile, decryptFile, quit."""
        cipher = SubstitutionCipher()
        while True:
            inputCommand = input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ")
            inputCommand = inputCommand.lower()
            if (inputCommand == "getkey"):
                print("  Current cipher key: " + cipher.getKey() + "\n")
        
            elif (inputCommand == "changekey"):
                while True:
                    changeKeyInput = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ")
                    if (changeKeyInput != "random") and (changeKeyInput != "quit"):

                        if (len(changeKeyInput) != 26) or (all([ ch not in changeKeyInput for ch in LETTERS ])):
                            print("    Illegal key entered. Try again!")
                        else:
                            print("    New cipher key: " + changeKeyInput + "\n")
                            cipher.setKey(changeKeyInput)
                            break

                    elif (changeKeyInput == "random"):
                        newKey = makeRandomKey()
                        print("    New cipher key: " + newKey + "\n")
                        cipher.setKey(newKey)
                        break
                    elif (changeKeyInput == "quit"):
                        print("")
                        break
                    
            elif (inputCommand == "encryptfile"):
                encryptFileInput = input("  Enter a file name: ")
                if not os.path.isfile(encryptFileInput):
                    print("File does not exist" + "\n")
                else:
                    inFilename = open(encryptFileInput, "r")
                    extension = "-Enc" 
                    if encryptFileInput.endswith(".txt"):
                        outFilename = encryptFileInput[:-4] + extension + ".txt"
                    else:
                        outFilename = encryptFileInput + extension
                    cipher.encryptFile(inFilename, outFilename)

            elif (inputCommand == "decryptfile"):
                decryptFileInput = input("  Enter a file name: ")
                if not os.path.isfile(decryptFileInput):
                    print("File does not exist" + "\n")
                else:
                    inFilename = open(decryptFileInput, "r")
                    extension = "-Dec"
                    if decryptFileInput.endswith(".txt"):
                        outFilename = decryptFileInput[:-4] + extension + ".txt"
                    else:
                        outFilename = decryptFileInput + extension
                    cipher.decryptFile(inFile = inFilename, outFile = outFilename)
 

            elif (inputCommand == "quit"):
                print("Thanks for visiting!")
                return False

            else:
                print("  Command not recognized. Try again!" + "\n")

                

main()