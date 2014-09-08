#!/usr/bin/env python2

import urllib2
import re
import os

getp = lambda u: urllib2.urlopen(u).read()

URLTEMPLATE = 'http://etimo.it/?cmd=id&id=%d&md=%s'
# (id md)
FIRSTPAGE = 'http://etimo.it/?cmd=id&id=1'

OUT = 'etimo.txt'

def main():

    words = set()

    url = FIRSTPAGE

    re_ahref = re.compile("<a href='\?cmd=id&id=(\d+)&md=([\w\d]+)'>(.+?)</a>")
    # (id, md, word)

    #cache
    if not os.path.exists('cache'):
        os.mkdir('cache')
    cachepathr = os.path.join('cache','%d')
    cachepathw = os.path.join('cache','%d')
    
    lastmaxid = 1
    lastword = 'a'
    while True:
        print 'Downloading %d, #words %d, last: %s' % (lastmaxid, len(words), lastword)
        # read cache
        if os.path.exists(cachepathr % lastmaxid):
            with open(cachepathr % lastmaxid) as f:
                page = f.read()
        else:
            # download page
            page = getp(url)

        # write cache
        if not os.path.exists(cachepathw % lastmaxid):
            with open(cachepathw % lastmaxid,'w') as f:
                f.write(page)
        
        maxid = 1
        maxidmd = None
        for id,md,word in re.findall(re_ahref,page):
            #print '>>',id,md,word
            id = int(id)
            if ',' in word:
                word = word.split(',')[0].strip()
            words.add(word.lower())

            if id>maxid:
                maxid = id
                maxidmd = md
                lastword = word

        if maxid > lastmaxid:
            #download continues
            url = URLTEMPLATE % (maxid, maxidmd)
            lastmaxid = maxid
        else:
            break

    with open(OUT,'w') as f:
        for w in sorted(words):
            f.write(w+'\n')

if __name__=="__main__":
    main()
