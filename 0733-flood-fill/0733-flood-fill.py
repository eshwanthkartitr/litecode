class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def traverse(i,j,color,orgi,visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            image[i][j] = color
            di=[[-1,0],[1,0],[0,-1],[0,1]]
            for dx,dy in di:
                if 0<=i+dx<len(image) and 0<=j+dy<len(image[0]) and image[i+dx][j+dy] == orgi:
                    traverse(i+dx,j+dy,color,orgi,visited)
        traverse(sr,sc,color,image[sr][sc],set())
        return image