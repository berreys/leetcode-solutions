-- LEETCODE PROBLEM 1148 : ARTICLE VIEWS I
-- https://leetcode.com/problems/article-views-i/description/

SELECT DISTINCT viewer_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY id;