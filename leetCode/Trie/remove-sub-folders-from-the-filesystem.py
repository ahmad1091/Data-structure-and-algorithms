# 1233. Remove Sub-Folders from the Filesystem

# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it.

# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 
 class Solution:
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    res = []
    prev = ""
    folder.sort()
    
    for f in folder:
        if len(prev) > 0 and f.startswith(prev) and f[len(prev)] == '/':
            continue
        res.append(f)
        prev = f

    return res