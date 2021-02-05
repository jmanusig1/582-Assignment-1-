import os
import glob
import nltk
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords  
from string import punctuation

porter_stemmer = PorterStemmer()
stop_words = stopwords.words('english')

"""
    tokenize takes in some string input and preprocesses it.
    Preprocessing tokenizes on white space and removes punctuation.
"""
def tokenize(text):

    #first lowercase the text to standardize the text
    text = text.lower()

    #then remove the punctuation from the text
    for letter in text:

        #checking for punctuation
        if letter in punctuation:
            #if so, replace the punctuation with " " to remove it
            #note: " " was used instead of "" for words that might be connected after replacement
            text = text.replace(letter, " ")

    #tokenize text by splitting on white space
    text = text.split()

    #return the tokenized and preprocessed text
    return text

"""
    function takes in some text array and calculated the frequency of words in the said array
"""
def determine_frequency(text):

    #create a dictionary to hold the frequency values
    freq_dict = {}

    #then loop through the text to count the words
    for word in text: 

        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict.update({word:1})

    return freq_dict

"""
    function uses the porter stemmer algorithm and creates porter stemmer tokens from the
    tokenized, preprocessed words 
"""
def porter_stemmer_tokenization(text):

    i = 0

    #loop throuhg the tokens
    for word in text:
        #perform the tokenization
        text[i] = porter_stemmer.stem(word)
        i += 1

    #return porter stemmer list
    return text

"""
    function removes the stop words from a tokenized file
"""
def remove_stopwords(text):

    #lambda expression to remove stop_words
    items = [item for item in text if item not in stop_words]
                             
    #return truncated list
    return items

"""
    function will return the minimum number of unique words needed to account
    for 15% of the total words given a dictionary and the fifteen per
"""
def return_min_number(tokens):

    fifteen = 0

    #first add up all the words
    for v in tokens.values():
        fifteen += int(v)

    #multiply by .15 to get 15%
    fifteen *= .15

    #variable to hold the number of words before we reach 15%
    threshold = 0
    count = 0

    #cycle through dictionary again
    for k, v in tokens.items():

        #increment the threshold and counts 
        threshold += int(v)
        count += 1 

        #check for 15%
        if(threshold > fifteen):
            #return if above
            return count
    
    #return anyways 
    return count

    
#get the path of the directory containing all the files
#NOTE: change "citeseer" to whatever directory or file desired
path = os.path.abspath('citeseer')

q1_array = []

#loop through the directory and preprocess the data 
for root, dirs, files in os.walk(path):
     for file in files:
        with open(os.path.join(root, file), "r") as auto:

            #read the file
            read_file = auto.read()

            #and add it to the array
            q1_array += tokenize(read_file)

#after getting all the words, perform some basic statistical analysis
q1_freq = determine_frequency(q1_array)

#create a list of sorted keys
q1_sorted_keys = sorted(q1_freq, key=q1_freq.get, reverse=True)

#dictionary to hold the sorted dictionary
q1_freq_sorted = {}

#fill the new dictionary with the sorted items
for w in q1_sorted_keys:
    q1_freq_sorted[w] = q1_freq[w]  

#print out the statistics 
print("Preprocessed words before Porter Stemmer adjustment and Stopwords removal")
print("Total number of words: ", len(q1_array))
print("Vocabulary Size: ", len(q1_freq))
print("Top 20 Words: ")

#go through the top 20 words and print
for i in range(20):
    key = str(q1_sorted_keys[i])
    val = str(q1_freq_sorted[key])
    print( str(i+1) + ".", key, val)

print("The stop words from this list are: ")

#looping through the top 20 
for i in range(20):
    key = str(q1_sorted_keys[i])
    
    #if key is a stop word, then print 
    if(key in stop_words):
        print(key)

print("Minimum number of words to account for 15 percent of total words: ", return_min_number(q1_freq_sorted))


"""
.
.
STOPWORDS AND PORTER STEMMER WILL BE APPLIED BELOW AND PROCESSED
.
. 
"""
print() 

#first remove stop words
q2_array = remove_stopwords(q1_array)

#then apply the porter stemmer algorithm 
q2_array = porter_stemmer_tokenization(q2_array)

q2_freq = determine_frequency(q2_array)

#create a list of sorted keys
q2_sorted_keys = sorted(q2_freq, key=q2_freq.get, reverse=True)

#dictionary to hold the sorted dictionary
q2_freq_sorted = {}

#fill the new dictionary with the sorted items
for w in q2_sorted_keys:
    q2_freq_sorted[w] = q2_freq[w]  

#print out the statistics 
print("***Preprocessed words AFTER Porter Stemmer adjustment and Stopwords removal***")
print()
print("Total number of words: ", len(q2_array))
print("Vocabulary Size: ", len(q2_freq))
print("Top 20 Words: ")

#go through the top 20 words and print
for i in range(20):
    key = str(q2_sorted_keys[i])
    val = str(q2_freq_sorted[key])
    print( str(i+1) + ".", key, val)

print("Minimum number of words to account for 15 percent of total words: ", return_min_number(q2_freq_sorted))

