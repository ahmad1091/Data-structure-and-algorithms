/**
 * @param {number[][]} accounts
 * @return {number}
 */
 var maximumWealth = function(accounts) {
    let max = -Infinity;
    for(let i = 0 ; i < accounts.length ; i++){
        let totalWealth = accounts[i].reduce((acc,e)=>acc+=e);
        if(totalWealth > max){
            max = totalWealth;
        }
    }
    return max;
};