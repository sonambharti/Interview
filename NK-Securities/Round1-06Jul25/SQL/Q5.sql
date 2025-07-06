-- A company stores the information of employees and departments in two data tables: Employee and Department. 
-- Write a query to print the respective employee name, salary, department name, and department location for each 
-- employee in the Employee table. Sort the results by employee salary in descending order, then sort those 
-- employees by name in alphabetical order

SELECT 
    E.NAME,
    E.SALARY,
    D.NAME,
    D.LOCATION
FROM 
    EMPLOYEE E
JOIN 
    DEPARTMENT D
ON 
    E.DEPT_ID = D.ID
ORDER BY 
    E.SALARY DESC,
    E.NAME ASC;
