# 875. Koko Eating Bananas

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        minH = 10000000
        for i in range(1,mx+1):
            hTrack = h
            c = 0 
            for j in range(len(piles)):
                if hTrack <= 0:
                    break 
                print(piles[j],i,ceil(piles[j]/i))
                if piles[j] > i:
                    hTrack -= ceil(piles[j]/i)
                    if hTrack < 0:
                        break 
                else:
                    hTrack -= 1
                c += 1

            if i < minH and c == len(piles):
                minH = i


        return minH