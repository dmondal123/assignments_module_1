WITH cte AS (
    SELECT num,
    lead(num, 1) OVER() num1,
    lead(num, 2) OVER() num2
    FROM logs
)

SELECT DISTINCT num ConsecutiveNums FROM cte WHERE (num=num1) and (num=num2)