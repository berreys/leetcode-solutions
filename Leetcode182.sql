-- LEETCODE PROBLEM 182 : DUPLICATE EMAILS
-- https://leetcode.com/problems/duplicate-emails/description/

SELECT email AS Email
FROM Person
GROUP BY EMAIL
HAVING COUNT(email) > 1;