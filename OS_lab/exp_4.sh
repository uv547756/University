# if-then-fi:

a=10
b=10
if [ $a -eq $b ]
then
	echo "a is equal to b"
fi

# if-then-else-fi

if [ $a -eq $b ]
then
	echo "a is equal to b"
else
	echo "a is not equal to b"
fi

# nested if-else

val=`expr $a + $b`
if [ $val -eq 30 ]
then
	echo "a+b is equal to 30"
else
	if [ $val -eq 20 ]
	then
		echo "a+b is equal to 20"
	fi
fi



