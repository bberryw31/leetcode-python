class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = {"()"}
        
        def nexter(prev):
            res = set()
            for item in prev:
                temp = [char for char in item]
                mid = len(temp) // 2
                for i in range(mid, len(temp) + 1):
                    temp2 = temp[:i] + ['(', ')'] + temp[i:]
                    res.add("".join(temp2))
            return res
        
        for _ in range(1, n):
            result = nexter(result)
        return list(result)
        
                

                    
                



        