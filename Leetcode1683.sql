-- LEETCODE PROBLEM 1683 : INVALID TWEETS
-- https://leetcode.com/problems/invalid-tweets/description/

SELECT tweet_id
FROM Tweets
WHERE LENGTH(CONTENT) > 15;