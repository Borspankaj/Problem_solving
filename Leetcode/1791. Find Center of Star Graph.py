class Solution:
    def findCenter(self, edges) -> int:
        degree = {}

        for v in edges:

            for i in range(2):

                if v[i] in degree:
                    degree[v[i]] += 1
                else:
                    degree[v[i]] = 1
                if degree[v[i]] > 1:
                    return v[i]