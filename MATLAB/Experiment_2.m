% A = [1 4 7 10; 2 5 8 11; 3 6 9 12];
% B = reshape(A, 2, 6);
% B
% A
% A = [1, 2; 3, 4];
% B = [5, 6; 7, 8];
% C = [A, B]; % Concatenate A and B horizontally, resulting in a 2x4 matrix
% C, A,B
% A = [1 2 3 4; 5 6 7 8; 9 10 11 12];
% B = circshift(A, [0 2]); % Shift the columns of A to the right by 2
% disp('This is a sentence printed in MATLAB without storing it in a variable.');
% A,B
% A = [1, 2; 3, 4];
% newSize = [3, 3];
% B = zeros(newSize);
% B
% B(1:size(A, 1), 1:size(A, 2)) = A;
% A,B
% size(A,1)

% % Create a 3x3 matrix
% A = [5 2 9; 1 7 6; 3 4 8];
% A
% % 
% % % Indexing
% % disp( A(2, 3)); % Access the element in the second row and third column
% 
% % Sorting
% A = sortrows(A,'descend'); % Sort the rows of A in ascending order
% A
% A = sort(A, 1,'descend'); % Sort the columns of A in ascending order
% A
% A = [5 2 9; 1 7 6; 3 4 8];
% A
% % Flip the matrix about a vertical axis
% B = fliplr(A);
% B
% C = flipud(A);
% C

% Create arrays X and Y of size 1*N
N = 5;
X = randi([1, 10], 1, N);
Y = randi([1, 10], 1, N);
% X,Y

% Relational operations
Z1 = X > Y; % Element-wise greater than comparison
Z1
Z2 = X == Y; % Element-wise equality comparison
Z2

% Logical operations
Z3 = ~Z1; % Element-wise logical NOT
Z4 = Z1 & Z2; % Element-wise logical AND
Z4
Z5 = Z1 | Z2; % Element-wise logical OR