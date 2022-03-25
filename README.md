# Sentiment-Analysis

## Project flow :
* Libraries import 
* Setting Stopwards  
* Pre-processing 
* Token vectorization 
* Build Model 
* Model evaluation 

 
 **Set stopwords :** here stopwords are downloaded from nltk then created a set of all the stopwords for the English words 

**Pre-processing :** At first we have created a helper function to get rid of all the unwanted columns. It deletes redundant column to which we will pass the dataframe and columns that is to be deleted 

Here we have performed 5 steps for pre-processing textual data 
* Casting 
* Noise removal 
* Tokenization 
* Stopword Removal 
* Text Normalization (Stemming and Lemmatization)

**Casing :** for converting all the letters to lowercase 

**Noise removal :** For eliminating unwanted characters such as html tags, punctuation marks, special characters and whitespaces so on. 

**Tokenization :** Converting all tweets into tokens and all of those tokens would be words that are separated by spaces in the text.

**Stopword removal :** these are some of the words that do not actually make sense in contributing to the ML model. A list of stopwords are defined by the nltk library 

**Text normalization :** it is done using two methods that is stemming operation and lemmatization 
**Stemming :** it includes elimination of all the fixes that is prefixes, suffixes, infixes. Removal of all those from a word is necessary in order to obtain a word stem basically to reach the root of the word. Stemmer that we have imported porter stemmer most widely used because it is very fast and generally stemming chops off the end of the word.
**Lemmatization :** stemming sometimes looses it's actual meaning while getting the root of the word so lemmatization is better to use because it reduces the infected word properly by ensuring it's morphological analysis and vocabulary. It returns the base or the dictionary form of a word which is also known as lemma.
Vectorising tokens : vectorization is basically a process of converting tokens to numbers and it is very important because ML algorithms do not work with textual data they work with numbers. Here we are using TfidfVectoriser ( term frequency inverse document frequency)  it is a numerical statistic that is intended to reflect how important a word is to document in a corpus.

Splitting data : train test split for reserving a set of the data for training purposes and a set of data for testing purposesAccuracy score - to find out how accurate our model is 
