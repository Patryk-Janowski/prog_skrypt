"use strict"

var expect = chai.expect;
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

describe('The sumDigits() function', function() {
    it('Returns 6 for "123"', function() {
        expect(sumDigits('123')).to.equal(6);
      });
    it('Returns 0 for "słowo"', function() {
        expect(sumDigits('słowo')).to.equal(0);
      });
    it('Returns 18 for "evil666"', function() {
        expect(sumDigits('evil666')).to.equal(18);
      });
    it('Returns 6 for "42Otrap"', function() {
        expect(sumDigits('42Otrap')).to.equal(6);
      });
    it('Returns 0 for ""', function() {
        expect(sumDigits('')).to.equal(0);
      });  
   });

describe('The numLetters() function', function() {
    it('Returns 0 for "123"', function() {
        expect(numLetters('123')).to.equal(0);
      });
    it('Returns 5 for "słowo"', function() {
        expect(numLetters('slowo')).to.equal(5);
      });
    it('Returns 4 for "evil666"', function() {
        expect(numLetters('evil666')).to.equal(4);
      });
    it('Returns 5 for "42Otrap"', function() {
        expect(numLetters('42Otrap')).to.equal(5);
      });
    it('Returns 0 for ""', function() {
        expect(numLetters('')).to.equal(0);
      });  
   });

describe('The sumAll() function', function() {
    it('Returns 123 for "123"', function() {
        sumAll('123');
        expect(sum_all).to.equal(123);
      });
    it('Returns 123 for "słowo"', function() {
        sumAll('słowo');
        expect(sum_all).to.equal(123);
      });
    it('Returns 123 for "evil666"', function() {
        sumAll('evil666');
        expect(sum_all).to.equal(123);
      });
    it('Returns 165 for "42Otrap"', function() {
        sumAll('42Otrap');
        expect(sum_all).to.equal(165);
      });
    it('Returns 165 for ""', function() {
        sumAll('');
        expect(sum_all).to.equal(165);
      });
   });