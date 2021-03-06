/*
    Title: whatabook.init.sql
    Author: Salahauddin Faisal
    Date: March 06, 2021
    Description: WhatABook database Creation and initialization. 
*/


DROP USER IF EXISTS 'whatabook_user'@'localhost';

------User creation
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

------Granting all  privilages to the user
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fkBook;
ALTER TABLE wishlist DROP FOREIGN KEY fkUser;

------ Drop tables if exists
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

------creating the tables 
CREATE TABLE book (
    bookID    INT             NOT NULL    AUTO_INCREMENT,
    bookName   VARCHAR(250)    NOT NULL,
    authorName      VARCHAR(250)    NOT NULL,
    descriptions     VARCHAR(700),
    PRIMARY KEY(bookID)
);

CREATE TABLE store (
    storeID  INT             NOT NULL    AUTO_INCREMENT,
    location      VARCHAR(400)    NOT NULL,
    PRIMARY KEY(storeID)
);

CREATE TABLE user (
    userID         INT         NOT NULL    AUTO_INCREMENT,
    firstName     VARCHAR(95) NOT NULL,
    lastName       VARCHAR(95) NOT NULL,
    PRIMARY KEY(userID) 
);

CREATE TABLE wishlist (
    wishlistID     INT         NOT NULL    AUTO_INCREMENT,
    userID         INT         NOT NULL,
    bookID        INT         NOT NULL,
    PRIMARY KEY (wishlistID),
    CONSTRAINT fkBook
    FOREIGN KEY (bookID)
        REFERENCES book(bookID),
    CONSTRAINT fkUser
    FOREIGN KEY (userID)
        REFERENCES user(userID)
);
------book record insertion 
INSERT INTO book(bookName, authorName, descriptions)
    VALUES('Murachs MySQL', 'Joel Murach', 'Great book for mastering MySQL');

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('In Search of Lost Time', 'Marcel Proust', "Swanns Way, the first part of A la recherche de temps perdu");

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('Ulysses', 'James Joyce', 'Ulysses chronicles the passage of Leopold Bloom');

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('Don Quixote', 'Miguel de Cervantes', 'Alonso Quixano, a retired country gentleman in his fifties');

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', "One of the 20th centurys enduring works");

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald', 'The novel chronicles an era that Fitzgerald himself dubbed the "Jazz Age"');

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('Moby Dick', 'Herman Melville', "First published in 1851, Melville's masterpiece is, in Elizabeth Hardwick's words");


INSERT INTO book(bookName, authorName, descriptions)
    VALUES('War and Peace', 'Leo Tolstoy', 'Epic in scale, War and Peace delineates in graphic detail events');

INSERT INTO book(bookName, authorName, descriptions)
    VALUES('Hamlet', 'William Shakespeare', 'The Tragedy of Hamlet');


  -----inserting store record 


INSERT INTO store(location)
    VALUES('555 Manhattan Street, New York, NY 10010');


-----inserting user

INSERT INTO user(firstName, lastName) 
    VALUES('john', 'smith');

INSERT INTO user(firstName, lastName)
    VALUES('jane', 'doe');

INSERT INTO user(firstName, lastName)
    VALUES('jennifer', 'smith');
    



------wishlist insertions

INSERT INTO wishlist(bookID, userID)
    VALUES ((SELECT bookID FROM book WHERE bookName = 'Hamlet'),
	    (SELECT userID FROM user WHERE firstName = 'John'));


INSERT INTO wishlist(bookID, userID)
    VALUES ((SELECT bookID FROM book WHERE bookName = 'Moby Dick'),
	    (SELECT userID FROM user WHERE firstName = 'Jane'));


INSERT INTO wishlist(bookID, userID)
    VALUES ((SELECT bookID FROM book WHERE bookName = 'War and Peace'),
	    (SELECT userID FROM user WHERE firstName = 'Jennifer'));



















