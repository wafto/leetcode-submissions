class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        curr = image[sr][sc]
        stack = [(sr, sc)]
        visited = set()

        while stack:
            r, c = stack.pop()

            if image[r][c] != curr or (r, c) in visited:
                continue
                
            image[r][c] = color
            visited.add((r, c))
            
            if r > 0 and image[r - 1][c] == curr:
                stack.append((r - 1, c))
            if r < rows - 1 and image[r + 1][c] == curr:
                stack.append((r + 1, c))
            if c > 0 and image[r][c - 1] == curr:
                stack.append((r, c - 1))
            if c < cols - 1 and image[r][c + 1] == curr:
                stack.append((r, c + 1))
            
        return image
                
