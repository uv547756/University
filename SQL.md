INSERT INTO Authors (AuthorID, FirstName, LastName, BirthDate) VALUES (1, 'Jane', 'Austen', '16-DEC-75');
INSERT INTO Authors (AuthorID, FirstName, LastName, BirthDate) VALUES (2, 'George', 'Orwell', '25-JUN-03');
INSERT INTO Authors (AuthorID, FirstName, LastName, BirthDate) VALUES (3, 'Mark', 'Twain', '30-NOV-35');
INSERT INTO Authors (AuthorID, FirstName, LastName, BirthDate) VALUES (4, 'J.K.', 'Rowling', '31-JUL-65');

INSERT INTO Categories (CategoryID, CategoryName) VALUES (1, 'Fiction');
INSERT INTO Categories (CategoryID, CategoryName) VALUES (2, 'Science Fiction');
INSERT INTO Categories (CategoryID, CategoryName) VALUES (3, 'Historical');
INSERT INTO Categories (CategoryID, CategoryName) VALUES (4, 'Fantasy');

INSERT INTO Books (BookID, Title, AuthorID, CategoryID, Pub_Date) VALUES (1, 'Pride and Prejudice', 1, 1, '28-JAN-13');
INSERT INTO Books (BookID, Title, AuthorID, CategoryID, Pub_Date) VALUES (2, '1984', 2, 2, '8-JUN-49');
INSERT INTO Books (BookID, Title, AuthorID, CategoryID, Pub_Date) VALUES (3, 'Adventures of Huckleberry Finn', 3, 3, '10-DEC-84');
INSERT INTO Books (BookID, Title, AuthorID, CategoryID, Pub_Date) VALUES (4, 'Harry Potter and the Sorcerers Stone', 4, 4, '26-JUN-97');

INSERT INTO Members (MemberID, FirstName, LastName, MembershipDate) VALUES (1, 'Alice', 'Smith','15-JAN-23');
INSERT INTO Members (MemberID, FirstName, LastName, MembershipDate) VALUES (2, 'Bob', 'Johnson', '22-MAR-23');
INSERT INTO Members (MemberID, FirstName, LastName, MembershipDate) VALUES (3, 'Carol', 'Williams', '10-MAY-23');
INSERT INTO Members (MemberID, FirstName, LastName, MembershipDate) VALUES (4, 'David', 'Brown','30-JUL-23');
