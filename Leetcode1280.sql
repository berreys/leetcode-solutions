-- LEETCODE PROBLEM 1280 : STUDENT AND EXAMINATIONS
-- https://leetcode.com/problems/students-and-examinations/description/

SELECT s.student_id, s.student_name, subs.subject_name, COUNT(e.student_id) as attended_exams
FROM students s
LEFT JOIN subjects subs
ON TRUE
LEFT JOIN examinations e
ON s.student_id = e.student_id AND subs.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, subs.subject_name
ORDER BY s.student_id, subs.subject_name;