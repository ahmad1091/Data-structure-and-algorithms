// Check if all digits of the given integer are even.

// Example

// For n = 248622, the output should be
// solution(n) = true;
// For n = 642386, the output should be
// solution(n) = false.

function solution(n) {
    while(n>0){
        mod = n %10
        if(mod % 2 != 0 ){
            return false;
        }
        n = Math.floor(n/10)
    }
    return true
    }