read -p 'Enter a:' a
read -p 'Enter b:' b

if [ "$a" == "Hello" ] && [ "$b" == "Hello" ]; then
    echo "Both inputs are the same"
else
    echo "Both inputs are not the same"
fi

if [ "$a" == "Hello" ] || [ "$b" == "Hello" ]; then
    echo "At least one of the inputs is 'Hello'"
else
    echo "None of the inputs are 'Hello'"
fi

if [ ! "$a" == "Hello" ]; then
    echo "a was initially not 'Hello'"
else
    echo "a was initially 'Hello'"
fi

