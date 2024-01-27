class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        added = set()
        curr_path = set()
        res = []
        
        def dfs(course):
            if course in added:
                return True
            
            if course in curr_path:
                return False
            
            curr_path.add(course)
            for prereq in adj_list[course]:
                if prereq in added:
                    continue
                
                can_complete = dfs(prereq)
                if not can_complete:
                    return False
            curr_path.remove(course)
            
            res.append(course)
            added.add(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
        