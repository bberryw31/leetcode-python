class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort()
        content = 0
        for child in g:
            if s and child <= s[-1]:
                s.pop()
                content += 1
        return content