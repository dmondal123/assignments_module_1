CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
 RETURN (
     # Write your MySQL query statement below.
   SELECT DISTINCT(sub.salary) FROM
   (
       SELECT salary, dense_rank() OVER (order by salary DESC) AS r
       FROM employee) AS sub
       WHERE sub.r = N


 );
END
