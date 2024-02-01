%Given Vector:
x = [1 8 3 9 0 1];

%Sum of all it's elements using sum() function:
s = sum(x);

%Running Sum of all the elements in the Vector:
runningSum = sum(hankel([zeros(1, numel(x)-1), x(1)], x))

%Generating a random sequence of numbers in the vector using rand()
seq = rand(1,20);

%Plotting the sequence:
plot(seq)
title('Random Sequence')
xlabel('Index');
ylabel('Value');