SELECT E2.name as Employee
FROM Employee E1
INNER JOIN Employee E2 ON E1.id = E2.managerId
WHERE E1.salary < E2.salary