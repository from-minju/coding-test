/**
 * 
 * ========== 정렬 ==========
 * 
 */

// 1. 문자 정렬

//2. 숫자 정렬
//  2-1. 한자리 수 정렬
let numbers = [5,3,2,1,4]
numbers.sort()
console.log(numbers)

//  2-3. 숫자 - 오름차순 정렬 
let arr2 = [74, 1, 8, 54, 23];
arr2.sort();
console.log(arr2); //[ 1, 23, 54, 74, 8 ] => 오류 발생
//sort()는 배열의 요소들을 문자열로 취급한다. -> 숫자를 정렬 시 값을 비교해줄 수 있는 함수를 넣어줘야 함.





/**
 * 
 * ========== 문자열 함수 ===========
 * 
 */


// * substring() : 문자열 부분 추출
let str = "Hello, world!";
let result = str.substring(0, 5);
console.log(result);
//  - 시작인덱스부터 끝까지 문자열 추출
let str1 = "0123456789";
let result1 = str1.substring(4); //인덱스4부터 문자열끝까지 추출
console.log(result1); 

// * parseInt() : 문자열을 정수로 변환
//  - 10진법 문자열을 정수로 변환
let num1 = parseInt("123");
console.log(num1);
//  - 2진법 문자열을 정수로 변환
let num2 = parseInt("1010", 2);
console.log(num2); // 10

/**
 * concat()
 */
// 두개의 배열을 하나로 합치기
let array1 = [1, 2, 3];
let array2 = [4, 5, 6];
let array3 = [7, 8, 9];

let newArray = array1.concat(array2, array3);
console.log(newArray); // 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]






/**
 * 
 * ========== 배열 함수 ===========
 * 
 */


/**
 * filter()
 */

const numbers0 = [1, 2, 3, 4];
const evenNumbers = numbers0.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]

const spyair = ["ike", "uz", "momiken", "kenta"]
const filtered = spyair.filter(string => string.includes("e"))
const filtered1 = spyair.filter(string => string.includes("e", 2))
const filtered2 = spyair.filter(string => string.includes("e", 3))
console.log(filtered) // [ 'ike', 'momiken', 'kenta' ]
console.log(filtered1) // [ 'ike', 'momiken' ]
console.log(filtered2) // [ 'momiken' ]



/*
    reduce()
*/
// 배열의 합을 구함
const numbers1 = [1, 2, 3, 4];
const sum = numbers1.reduce((acc, num) => acc + num, 0);
console.log(sum); // 10

// 객체 배열을 하나의 객체로 변환
const newJeans = [
    { name: 'minji', age: 25 },
    { name: 'hani', age: 30 },
    { name: 'daniel', age: 35 }
];

const peopleObject = newJeans.reduce((accumulator, currentValue) => {
    accumulator[currentValue.name] = currentValue.age;
    return accumulator;
}, {});

console.log(peopleObject); // { minji: 25, hani: 30, daniel: 35 }


// 중첩된 배열 평탄화
const nestedArray = [[1, 2], [3, 4], [5, 6]];
const flatArray = nestedArray.reduce((acc, cur) => acc.concat(cur), []);
console.log(flatArray);

