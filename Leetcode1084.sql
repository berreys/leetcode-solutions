-- LEETCODE PROBLEM 1084 : SALES ANALYSIS III
-- https://leetcode.com/problems/sales-analysis-iii/description/

SELECT p.product_id as product_id, p.product_name as product_name
FROM Sales s
LEFT JOIN Product p
ON s.product_id = p.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31';