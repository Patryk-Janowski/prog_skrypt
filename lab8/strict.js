"use strict"


var sum_all = 0;

function sumDigits(str) {
    var sum = 0;
    if (str && str.match(/\d/g)){
        var numbers = str.match(/\d{1}/g).map(Number);
        for (var i = 0; i < numbers.length; i++) {
            sum += numbers[i]
        }
    }
    return sum;
}

function numLetters(str) {
    if (str && str.match(/[a-zA-Z]/g)){
    return Number(str.match(/[a-zA-Z]/g).length);
    } else {
        return 0
    }
}

function sumAll(str) {
    var sum = 0;
    if (str && str[0].match(/\d/g)){
        var numbers = str.match(/\d+/g).map(Number);
        for (var i = 0; i < numbers.length; i++) {
            sum += numbers[i]
        }
    }
    sum_all += sum;
    return sum_all
}

function run(event){
    var res = window.prompt("Enter str:");
    while(res){
        console.log(`${sumDigits(res)}\t${numLetters(res)}\t${sumAll(res)}`);
        var res = window.prompt("Enter str:");
    }
}

