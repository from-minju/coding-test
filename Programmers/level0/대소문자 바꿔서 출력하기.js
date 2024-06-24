const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    for (let i=0; i<str.length; i++){
    if (isUpperCase(str[i])) {
        process.stdout.write(str[i].toLowerCase());
    } else {
        process.stdout.write(str[i].toUpperCase());
    }
}
});

function isUpperCase(char){
    return char == char.toUpperCase();
}
