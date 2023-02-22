# 1011. Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2

            if self.can_ship(mid, weights, days):
                r = mid
            else:
                l = mid + 1

        return r

    def can_ship(self, candidate: int, weights: List[int], days: int) -> bool:
        days_taken = 1
        cur_weight = 0

        for weight in weights:
            cur_weight += weight
            if cur_weight > candidate:
                days_taken += 1
                cur_weight = weight
            
        return days_taken <= days

