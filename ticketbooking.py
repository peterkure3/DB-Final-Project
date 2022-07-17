import csv

from cs50 import SQL

open("ticketbookings.db", "w").close()

db = SQL("sqlite:///ticketbookings.db")

db.execute("CREATE TABLE customers(id INTEGER, name TEXT, email TEXT, accessnumber INTEGER, PRIMARY KEY(id))")

db.execute("CREATE TABLE tickets(ticket_id INTEGER, name TEXT, viewer TEXT, FOREIGN KEY(ticket_id) REFERENCES customers(id))")

db.execute("CREATE TABLE movies(movie_id INTEGER, movie TEXT, viewer TEXT, movie_number INTEGER, FOREIGN KEY(movie_id) REFERENCES customers(id))" )

with open("ticketbookings.csv","r") as file:
    reader = csv.DictReader(file)

    # for row in reader:
    #     name = row["Name"].upper()
    #     accessnumber=row["Access Number"]
    #     email=row["Email"]
        
    #     viewer=row["Viewing"]

    #     nameid = db.execute("INSERT INTO customers (name, accessnumber, email) VALUES(?,?,?)", name, accessnumber, email)

    #     ticket_id = row["Ticket Number"]
    #     db.execute("INSERT INTO tickets(ticket_id, viewer) VALUES(?,?)",ticket_id, viewer)

    #     movieId=row["Movie"]
    #     db.execute("INSERT INTO movies(movie_id) VALUES(?)",movieId)
    for row in reader:
        name = row["Name"].upper()
        accessnumber=row["Access Number"]
        email=row["Email"]

        id=db.execute("INSERT INTO customers(name,email,accessnumber) VALUES(?,?,?)",name,email,accessnumber)
        
        
        ticket_id=id
        name = row["Name"].upper()
        viewer=row["Viewing"]
        ticket_id=db.execute("INSERT INTO tickets(ticket_id,name,viewer) VALUES(?,?,?)",ticket_id,name,viewer)

        
        movie=row["Movie"]
        movie_id=id
        movie_number=row["MovieID"]
        viewer=row["Viewing"]
        id = db.execute("INSERT INTO movies(movie_id,movie, movie_number, viewer) VALUES(?,?,?,?)",movie_id,movie, movie_number,viewer)

        # # ticketid=row["Ticket Number"]
        



