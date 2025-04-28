-- LEETCODE PROBLEM 1075 : PROJECT EMPLOYEES I
-- https://leetcode.com/problems/project-employees-i/description/

SELECT p.project_id as project_id, ROUND(AVG(e.experience_years), 2) as average_years
FROM Project p
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY p.project_id;