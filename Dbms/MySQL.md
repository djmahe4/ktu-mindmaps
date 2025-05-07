Below is a comprehensive tutorial that starts completely from scratch. We’ll create our sample tables, insert some values, and then run a series of queries to illustrate a wide range of SQL topics—from basic retrievals and sorting to set operations, grouping, joins, subqueries, views, assertions, and triggers.

For this tutorial, we’ll use two main tables: a **staff** table and a **dep** (department) table. We’ll also create a **Student** table later for the trigger example. Feel free to run these commands in your SQL environment (adjusting data types or syntax as needed for your specific DBMS).

---

## 1. Creating Tables and Inserting Values

### a) Creating the Department and Staff Tables

We start by creating a table for departments and one for staff. The **staff** table will reference **dep** by a foreign key.

```sql
-- Create the department (dep) table
CREATE TABLE dep (
    dno INT PRIMARY KEY,
    dname VARCHAR(100),
    block VARCHAR(50)
);

-- Create the staff table with a foreign key reference to dep
CREATE TABLE staff (
    sno INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    dno INT,
    CONSTRAINT fk_dep FOREIGN KEY (dno) REFERENCES dep(dno)
);
```

### b) Inserting Sample Data into dep and staff

Now insert sample records into each table.

```sql
-- Insert sample departments
INSERT INTO dep (dno, dname, block) VALUES
    (101, 'Finance', 'Block A'),
    (102, 'HR', 'Block B'),
    (103, 'IT', 'Block C');

-- Insert sample staff records
INSERT INTO staff (sno, name, position, salary, dno) VALUES
    (1, 'Alice', 'Manager', 7500, 101),
    (2, 'Bob', 'Project Manager', 6800, 102),
    (3, 'Charlie', 'Clerk', 4000, 101),
    (4, 'David', 'Manager', 8000, 103),
    (5, 'Eve', 'Project Manager', 6500, 101);
```

---

## 2. Basic Retrieval, Filtering, and Sorting

### a) Simple SELECT and WHERE

Retrieve all staff names:

```sql
SELECT name
FROM staff;
```

Retrieve staff names and salaries for employees who earn more than 5000, sorted in descending order:

```sql
SELECT name, salary
FROM staff
WHERE salary > 5000
ORDER BY salary DESC;
```

---

## 3. Set Operations

These examples assume that you have compatible queries; note that not all SQL dialects support every operation (e.g., `INTERSECT` and `MINUS` may require Oracle or PostgreSQL).

### a) UNION

Combine results from two queries (removes duplicates):

```sql
SELECT name
FROM staff
WHERE position = 'Manager'
UNION
SELECT name
FROM staff
WHERE position = 'Project Manager';
```

### b) UNION ALL

Combine results while keeping duplicates:

```sql
SELECT name
FROM staff
WHERE position = 'Manager'
UNION ALL
SELECT name
FROM staff
WHERE position = 'Project Manager';
```

### c) INTERSECT

Return only those names common to both queries:

```sql
SELECT name
FROM staff
WHERE position = 'Manager'
INTERSECT
SELECT name
FROM staff
WHERE salary > 7000;
```

### d) MINUS (or EXCEPT)

Return the names present in the first query but not in the second:

```sql
SELECT name
FROM staff
WHERE position = 'Manager'
MINUS
SELECT name
FROM staff
WHERE salary < 6000;
```

---

## 4. Aggregate Functions, Grouping, and Filtering

### a) Aggregates

Count the number of managers and sum their salaries:

```sql
SELECT COUNT(sno) AS total_managers, SUM(salary) AS sum_salary
FROM staff
WHERE position = 'Manager';
```

### b) GROUP BY with HAVING

Find the average salary by department and list only those departments where the average wage is above 5000:

```sql
SELECT dno, AVG(salary) AS avg_salary
FROM staff
GROUP BY dno
HAVING AVG(salary) > 5000;
```

---

## 5. Joining Tables

### a) INNER JOIN

Retrieve staff names along with their corresponding department names:

```sql
SELECT s.name, d.dname
FROM staff s
INNER JOIN dep d ON s.dno = d.dno;
```

### b) LEFT JOIN

List all staff details along with department information (if available):

```sql
SELECT s.name, s.position, d.dname
FROM staff s
LEFT JOIN dep d ON s.dno = d.dno;
```

### c) RIGHT JOIN

List all departments even if there is no matching staff record:

```sql
SELECT s.name, s.position, d.dname
FROM staff s
RIGHT JOIN dep d ON s.dno = d.dno;
```

---

## 6. Subqueries and Nested Queries

### a) Non-Correlated Subquery – Single-Row Example

Retrieve the details of the highest-paid employee:

```sql
SELECT *
FROM staff
WHERE salary = (SELECT MAX(salary) FROM staff);
```

### b) Non-Correlated Subquery – Multiple-Row Example

Retrieve staff working in the Finance department:

```sql
SELECT *
FROM staff
WHERE dno IN (SELECT dno FROM dep WHERE dname = 'Finance');
```

### c) Correlated Subquery

List each staff member whose salary is above the average salary for their own position:

```sql
SELECT s.name, s.salary
FROM staff s
WHERE s.salary > (
    SELECT AVG(salary)
    FROM staff
    WHERE position = s.position
);
```

---

## 7. Creating and Using SQL Views

Views allow you to save frequently used queries as virtual tables.

### a) Creating a View

Create a view that lists high-earning staff (salary greater than 7000):

```sql
CREATE VIEW high_earning_staff AS
SELECT name, position, salary
FROM staff
WHERE salary > 7000;
```

### b) Querying the View

```sql
SELECT * FROM high_earning_staff;
```

### c) Updating the View

*Note:* Not all views are updatable. In systems where they are, you can run something like:

```sql
UPDATE high_earning_staff
SET salary = salary * 1.1
WHERE position = 'Manager';
```

---

## 8. Assertions and Triggers

### a) Assertion Example

Assertions ensure overall database consistency by enforcing conditions. (Keep in mind that many DBMS—like MySQL—do not support assertions.)

```sql
CREATE ASSERTION salary_staff CHECK (
    NOT EXISTS (
        SELECT *
        FROM staff
        WHERE position = 'Manager'
          AND salary < (SELECT MIN(salary)
                        FROM staff
                        WHERE position = 'Project Manager')
    )
);
```

### b) Creating a Table for Triggers

Let’s create a **Student** table for a trigger example. This table will hold a student’s marks in three subjects along with calculated total and percentage.

```sql
CREATE TABLE Student (
    roll INT PRIMARY KEY,
    name VARCHAR(100),
    subj1 INT,
    subj2 INT,
    subj3 INT,
    total INT DEFAULT 0,
    per DECIMAL(5,2) DEFAULT 0.0
);
```

### c) Creating a Trigger

In this example (using MySQL syntax), the trigger will automatically calculate the total marks and percentage before a new record is inserted.

```sql
DELIMITER //

CREATE TRIGGER before_student_insert
BEFORE INSERT ON Student
FOR EACH ROW
BEGIN
    SET NEW.total = NEW.subj1 + NEW.subj2 + NEW.subj3;
    SET NEW.per = (NEW.total * 100) / 300;  -- Assuming each subject is out of 100 marks
END;
//

DELIMITER ;
```

### d) Testing the Trigger

Insert a sample record to see the trigger in action:

```sql
INSERT INTO Student (roll, name, subj1, subj2, subj3)
VALUES (1, 'John', 80, 90, 85);

-- Verify the computed total and percentage:
SELECT * FROM Student;
```

---

## Final Thoughts

This end-to-end example has covered:

- **Table creation and data insertion**
- **Basic SELECT, WHERE, and ORDER BY clauses**
- **Set operations** (UNION, UNION ALL, INTERSECT, MINUS)
- **Aggregate functions with GROUP BY and HAVING**
- **Different types of JOINs** (INNER, LEFT, RIGHT)
- **Subqueries** (non-correlated and correlated)
- **Views** for more modular queries
- **Assertions** for enforcing database-wide rules
- **Triggers** to automate calculations upon data insertion

By running and modifying these examples in your environment, you’ll get hands-on experience on each topic. As you progress, consider exploring more advanced join conditions, nested subqueries with more levels, and different types of triggers to cover additional event types.

What other SQL topics would you like to dive deeper into next?
