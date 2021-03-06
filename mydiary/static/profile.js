var canvas = document.getElementById("canvas");
var numPosts = document.getElementById("filler").innerHTML;
numPosts = numPosts.replace("[","");
numPosts = numPosts.replace("]","");
numPosts = numPosts.replace(" ","");
numPosts = numPosts.split(",");

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();


var height1 = numPosts[0];
var height2 = numPosts[1];
var height3 = numPosts[2];
var height4 = numPosts[3];
var height5 = numPosts[4];
var height6 = numPosts[5];
var height7 = numPosts[6];

var maxNum = Math.max(height1,height2,height3,height4,height5,height6,height7);

var draw = function(){
    d3.selectAll("svg > *").remove();
    
    console.log(numPosts);
    
    var bar1 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar1.setAttribute("fill", "lightsteelblue");
    bar1.setAttribute("x", 0);
    bar1.setAttribute("y", (360-((360/maxNum)*height1)));
    bar1.setAttribute("height", (360/maxNum)*height1);
    bar1.setAttribute("width", 100);
    canvas.appendChild(bar1);

    var bar2 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar2.setAttribute("fill", "lightsteelblue");
    bar2.setAttribute("x", 100);
    bar2.setAttribute("y", (360-((360/maxNum)*height2)));
    bar2.setAttribute("height", (360/maxNum)*height2);
    bar2.setAttribute("width", 100);
    canvas.appendChild(bar2);

    var bar3 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar3.setAttribute("fill", "lightsteelblue");
    bar3.setAttribute("x", 200);
    bar3.setAttribute("y", (360-((360/maxNum)*height3)));
    bar3.setAttribute("height", (360/maxNum)*height3);
    bar3.setAttribute("width", 100);
    canvas.appendChild(bar3);

    var bar4 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar4.setAttribute("fill", "lightsteelblue");
    bar4.setAttribute("x", 300);
    bar4.setAttribute("y", (360-((360/maxNum)*height4)));
    bar4.setAttribute("height", (360/maxNum)*height4);
    bar4.setAttribute("width", 100);
    canvas.appendChild(bar4);

    var bar5 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar5.setAttribute("fill", "lightsteelblue");
    bar5.setAttribute("x", 400);
    bar5.setAttribute("y", (360-((360/maxNum)*height5)));
    bar5.setAttribute("height", (360/maxNum)*height5);
    bar5.setAttribute("width", 100);
    canvas.appendChild(bar5);

    var bar6 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar6.setAttribute("fill", "lightsteelblue");
    bar6.setAttribute("x", 500);
    bar6.setAttribute("y", (360-((360/maxNum)*height6)));
    bar6.setAttribute("height", (360/maxNum)*height6);
    bar6.setAttribute("width", 100);
    canvas.appendChild(bar6);

    var bar7 = document.createElementNS("http://www.w3.org/2000/svg","rect");
    bar7.setAttribute("fill", "lightsteelblue");
    bar7.setAttribute("x", 600);
    bar7.setAttribute("y", (360-((360/maxNum)*height7)));
    bar7.setAttribute("height", (360/maxNum)*height7);
    bar7.setAttribute("width", 100);
    canvas.appendChild(bar7);

    var axes;
    var label;
    for(i = 0; i < maxNum; i ++){
	axes = document.createElementNS('http://www.w3.org/2000/svg','line');
	axes.setAttribute('x1', '0');
	axes.setAttribute('y1', 360 - ((360/maxNum) * (i + 1)) );
	axes.setAttribute('x1', '700');
	axes.setAttribute('y2', 360 - ((360/maxNum) * (i + 1)) );
	axes.setAttribute('stroke', 'white');
	canvas.appendChild(axes);

	label = document.createElementNS("http://www.w3.org/2000/svg","text");
	label.setAttribute("x", 705);
	label.setAttribute("y", 360 - ((360/maxNum) * (i + 1)) + 18);
	label.setAttribute("font-size","20px");
	label.setAttribute("fill","gray");
	label.innerHTML = i + 1;
	canvas.appendChild(label);
    }
    var prevDay;
    var datelabel;
    for( i = 0 ; i < 7 ; i ++ ){
	prevDay = new Date(today);
	prevDay.setDate(today.getDate()-(6-i));
	mm = prevDay.getMonth() + 1;
	dd = prevDay.getDate();
	yyyy = prevDay.getFullYear();
	datelabel = document.createElementNS("http://www.w3.org/2000/svg","text");
	datelabel.setAttribute("x", (100*i)+2);
	datelabel.setAttribute("y", 380);
	datelabel.setAttribute("font-size", "15px");
	datelabel.setAttribute("fill", "gray");
	datelabel.innerHTML = mm + "/" +  dd + "/" + yyyy;
	canvas.appendChild(datelabel);


    }
    
    
}

draw();
