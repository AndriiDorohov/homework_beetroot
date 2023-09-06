-- Task 1
-- Create a table
-- Create a table of your choice inside the sample SQLite database,
-- rename it, and add a new column. Insert a couple rows inside your table.
-- Also, perform UPDATE and DELETE statements on inserted rows.

-- As a solution to this task, create a file named: task1.sql, with all
-- the SQL statements you have used to accomplish this task



-- terminal command: sqlite3 new.db
CREATE TABLE emp(empid INTEGER NOT NULL PRIMARY KEY, empname TEXT NOT NULL, email TEXT NOT NULL);
-- terminal command: .quit
-- terminal command: mv new.db newdatabase.db
INSERT INTO emp (empid, empname, email) VALUES (1, 'Ket', 'keaaas@gmail.com');
INSERT INTO emp (empid, empname, email) VALUES (2, 'Met', 'meaaas@gmail.com');
INSERT INTO emp (empid, empname, email) VALUES (3, 'Bet', 'beaaas@gmail.com');
INSERT INTO emp (empid, empname, email) VALUES (4, 'Sia', 'siaaas@gmail.com');
SELECT * FROM emp;
UPDATE emp SET email = 'metmet@gmail.com' WHERE empid = 2;
SELECT * FROM emp;
DELETE FROM emp WHERE empname = 'Bet';
SELECT * FROM emp;
