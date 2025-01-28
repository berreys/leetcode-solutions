-- LEETCODE PROBLEM 196 : DELETE DUPLICATE EMAILS
-- https://leetcode.com/problems/delete-duplicate-emails/?envType=problem-list-v2&envId=2hv17fjt

DELETE a
FROM Person a
INNER JOIN Person b
ON a.email = b.email AND a.id > b.id;