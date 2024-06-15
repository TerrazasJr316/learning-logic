var a = 0;
function foo(a) {
    console.log(a);
    var a = 5;
}

foo(10)