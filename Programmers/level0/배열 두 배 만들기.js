
// 나의 코드
function solution(numbers) {
    
    for(let num in numbers){
        numbers[num] *= 2
    }
    
    return numbers;
}


// 다른 코드 - reduce()사용
function solution(numbers) {
    return numbers.reduce((a, b) => [...a, b * 2], []);
}
/**
 * 입력값 : [1,2,3,4,5]
 * 
 * 초기값 : []
 * b : 현재값
 * 
 * 현재값이 1일때 : ..a는 비어있음, b*2==1*2==2, [2]
 * 현재값이 2일때 : ..a는 [2], b*2==2*2==4, [2,4]
 * ...
 * 최종결과 : [2,4,6,8,10]
 * */


// 다른 코드 - map() 사용
const solution = (numbers) => numbers.map((number) => number * 2)

// map예시
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(function(num) {
  return num * 2;
});
console.log(doubledNumbers); // [2, 4, 6, 8, 10]
