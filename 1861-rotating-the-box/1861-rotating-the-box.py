class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m,n=len(boxGrid),len(boxGrid[0])
        
        items = [["."]*(m) for _ in range(n)]
        
        for i in range(m):
            empty_spot = n-1
            for j in range(n-1,-1,-1):

                if boxGrid[i][j]=="#":
                    boxGrid[i][j]="."
                    boxGrid[i][empty_spot]="#"
                    empty_spot-=1
                if boxGrid[i][j]=="*":
                    empty_spot=j-1

        for i in range(m):
            for j in range(n):
                items[j][m-i-1] = boxGrid[i][j]
        
        return items
                
                 
