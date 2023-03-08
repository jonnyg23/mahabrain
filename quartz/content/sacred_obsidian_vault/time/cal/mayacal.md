<body background="mayawall.jpg">
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
 <a href="index.htm">Sacred Calendars</a> 
 <a href="../../nam/index.htm">Native American</a> 
 <a href="astro.htm">Planetary Positions</a> 
 <a href="isldate.htm">Islamic Date</a>
 <a href="jdate.htm">Jewish Date</a>
 </center>
 </span>
 </td></tr>
 </table>
 
 <center>
 <table width="800" bgcolor="white">
 <tr><td>
 <h1 align="CENTER">Current Mayan Date</h1>
 
 <script language="JavaScript">;
 <!-- Hide script from older browsers
 /// This script and all other content on this page
 /// Copyright (c) 2002 John Bruno Hare, All Rights Reserved
 /// This code may not be copied, reused or published
 /// for any reason without express permission
 /// of the copyright holder.
 
 // alias floor
 function floor(x)
 {
 	return Math.floor(x);
 }
 
 //  MOD  --  Modulus function which works for non-integers.
 function mod(a, b)
 {
     return a - (b * floor(a / b));
 }
 
 //  AMOD  --  Modulus function which returns numerator if modulus is zero
 function amod(a, b)
 {
     return mod(a - 1, b) + 1;
 }
 
 function leap_gregorian(year)
 {
     return ((year % 4) == 0) &&
 (!(((year % 100) == 0) && ((year % 400) != 0)));
 }
 
 var GREGORIAN_EPOCH = 1721425.5;
 
 function gregorian_to_jd(year, month, day)
 {
     return (GREGORIAN_EPOCH - 1) +
            (365 * (year - 1)) +
            floor((year - 1) / 4) +
            (-floor((year - 1) / 100)) +
            floor((year - 1) / 400) +
            floor((((367 * month) - 362) / 12) +
            ((month <= 2) ? 0 :
                                (leap_gregorian(year) ? -1 : -2)
            ) +
            day);
 }
 
 function jd_to_gregorian(jd) {
     var wjd, depoch, quadricent, dqc, cent, dcent, quad, dquad,
         yindex, dyindex, year, yearday, leapadj;
 
     wjd = Math.floor(jd - 0.5) + 0.5;
     depoch = wjd - GREGORIAN_EPOCH;
     quadricent = Math.floor(depoch / 146097);
     dqc = mod(depoch, 146097);
     cent = Math.floor(dqc / 36524);
     dcent = mod(dqc, 36524);
     quad = Math.floor(dcent / 1461);
     dquad = mod(dcent, 1461);
     yindex = Math.floor(dquad / 365);
     year = (quadricent * 400) + (cent * 100) + (quad * 4) + yindex;
     if (!((cent == 4) || (yindex == 4))) {
         year++;
     }
     yearday = wjd - gregorian_to_jd(year, 1, 1);
     leapadj = ((wjd < gregorian_to_jd(year, 3, 1)) ? 0
                                                   :
                   (leap_gregorian(year) ? 1 : 2)
               );
     month = Math.floor((((yearday + leapadj) * 12) + 373) / 367);
     day = (wjd - gregorian_to_jd(year, month, 1)) + 1;
 
     return new Array(year, month, day);
 }
 
 //  JD_TO_MAYAN_COUNT  --  Calculate Mayan long count from Julian day
 var MAYAN_COUNT_EPOCH = 584282.5;
 
 function jd_to_mayan_count(jd)
 {
     var d, baktun, katun, tun, uinal, kin;
 
     d = jd - MAYAN_COUNT_EPOCH;
     baktun = floor(d / 144000);
     d = mod(d, 144000);
     katun = floor(d / 7200);
     d = mod(d, 7200);
     tun = floor(d / 360);
     d = mod(d, 360);
     uinal = floor(d / 20);
     kin = mod(d, 20);
 
     return new Array(baktun, katun, tun, uinal, kin);
 }
 
 //  JD_TO_MAYAN_HAAB  --  Determine Mayan Haab "month" and day from Julian day
 
 var MAYAN_HAAB_MONTHS = new Array("Pop", "Uo", "Zip", "Zotz", "Tzec", "Xul",
                                   "Yaxkin", "Mol", "Chen", "Yax", "Zac", "Ceh",
                                   "Mac", "Kankin", "Muan", "Pax", "Kayab", "Cumku");
 
 function print_haab_months()
 {
 	var i,len=MAYAN_HAAB_MONTHS.length,halflen=floor(len/2);
 	document.write("<TABLE BORDER=2>");
 	for (i=0;i<halflen;i++) {
 
 		document.write("<TR>");
 		document.write("<TD><span class=\"p-small2\">");
 		document.write((1+i) + " " + MAYAN_HAAB_MONTHS[i]);
 		document.write("</span></TD>");
 		document.write("<TD><span class=\"p-small2\">");
 		document.write((1+i+halflen) + " " + MAYAN_HAAB_MONTHS[i+halflen]);
 		document.write("</span></TD>");
 		document.write("</TR>");
 	}
 	document.write("</TABLE>");
 }
 
 function jd_to_mayan_haab(jd)
 {
     var lcount, day;
 
     lcount = jd - MAYAN_COUNT_EPOCH;
     day = mod(lcount + 8 + ((18 - 1) * 20), 365);
 
     return new Array (floor(day / 20) + 1, mod(day, 20));
 }
 
 //  JD_TO_MAYAN_TZOLKIN  Determine Mayan Tzolkin "month" and day from Julian day
 // the term 'month' is a misnomer.
 
 var MAYAN_TZOLKIN_MONTHS = new Array("Imix", "Ik", "Akbal", "Kan", "Chicchan",
                                      "Cimi", "Manik", "Lamat", "Muluc", "Oc",
                                      "Chuen", "Eb", "Ben", "Ix", "Men",
                                      "Cib", "Caban", "Etxnab", "Cauac", "Ahau");
 
 function print_tzolkin_months()
 {
 	var i,len=MAYAN_TZOLKIN_MONTHS.length,halflen=floor(len/2);
 	document.write("<TABLE BORDER=2>");
 	for (i=0;i<halflen;i++) {
 
 		document.write("<TR>");
 		document.write("<TD><span class=\"p-small2\">");
 		document.write((1+i) + " " + MAYAN_TZOLKIN_MONTHS[i]);
 		document.write("</span></TD>");
 		document.write("<TD><span class=\"p-small2\">");
 		document.write((1+i+halflen) + " " + MAYAN_TZOLKIN_MONTHS[i+halflen]);
 		document.write("</span></TD>");
 		document.write("</TR>");
 	}
 	document.write("</TABLE>");
 }
 var MONTH_NAMES=new Array("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec");
 
 function jd_to_mayan_tzolkin(jd)
 {
     var lcount = jd - MAYAN_COUNT_EPOCH;
 
     return new Array (amod(lcount + 20, 20), amod(lcount + 4, 13));
 }
 
 function print_maya_date()
 {
 	var today=new Date();
 	var sec=today.getSeconds();
 	var min=today.getMinutes();
 	var hour=today.getHours();
 	var mday=today.getDate();
 	var mon=today.getMonth();
 	var year=today.getFullYear();
     var j = gregorian_to_jd(year, mon + 1, mday) +
            ((sec + 60 * (min + 60 * hour)) / 86400.0);
 	mayadate=jd_to_mayan_count(j);
 	document.write(
 	"baktun " + mayadate[0] +
 	" katun " + mayadate[1] +
 	" tun " + mayadate[2] +
 	" uinal " + mayadate[3] +
 	" kin " + floor(mayadate[4]));
 
 	document.write("<BR>");
     mayhaabcal = jd_to_mayan_haab(j);
     document.write("Haab: " + 
 		floor(mayhaabcal[1]) + " " + 
 		MAYAN_HAAB_MONTHS[mayhaabcal[0] - 1]);
 	document.write("<BR>");
     maytzolkincal = jd_to_mayan_tzolkin(j);
     document.write("Tzolkin: " + 
 		floor(maytzolkincal[1]) + " " + 
 		MAYAN_TZOLKIN_MONTHS[floor(maytzolkincal[0]) - 1]);
 	
 	document.write("<P>Mayan epoch: ");
 	mcedate=jd_to_gregorian(MAYAN_COUNT_EPOCH);
 	document.write(
 	mcedate[2] + " " +
 	MONTH_NAMES[mcedate[1]-1] + ", " +
 	(1+Math.abs(mcedate[0])));
 	document.write(" B.C.E.</P>");
 }
 
 function OutputLocalTime() {
 	var mon,day,now,hour,min,ampm,time,str,tz,end,beg;
 	day=new Array("Sun","Mon","Tue","Wed","Thu","Fri","Sat");
 	d=new Date();
 	sss=Math.round(d.getTime()/1000);
 	now=new Date(sss*1000);
 	hour=now.getHours();
 	min=now.getMinutes();
 	sec=now.getSeconds();
 	ampm=(hour>=12)?"pm":"am";
 	hour=(hour==0)?12:(hour>12)?hour-12:hour;
 	min=(min<10)?"0"+min:min;
 	tz="";
 	time=hour+":"+min+":"+sec + ampm + tz+
 	", "+day[now.getDay()]+
 	" "+MONTH_NAMES[now.getMonth()]+
 	" "+now.getDate()+
 	", "+now.getFullYear();
 	document.write("...date based on local time "+time);
 }
 
 //End hiding script-->
 </script>
 
 <center>
 <b>
 
 <script language="JavaScript">;
 <!-- Hide script from older browsers
 print_maya_date();
 document.write("<P>");
 OutputLocalTime();
 document.write("</P>");
 //End hiding script-->
 </script>
 
 <hr>
 </b>
 </center>
 
 <span class="p-small2">
 <p>
 The Mayans had an elaborate calendrical system, no longer in use,
 which obviously evolved in complete isolation from those of the old world.
 This system ended with the fall of the Mayan civilization.
 Most of the remaining knowledge of it was destroyed by
 the Spanish during the conquest.
 It was not until very recently, during the 1990s, that archeologists
 have finally been able to fill in many of the gaps in our knowledge of
 Mayan civilization, including the calendrical system.
 </p>
 <p>
 The Mayans were skilled mathematicians, and this
 shows in their calendar; besides having a concept of zero,
 they also had a firm grasp of modular arithmetic; they also
 worked extensively in base 20.
 However, despite their great skill at observing the heavens,
 their calendar has no relationship to lunar or seasonal cycles,
 and is only synchronized with the solar cycle year approximately.
 The Mayans were aware of this discrepancy;
 they simply didn't feel the compelling need
 to synchronize their calendar with the sun that Old World civilizations did.
 </p>
 <p>
 The Mayans used three separate calendars.
 The Long Count was pricipally used for historical purposes,
 since it can define any date for millenia in the past and future.
 The Haab was a civil calendar based on a year of 360 days
 consisting of 18 periods of 20 days.
 Five days were added at the end of the Haab year to approximately
 synchronize it with the solar year.
 The Tzolkin calendar was used for ceremonial purposes,
 which had 20 periods of 13 days.
 The Tzolkin calendar went through a complete cycle every 260 days.
 The signficance of this cycle is unknown; it may be connected with
 the orbit of Venus, which has a period of 263 days.
 The Haab and Tzolkin dates did not have a year component; however,
 a combined Haab and Tzolkin date specify a unique day within a 52 year cycle.
 </p>
 </span>
 
 <h3 align="CENTER">It's the end of the world as we know it...</h3>
 <span class="p-small2">
 <dir><i>
 ...I feel confident that there was no such thing as an initial point of departure for the Maya calendar, but, rather, <b>time was conceived of as without beginning or end</b>, and therefore one could project one's calculations farther and farther into the past without ever reaching a starting point.</i>--J. Eric S. Thompson, <cite>Maya Hieroglyphic Writing</cite>, <a href="../../nam/maya/mhw/mhw06.htm#page_149">p. 149</a> (<b>emphasis</b> added)</dir>
 
 <p>
 There is a great deal of nonsense that has been written about the Mayan
 long count.
 It has been claimed (most egregiously, in a Discovery Channel TV series)
 that it will 'come to an end' in the near future, and along with it
 will arrive a Mayan apocalypse, a pole shift, earth change, cosmic
 convergence, whatever.
 Given the completely cyclic nature of the long count, this is an
 idiotic characterization.
 Once any given cycle ends, another begins, endlessly.
 The full long count is currently only at baktun 12; there are still 8
 baktuns (or about three thousand years) before it turns over.
 The current Katun <i>will</i> increment about ten years
 from now (13.0.0.0.0 will be on December 21st, 2012). 
 However, there is no reason
 that date should be any more cosmologically
 significant than the end of the common era millenium was!
 </p>
 
 <p>
 For one thing, this is a theoretical reconstruction of the Mayan calendar,
 since it hasn't been in use for hundreds of years.
 The Mayan epoch shown above was hotly debated
 by archeologists for many decades.
 The date shown is a consensus date, originally proposed by J.E.S. Thompson,
 and supported by carbon dating and other methods.
 However, this particular date for the Mayan epoch could
 still be off by some amount, possibly by years.
 Thus any eschatological theories based on this calendar would have
 to be adjusted accordingly.
 This is similar to the Christian era, which may be off by several years
 since we don't have Jesus' birth certificate in hand; so any predictions
 of the end of the world based on when that calendar ticks over were just
 as absurd.
 Furthermore, the assumption that some occurance of the Christian
 millenium marks the expiration date of the Universe is
 based on base 10 math: the fact that the Mayans adopted
 a base 20 system shows how arbitrary this assumption is.
 And anyway, last time I checked, the date is now 2000 and counting, and
 the universe is still here...
 </p>
 </span>
 
 <h3 align="CENTER">Long Count</h3>
 <span class="p-small2">
 <p>
 The long count was broken down into five components:
 </p>
 </span>
 <center>
 <table border="2">
 <tr>
 <td> </td>
 <th><span class="p-small2">Baktun</span></th>
 <th><span class="p-small2">Katun</span></th>
 <th><span class="p-small2">Tun</span></th>
 <th><span class="p-small2">Uinal</span></th>
 <th><span class="p-small2">Kin</span></th>
 </tr>
 
 <tr>
 <td><span class="p-small2"><i>Equals:</i></span></td>
 <td><span class="p-small2">20 Katun</span></td>
 <td><span class="p-small2">20 Tun</span></td>
 <td><span class="p-small2">18 Uinal</span></td>
 <td><span class="p-small2">20 kin</span></td>
 <td><span class="p-small2"> </span></td>
 </tr>
 
 <tr>
 <td><span class="p-small2"><i>Days</i></span></td>
 <td><span class="p-small2">144,000</span></td>
 <td><span class="p-small2">7,200</span></td>
 <td><span class="p-small2">360</span></td>
 <td><span class="p-small2">20</span></td>
 <td><span class="p-small2">1</span></td>
 </tr>
 
 <tr>
 <td><span class="p-small2"><i>Years</i></span></td>
 <td><span class="p-small2">394.3</span></td>
 <td><span class="p-small2">19.7</span></td>
 <td><span class="p-small2">0.97</span></td>
 <td><span class="p-small2"> </span></td>
 <td><span class="p-small2"> </span></td>
 </tr>
 
 </table>
 </center>
 
 <span class="p-small2">
 <p>The zero day of the Mayan calendar is the date given above
 as the 'Mayan Epoch'.
 The significance of this particular date, which far exceeds any
 known historical horizon for Mayan civilization, is unknown.
 No recorded Mayan date preceeds baktun 7, and most of the historical
 Mayan events occurred during baktun 9 (from 435-830 C.E.).
 </p>
 
 <p>
 Even <i>longer</i> dates with more components have been found.
 This includes enough additional base 20 components
 to write dates millions of years
 in the past or future, even though
 no such dates actually occur in the Mayan inscriptions, just contemporary
 dates with more digits in front of them.
 Imagining that kind of chronological depth to the universe is another
 Mayan accomplishment, similar to Hindu and Buddhist chronologies which
 encompass not just millenia, but billions of years of cosmic history.
 </p>
 </span>
 
 <h3 align="CENTER">Haab Date</h3>
 
 <span class="p-small2">
 <p>Each Haab date consists of a one of twenty day numbers,
 (numbered from 0 to 19), and a 'month' or <i>uinal</i> name,
 of which there are 18. The uinal names are as follows:
 
 </p><center>
 <script language="JavaScript">;
 <!-- Hide script from older browsers
 print_haab_months();
 //End hiding script-->
 </script>
 </center>
 
 <p>Five days were added at the end of the year: this
 Uinal was called Uayeb.
 There is no year component to the Haab date.
 </p>
 </span>
 
 <h3 align="CENTER">Tzolkin Date</h3>
 
 <h3 align="CENTER">Haab Date</h3>
 <span class="p-small2">
 <p>
 The Tzolkin was a cycle of 260 days, consisting of a day number from 1 to 13
 and one of 20 day names.
 In this case both the day number and the day name are incremented each day,
 that is, both advance in parallel.
 Since 13 and 20 do not divide evenly, it is 260 days before a particular
 Tzolkin date repeats.
 There is no year component to the Tzolkin date.
 </p>
 <p>This is a list of the Tzolkin day names:</p>
 
 <center>
 <script language="JavaScript">;
 <!-- Hide script from older browsers
 print_tzolkin_months();
 //End hiding script-->
 </script>
 </center>
 </span>
 
 </td></tr>
 </table>
 </center>
 
 
 </center></span>
 </body>