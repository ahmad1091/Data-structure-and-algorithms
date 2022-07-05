var solution = function (isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    return function (n) {
      let start = 1;
      let end = n;
      let mid = Math.floor((start + end) / 2);
      while (end - start > 3) {
        if (isBadVersion(mid)) {
          end = mid;
          mid = Math.floor((start + end) / 2);
        } else {
          start = mid;
          mid = Math.floor((start + end) / 2);
        }
      }
      console.log(start, end);
      for (let i = start; i <= end; i++) {
        if (isBadVersion(i)) return i;
      }
      return 0;
    };
  };