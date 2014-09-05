#!/usr/bin/env python2

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
    #www = www[:1000]

    print '?',len(www)


    while True:

        print 'New cycle'
        ht = hamming_table(www)
        min_h = min(ht.keys())
    
        #for h in sorted(ht.keys()):
        #    print 'Hamming:',h
        #    print 'Couples:',['(%s %s)'%(www[x],www[y]) for x,y in ht[min_h]]

        # remove a word for each couple
        to_remove = set([www[x[0]] for x in ht[min_h]])
        #print to_remove
        for word in to_remove:
            www.remove(word)

        print '?',len(www), min_h

        if len(www) < 30000:
            break

        
    with open('italian.out','w') as f:
        f.writelines([x+'\n' for x in www])
