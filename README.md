<!--
Candy Weaver © 2022 by Sean Gugler is licensed under CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike 4.0 International). To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/
-->
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
 <a property="dct:title" rel="cc:attributionURL" href="https://github.com/sean-gugler/candyweaver">Candy Weaver</a>
 © 2022 by <span property="cc:attributionName">Sean Gugler</span>
 is licensed under 
 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1">
  (Attribution-NonCommercial-ShareAlike 4.0 International)
 </a>
</p>

This game was created for the Apple II Software Enthusiasts "strange jobs/tasks" [challenge](https://www.callapple.org/programming/apple-ii-software-enthusiasts-summer-2022-challenge/). Entries must be primarily in Applesoft (data files and small ASM routines allowed) and submitted by 2022-10-31.

# Play Now!

You can play online in two ways:

1. Download [CandyWeaver.dsk](https://github.com/sean-gugler/candy-weaver/raw/main/CandyWeaver.dsk) and click the "open folder" icon at https://www.scullinsteel.com/apple2/ (tip: F2 toggles full-screen)

2. Visit [CandyWeaver.txt](https://github.com/sean-gugler/candy-weaver/raw/main/CANDYWEAVER.txt) and copy the entire page into your clipbard, then paste into [CyanIIde](https://www.paleotronic.com/applesoft/), click "Update", and click "Run"

You can also download either of those files to use with your favorite local emulator, or real Apple II machine.

# Behind The Scenes

Time spent:
* 30 hours development spread over 6 weeks
* 4 hours QA and playtesting

Tools used:
* [AppleWin 1.30.8.0](https://github.com/AppleWin/AppleWin)
* [CyanIIde](https://www.paleotronic.com/applesoft/)
* [CiderPress v4.1.0](http://a2ciderpress.com/)

References consulted:
* https://www.calormen.com/jsbasic/reference.html
* https://www.applefritter.com/content/random-number-generation-apple-ii-applesoft-basic
* http://www.txbobsc.com/aal/1984/aal8405.html#a1
* https://github.com/tilleul/apple2/tree/master/applesoft/nfs

Yes, I wrote my own simplistic text pre-processor for BASIC. I wanted to use labels instead of line numbers, unpublished code comments, and conditionally-excluded blocks. 20 minutes of Python saved me hours vs trying to develop exclusively in proper Applesoft syntax.

I also put a crude dependency-graph generator into the pre-processor to help me study my program's flow and target certain sections for performance tweaks. You can view the results with any [Graphviz](https://graphviz.org/) implementation, such as https://viz-js.com/
