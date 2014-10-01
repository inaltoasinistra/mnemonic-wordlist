#!/usr/bin/env python2

import sys

def main():
    
    with open('english.txt') as f:
        eng = [x.strip() for x in f]
    with open('italian.txt') as f:
        ita = [x.strip() for x in f]

    assert len(eng)==2048
    assert len(ita)==2048

    engt = {}
    itat = {}
    for e,i in zip(eng,ita):
        engt[e] = i
        itat[i] = e

    seed = sys.argv[1:]

    if set(seed) <= set(ita):
        table = itat
    elif set(seed) <= set(eng):
        table = engt
    else:
        assert False, 'Invalid seed'

    print ' '.join( [table[x] for x in seed] )

if __name__=="__main__":
    main()
