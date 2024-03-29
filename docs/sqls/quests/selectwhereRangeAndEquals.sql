-- refer : https://www.w3schools.com/sql/sql_where.asp

-- 조건 : Country 가 Germany 와 USA가 아닌 것들
SELECT *
FROM Customers
WHERE Country NOT IN ('Germany', 'USA');    -- COUNT : 67

-- 조건 : CustomerID가 50에서 89이고, City가 London인 고객
SELECT *
FROM Customers
WHERE (CustomerID BETWEEN 50 AND 89) AND (City = 'London');   -- COUNT : 2