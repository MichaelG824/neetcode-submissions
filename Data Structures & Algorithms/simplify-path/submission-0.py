class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        /./..
        """
        stack = []
        curr = ""
        for c in path + '/':
            print(stack, "char: ", c)
            if c == "/":
                if curr == '.':
                    curr = ""
                elif curr == "..":
                    if stack:
                        stack.pop()
                    curr = ""
                else:
                    if curr:
                        stack.append(curr)
                        curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)