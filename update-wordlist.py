#!/usr/bin/env python2

'''USAGE: update-wordlist.py <well formed list> <new list>
return: words of the new list that can be added to the first one'''

import sys
from select import hamming, load_words, fourfilter, remove_similars

def main():

    if len(sys.argv)!=3:
        print __doc__
        sys.exit(1)

    www = load_words(sys.argv[1])
    new = load_words(sys.argv[2])

    wwwnew = www + new
    remove_similars(wwwnew,3) # keeps
    new = set(fourfilter(wwwnew,4)) - set(www)

    for w in sorted(new):
        print w


if __name__=="__main__":
    main()
