var num = "100.1212312";


// parseInt; parseFloat
if(typeof(num) === 'number'){
    console.log(num + 10);
}else{
    // var test = parseInt(num);
    var test = parseFloat(num);
    // console.log(test + 10);
}

var abc = 1231231;
// console.log(abc.toString());

// Math.round, Math.ceil, Math.floor, Math.random;

// console.log(Math.round(10.5));
// console.log(Math.ceil(10.0001));
// console.log(Math.floor(10.99999));
console.log(Math.ceil(Math.random() * 6)); // 0 - 1;


var q1 = prompt('Please guess a number b/w 1 - 6');
console.log(q1);
// Task
// Rolling Dice, ===






