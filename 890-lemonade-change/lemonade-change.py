class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0  
        count10 = 0 
        
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                if count5 > 0:
                    count5 -= 1
                    count10 += 1  
                else:
                    return False  
            else:  
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1  
                elif count5 >= 3:
                    count5 -= 3  
                else:
                    return False  

        return True  # If all transactions were successful
