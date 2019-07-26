#python3, Ubuntu linux
#Natural Language Tool Kit in: http://www.nltk.org/install.html
#NLTK Data explained in: http://www.nltk.org/data.html
#pip3 install -U nltk
#python3
# >>> import nltk
# >>> nltk.download()
#Go ahead and download all, then run the script below:
print('Working....this may take a minute or two....')

import nltk
from nltk.util import ngrams

cpus = ''
for a in nltk.corpus.reuters.fileids():
    cpus += nltk.corpus.reuters.raw(a)

chrs = [c for c in cpus]

bgs = ngrams(chrs,2)
fdist = nltk.FreqDist(bgs)

print('\nReuters 20 commonest digrams:',[(''.join(k),v) for k,v in fdist.most_common(20)])

fdic = {''.join(k):v for k,v in fdist.items()}

tot1 = sum([a for b,a in fdic.items()])
print('\nTotal digrams:',tot1)
tot2 = len([b for b,a in fdic.items()])
print('Total entries:',tot2,'\n')

outfile = open('fdc','w')
outfile.write(str(fdic))
outfile.close()
