var canvas = document.getElementById("canvas");
var listBoxes = [];
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
var curMonth = today.getMonth();
var tempMonth = today.getMonth();
var curYear = yyyy;
var tempYear = yyyy;
if(dd<10) {
    dd = '0'+dd
} 

if(mm<10) {
    mm = '0'+mm
}

var dateString = mm+dd+yyyy;

var numDays = function(mon,year){
    if (mon == 0){
	return 31;
    }
    if (mon == 1){
	if (year % 4 != 0 || (year % 100 == 0 && year % 400 != 0)){
	    return 28;
	}
	else{
	    return 29;
	}
    }
    if (mon == 2){
	return 31;
    }
    if (mon == 3){
	return 30;
    }
    if (mon == 4){
	return 31;
    }
    if (mon == 5){
	return 30;
    }
    if (mon == 6){
	return 31;
    }
    if (mon == 7){
	return 31;
    }
    if (mon == 8){
	return 30;
    }
    if (mon == 9){
	return 31;
    }
    if (mon == 10){
	return 30;
    }
    if (mon == 11){
	return 31;
    }
}

var setMonth = function(mon){
    if (mon == 0){
	return "January";
    }
    if (mon == 1){
	return "February";
    }
    if (mon == 2){
	return "March";
    }
    if (mon == 3){
	return "April";
    }
    if (mon == 4){
	return "May";
    }
    if (mon == 5){
	return "June";
    }
    if (mon == 6){
	return "July";
    }
    if (mon == 7){
	return "August";
    }
    if (mon == 8){
	return "September";
    }
    if (mon == 9){
	return "October";
    }
    if (mon == 10){
	return "November";
    }
    if (mon == 11){
	return "December";
    }
}

var drawCal = function(mont,year){
    d3.selectAll("svg > *").remove();
    listBoxes = [];
    
    var cal = document.createElementNS("http://www.w3.org/2000/svg","rect");
    cal.setAttribute("fill","white");
    cal.setAttribute("stroke","black");
    cal.setAttribute("x",100);
    cal.setAttribute("y",100);
    cal.setAttribute("height",600);
    cal.setAttribute("width",600);
    canvas.appendChild(cal);

    var mon = document.createElementNS("http://www.w3.org/2000/svg","rect");
    mon.setAttribute("fill","lightsteelblue");
    mon.setAttribute("stroke","black");
    mon.setAttribute("x",100);
    mon.setAttribute("y",100);
    mon.setAttribute("height",140);
    mon.setAttribute("width",600);
    canvas.appendChild(mon);

    var next = document.createElementNS("http://www.w3.org/2000/svg","polygon");
    next.setAttribute("points", "630,120 630,180 680,150");
    next.setAttribute("fill", "white");
    canvas.appendChild(next);

    next.addEventListener("click", function(){
	if (tempMonth == 11){
	    tempMonth = 0;
	    tempYear = tempYear + 1;
	}
	else{
	    tempMonth = tempMonth + 1;
	}
	drawCal(tempMonth,tempYear);
    });

    var back = document.createElementNS("http://www.w3.org/2000/svg","polygon");
    back.setAttribute("points", "120,150 170,120 170,180");
    back.setAttribute("fill", "white");
    canvas.appendChild(back);

    back.addEventListener("click", function(){
	if (tempMonth == 0){
	    tempMonth = 11;
	    tempYear = tempYear - 1;
	}
	else{
	    tempMonth = tempMonth - 1;
	}
	drawCal(tempMonth,tempYear);
    });

    var days = numDays(mont, year);
    var start = new Date(year, mont, 1).getDay();

    var rows = Math.ceil((days - (7 - start))/7) + 1;
    
    var box;
    for (i = 0; i < rows; i++){
	for (n = 0; n <7; n++){
	    box = document .createElementNS("http://www.w3.org/2000/svg","rect");
	    box.setAttribute("fill","white");
	    box.setAttribute("stroke","black");
	    box.setAttribute("x",100 + (n*(600/7)));
	    box.setAttribute("y", 240 + (i*(460/rows)));
	    box.setAttribute("height",460/rows);
	    box.setAttribute("width",600/7);
	    canvas.appendChild(box);
	    listBoxes.push(box);
	}
    }

    //for (i = 0; i < listBoxes.length; i++){
//	item = listBoxes[i];
//	if (typeof window.addEventListener === 'function'){
//	    (function (item){
//		item.addEventListener("mouseover", function(){
//		    item.setAttribute("fill","gray");
//		});
//		item.addEventListener("mouseout", function(){
//		    item.setAttribute("fill","white");
//		});
//	    })(item);
//	}
  //  }

    //change later
    var monName = document.createElementNS("http://www.w3.org/2000/svg","text");
    monName.setAttribute("x",180);
    monName.setAttribute("y",170);
    monName.setAttribute("font-size","80px");
    monName.setAttribute("fill","white");
    monName.innerHTML = setMonth(mont);
    canvas.appendChild(monName);

    var Sun = document.createElementNS("http://www.w3.org/2000/svg","text");
    Sun.setAttribute("x",140);
    Sun.setAttribute("y",220);
    Sun.setAttribute("font-size","30px");
    Sun.setAttribute("fill","white");
    Sun.innerHTML = "S";
    canvas.appendChild(Sun);

    var Mon = document.createElementNS("http://www.w3.org/2000/svg","text");
    Mon.setAttribute("x",225);
    Mon.setAttribute("y",220);
    Mon.setAttribute("font-size","30px");
    Mon.setAttribute("fill","white");
    Mon.innerHTML = "M";
    canvas.appendChild(Mon);

    var Tue = document.createElementNS("http://www.w3.org/2000/svg","text");
    Tue.setAttribute("x",310);
    Tue.setAttribute("y",220);
    Tue.setAttribute("font-size","30px");
    Tue.setAttribute("fill","white");
    Tue.innerHTML = "T";
    canvas.appendChild(Tue);

    var Wed = document.createElementNS("http://www.w3.org/2000/svg","text");
    Wed.setAttribute("x",395);
    Wed.setAttribute("y",220);
    Wed.setAttribute("font-size","30px");
    Wed.setAttribute("fill","white");
    Wed.innerHTML = "W";
    canvas.appendChild(Wed);

    var Thu = document.createElementNS("http://www.w3.org/2000/svg","text");
    Thu.setAttribute("x",480);
    Thu.setAttribute("y",220);
    Thu.setAttribute("font-size","30px");
    Thu.setAttribute("fill","white");
    Thu.innerHTML = "T";
    canvas.appendChild(Thu);

    var Fri = document.createElementNS("http://www.w3.org/2000/svg","text");
    Fri.setAttribute("x",565);
    Fri.setAttribute("y",220);
    Fri.setAttribute("font-size","30px");
    Fri.setAttribute("fill","white");
    Fri.innerHTML = "F";
    canvas.appendChild(Fri);

    var Sat = document.createElementNS("http://www.w3.org/2000/svg","text");
    Sat.setAttribute("x",650);
    Sat.setAttribute("y",220);
    Sat.setAttribute("font-size","30px");
    Sat.setAttribute("fill","white");
    Sat.innerHTML = "S";
    canvas.appendChild(Sat);


    setup(mont,year);

}

var setup =  function(mon, year){
    var days = numDays(mon, year);
    var start = new Date(year, mon, 1).getDay();
    //console.log(numDays(4,2018));
    var dayNum;
    var name;
    var temp = 1;
    var link;
    var dest;
    for (i = start; i < days + start; i++){
	item = listBoxes[i];
	dayNum = document.createElementNS("http://www.w3.org/2000/svg","text");
	dayNum.setAttribute("x",d3.select(listBoxes[i]).attr("x")-(-2));
	dayNum.setAttribute("y",d3.select(listBoxes[i]).attr("y")-(-18));
	dayNum.setAttribute("font-size","20px");
	dayNum.setAttribute("fill","black");
	dayNum.innerHTML = temp;
	if (mon < 9){
	    if (temp < 10){
		name = "0" + (mon + 1) + "0" + temp + "" + year;
	    }
	    else{
		name = "0" + (mon + 1) + "" + temp + "" + year;
	    }
	}
	else {
	    if (temp < 10){
		name = (mon + 1) + "0" + temp + "" + year;
	    }
	    else{
		name = (mon + 1) + "" + temp + "" + year;
	    }
	}
	listBoxes[i].setAttribute("class",name);
	if (name == dateString){
	    listBoxes[i].setAttribute("fill","lightsteelblue");
	    //canvas.appendChild(listBoxes[i]);
	    if (typeof window.addEventListener === 'function'){
		(function (item){
		    item.addEventListener("mouseover", function(){
			item.setAttribute("fill","gray");
		    });
		    item.addEventListener("mouseout", function(){
			item.setAttribute("fill","lightsteelblue");	
		    });
		})(item);
	    }
	}

	else{
	    if (typeof window.addEventListener === 'function'){
		(function (item){
		    item.addEventListener("mouseover", function(){
			item.setAttribute("fill","gray");
		    });
		    item.addEventListener("mouseout", function(){
			item.setAttribute("fill","white");
			
		    });
		})(item);
	    }
	}
	link = document.createElementNS("http://www.w3.org/2000/svg", "a");
	dest = "input?date=" + name;
	link.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', dest);
	canvas.appendChild(link);
	link.appendChild(listBoxes[i]);
	canvas.appendChild(dayNum);
	temp ++;
	//console.log(d3.select(listBoxes[i]).attr("class"))
    }
}

drawCal(curMonth,curYear);

