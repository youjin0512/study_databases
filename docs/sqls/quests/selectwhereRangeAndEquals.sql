-- refer : https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_columns

-- 조건 : Country 가 Germany 와 USA가 아닌 것들
SELECT *
FROM Customers                              -- Number of Records: 91
WHERE Country NOT IN ('Germany', 'USA');    -- Number of Records: 67

-- 조건 : CustomerID가 50에서 89이고, City가 London인 고객
-- 방법1)
SELECT *
FROM Customers
WHERE (CustomerID BETWEEN 50 AND 89) AND (City = 'London');   -- Number of Records: 2

-- 방법2)
SELECT CustomerID, City
FROM Customers
WHERE CustomerID BETWEEN 50 AND 89
AND City = 'London';    -- Number of Records: 2