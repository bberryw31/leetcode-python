class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m - 1 or not n - 1:
            return 1
        cache = [1, 1]
        pointer = [m - 2, n - 2]
        while len(cache) - 1:
            temp = []
            if pointer[1]:
                temp.append(cache[0])
                pointer[1] -= 1
            for i in range(len(cache) - 1):
                temp.append(cache[i] + cache[i + 1])
            if pointer[0]:
                temp.append(cache[-1])
                pointer[0] -= 1
            cache = temp[:]
            print(cache, pointer)
        return cache[0]
            