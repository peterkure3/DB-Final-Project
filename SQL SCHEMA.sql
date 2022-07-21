CREATE DATABASE ticketbookings.db;

CREATE TABLE customers(id INTEGER, name TEXT, email TEXT, accessnumber INTEGER, phone TEXT, PRIMARY KEY(id));
CREATE TABLE tickets(ticket_id INTEGER, name TEXT, viewer TEXT, FOREIGN KEY(ticket_id) REFERENCES customers(id));
CREATE TABLE movies(movie_id INTEGER, movie TEXT, viewer TEXT, movie_number INTEGER, FOREIGN KEY(movie_id) REFERENCES customers(id));
