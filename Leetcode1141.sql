-- LEETCODE PROBLEM 1141 : USER ACTIVITY FOR THE PAST 30 DAYS I
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description

SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN ('2019-07-27' - INTERVAL 29 DAY) AND DATE('2019-07-27')
GROUP BY activity_date;