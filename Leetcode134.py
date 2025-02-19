# LEETCODE PROBLEM 134 : GAS STATION
# https://leetcode.com/problems/gas-station/description/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #find starting spot
        for i in range(len(gas)):
            #try to go around the circle, returning if possible, breaking if not