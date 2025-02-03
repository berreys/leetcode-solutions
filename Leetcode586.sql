-- LEETCODE PROBLEM 586 :  CUSTOMER PLACING LARGEST NUMBER OF ORDERS
-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;