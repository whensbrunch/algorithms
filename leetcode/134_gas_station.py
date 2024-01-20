class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # short circuit: it's not possible to make it all the way around
        if sum(gas) < sum(cost):
            return -1

        # the surplus at i since the current starting station
        total = 0

        # current starting station
        res = 0
        for i in range(len(gas)):
            # at the surplus we gain / lose at station i
            total += (gas[i] - cost[i])

            # if we go negative then it's not possible to make 
            # a complete trip from the current starting station
            # aka res
            if total < 0:
                # reset surplus
                total = 0

                # start an attempt from station i+1
                res = i + 1
        
        return res