<body>
 <center>
 <a href="../../index.htm">Sacred-texts</a>
 <a href="../index.htm">The Bible</a>
 </center>
 <hr>
 <h3 align="CENTER">Bible Data Files</h3>
 <p>
 This page has links to archives of the sacred-texts Bible 
 data files, compressed in the 'zip' format, and other technical resources
 for developers.
 These are the best possible data files which we have been able
 to obtain, and to the best of our knowledge are free of copyright
 restrictions or stipulations on their reuse.
 These are the same files which are used to build the sacred-texts
 Bible hypertext.
 These files will be useful for advanced
 developers who wish to create their own Bible websites or software,
 and require programming experience.
 They are not as useful if all you want to do is read the Bible, as they
 require some programming to turn into a readable version.
 </p>
 <p>
 The files contain one verse per line.
 Line breaks in a verse are indicated in some files using tildes.
 Each line is prefixed by the book, verse and chapter,
 separated by vertical bars.
 The book abbreviations are listed in <a href="#bibtab">the table below</a>.
 </p>
 <p>
 The Greek and Hebrew files (Septuagint, Tanach and Greek NT) are
 in UTF-8 format for compactness.
 There are <a href="#utf8code">code samples</a>
 below which demonstrate how to convert 
 a sequence of Unicode characters into UTF-8 and UTF-8 into HTML entities.
 </p>
 <p>
 There are no restrictions on the use of these data files.
 They can be used for commercial or non-commercial projects and altered freely.
 We welcome reports of errors or omissions from these files.
 </p>
 <hr>
 <blockquote>
 <a href="apodat.zip">The Apocrypha (apodat.zip)</a> 267Kb<br>
 <a href="kjvdat.zip">The King James Version (kjvdat.zip)</a> 1,325Kb<br>
 <a href="gntdat.zip">Greek New Testament (gntdat.zip)</a> 448Kb<br>
 <a href="sept.zip">The Septuagint (sept.zip)</a> 1,797Kb<br>
 <a href="tandat.zip">The Tanach (tandat.zip)</a> 1,506Kb<br>
 <a href="vuldat.zip">The Vulgate (vuldat.zip)</a> 1,524Kb<br>
 </blockquote>
 <hr>
 <h3 align="center">Technical specifications</h3>
 <p>
 <a href="tanxlit.htm">Tanach transliteration table</a>.
 </p>
 <hr>
 <a name="bibtab"></a>
 <h4 align="center">Bible data file format</h4>
 <p>
 Below is a table written in the C programming language which
 defines the each of the book abbreviations.
 </p>
 <pre>
 
 typedef struct BibBookDef {
 	string ltitle;				// long title of this book
 	string abbr;				// lowercase abbreviation
 } BibBookDef,*pBibBookDef;
 
 static BibBookDef BibBookTab[]=
 {
 {"Genesis","gen"},
 {"Exodus","exo"},
 {"Leviticus","lev"},
 {"Numbers","num"},
 {"Deuteronomy","deu"},
 {"Joshua","jos"},
 {"Judges","jdg"},
 {"Ruth","rut"},
 {"1 Samuel","sa1"},
 {"2 Samuel","sa2"},
 {"1 Kings","kg1"},
 {"2 Kings","kg2"},
 {"1 Chronicles","ch1"},
 {"2 Chronicles","ch2"},
 {"Ezra","ezr"},
 {"Nehemiah","neh"},
 {"Esther","est"},
 {"Job","job"},
 {"Psalms","psa"},
 {"Proverbs","pro"},
 {"Ecclesiastes","ecc"},
 {"Song of Solomon","sol"},
 {"Isaiah","isa"},
 {"Jeremiah","jer"},
 {"Lamentations","lam"},
 {"Ezekiel","eze"},
 {"Daniel","dan"},
 {"Hosea","hos"},
 {"Joel","joe"},
 {"Amos","amo"},
 {"Obadiah","oba"},
 {"Jonah","jon"},
 {"Micah","mic"},
 {"Nahum","nah"},
 {"Habakkuk","hab"},
 {"Zephaniah","zep"},
 {"Haggai","hag"},
 {"Zechariah","zac"},
 {"Malachi","mal"},
 {"1 Esdras","es1"},
 {"2 Esdras","es2"},
 {"Tobias","tob"},
 {"Judith","jdt"},
 {"Additions to Esther","aes"},
 {"Wisdom","wis"},
 {"Baruch","bar"},
 {"Epistle of Jeremiah","epj"},
 {"Susanna","sus"},
 {"Bel and the Dragon","bel"},
 {"Prayer of Manasseh","man"},
 {"1 Macabees","ma1"},
 {"2 Macabees","ma2"},
 {"3 Macabees","ma3"},
 {"4 Macabees","ma4"},
 {"Sirach","sir"},
 {"Prayer of Azariah","aza"},
 {"Laodiceans","lao"},
 {"Joshua B","jsb"},
 {"Joshua A","jsa"},
 {"Judges B","jdb"},
 {"Judges A","jda"},
 {"Tobit BA","toa"},
 {"Tobit S","tos"},
 {"Psalms of Solomon","pss"},
 {"Bel and the Dragon Th","bet"},
 {"Daniel Th","dat"},
 {"Susanna Th","sut"},
 {"Odes","ode"},
 {"Matthew","mat"},
 {"Mark","mar"},
 {"Luke","luk"},
 {"John","joh"},
 {"Acts","act"},
 {"Romans","rom"},
 {"1 Corinthians","co1"},
 {"2 Corinthians","co2"},
 {"Galatians","gal"},
 {"Ephesians","eph"},
 {"Philippians","phi"},
 {"Colossians","col"},
 {"1 Thessalonians","th1"},
 {"2 Thessalonians","th2"},
 {"1 Timothy","ti1"},
 {"2 Timothy","ti2"},
 {"Titus","tit"},
 {"Philemon","plm"},
 {"Hebrews","heb"},
 {"James","jam"},
 {"1 Peter","pe1"},
 {"2 Peter","pe2"},
 {"1 John","jo1"},
 {"2 John","jo2"},
 {"3 John","jo3"},
 {"Jude","jde"},
 {"Revelation","rev"},
 };
 </pre>
 
 <hr>
 <h4 align="center">UTF encode/decode Utility Routines</h4>
 <a name="utf8code"></a>
 <p>
 These are some code samples which show how to convert to and from UTF-8.
 We have used them during the development process at this site.
 They will be helpful to experienced software developers with
 a knowledge of C.
 While we believe that they are correct, we do not
 warranty their fitness for any particular use.
 By copying this code you affirm that you use it at your own risk.
 We cannot provide any programming advice as to how to use this code,
 so do not write us with questions about these routines.
 </p>
 
 <pre>
 /// these routines assume the following typedefs:
 typedef char*string;
 typedef unsigned short int WORD;
 typedef unsigned char BYTE;
 
 
 // this is a C routine to convert a 16 bit unsigned integer into its
 // UTF-8 equivalent.
 // The UTF-8 is written to output file ofp
 void EncUTF8(WORD w,FILE*ofp)
 {
 	BYTE b1,b2,b3;
 
 	if (w&lt;0x80) {
 		b1=w&amp;0x7f;
 		fputc(b1,ofp);
 	} else if (w&lt;0x800) {
 		b1=0x80+(w&amp;0x3F);		// lower 6 bits
 		b2=0xC0+((w&gt;&gt;6)&amp;0x1F);	// upper 5 bits
 		fputc(b2,ofp);
 		fputc(b1,ofp);
 	} else {
 		b1=0x80+(w&amp;0x3F);		// lower 6 bits
 		b2=0x80+((w&gt;&gt;6)&amp;0x3F);	// next 6 bits
 		b3=0xE0+((w&gt;&gt;12)&amp;0xF);	// upper 4 bits
 		fputc(b3,ofp);
 		fputc(b2,ofp);
 		fputc(b1,ofp);
 	}
 }
 
 
 // this routine takes string 's' encoded in UTF8 format and
 // writes out the equivalent HTML entities to output file 'ofp'
 // note: we have omitted code to generate standard entities such as
 // &amp;quot; or &amp;aacute; which will be required to create a
 // standard HTML file.
 void UTF8toUnicode(FILE*ofp,string s)
 {
 	int i;
 	unsigned long u;
 
 	for (i=0;s[i];i++) {
 		unsigned char b0=(unsigned char)s[i];
 		unsigned char b1=-1;
 		unsigned char b2=-1;
 
 		if (b0&lt;0x7F) {
 			fprintf(ofp,"%c",b0);
 			continue;
 		} else if (b0&gt;=0xC0 &amp;&amp; b0&lt;=0xDF) {
 			b1=(unsigned char)s[i+1];
 			u=((b0-0xC0) * 64) + (b1-0x80);
 			i++;
 			fprintf(ofp,"%d;",u);
 			continue;
 		} else if (b0&gt;=0xE0 &amp;&amp; b0&lt;=0xEF) {
 			b1=(unsigned char)s[i+1];
 			b2=(unsigned char)s[i+2];
 			u=((b0-0xE0) * 4096) + ((b1-0x80)*64) + (b2-0x80);
 			i+=2;
 			fprintf(ofp,"%d;",u);
 			continue;
 		}
 
 		printf("UTF character %x %x %x out of range!!!\n",b0,b1,b2);
 	}
 }
 </pre>
 
 </body>