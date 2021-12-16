function title()  {
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    ctx.font = "30px Verdana";
    ctx.fillText("Geometric figures", 150, 50);
}


function rectangle()  {
    var canvas = document.getElementById('canvas');
    var rectangle = canvas.getContext('2d'); 
    rectangle.fillStyle = 'brown';
    rectangle.fillRect(400,150,100,200);
}

function triangle()  {
    var canvas = document.getElementById('canvas');
    var triangle = canvas.getContext('2d');
    triangle.beginPath();
    triangle.fillStyle = 'green';
    triangle.moveTo(150,150);
    triangle.lineTo(310,150);
    triangle.lineTo(150,310);
    triangle.closePath();
    triangle.fill();
    triangle.stroke();
}

function circle()  {
    var canvas = document.getElementById('canvas');
    var circle = canvas.getContext('2d');
    circle.beginPath();
    circle.fillStyle = "blue";
    circle.arc(300, 300, 100, 0, 2 * Math.PI);
    circle.fill();
    circle.stroke();
}