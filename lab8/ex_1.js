var input = window.prompt("Enter data:");
console.log(input);
console.log(typeof (input));


function func(event) {
  event.preventDefault();
  var str = document.forms[0].elements[0].value; // zawsze są zwracane wartości typu "string" 
  var num = document.forms[0].elements[1].value;
  console.log(str);
  console.log(typeof (str));
  console.log(num);
  console.log(typeof (num));
  return false;
}