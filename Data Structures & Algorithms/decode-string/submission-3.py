class Solution:
    def decodeString(self, s: str) -> str:
        # [2] "2[a3[b]ee]c"
        # curr = "a"
        # res = ""

        stack = []

        for c in s:
            if c == ']':
                val = []
                while stack and not stack[-1].isdigit():
                    print(stack)
                    if stack[-1] == '[':
                        stack.pop()
                        break
                    val.append(stack[-1])
                    stack.pop()
                tot = []
                while stack and stack[-1].isdigit():
                    tot.append(stack.pop())
                    print(tot)
                tot.reverse()
                tot = ''.join(tot)
                val.reverse()
                for i in range(int(tot)):
                    for c in val:
                        print(i, c)
                        stack.append(c)
            else:
                stack.append(c)
        return ''.join(stack)