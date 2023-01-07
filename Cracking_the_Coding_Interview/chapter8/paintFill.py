# Paint Fill: Implement the "paint nil" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# nil in the surrounding area until the color changes from the original color.


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def paint_fill(screen: List[List[int]], i: int, j: int, old_color: int, new_color: int):
            if (i < 0 or j < 0   or 
                i >= len(screen) or
                j >= len(screen[0])
            ):
                return image
            if screen[i][j] == old_color:
                screen[i][j] = new_color
                paint_fill(screen, i + 1, j, old_color, new_color)
                paint_fill(screen, i - 1, j, old_color, new_color)
                paint_fill(screen, i, j + 1, old_color, new_color)
                paint_fill(screen, i, j - 1, old_color, new_color)

            return image

        if image[sr][sc] == color: return image
        return paint_fill(image, sr, sc, image[sr][sc], color)


# sol 2: cleaner code 
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        def dfs(i, j):
            if (
                not 0 <= i < m
                or not 0 <= j < n
                or image[i][j] != oc
                or image[i][j] == newColor
            ):
                return
            image[i][j] = newColor
            for a, b in pairwise(dirs):
                dfs(i + a, j + b)

        dirs = (-1, 0, 1, 0, -1)
        m, n = len(image), len(image[0])
        oc = image[sr][sc]
        dfs(sr, sc)
        return image