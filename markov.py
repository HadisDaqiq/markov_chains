"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_data = open(file_path)
    contains  = file_data.read()


    return contains


def make_chains(text_string):
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

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):  # Iterate over each bigram, skipping last.

        if (words[i], words[i + 1]) in chains:
            chains[(words[i], words[i + 1])].append(words[i + 2])

        else:
            chains[(words[i], words[i + 1])] = [words[i + 2]]


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    key = choice(list(chains.keys()))
    words.extend(list(key))

    while key in chains:
        random_next_word = choice(chains[key])
        words.append(random_next_word)
        key = (key[1], random_next_word)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
