#!/usr/bin/env python2

import time
import sys
from select import hamming, load_words

def main():


    www = load_words(sys.argv[1])
    den = len(www)-1
    #print www
    
    out = []
    t = time.time()
    for i,w in enumerate(www):
        # compute min h distance for w
        minh = None
        s = 0
        for u in www:
            if w==u:
                continue
            h = hamming(u,w)
            s += h
            if minh == None or h<minh:
                minh = h
        avg = 1.*s / den
        avgl = avg / len(w)
        out.append((w,minh,avg,avgl))
        # log
        if i%100 == 0:
            if time.time() - t > 10:
                print '%d %.2fs %s %d %.2f %.2f' % (i,time.time()-t,w,minh,avg,avgl)
                t = time.time()

    orders = [
        (sys.argv[1]+'.minh.len', lambda x: len(x[0]), False),
        (sys.argv[1]+'.minh.minh', lambda x: x[1], True),
        (sys.argv[1]+'.minh.avg', lambda x: x[2], True),
        (sys.argv[1]+'.minh.avgl', lambda x: x[3], True),
    ]

    for fname,key,reverse in orders:
        with open(fname+'.words','w') as fw:
            with open(fname,'w') as f:
                for w in sorted(out, key = key, reverse = reverse):
                    fw.write(w[0]+'\n')
                    f.write('%s %d %.2f %.2f\n' % (w[0],w[1],w[2],w[3]))

if __name__=="__main__":
    main()
