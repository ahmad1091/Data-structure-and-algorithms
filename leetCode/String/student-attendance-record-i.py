# 551. Student Attendance Record I

# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:

# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.

class Solution:
    def checkRecord(self, s: str) -> bool:
        attendance = {}
        consecutive = 0
        for c in s:
            if (c == 'A' and c in  attendance or
                c == 'L' and consecutive >= 2):
                return False
            else:
                attendance[c] = 1 + attendance.get(c, 0)
                if c != 'L': consecutive = 0
                else: consecutive += 1
        return True

# sol 2:
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s