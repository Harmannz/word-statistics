'''Program that determines the valid words in a given file and prints
   statistics about the words, a table and a horizontal bar graphs
   of the lengths of the words and their occurences.
   Author: Harman Singh
   Version: 4 June 2014 '''


import os

TABLE_TITLE = " Len  Freq"
FREQ_TABLE_TEMPLATE = "{:>4}{:>6}"

GRAPH_TITLE = " Len  Freq Graph"
GRAPH_LINE_TEMPLATE = "{:>4}{:>5}% {}"


def get_filename():
    """Returns a valid filename"""
    filename = input ("Please enter filename: ")
    while not os.path.isfile(filename):
        print(filename, "not found...")
        filename = input("Please enter filename: ")
    return filename


def display_word_length_table(words, word_len_max):
    '''prints a table of the lengths of words in the word list 
       and their respective frequencies.'''
    print()
    print(TABLE_TITLE)
    word_length_dict = {}
     
    for i in range(1, word_len_max + 1):
        word_length_dict[i] = 0
        
    for word in words:
        word_length_dict[len(word)] += 1
              
    for length, count in sorted(word_length_dict.items()):
        print(FREQ_TABLE_TEMPLATE.format(length, count))

    display_frequency_graph(word_length_dict, len(words))
    
    
        
def display_frequency_graph(word_length_dict, length_of_words):
    '''prints a graph of the word lengths in the list of words
       and their respective occurence as a percentage. The horizontal bars are
       displayed as multiples of: '='. '''
    print()
    print(GRAPH_TITLE)
    
    for length, count in sorted(word_length_dict.items()):
        
        relative_freq = int(count / length_of_words * 100)
        num_of_equals = relative_freq * '='
        print(GRAPH_LINE_TEMPLATE.format(length, relative_freq, num_of_equals))
    
            
def max_word_frequency(words):
    '''returns the most frequently ocuring word in the list of valid words 
       from the given file'''
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
        
    return (max(word_dict.values()))
    


def get_words_from_file(filename):
    '''Reads the file with given name and returns a list of valid words. 
    The valid words are between the sentences: 
    '*** START OF' and '*** END'. '''
    
    word_list = []
    is_reading = True   
    infile = open(filename, 'r', encoding="utf-8")
    sentence = infile.readline()
    
    while not(sentence.startswith("*** START OF")):
        sentence = infile.readline()

    while is_reading:
        sentence = infile.readline()
        if sentence.startswith("*** END"):
            is_reading = False
        else:
            word_list += check_words_in_sentence(sentence)    
        
    return word_list


def check_words_in_sentence(sentence):
    '''Checks each word in a valid sentence and returns a list of 
       valid lower case words'''

    valid_words = []
    
    for word in sentence.split():
        word = word.strip('\n"-:\';,.').lower()
        if word.isalpha():
            valid_words.append(word)
            
    return valid_words
# ----------------------------------------------

def avg_length(words):
    """Returns the average length of words in the words list"""
    sum_lengths = 0
    for word in words:
        sum_lengths += len(word)
    average = sum_lengths / len(words)
    return average
    

def max_word_length(words):
    """Returns the length of the longest word in the list of words.
    Or 0 if there are no words in the list...
    """
    if len(words) > 0:
        max_length = len(words[0])
        for word in words:
            length = len(word)
            if length > max_length:
                max_length = length
    else:
        max_length = 0
    return max_length


def main():
    '''Main function: prompt for filename, prints statistics about 
       valid words in the given file. Also, prints a table and graph
       of different lengths of the words in the file and 
       their respective frequencies.'''
    
    filename = get_filename()
    words = get_words_from_file(filename)
    word_len_max = max_word_length(words)
    
    print(" {} loaded ok.".format(filename))
    print()
    print('Word summary (all words):')
    print(' Number of words = {}'.format(len(words)))
    print(' Avg word length = {:.2f}'.format(avg_length(words)))
    print(' Max word length = {}'.format(word_len_max))
    print(' Max frequency = {}'. format(max_word_frequency(words)))

    display_word_length_table(words, word_len_max)



main()