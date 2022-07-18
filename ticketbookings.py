import csv

from cs50 import SQL

open("ticketbookings.db", "w").close()

db = SQL("sqlite:///ticketbookings.db")

db.execute("CREATE TABLE customers(id INTEGER, name TEXT, email TEXT, accessnumber INTEGER, phone TEXT, PRIMARY KEY(id))")

db.execute("CREATE TABLE tickets(ticket_id INTEGER, name TEXT, viewer TEXT, FOREIGN KEY(ticket_id) REFERENCES customers(id))")

db.execute("CREATE TABLE movies(movie_id INTEGER, movie TEXT, viewer TEXT, movie_number INTEGER, FOREIGN KEY(movie_id) REFERENCES customers(id))" )

with open("ticketbookings.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"].upper()
        accessnumber=row["Access Number"]
        email=row["Email"]
        phone=row["Phone Number"]

        id=db.execute("INSERT INTO customers(name,email,accessnumber,phone) VALUES(?,?,?,?)",name,email,accessnumber,phone)
        
        
        ticket_id=id
        name = row["Name"].upper()
        view=row["Viewing"]
        ticket_id=db.execute("INSERT INTO tickets(ticket_id,name,viewer) VALUES(?,?,?)",ticket_id,name,view)

        
        movie=row["Movie"]
        movie_id=id
        movie_number=row["MovieID"]
        viewer=row["Viewing"]
        id = db.execute("INSERT INTO movies(movie_id,movie, movie_number, viewer) VALUES(?,?,?,?)",movie_id,movie, movie_number,view)
        



