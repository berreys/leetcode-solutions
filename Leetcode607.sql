-- LEETCODE PROBLEM 607 :  SALES PERSON
-- https://leetcode.com/problems/sales-person/description/

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT s.sales_id
    FROM SalesPerson s
    INNER JOIN Orders o ON s.sales_id = o.sales_id
    INNER JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);