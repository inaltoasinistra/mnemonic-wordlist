#!/usr/bin/env python2

from time import time
from random import shuffle, choice

def hamming(ww,w):
    '''
    find the hamming distance between words w and u
    '''

    l = []
    if len(w) > len(ww):
        ww,w = w,ww
        # ww is the longest

    for o in range(len(ww) - len(w) + 1):
        d = 0
        for h,k in zip(ww,' '*o + w):
            if h != k:
                d += 1
        d += len(ww) - (len(w)+o)
        l.append(d)
    return min(l)


is_alpha = lambda w: not bool([c for c in w if c<'a' or c>'z'])

def load_words(fname):
    
    with open(fname) as f:
        return [x.strip() for x in f.readlines() if len(x.strip())>=4 and is_alpha(x.strip())]

def hamming_table(www):

    table = {}
    for i in range(len(www)):
        #print 'Word:',www[i]
        for j in range(i+1,len(www)):

            if www[i][:4] == www[j][:4]:
                # One of those two words can't be selected, i'll not compere them
                continue

            h = hamming(www[i],www[j])
            value = table.get(h,[])
            value.append( (i,j) )
            table[h] = value
    return table

def fourfilter(www):
    
    table = {}
    for w in www:
        value = table.get(w[:4],[])
        value.append(w)
        table[w[:4]] = value

    out = []
    for v in table.itervalues():
        out.append(choice(v))

    return out

if __name__=="__main__":
    
    # test
    assert hamming("ciao","ciao") == 0
    assert hamming("ciao","cia") == 1
    assert hamming("mare","pare") == 1
    assert hamming("","pare") == 4
    assert hamming("re","pare") == 2
    assert hamming("ar","pare") == 2
    assert hamming("abcdefghi","d") == 8
    
    www = load_words('italian60k.txt')
    #www = load_words('italian-1000-4-2.out')

    print 'fourfilter len:', len(fourfilter(www))

    piece_dim = 1000
    min_valid_h = 4

    shuffle(www)

    parameters = (piece_dim,min_valid_h)
    
    wwww = ['# parameters -> piece_dim: %d; min_valid_h: %d' % parameters]
    for n_slice in range(len(www)/piece_dim):
        slice_index = n_slice*piece_dim
        slice_end = (n_slice+1)*piece_dim
        t = time()

        print 'slice:',n_slice,'[%d, %d)'%(slice_index,slice_end)
        
        slice = www[slice_index:slice_end]

        print '?',len(slice)

        ht = hamming_table(slice)
        remove_h = [x for x in ht.keys() if x<min_valid_h]
        print remove_h, ht.keys()
        
    
        #for h in sorted(ht.keys()):
        #    print 'Hamming:',h
        #    print 'Couples:',['(%s %s)'%(www[x],www[y]) for x,y in ht[min_h]]

        # remove a word for each couple
        to_remove = set()
        for h in remove_h:
            to_remove.update([slice[x[0]] for x in ht[h]])
            #print to_remove
        for word in to_remove:
            slice.remove(word)

        t = time()-t
        # seconds or minutes
        tw = 1000. * t / piece_dim
        tc = 's' if t<60 else 'm'
        t = t if t<60 else t/60. 
        print '?',len(slice),'time [%s]: %.2f (ms per word: %.4f)' % (tc, t, tw)

        wwww.extend(slice)
        
    print '??',len(wwww)
    print 'fourfilter len:', len(fourfilter(wwww))

    with open('italian-%d-%d.out' % parameters,'w') as f:
        f.writelines([x+'\n' for x in wwww])
