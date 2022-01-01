### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is a relational database management system

- What is the difference between SQL and PostgreSQL?
SQL is a language designed to manage and manipulate data on a relational database system while postgreSQL is an RDBMS which uses SQL to maniplate and manage .

- In `psql`, how do you connect to a database?
using the command \c databaseName

- What is the difference between `HAVING` and `WHERE`?
The main difference between them is that the WHERE clause is used to specify a condition for filtering records before any groupings are made, while the HAVING clause is used to specify a condition for filtering values from a group.

- What is the difference between an `INNER` and `OUTER` join?
The major difference between inner and outer joins is that inner joins result in the intersection of two tables, whereas outer joins result in the union of two tables

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
The key difference between a left outer join, and a right outer join is that in a left outer join it's the table in the FROM clause whose all rows are returned. Whereas, in a right outer join we are returning all rows from the table specified in the join clause

- What is an ORM? What do they do?
An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  almost same

- What is CSRF? What is the purpose of the CSRF token?
A CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. 

The tokens are generated and submitted by the server-side application in a subsequent HTTP request made by the client.

After the request is made, the server side application compares the two tokens found in the user session and in the request. If the token is missing or does not match the value within the user session, the request is rejected, the user session terminated and the event logged as a potential CSRF attack.

- What is the purpose of `form.hidden_tag()`?
The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks
