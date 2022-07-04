const generateMatrix = function (n) {
    const array = Array.from({ length: n }, () => [[...Array(n)]]);
    if (n >= 1 && n <= 20) {
      let top = 0;
      let left = 0;
      let right = n - 1;
      let bottom = n - 1;
      let direction = "right";
      let incrementor = 1;
  
      while (top <= bottom && left <= right) {
        if (direction === "right") {
          for (let i = left; i <= right; i += 1) {
            array[top][i] = incrementor;
            incrementor += 1;
          }
          top += 1;
          direction = "down";
        } else if (direction === "down") {
          for (let i = top; i <= bottom; i += 1) {
            console.log(i, right, incrementor);
            array[i][right] = incrementor;
            incrementor += 1;
          }
          right -= 1;
          direction = "left";
        } else if (direction === "left") {
          for (let i = right; i >= left; i -= 1) {
            array[bottom][i] = incrementor;
            incrementor += 1;
          }
          bottom -= 1;
          direction = "up";
        } else if (direction === "up") {
          for (let i = bottom; i >= top; i -= 1) {
            array[i][left] = incrementor;
            incrementor += 1;
          }
          left += 1;
          direction = "right";
        }
      }
  
      return array;
    }
    return null;
  };