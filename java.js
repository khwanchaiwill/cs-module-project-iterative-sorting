
function get(){
    var arr = new Array();
    for (var i in arr){
        if (i % 3 == 0) {
            return arr[i]
        }  
    }
}
console.log(get([85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]))
