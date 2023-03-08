<body background="tile.jpg" onload="OnLoad()">
 <center>
 <a href="../../cdshop/index.htm"><img src="../../cdshop/cdinfo.jpg" border="0"></a>
 </center>
 <hr>
 <span class="p-small">
 
 <center>
 <table width="75%" bgcolor="white">
 <tr><td>
 <span class="p-small2">
 <center>
 <a href="../../index.htm">Sacred-texts</a> 
 <a href="../index.htm">Sacred Time Index</a> 
 <a href="../../astro/index.htm">Astrology</a> 
 <a href="index.htm">Sacred Calendars</a> 
 <a href="../../pag/index.htm">Wicca &amp; Neo-Paganism</a> 
 <!-- @+CDEXCL -->
 <a href="../../bos/index.htm">Internet Book of Shadows</a><br>
 <!-- @-CDEXCL -->
 <a href="pom.htm">Phase of the Moon</a>
 </center>
 </span>
 </td></tr>
 </table>
 </center>
 <p>
 </p>
 
 <center>
 <table width="75%" bgcolor="white">
 <tr><td>
 <h1 align="CENTER">Planetary Positions</h1>
 <p>
 <span class="p-small2">
 This page gives the geocentric (earth-centered)
 positions of the Sun, Moon and the planets.
 A list of astrological conjunctions is attached.
 The right ascension is correct to within a couple of minutes.
 Some of the declinations have reversed signs; this is a known bug
 (however these are not used in conventional astrology).
 The position of Pluto will be off by a bit more than the other planets, but
 accurate to within a degree or two.
 The algorithm does not take into account interplanetary
 gravitational interactions; it uses the current
 orbital characteristics of each planet and
 interpolates from a known set of values.
 Hence, the further back or forward in time you set the date to,
 the less accurate the positions will be; they will be more
 accurate the closer they are to 1 January 1980.
 This algorithm does not take into account the precession of the
 equinox.
 </span></p>
 <p>
 This page defaults to the current local time, but you can also set
 other values for the date and time using the
 <a href="#a_datetimeform">form at the bottom of this page</a>.
 The entered time must be Greenwich Mean Time.
 Note that you can set a value B.C.E. by using
 negative numbers in the year field.
 Dates prior to 15 October 1582 are considered be Julian, after that, Gregorian.
 Since not all countries (e.g. Russia) changed their calendar on exactly
 that date, you may need to adjust historical dates accordingly.
 </p><p>
 </p>
 The 'sign' reported
 assumes that Aries coincides with the vernal
 equinox and that each of the zodiacal signs occupy
 exactly one-twelfth of the sky.
 The 'events' are triggered if the two planets are within 15 degrees
 of the exact angle.
 These assumptions will not correspond exactly to some astrological systems,
 and the planets may or may not be in these exact constellations
 (in the strict astronomical sense).
 
 
 <hr>
 <center>
 <script language="JavaScript">;
 <!-- Hide script from older browsers
 
 DecodeArgs();
 OutputTable();
 
 function OutputTable() {
 	if (is_default_time) {
 		OutputLocalTime();
 	} else {
 		time_str=hour_arg+":"+
 		 	minute_arg+":"+
 		 	sec_arg+"."+ 
 		 	msec_arg +
 		 	", "+day_arg+
 		 	" "+month_names[month_arg-1]+
 		 	", "+year_arg;
 		document.write("<span class=\"p-small2\">"+time_str+"</span>");
 	}
 	display_positions(year_arg,
 		month_arg,
 		day_arg,
 		hour_arg,
 		minute_arg,
 		sec_arg,
 		msec_arg);
 }
 
 document.write("</CENTER>");
 document.write("<HR>")
 
 document.write("<DIR>");
 document.write("<span class=\"p-small2\">");
 analyze_events(5.0);
 document.write("</span>");
 document.write("</DIR>");
 
 //End hiding script-->
 </script>
 
 <script language="JAVASCRIPT" type="TEXT/JAVASCRIPT">
 <!-- Hide script from older browsers
 function IsNumericValue(val,bNegOk) {
 	var i;
 	if (bNegOk) {
 		if (val=="")
 			return false;
 	} else {
 		if (val=="" || val<=0) {
 			return false;
 		}
 	}
 	i=0;
 	if (bNegOk) {
 		if (val.charAt(0)=="-") {
 			i=1;
 		}
 	}
 	for (;i<val.length;i++) {
 		if (val.charAt(i)<"0" || val.charAt(i)>"9") {
 			return false;
 		}
 	}
 	return true;
 }
 
 function PopulateDateTimeForm()
 {
 	DateTimeForm.year.value=year_arg;
 	DateTimeForm.month.value=month_arg;
 	DateTimeForm.day.value=day_arg;
 	DateTimeForm.hour.value=hour_arg;
 	DateTimeForm.minute.value=minute_arg;
 	DateTimeForm.sec.value=sec_arg;
 	DateTimeForm.msec.value=msec_arg;
 }
 
 
 function validateForm(theForm) {
 	if (!IsNumericValue(theForm.year.value,true)) {
 		alert("Please enter a number for the year");
 		return false;
 	}
 	if (!IsNumericValue(theForm.month.value,false)) {
 		alert("Please enter a number for the month");
 		return false;
 	}
 	if (theForm.month.value<1 || theForm.month.value>12) {
 		alert("Please enter a month between 1 and 12");
 		return false;
 	}
 	if (!IsNumericValue(theForm.day.value,false)) {
 		alert("Please enter a number for the day");
 		return false;
 	}
 	if (theForm.day.value<1 || theForm.day.value>31) {
 		alert("Please enter a day between 1 and 31");
 		return false;
 	}
 	if (!IsNumericValue(theForm.hour.value,false)) {
 		theForm.hour.value=0;
 		return true;
 	}
 	if (theForm.hour.value<0 || theForm.hour.value>23) {
 		alert("Please enter an hour between 0 and 23");
 		return false;
 	}
 	if (!IsNumericValue(theForm.minute.value,false)) {
 		theForm.minute.value="0";
 		return true;
 	}
 	if (theForm.minute.value<0 || theForm.minute.value>59) {
 		alert("Please enter a minute between 0 and 59");
 		return false;
 	}
 	if (!IsNumericValue(theForm.sec.value,false)) {
 		theForm.sec.value="0";
 		return true;
 	}
 	if (theForm.sec.value<0 || theForm.sec.value>59) {
 		alert("Please enter a second between 0 and 59");
 		return false;
 	}
 	if (!IsNumericValue(theForm.msec.value,false)) {
 		theForm.msec.value="0";
 		return true;
 	}
 	if (theForm.msec.value<0 || theForm.msec.value>999) {
 		alert("Please enter a millisecond between 0 and 999");
 		return false;
 	}
 	return true;
 }
 
 //End hiding script-->
 </script>
 
 <hr>
 <p align="center">
 <span class="p-small2">Enter a date and time (GMT)<br>
 [i.e., The time displayed below is offset by your current timezone, so
 it will not match your local time (unless you live in the
 prime meridian time zone).
 If you enter a new value,
 you need to adjust for daylight savings time (if applicable)
 and your timezone.]
 </span>
 </p>
 
 <a name="a_datetimeform"></a>
 <form onsubmit="return validateForm(this)" action="astro.htm" method="GET" name="DateTimeForm">
 <center>
 <table>
 <td>
 
 </td><tr>
 
 <td><span class="p-small2">year</span></td>
 <td><input type="TEXT" maxlength="12" size="12" name="year"></td>
 
 <td><span class="p-small2">month</span></td>
 <td><input type="TEXT" maxlength="2" size="2" name="month"></td>
 
 <td><span class="p-small2">day</span></td>
 <td><input type="TEXT" maxlength="2" size="2" name="day"></td>
 
 <td> </td>
 <td> </td>
 </tr>
 
 <tr>
 <td><span class="p-small2">hour</span></td>
 <td><input type="TEXT" maxlength="2" size="2" name="hour"></td>
 
 
 <td><span class="p-small2">minute</span></td>
 <td><input type="TEXT" maxlength="2" size="2" name="minute"></td>
 
 <td><span class="p-small2">sec</span></td>
 <td><input type="TEXT" maxlength="2" size="2" name="sec"></td>
 
 <td><span class="p-small2">msec</span></td>
 <td><input type="TEXT" maxlength="2" size="2" name="msec"></td>
 </tr>
 </table>
 <input type="SUBMIT" value="Continue &gt;&gt;&gt;">
 <br>
 <span class="p-small2"><a href="astro.htm">Reset to Current Local Time</a></span>
 </center></form>
 </center>
 </td></tr>
 </table>
 <hr>
 <center>
 <span class="p-small2">
 PLANETARY POSITIONS JAVASCRIPT PROGRAM<br>
 Copyright © 2006 John Bruno Hare, All Rights Reserved
 This code may not be copied, reused or published
 for any reason without express permission
 of the copyright holder.
 </span>
 </center>
 </center>
 
 </span>
 </body>