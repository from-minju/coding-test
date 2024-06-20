//JavaScript 기본


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





//===== 비교 연산자 =====
// - 불린형 반환
console.log(2 < 1); //>>>false
console.log(2 != 1) //>>>true

// - 문자열 비교
console.log('Z' > 'A') //>>>true
console.log('aza' > 'abc') //>>>true

// - 다른 자료형 간의 비교
console.log('2' > 1) //>>>true
console.log(true == 0) //>>>false
// ==비교나 >비교에서는 피연산자를 숫자형으로 바꿔 연산하지만, Boolean()변환에서는 형변환을하지않는다. 문자열
let a1 = 0;
let b1 = "0";
console.log(Boolean(a1)); //>>>false
console.log(Boolean(b1)); //>>>true //숫자0으로 변환시키지 않음. 문자열이 존재하므로 true임.
console.log(a1 == b1); //>>>true //b1을 숫자0으로 변환시켜 ==비교함.

// - 일치 연산자
console.log(0 == false) //>>>true
console.log('' == false) //>>>true

// - null, undefined와 비교하기
console.log(null == undefined) //>>>true

// - null vs 0
console.log(null > 0) //>>>false
console.log(null < 0) //>>>false
console.log(null == 0) //>>>false
console.log(null >= 0) //>>>true
console.log(null <= 0) //>>>true

// - undefined vs 0 
// undefined는 비교불가능함. 다른값과 비교해서는 안됨. 항상 false
console.log(undefined > 0) //>>>false
console.log(undefined < 0) //>>>false
console.log(undefined == 0) //>>>false
console.log(undefined >= 0) //>>>false
console.log(undefined <= 0) //>>>false





//===== if와 '?'를 사용한 조건 처리 =====
// :: if문 ::
if (true) {
    console.log("-----if문")
}

// :: else절 ::
if (true) {
    console.log("t r u e")
} else {
    console.log("f a l s e")
}

// :: else if ::
let year = 2000;
if (year < 2000 ) {
    console.log("2000년 이전")
}else if (year > 2000) {
    console.log("2000년 이후")
}else {
    console.log("2000년 입니다.")
}

// :: 조건부 연산자 '?' ::
let result = (year > 2000) ? '* 2000년 이후' : '* 2000년 or 이전';
console.log(result)

// :: 다중 '?' ::
let ages = 25;
let messages = (ages < 3) ? '아기야 안녕?' :
  (ages < 18) ? '안녕!' :
  (ages < 100) ? '환영합니다!' :
  '나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!';
console.log(messages) //>>>환영합니다!





//===== while과 for =====
let ii = 3;
while (ii) {
    console.log(ii)
    ii--;
}

// - do...while 반복문
// 최소 한번의 실행을 보장하는 while문
ii = 0;
do {
    console.log(ii); //0 1 2
    ii++;
} while (ii < 3);


// - for
// 두개의 세미콜론을 꼭 넣어주어야 함.
for (let i = 0; i <3; i++) {
    console.log(i) //0 1 2
}

// - 중첩 for문을 빠져나오고(break) 싶을 때
labelName: for (let i = 0; i<3; i++){
    for(let j = 0; j<3; j++){
        console.log(i, j) //0 0
        break labelName;

    }
}




//===== switch문 =====
a = 1;
switch(a){
    case 1:
        console.log("값은 1");
        break
    case 2:
    case 3:
        console.log("값은 2또는 3")
        break
    case 4:
        console.log("값은 4");
        break
    default:
        console.log("모든 경우에 해당하지 않습니다.")
}





//===== 함수 =====
// - 함수 선언
function showMessage() {
    console.log("안녕?")

    // - 지역 변수
    let localv = "지역변수입니다.";
    console.log(localv)

    // - 외부 변수
    a = "외부변수입니다."
    console.log(a)

    // - 동일한 이름의 지역변수와 외부변수
    let b = "지역변수b"
    console.log(b)
    this.b = "외부변수b"
    console.log(this.b) //
}
showMessage();
// console.log(localv)//error

// - 함수 이름짓기
// "get…" – 값을 반환함
// "calc…" – 무언가를 계산함
// "create…" – 무언가를 생성함
// "check…" – 무언가를 확인하고 불린값을 반환함




//===== 함수 표현식 =====
// 함수를 변수에 할당
let say = function() {
    console.log("Hello???")
};
console.log(say) //>>>[Function: sayHi]
say() //>>>Hello???

// 
function sayHi() {
    console.log("say hi~~");
}
let v = sayHi; //괄호없음유의! 함수자체를 넘긴것. sayHi()라면 함수결과값을 넘김.
v();
sayHi();




//===== 콜백 함수 =====
function ask(question, yes, no) {
    if (question) yes()
    else no();
}
function showOk() {
    console.log("동의하셨습니다.")
}
function showCancel() {
    console.log("취소버튼을 누르셨습니다.")
}
ask("질문", showOk, showCancel) //>>>동의하셨습니다.
//showOk, showCancel처럼 함수의 인수가 되는 함수를 콜백함수 또는 콜백이라 한다.

// - 익명함수
// 이름없이 선언한 함수. 익명함수는 변수에 할당된 것이 아니므로 스코프 바깥에서는 접근불가능.
ask("질문2",
    function() {console.log("동의하셨습니다.2")},
    function() {console.log("취소버튼을 누르셨습니다.2")}
); ///>>>동의하셨습니다.2





//===== 함수 표현식 vs 함수 선언문 =====
/*
- 함수 표현식 : 실제 실행 흐름이 해당 함수에 도달했을 때 함수를 생성. 따라서 실행 흐름이 함수에 도달했을 때부터 해당 함수 사용가능
- 함수 선언문 : 함수 선언문이 정의되기 전에도 호출 가능
  - 이것이 가능한 이유 : 자바스크립트는 실행하기 전, 준비단계에서 전역에 선언된 함수 선언문을 찾고, 해당함수를 생성함.
*/




//===== 화살표 함수 기본 =====
// 본문이 한 줄인 함수를 작성할 때 유용하다. 본문이 여러줄일땐 중괄호와 함께 작성
let sum = (a, b) => a + b;
/*
let sum = function(a, b) {
    return a+b;
}
*/

let no_parameter = () => console.log("no parameter")
no_parameter()

// - 본문이 여러줄일때 화살표함수 사용법
let sum2 = (a, b) => { //중괄호 사용
    let result = a + b;
    return result; //return 사용
}





























 





