class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        re=""
        if num>=1000000000:
            re+=f"{self.numberToWords(num//1000000000)} Billion" 
            if num%1000000000!=0:
                re+=f" {self.numberToWords(num%1000000000)}"
        elif num>=1000000:
            re+=f"{self.numberToWords(num//1000000)} Million"
            if num%1000000!=0:
                re+=f" {self.numberToWords(num%1000000)}"
        elif num>=1000:
            re+=f"{self.numberToWords(num//1000)} Thousand"
            if num%1000!=0:
                re+=f" {self.numberToWords(num%1000)}"
        elif num>=100:
            re+=f"{self.numberToWords(num//100)} Hundred" 
            if num%100!=0:
                re+=f" {self.numberToWords(num%100)}"
        elif num>19 and num%10!=0:
            re += f"{d[(num//10)*10]} "+self.numberToWords(num%10)
        else:
            re+=d[num]
        return re