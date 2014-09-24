
FNAME=etimo.txt-rs-4.4.enum
grep -e "^0 " $FNAME | cut -d ' ' -f 3 > $FNAME.blacklist
grep -e "^1 " $FNAME | cut -d ' ' -f 3 > $FNAME.ni
grep -e "^2 " $FNAME | cut -d ' ' -f 3 > $FNAME.ok
