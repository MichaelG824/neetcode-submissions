class Solution:
    def simplifyPath(self, path: str) -> str:
        char = ""
        stack = []
        for c in path + "/":
            if c == "/":
                if char == "..":
                    if stack:
                        stack.pop()
                elif char != "" and char != ".":
                    stack.append(char)
                char = ""
            else:
                char += c


        return "/" + '/'.join(stack)


