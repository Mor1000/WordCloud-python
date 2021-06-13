import  wordcloud
from matplotlib import pyplot as plt

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]
    words_list = file_contents.translate(str.maketrans('', '', punctuations)).split() #remove punctuations
    words_list = list(filter(lambda word: word not in uninteresting_words, words_list)) #uninteresting words
    word_frequencies = count_words_occurrences_in_list(words_list)
    print(word_frequencies)
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequencies)
    return cloud.to_array()

def count_words_occurrences_in_list(words_list):
    words_occurrences = {}
    for word in words_list:
        if not word in words_occurrences:
            words_occurrences[word] = 1
        else:
            words_occurrences[word] += 1
    return words_occurrences
with open('./test_file.txt', 'r') as f:
    file_contents = f.read()
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation='nearest')
    plt.axis('off')
    plt.show()
