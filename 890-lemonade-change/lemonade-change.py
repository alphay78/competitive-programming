from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0  # Count of $5 bills
        count10 = 0  # Count of $10 bills
        
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                if count5 > 0:
                    count5 -= 1
                    count10 += 1  # Store the $10 bill
                else:
                    return False  # No $5 to give as change
            else:  # When bill == 20
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1  # Give $10 and $5 as change
                elif count5 >= 3:
                    count5 -= 3  # Give three $5 bills as change
                else:
                    return False  # Not enough change

        return True  # If all transactions were successful
