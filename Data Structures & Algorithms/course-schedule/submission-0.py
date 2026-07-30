class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = [0] * numCourses
        neighbors = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            count[b] += 1
            neighbors[a].append(b)

        taken = set()
        for _ in range(numCourses):
            for i, c in enumerate(count):
                if c == 0 and i not in taken:
                    taken.add(i)
                    for neighbor in neighbors[i]:
                        count[neighbor] -= 1
                    break
                elif i == numCourses - 1:
                    return False

        return True