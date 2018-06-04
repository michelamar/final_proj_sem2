var canvas = document.getElementById("canvas");

var height1 = 0;
var height2 = 0;
var height3 = 0;
var height4 = 0;
var height5 = 0;
var height6 = 0;
var height7 = 0;

var draw = function(){
    d3.selectAll("svg > *").remove();
    
    var bar1 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar1.setAttribute("fill", "lightsteelblue");
    bar1.setAttribute("x", 0);
    bar1.setAttribute("y", (400-(40*height1)));
    bar1.setAttribute("height", 40*height1);
    bar1.setAttribute("width", 100);
    canvas.appendChild(bar1);

    var bar2 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar2.setAttribute("fill", "lightsteelblue");
    bar2.setAttribute("x", 100);
    bar2.setAttribute("y", (400-(40*height2)));
    bar2.setAttribute("height", 40*height2);
    bar2.setAttribute("width", 100);
    canvas.appendChild(bar2);

    var bar3 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar3.setAttribute("fill", "lightsteelblue");
    bar3.setAttribute("x", 200);
    bar3.setAttribute("y", (400-(40*height3)));
    bar3.setAttribute("height", 40*height3);
    bar3.setAttribute("width", 100);
    canvas.appendChild(bar3);

    var bar4 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar4.setAttribute("fill", "lightsteelblue");
    bar4.setAttribute("x", 300);
    bar4.setAttribute("y", (400-(40*height4)));
    bar4.setAttribute("height", 40*height4);
    bar4.setAttribute("width", 100);
    canvas.appendChild(bar4);

    var bar5 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar5.setAttribute("fill", "lightsteelblue");
    bar5.setAttribute("x", 400);
    bar5.setAttribute("y", (400-(40*height5)));
    bar5.setAttribute("height", 40*height5);
    bar5.setAttribute("width", 100);
    canvas.appendChild(bar5);

    var bar6 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar6.setAttribute("fill", "lightsteelblue");
    bar6.setAttribute("x", 500);
    bar6.setAttribute("y", (400-(40*height6)));
    bar6.setAttribute("height", 40*height6);
    bar6.setAttribute("width", 100);
    canvas.appendChild(bar6);
