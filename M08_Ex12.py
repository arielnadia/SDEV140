# Pig Latin Program

# Explain the program
def welcome():
    print("Ariel Merriman's Pig Latin Translator!")
    print('This program allows the user to input a sentence '\
          'and converts that sentence into Pig Latin.')
    print()

def main():
    welcome()
    # Declare variables
    Index = 0
    Pig_Latin = "ay"
    # Receive user input and convert to list
    Sentence = input('Enter a sentence: ')
    Sentence_List = Sentence.split()
    print('Your sentence in Pig Latin is:')
    # Convert sentence to Pig Latin
    while Index < len(Sentence_List):
        Word = Sentence_List[Index]
        print(Word[1:].lower(), Word[0:1].lower(), Pig_Latin, sep='', end=' ')
        Index += 1

# Run the program!
main()
    
