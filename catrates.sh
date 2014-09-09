
C0=$(grep -e "^0 " etimo.txt-\(rs-4\).4.enum | wc -l)
C1=$(grep -e "^1 " etimo.txt-\(rs-4\).4.enum | wc -l)
C2=$(grep -e "^2 " etimo.txt-\(rs-4\).4.enum | wc -l)

echo No $C0
echo Ni $C1
echo Si $C2

echo $C0 + $C1 + $C2 | bc
