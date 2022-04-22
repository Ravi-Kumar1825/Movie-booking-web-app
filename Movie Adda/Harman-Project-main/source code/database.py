import sqlite3
con=sqlite3.connect("Movie_Adda.db")


"""

con.execute('''create table user 
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name text not null,
Mobile long int not null,
Gender text not null,
Email varchar(20) not null,
Date_of_Birth date not null,
Place varchar(255) not null,
Password varchar(20) not null);''')

con.execute('''create table theater 
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
Owner_Name varchar(255) not null,
Password varchar(50) not null,
Theater_Name varchar(255) not null,
Place varchar(255) not null,
Timing varchar(100) not null,
Food text not null,
Number_Of_Screen int not null);''')

con.execute('''create table movies 
(Movie_Name varchar(255) not null,
Theater_Name varchar(255) not null,
Duration varchar(50) not null,
Release_Date text not null,
Ratings text not null,
Languages_available varchar(100) not null,
Genre text not null,
Ticket_cost text not null,
Image varchar(100),
Description varchar(255) not null,
trailer varchar(255) not null);''')

con.execute('''create table payment
(Username varchar(50),
Movie_name varchar(50),
Ticket_cost long int);''')


"""



