class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      candidates.sort()
      result = []
      
      def helper(new_candidates, temp, temp_sum):
        if temp_sum == target:
          result.append(temp[:])
          return

        for i in range(len(new_candidates)):
          if new_candidates[i] > target - temp_sum:
            break
          temp.append(new_candidates[i]) #2 3
          temp_sum += new_candidates[i] #5
          helper(new_candidates[i:], temp, temp_sum)
          temp_sum -= temp.pop()

      helper(candidates, [], 0)
      return result