#elif example:

a=10
b=20
if [ $a == $b ]
then
	echo "a is equal to b"
elif [ $a -gt $b ]
then
	echo "a is greater than b"
elif [ $a -lt $b ]
then
	echo "a is less than b"
else
	echo "None of the conditions stated are true"
fi

#case example:
echo;echo "Now running script for case structure: "

echo "enter a word"
read word
case "$word" in
	"Hello")
		echo "Hello, nice to meet you."
		;;
	
	"Bye")
		echo "...."
		;;
	*)
		echo "Default arguement is undefined."
		;;
esac
