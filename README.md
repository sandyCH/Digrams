# Digrams
ASCII character pair frequencies in the English language.  Useful for breaking ciphers.

Decrypting ciphers, such as the two-time pad, often comes down to analyzing character
frequencies.  Digrams, or 2 character frequencies, contains even more information of
the target language.  This project generates digrams from a large collection of news
reports from Reuters available from the Natural Language Tool Kit in: 
http://www.nltk.org/install.html.  To install the python3 code and generate a dictionary
of digrams using python 3.5 or above in an Ubuntu linux environment bring up a console:

 pip3 install -U nltk
 
 python3

">>>" import nltk
">>>" nltk.download()

Go ahead and download all, then run the script digramGEN.py
This will generate a file called digrams.py which can be imported into your python crack
program and used to analyze the ciphertext against a frequency of digrams.
