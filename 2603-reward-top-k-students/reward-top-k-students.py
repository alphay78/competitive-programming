from collections import defaultdict
from typing import List

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # Step 1: Convert positive and negative feedback lists to sets for faster lookup
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        
        # Step 2: Initialize dictionary to store student points
        student_points = defaultdict(int)
        
        # Step 3: Process each report
        for i in range(len(report)):
            words = report[i].split()  # Split report into words
            student = student_id[i]    # Get the corresponding student ID
            for word in words:
                if word in positive_set:
                    student_points[student] += 3  # Positive word adds 3 points
                elif word in negative_set:
                    student_points[student] -= 1  # Negative word subtracts 1 point
        
        # Step 4: Ensure all students have an entry in the student_points dictionary
        for sid in student_id:
            if sid not in student_points:
                student_points[sid] = 0  # Default score is 0 if no feedback affects the student
        
        # Step 5: Sort students by points (descending), and by student_id (ascending) in case of tie
        ranked_students = sorted(student_id, key=lambda x: (-student_points[x], x))
        
        # Step 6: Return the top k students
        return ranked_students[:k]
