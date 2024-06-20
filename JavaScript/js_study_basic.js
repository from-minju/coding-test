//JavaScript 기초

//===== 변수와 상수 =====
//:: 변수 선언 ::
let a = 'hello';
// let a = '...'같은 변수를 두 번 선언하면 에러 발생
let b = 'world'
console.log(a, b)

let user = 'ike', 
    age = 25, 
    message = 'spyair'
console.log(user, age, message)


//:: 변수의 복사 ::
let copy = 'Hello world!';
let copy2;
copy2 = copy
console.log(copy) //>>>Hello world!
console.log(copy2) //>>>Hello world!


//:: 상수 ::
const myBirthday = '1998.10.10'
// myBirthday = '2000.10.10' //error : 상수는 재할당불가능
const BIRTH = '1998'




//===== 자료형 =====
// 동적 타입: 자료의 타입은 있지만 변수에 저장되는 값의 타입은 언제든지 바꿀 수 있다.

// - 숫자형
// : 정수, 부동소수점 숫자, 특수숫자값
let message1 = "hello";
message1 = 100;
// 특수 숫자값
console.log(1 / 0); //>>>Infinity
console.log("문자열" / 2); //>>>NaN

// - BigInt
// 끝에 'n'이 붙으면 BigInt형 자료입니다.
const bigInt = 1234567890123456789012345678901234567890n;

// - 문자형
let namae = "gintoki";
let message2 = `his name is ${namae}`; //백틱문자
console.log(message2) //>>>his name is gintoki
// ${}
console.log(`${1+2}`) //>>>3
console.log(`${"helloooooooo"}`) //>>>helloooooooo
console.log(`${namae}`) //>>>gintoki
console.log(`${'namae'}`) //>>>namae


// - 불린형 boolean
let isChecked = true;
let isDone = false;
let isGreater = 4 > 1;
console.log(isGreater) //>>>true

// - null값
// 비어있음, 존재하지 않음을 나타낼 때 사용
let n1 = null;

// - undefined 값
// 값이 할당되지 않은 상태를 나타낼 때 사용
let n2;
console.log(n2) //>>>undefined

// - 객체(Object)
// - 심볼

// - typeof 연산자
// 연산자 typeof x 또는 함수 typeof(x)
// 인수의 자료형을 반환
console.log(typeof(isDone)) //>>>boolean
console.log(typeof isDone)
console.log(typeof null)//>>>object //언어상의 오류, null은 객체가 아니다.




//===== 형 변환 =====
// - 문자형으로 변환
let value = true;
value = String(value);
console.log(value) //>>>true
console.log(typeof value) //>>>string

// - 숫자형으로 변환
let str1 = "100"
let num1 = Number(str1)
console.log(num1) //>>>100
console.log(typeof num1) //>>>number

console.log("6" / "2") //>>>3 //자동으로 숫자로 형변환된 후 연산 수행됨.
console.log(Number("123 문자열입니다.")) //>>>NaN
console.log(Number(true)) //>>>1
console.log(Number(undefined)) //>>>NaN
console.log(Number("      123    ")) //>>>123
console.log(Number("      12   3    ")) //>>> NaN


// - 불린형으로 변환
console.log(Boolean(1)) //>>>true
console.log(Boolean(0)) //>>>false
console.log(Boolean("0")) //>>>true //문자열'0'은 true! 주의!

console.log(Boolean("hello")) //>>>true
console.log(Boolean("")) //>>>false
console.log(Boolean(null)) //>>>false
console.log(Boolean(NaN)) //>>>false
console.log(Boolean(undefined)) //>>>false




//===== 기본 연산자와 수학 =====
// :: + 덧셈연산자 ::
// :: - 뺄셈연산자 ::
// :: * 곱셈연산자 ::
// :: / 나눗셈연산자 ::
// :: % 나머지연산자 ::
// :: ** 거듭제곱연산자 ::


// - 이항 연산자 '+'와 문자열 연결
let s = "my" + "string"
console.log(s) //>>>mystring


// - 문자열 + 정수
// 피연산자 중 하나가 문자열이면 다른 하나도 문자열로 변환된다.
console.log( '1' + 2 ); //>>>12
console.log(typeof('1' + 2))//>>>string
console.log( 2 + '1' ); //>>>21


// - 정수 + 정수 + 문자열
// 연산은 왼쪽에서 오른쪽으로 순차적으로 진행되므로, 숫자먼저 더해지고 문자열과의 병합이 일어남.
console.log(2 + 2 + '1') //>>>41
console.log(typeof(2 + 2 + '1')) //>>>string

// - 문자열 + 정수 + 정수
console.log(4 + 5 + "$") //>>>9$
console.log("$" + 4 + 5) //>>>$45

console.log(6 - '2') //>>>4
console.log('6' / '2') //>>>3
console.log('6' + '2') //>>>62


// :: 단항연산자 '+' 와 숫자형으로의 변환 :: 
console.log(+2) //>>>2

// 숫자형이 아닌 피연산자는 숫자형으로 변화 (Number()와 동일한 역할하게함.)
console.log(+true) //>>>1
console.log(+"") //>>>0

let apples = "2"
let oranges = "5"
console.log(apples + oranges) //>>>25
console.log(+apples + +oranges) //>>>7 //이항덧셈연산자가 적용되기 전에, 숫자형으로 변화됨. 단항덧셈연산자가 덧셈연산자보다 우선순위가 높기때문. 
console.log(Number(apples) + Number(oranges)) //>>>7 //단항덧셈연산자가 더 짧은 코드로 작성가능.


//:: 단항 마이너스 연산자 '-' ::
// 피연산자의 부호를 뒤집음.
let x = 1;
x = -x
console.log(x) //>>> -1


// :: 연산자의 우선순위 ::
// 단항덧셈'+' > 단항부정'-' > 지수'**' > 곱셈'*' > 나눗셈 > 덧셈 > 뺄셈 > ... > 할당 > ...


// :: 할당 연산자 '=' :: 
i = 2 * 2 + 1; //가장 마지막에 할당됨. -> '=' 우선순위가 제일 낮기 때문

let aa = 1;
let bb = 2;
let cc = 3 - ( aa = bb + 1);
console.log(aa); //>>>3
console.log(cc); //>>>0


// :: 복합 할당 연산자 ::
// += *= -= /=


// :: 증가,감소 연산자 ++ -- ::
let counter = 2;
counter++; //counter = counter + 1
console.log(counter) //>>>3
// 5++ -> error, 변수에만 쓸 수 있다.

// 후위형 counter++
counter = 1
console.log(counter++) //>>>1
console.log(counter) //>>>2

// 전위형 ++counter
counter = 1
console.log(++counter) //>>>2
console.log(counter) //>>>2


// :: 비트 연산자 ::
// - & : AND
// - | : OR
// - ^ : XOR
// - ~ : NOT
// - << : 왼쪽시프트
// - >> : 오른쪽시프트
// - >>> : 부호없는오른쪽시프트






















 





