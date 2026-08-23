class Solution:
    def decodeString(self, s: str) -> str:
        # [2] "2[a3[b]ee]c"
        # curr = "2[a3[b]"
        # res = "bbb"
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sub_str = ""
                while stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                stack.pop()
                new_num = ""
                while stack and stack[-1].isdigit():
                    new_num = stack.pop() + new_num
                print(new_num)
                stack.append(int(new_num) * sub_str)
        return ''.join(stack)