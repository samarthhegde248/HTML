var emp = [
    {"name":'x', "age":20, "salary":1000},
    {"name":'y', "age":30, "salary":2000},
]


// for, forEach, while, forin;


for(var i = 0; i < 2; i++){
    // console.log(emp[i].salary);
}

emp.forEach(function(value,index,array){
    // console.log(value.name);
});

for(var i in emp){
    console.log(emp[i].name);
}


var j = 0;
while(j < 2){
    console.log(emp[j]);
    j++;
};