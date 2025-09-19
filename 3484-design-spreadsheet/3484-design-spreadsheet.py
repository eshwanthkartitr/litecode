class Spreadsheet:

    def __init__(self, rows: int):
        self.cont = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cont[cell]=value

    def resetCell(self, cell: str) -> None:
        self.cont[cell]=0

    def getValue(self, form: str) -> int:
        form = form[1:]
        for i in range(len(form)):
            if form[i] == "+":
                s1 = form[:i]
                s2 = form[i+1:]
                if s1.isupper():
                    s1 = self.cont[s1]
                else:
                    s1 = int(s1)
                if s2.isupper():
                    s2 = self.cont[s2]
                else:
                    s2 = int(s2)
                return s1 + s2
        return 0
                



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)