# 981. Time Based Key-Value Store

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values,
#  it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        val = self.hash.get(key)
        if val:
            if timestamp in dict(self.hash[key]):
                return dict(self.hash[key])[timestamp]
            else:
                # mx = max(dict(self.hash[key]).keys())
                mn = min(dict(self.hash[key]).keys())
                if timestamp < mn:
                    return ''
                else:
                    for i in range(len(self.hash[key])):
                        if self.hash[key][i][0] > timestamp:
                            return self.hash[key][i-1][1]
                    return self.hash[key][-1][1]
        return None
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# sol 2:
        
class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash.get(key,[])
        res = ''
        l, r = 0, len(values) -1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] == timestamp:
                return values[m][1]

            elif values[m][0] < timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res  
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)