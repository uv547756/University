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



// RECORD
create table authors(author_id number(3) PRIMARY KEY, fname varchar(10) NOT NULL, lname varchar(10) NOT NULL, dob DATE);

create table categories(category_id number(3) PRIMARY KEY, category_name varchar(10) NOT NULL);

create table books(book_id number(3) PRIMARY KEY, title varchar(10) NOT NULL, author_id number(3), category_id number(3),
 pub_date DATE, FOREIGN KEY(author_id) references authors(author_id), 
FOREIGN KEY (category_id) REFERENCES categories(category_id));

create table members(member_id number(3) PRIMARY KEY, 
fname varchar(10) NOT NULL,
lname varchar(10) NOT NULL,
mem_date DATE);

create table borrow_transactions(trans_id number(3) PRIMARY KEY, 
book_id number(3),
member_id number(3),
borrow_date DATE NOT NULL,
return_date DATE,
FOREIGN KEY(book_id) REFERENCES members(member_id));

INSERT INTO authors (author_id, fname, lname, dob) VALUES (1, 'Jane', 'Austen', '16-DEC-75'); 
INSERT INTO authors (author_id, fname, lname, dob) VALUES (2, 'George', 'Orwell', '25-JUN-03'); 
INSERT INTO authors (author_id, fname, lname, dob) VALUES (3, 'Mark', 'Twain', '30-NOV-35'); 
INSERT INTO authors (author_id, fname, lname, dob) VALUES (4, 'J.K.', 'Rowling', '31-JUL-65');
