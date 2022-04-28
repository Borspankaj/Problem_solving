class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        graph = {i : [] for i in range(numCourses)}
        indegree = { i : 0 for i in range(numCourses)}

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1


        q = []
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        ans = []
        if not q:
            return False

        while q:

            vertex = q.pop(0)
            ans.append(vertex)
            for neigh in graph[vertex]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        if len(ans) == numCourses :
            return True
        else:
            return False