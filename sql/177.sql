CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT
        NULLIF (
            (SELECT DISTINCT Salary
                from Employee
                order by Salary desc
                limit N-1,1)
        ),NULL
  );
END