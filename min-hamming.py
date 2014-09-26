#!/usr/bin/env python2

import time
from select import hamming, load_words

def main():

    www = load_words('ok')
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
        out.append((w,minh,1.*s/den))
        if i%100 == 0:
            if time.time() - t > 10:
                print '%d %.2fs %s %d %.2f' % (i,time.time()-t,w,minh,1.*s/den)
                t = time.time()

    with open('ok.minh','w') as f:
        for w in sorted(out, key = lambda x: x[2], reverse = True):
            f.write('%s %d %.2f\n' % (w[0],w[1],w[2]))

if __name__=="__main__":
    main()
