class Solution:
    def numberToWords(self, num: int) -> str:
        ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]  
        TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]  
        TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
        if num == 0:  
            return "Zero"  
        elif num< 0:  
                return "minus " + numberToWords(abs(num))  
        elif num< 10:  
                return ONES[num]  
        elif num< 20:  
                return TEENS[num - 10]  
        elif num< 100:  
                return TENS[num // 10] + (" " + self.numberToWords(num % 10) if num % 10 != 0 else "")  
        elif num< 1000:  
                return ONES[num // 100] + " Hundred" + (" " + self.numberToWords(num % 100) if num % 100 != 0 else "")  
        elif num< 1000000:  
                return self.numberToWords(num // 1000) + " Thousand" + (" " + self.numberToWords(num % 1000) if num % 1000 != 0 else "")  
        elif num< 1000000000:  
                return self.numberToWords(num // 1000000) + " Million" + (" " + self.numberToWords(num % 1000000) if num % 1000000 != 0 else "")  
        elif num< 10000000000:  
                return self.numberToWords(num // 1000000000) + " Billion" + (" " + self.numberToWords(num % 1000000000) if num % 1000000000 != 0 else "")  
        else:  
            return ""  