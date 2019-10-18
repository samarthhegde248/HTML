if( 1 === '1' ){
    console.log(1);
}else if( 2 === 2 ){
    console.log('1111');
}else{
    console.log('not 1');
}


if(1 == 1 || 1 === 1 || 1 === 'one'){
    console.log(1);
}else if( (1== 1 || 1 === 1 ) && 2 == 2){
    console.log('yes..');
}


switch('somey'){
    case 'somex':
    case 'somey':
        alert('yes it is Some x');
        break;
    default:
        alert('Yes it is something else');
}