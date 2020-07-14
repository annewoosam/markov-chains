"""Generate Markov text from text files."""

from random import choice


# def open_and_read_file(file_path):
#     """Take file path as string; return text as string.

#     Takes a string that is a file path, opens the file, and turns
#     the file's contents as one string of text.
#     """
 
    text_string = open(file_path).read()
    print(text_string)
    return text_string #"Contents of your file as one long string"


def make_chains(file_path):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

        

# 
# meshing https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list  and
# https://www.geeksforgeeks.org/python-bigram-formation-from-given-list/ using list comprehension + enumerate() + split(), to get bigrams for dictionary keys
# initializing list  
# text_string = open("green-eggs.txt").read()
# print(text_string)
    with open("green-eggs.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    test_list= lines
    print(test_list)
      
    # printing the original list  
    print ("The original list is : " + str(test_list)) 
      
    # using list comprehension + enumerate() + split() 
    # for Bigram formation 
    res = [(x, i.split()[j + 1]) for i in test_list  
           for j, x in enumerate(i.split()) if j < len(i.split()) - 1] 
      
    # printing result 
    print ("The formed bigrams are : " + str(res)) 

    # chains = {}
    # return chains
make_chains("green-eggs.txt")

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
#input_text = open_and_read_file(input_path)

# Get a Markov chain
## temp hashchains = make_chains(input_text)

# Produce random text
## temp hash random_text = make_text(chains)

## temp hash print(random_text)
