FILES=
for i in $*
do
    git mv final.$i double.$i
    FILES=$FILES' final.$i double.$i'
done
git commit -m 'Double check' $FILES
