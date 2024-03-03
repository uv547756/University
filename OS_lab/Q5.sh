# Shell script that deletes all lines containing a given word

if [ $# -lt 1 ]
then
	echo "Need atleast 1 arguement."
	exit
fi
echo "Enter a word: "
read word
for fname in $@
do
	if [ -f "$fname" ]
	then
		grep -iv "$word" "$fname" > "$fname.tmp"
		mv "$fname.tmp" "$fname"
		echo "Lines containing "$word" have been deleted from "$fname"."
	else
		echo "File "$fname" not found."
	fi
done
