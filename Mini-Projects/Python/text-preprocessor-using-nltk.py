import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
# Replace the placeholder text with your text in order to preprocess it
text = """
Add your text here which needs to be preprocessed.
Pre-processing includes removal of noise, Tokenization, stop words removal and Text Normalization
Text normalization consists of stemming and lemmatization.
Have a look at the code below which removes all the unnecessary data.
"""
def text_preprocessor(text):

# remove punctuation and convert text to lower case
      filtered_text = re.sub(r"[\W]"," ", text)

# Tokenizing the text 
      word_tokenized_text = word_tokenize(filtered_text)
      sentence_tokenized_text = sent_tokenize(filtered_text)

# stop words removal
      stop_words = set(stopwords.words('english'))
      stop_words_removed_tokenized_text = [word for word in word_tokenized_text if word not in stop_words]

# Text Normalization
      stemmer = PorterStemmer()
      lemmatizer = WordNetLemmatizer()
      final_normalized_text = [lemmatizer.lemmatize(stemmer.stem(word)) for word in stop_words_removed_tokenized_text]

      return final_normalized_text

print(text_preprocessor(text))