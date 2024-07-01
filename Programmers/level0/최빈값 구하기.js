// 나의 코드 - Map 사용
function solution(array) {
    let counter = new Map();
    
    // counter
    for (let i of array) {
        if (counter.has(i)){
            counter.set(i, counter.get(i) + 1)
        }else {
            counter.set(i, 1)
        }
    }
    
    // sort
    let mapEntries = Array.from(counter.entries());
    mapEntries.sort((a, b) => b[1] - a[1])
    
    // return
    if(counter.size >= 2 && mapEntries[0][1] == mapEntries[1][1]){
        return -1
    }else{
        return mapEntries[0][0]
    }
    
    return mapEntries[0][0]
}

// 다른 코드 - 객체 사용
function solution(array) {
    let count = {};
    
    // 배열 요소의 빈도를 계산
    for (let element of array) {
        if (count[element]) {
            count[element]++;
        } else {
            count[element] = 1;
        }
    }
    
    // 가장 빈도가 높은 요소 찾기
    let maxCount = 0;
    let mostFrequent = null;
    let multipleMax = false;
    
    for (let key in count) {
        if (count[key] > maxCount) {
            maxCount = count[key];
            mostFrequent = key;
            multipleMax = false;
        } else if (count[key] === maxCount) {
            multipleMax = true;
        }
    }
    
    // 최빈값이 여러 개인 경우 -1 반환
    return multipleMax ? -1 : +mostFrequent;
    
}