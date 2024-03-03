# Shell Script to display a list of all files in the pwd.
# Run "chmod +x Q6.sh" before running
# $# variable stores total number of arguments
# $@ varibale stores the individual arguements

if [ $# -lt 1 ]
then
	echo "Missing Arguments."
	exit
fi
for dname in "$@"
do
	if [ -d "$dname" ]
	then
		cd "$dname" || exit
		ls > list
		exec < list
		while read -r line
		do
			if [ -f "$line" ]
			then
				if [ -r "$line" ] && [ -w "$line" ] #check read, write permissions of said files
				then
					echo "$line has rw the permissions. "
				else
					echo "files not having all permissions. "
				fi
			fi
		done < list
		rm list
		cd - > /dev/null #Return pwd to original directory
	else
		echo "$dname is not a directory."
	fi
done
