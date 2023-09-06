-- Task 1
-- Joins
-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)
-- As a solution to HW, create a file named: task1.sql with all SQL queries:
-- write a query in SQL to display the first name, last name, department number, and department name for each employee
-- write a query in SQL to display the first and last name, department, city, and state province for each employee
-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
-- write a query in SQL to display all departments including those where does not have any employee
-- write a query in SQL to display the first name of all employees including the first name of their manager
-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
-- write a query in SQL to display the job title and the average salary of employees
-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
-- write a query in SQL to display the department name and the number of employees in each department

SELECT employees.first_name, employees.last_name, departments.depart_name AS department_name FROM employees JOIN departments ON employees.department_id = departments.department_id;
SELECT employees.first_name, employees.last_name, departments.depart_name AS department_name, locations.city, locations.state_province AS province FROM employees JOIN departments ON employees.department_id = departments.department_id JOIN locations ON departments.location_id = locations.location_id;
SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name FROM employees JOIN departments ON employees.department_id = departments.department_id WHERE employees.department_id IN (80, 40);
SELECT depart_name FROM departments;
SELECT e1.first_name AS employee_name, COALESCE(e2.first_name, 'No manager') AS boss FROM employees e1 LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
SELECT employees.first_name, employees.last_name, jobs.job_title, (jobs.max_salary - employees.salary) AS dif_salary FROM employees JOIN jobs ON employees.job_id = jobs.job_id;

SELECT employees.first_name, employees.last_name, jobs.job_title, AVG(employees.salary) AS avg_salary FROM employees JOIN jobs ON employees.job_id = jobs.job_id GROUP BY jobs.job_title;

SELECT employees.first_name, employees.last_name, employees.salary FROM employees JOIN departments ON employees.department_id = departments.department_id JOIN locations ON departments.location_id = locations.location_id WHERE locations.city = 'London';
SELECT departments.depart_name, COUNT(employees.employee_id) AS employee_count FROM departments JOIN employees ON departments.department_id = employees.department_id GROUP BY departments.depart_name;
