git add $1
concatenated=""
for arg in "${@:2}"; do
    concatenated="concatenated $arg"
done
git commit -m "$concatenated"
git push

