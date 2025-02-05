-- LEETCODE PROBLEM 1407 : TOP TRAVELLERS
-- https://leetcode.com/problems/top-travellers/description/

SELECT u.name, IF(SUM(r.distance) IS NULL, 0, SUM(r.distance))as travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name;