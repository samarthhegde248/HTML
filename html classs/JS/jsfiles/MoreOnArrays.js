var ages = [32,19,18,17,16,23,21,20,24,28,30, 35, 05];

console.log(ages[1]);

var _names = [];

// push, unshift
// pop, shift,

_names.push('x');
_names.push('y');
_names.push('z');
_names.unshift('a');
_names.unshift('1');

console.log(_names);

_names.shift();
console.log(_names);

// _names[0] = '';

// delete _names[0];
_names.splice(1, 2);
console.log(_names);


var example = [111, 'asdasdasd', true, null, undefined, {name:'shiva', favcolors:['red','blue']}, [11,22,33, [{favMovie:['sahoo']}]]];

console.log(example);

// JSON

var emp = [
    {"name":'x', "age":20, "salary":1000},
    {"name":'y', "age":30, "salary":2000},
]

console.log(emp[0].age);


var arr = '1 2 3 4';
console.log(arr.split( ));

arr = [1,2,3,4];
arr.join('*');



