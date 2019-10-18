// 'use strict'

function demo(Name){
    console.log('Hello'+ Name);
}

// demo('Shiva');


function sum(a, b){
    return a + b;
}

console.log(sum(10, 10) + 20);


var abc = 'test';

function test(){
    var abc = 20;
    console.log(abc);
}

test();
console.log(abc);

// closure
function demo1(name){
    var abc = '10';
    function test1(){
        console.log(abc + ' ' + name);
    }
    test1();
}

// demo1('is a String');


let demo11 = 'shiva';
demo11 = 100;
console.log(demo11);
const demo22 = 'Prasad';
// demo22 = 200;
console.log(demo22+'asdasda');
let test123 = () => {
    console.log(12312321);
}
test123();

