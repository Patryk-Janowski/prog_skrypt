


  function decrement_util(){
    var counter = document.getElementById('counter').value;
    var num = Number(counter)
    if(!isNaN(counter) && num > 0){
    num--;
    document.getElementById('counter').value = num;
    l_span = document.querySelectorAll('span');
    for (let i = 0; i < l_span.length; i++) {
        l_span[i].textContent = num;
      }
    }
  }

  function decrement(){    
    setInterval(decrement, 1000);
  }