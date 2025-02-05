-- LEETCODE PROBLEM 619 : BIGGEST SINGLE NUMBER
-- https://leetcode.com/problems/biggest-single-number/description/

SELECT temp2.num
FROM (SELECT NULL AS num) null_table
LEFT JOIN (
    SELECT * 
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC
    LIMIT 1
) temp2 ON TRUE;