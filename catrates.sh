
FNAME=etimo.txt-rs-3.4.grouped
C0=$(grep -e "^[03] " $FNAME | wc -l)
C1=$(grep -e "^1 " $FNAME | wc -l)
C2=$(grep -e "^2 " $FNAME | wc -l)

echo No $C0
echo Ni $C1
echo Si $C2

echo $C0 + $C1 + $C2 | bc
echo -n "SI "
echo 979 + $C2 | bc
