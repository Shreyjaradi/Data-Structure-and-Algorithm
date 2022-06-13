# LInk to problem : https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(sandwiches and sandwiches[0] in students):
            if(sandwiches[0] == students[0]):
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
                
        return len(students)
