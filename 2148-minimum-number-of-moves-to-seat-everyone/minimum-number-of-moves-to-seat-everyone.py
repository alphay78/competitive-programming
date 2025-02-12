class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i = 0
        j = 0
        move = 0
        while i < len(seats) and j< len(students):
            s = students[j] - seats[i] 
            move+=abs(s)
            i+=1
            j+=1
        return move

