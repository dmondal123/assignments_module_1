SELECT MAX(salary) as SecondHighestSalary
FROM Employee
WHERE salary IN (SELECT salary FROM Employee MINUS SELECT MAX(salary) FROM Employee)
