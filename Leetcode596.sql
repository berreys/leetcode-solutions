-- LEETCODE PROBLEM 596 : CLASSES MORE THAN 5 STUDENTS
-- https://leetcode.com/problems/classes-more-than-5-students/description/

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;