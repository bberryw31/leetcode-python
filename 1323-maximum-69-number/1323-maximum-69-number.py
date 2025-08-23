class Solution:
    def maximum69Number (self, num: int) -> int:
        num_string = [char for char in str(num)]
        print(num_string)
        for i in range(len(num_string)):
            if num_string[i] == '6':
                num_string[i] = '9'
                break
        res = "".join(num_string)
        return int(res)
                
                
            