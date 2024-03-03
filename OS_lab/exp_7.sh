#While Statement
echo Running While Loop
a=0
while [ $a -lt 10 ]
do
	echo $a
	a=`expr $a + 1`
done

#Until Statement
echo; echo Now running Until Loop
b=0
until [ $b -gt 10 ]
do
	echo $b
	b=`expr $b + 1`
done

#Break statement
echo; echo demonstrating Break statement
c=0
while [ $c -lt 10 ]
do
	echo $c
	if [ $c -eq 5 ]
	then
		echo stopping loop as c=5.
		break
	fi
	c=`expr $c + 1`
done

#For Loop
echo; echo Now running For loop
for a in 1 2 3
do
	for b in 0 5
	do
		if [ $a -eq 2 -a $b -eq 2 ]
		then
			break 
		else
			echo "$a $b"
		fi
	done
done
	
