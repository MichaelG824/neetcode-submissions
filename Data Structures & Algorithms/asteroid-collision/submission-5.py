class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            if a < 0:
                # [2, 4, -4, 5, 1, -1, -7]
                """
                [2, 4]

                """
                while len(s) > 0 and s[-1] > 0:
                    top_val = s[-1]
                    if a + top_val < 0:
                        s.pop()
                        continue
                    elif a + top_val == 0:
                        s.pop()
                        break
                    else:
                        break
                else:
                    s.append(a)
            else:
                s.append(a)
        return s
            
                