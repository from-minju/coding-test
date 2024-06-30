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
 * split()과 join()
 */
const originalStr = "apple, banana, cherry";
const array = originalStr.split(", "); // 문자열을 배열로 변환
console.log(array); // ["apple", "banana", "cherry"]

const newStr = array.join(" | "); // 배열을 문자열로 변환
console.log(newStr); // "apple | banana | cherry"




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



/**
 * splice()
 * 배열의 요소를 추가, 제거 또는 교체 (원본을변경.파괴적!, 반환값: 제거된요소)
 * 문법 : array.splice(start, deleteCount, item1, item2, ...);
 */




/**
 * 
 * Set
 * 중복을 허용하지 않는 값들의 집합을 나타냄. 배열->Set으로 변환하면 중복값 제거됨.
 * 
 */

const numbers2 = [1, 2, 2, 3, 4, 4, 5];
const uniqueNumbers = [...new Set(numbers2)];
console.log(uniqueNumbers); // [1, 2, 3, 4, 5]

/**
 * Set객체 -> 배열
 * 
 */
const myArray = [...mySet];

// 1. 스프레드 연산자
const mySet = new Set([1, 2, 3, 4, 5]);
console.log(myArray); // [1, 2, 3, 4, 5]

// 2. Array.from()
const myArray2 = Array.from(mySet); 
console.log(myArray2); // [1, 2, 3, 4, 5]


/**
 * Math.max / Math.min
 * 배열의 최댓갑과 최솟값 구하기
 */
const numbers4 = [1, 2, 3, 4, 5];
const max = Math.max(...numbers4);
console.log(max); // 5

console.log(Math.max(4, 8)) //8