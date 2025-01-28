-- LEETCODE PROBLEM 197 : RISING TEMPEREATURE
-- https://leetcode.com/problems/rising-temperature/description/

SELECT w2.id
FROM Weather w1
LEFT JOIN Weather w2
ON w1.recordDate = DATE_SUB(w2.recordDate, INTERVAL 1 DAY)
WHERE w2.temperature > w1.temperature;