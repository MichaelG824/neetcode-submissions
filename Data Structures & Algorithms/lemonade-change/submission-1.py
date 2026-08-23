class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tot_five_dollar_bills = 0
        tot_ten_dollar_bills = 0
        tot_twenty_dollar_bills = 0
        for bill in bills:
            if bill == 5:
                tot_five_dollar_bills += 1
            elif bill == 10:
                tot_five_dollar_bills -= 1
                tot_ten_dollar_bills += 1
                if tot_five_dollar_bills < 0:
                    return False
            elif tot_ten_dollar_bills > 0:
                tot_five_dollar_bills -= 1
                tot_ten_dollar_bills -= 1
                if tot_five_dollar_bills < 0 or tot_ten_dollar_bills < 0:
                    return False
            else:
                tot_five_dollar_bills -= 3
                if tot_five_dollar_bills < 0:
                    return False
        return True