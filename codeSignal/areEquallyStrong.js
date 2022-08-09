function solution(yourLeft, yourRight, friendsLeft, friendsRight) {
    you = [yourLeft,yourRight].sort()
    friend = [friendsLeft,friendsRight].sort()
    
    return String(you) == String(friend)
    }