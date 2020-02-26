import ssl
import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import string
import nltk


def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	# filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	# return " ".join(filtered_words)
	return " ".join(tokens)


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

if __name__ == '__main__':
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # nltk.download('gutenberg')
    # nltk.download('punkt')
    # nltk.download('stopwords')

    file = open("corpus-sentence.txt", "w+")

    emma = nltk.Text(nltk.corpus.gutenberg.sents('austen-emma.txt'))
    for words in emma :
        if (len(words) >= 5 and len(words) <= 13):
            sentence = " ".join(words)
            if (not hasNumbers(sentence)) :
                preprocessed = preprocess(sentence)
                if ("_" not in preprocessed and " s " not in preprocessed and " d " not in preprocessed and " d" != preprocessed[-2:] and len(preprocessed) > 13):
                    file.write(preprocessed + "\n")

    persuasion = nltk.Text(nltk.corpus.gutenberg.sents('austen-persuasion.txt'))
    for words in persuasion :
        if (len(words) >= 5 and len(words) <= 13):
            sentence = " ".join(words)
            if (not hasNumbers(sentence)):
                preprocessed = preprocess(sentence)
                if ("_" not in preprocessed and " s " not in preprocessed and " d " not in preprocessed and " d" != preprocessed[-2:] and len(preprocessed) > 13):
                    file.write(preprocessed + "\n")

    sense = nltk.Text(nltk.corpus.gutenberg.sents('austen-sense.txt'))
    for words in sense:
        if (len(words) >= 5 and len(words) <= 13):
            sentence = " ".join(words)
            if (not hasNumbers(sentence)):
                preprocessed = preprocess(sentence)
                if ("_" not in preprocessed and " s " not in preprocessed and " d " not in preprocessed and " d" != preprocessed[-2:] and len(preprocessed) > 13):
                    file.write(preprocessed + "\n")

    caesar = nltk.Text(nltk.corpus.gutenberg.sents('shakespeare-caesar.txt'))
    for words in caesar:
        if (len(words) >= 5 and len(words) <= 13):
            sentence = " ".join(words)
            if (not hasNumbers(sentence)):
                preprocessed = preprocess(sentence)
                if ("_" not in preprocessed and " s " not in preprocessed and " d " not in preprocessed and " d" != preprocessed[-2:] and len(preprocessed) > 13):
                    file.write(preprocessed + "\n")

    hamlet = nltk.Text(nltk.corpus.gutenberg.sents('shakespeare-hamlet.txt'))
    for words in hamlet:
        if (len(words) >= 5 and len(words) <= 13):
            sentence = " ".join(words)
            if (not hasNumbers(sentence)):
                preprocessed = preprocess(sentence)
                if ("_" not in preprocessed and " s " not in preprocessed and " d " not in preprocessed and " d" != preprocessed[-2:] and len(preprocessed) > 13):
                    file.write(preprocessed + "\n")

    macbeth = nltk.Text(nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt'))
    for words in macbeth:
        if (len(words) >= 5 and len(words) <= 13):
            sentence = " ".join(words)
            if (not hasNumbers(sentence)):
                preprocessed = preprocess(sentence)
                if ("_" not in preprocessed and " s " not in preprocessed and " d " not in preprocessed and " d" != preprocessed[-2:] and len(preprocessed) > 13):
                    file.write(preprocessed + "\n")

    
    file.close()

