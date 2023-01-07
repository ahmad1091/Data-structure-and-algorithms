# Paint Fill: Implement the "paint nil" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# nil in the surrounding area until the color changes from the original color.


def paintFill(screen, r, c, ncolor):
    if screen[][] == ncolor: return False
    return paintFill(screen, r, c, screen[r][c], ncolor)

    def paintFill(screen, r, c, ocolor, ncolor):
        if r < 0 or c < 0 or c >= screen[0].length or r >= screen[0].length:
            return False
        if screen[r][c] == ocolor:
           screen[r][c] = ncolor 
           paintFill(screen, r - 1, c, ocolor, ncolor)
           paintFill(screen, r + 1, c, ocolor, ncolor)
           paintFill(screen, r, c + 1, ocolor, ncolor)
           paintFill(screen, r, c - 1, ocolor, ncolor)
        
        return True
