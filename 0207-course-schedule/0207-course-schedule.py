class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i : [] for i in range(numCourses)}
        for p in prerequisites:
            pre[p[0]].append(p[1])
        
        memo = set()
        def helper(n, temp):
            if n in memo:
                return True
            if n in temp:
                return False
            temp.add(n)
            for p in pre[n]:
                if not helper(p, temp):
                    return False
                else:
                    memo.add(p)
            temp.remove(n)
            memo.add(n)
            return True
        
        for i in range(numCourses):
            if not helper(i, set()):
                return False
        return True