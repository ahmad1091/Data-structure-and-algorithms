var twoSum = function (numbers, target) {
    if (target <= 0) {
      for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < numbers.length; j++) {
          if (numbers[i] + numbers[j] == target && i !== j) {
            return [i + 1, j + 1];
          }
        }
      }
    } else {
      arr = [];
      length = target;
      for (let i = 0; i < length; i++) {
        console.log(numbers.indexOf(target) != -1, numbers.indexOf(i) != -1);
        if (numbers.indexOf(target) != -1 && numbers.indexOf(i) != -1) {
          first = numbers.indexOf(target) + 1;
          numbers[numbers.indexOf(target)] = undefined;
          second = numbers.indexOf(i) + 1;
          arr = [first, second];
          return arr.sort((a, b) => a - b);
        }
        target--;
      }
      return arr;
    }
  }