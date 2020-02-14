SELECT
    NULLIF
    (
        (
        SELECT DISTINCT Salary
            from Employee
            order by desc
            limit 1,1
            )
        ,NULL
        ) as SecondHighestSalary;
