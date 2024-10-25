# LeetCode 1233 : 1233. Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
class Solution:
  def removeSubfolders(self, folder: list[str]) -> list[str]:
    riz = []
    prev = ""

    folder.sort()

    for f in folder:
      if len(prev) > 0 and f.startswith(prev) and f[len(prev)] == '/':
        continue
      riz.append(f)
      prev = f

    return riz