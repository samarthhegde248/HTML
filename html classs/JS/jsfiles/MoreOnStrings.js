var str = "";
str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book";

// length;
// console.log(str.length);

// toUpperCase(), toLowerCase();
// console.log(str.toUpperCase());;

// trim();
// console.log(str.trim());


// indexOf, lastIndexOf, search,
// console.log(str.lastIndexOf('dummy', 119));
// console.log(str.search('dummy'));


// replace;
// console.log(str.replace(/dummy/g, 'TEST'));


// subString, substr, slice;
var somex;
var dummy = "dummy";
somex = str.substring(str.search('dummy'), str.search('dummy') + (dummy.length));
// console.log(somex);

somex = str.slice(str.search('dummy'), str.search('dummy') + (dummy.length));
// console.log(somex);

somex = str.substr(str.search('dummy'), dummy.length);
// console.log(somex);


if(str.search('dummyy') > -1){
    console.log(str.replace(/dummy/g, 'TEST'));
}else{
    console.log('This word can"t find');
}


