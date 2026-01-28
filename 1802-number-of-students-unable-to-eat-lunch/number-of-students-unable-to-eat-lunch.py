class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for student in students:
            counts[student] += 1

        res = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if res == 0:
                break
            counts[sandwich] -= 1
            res -= 1
        
        return res