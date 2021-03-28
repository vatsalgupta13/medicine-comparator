# Backend
Python scipts for Api Calls


<h2>The Altered CSV file is not in this repository due to file restrictions</h2>
(https://www.dropbox.com/s/a16wonw628z27ga/file2.csv?dl=0)<br><br>
Download the CSV dataset from the link as it could not be uploaded due to Github size restrictions<br><br>
This file2.csv is already ready to be used but incase more entries need to be added, Delete the Alternatives column first , rename the file and follow the steps below<br><br>
In order to have the Alternatives Generated :
<ul>
<li>Put the csv in the same folder as Alternatives.py</li>
<li>Input the name of the file in the code where it reads the file</li>
<li>A new file will be generated with the Alternatives column made</li>
</ul>

<h3>NOTE: The Alternatives column should not be present in the original file</h3>


<h2>HostApi1.py</h2>
This is the script that needs to be run in order to host the API on the localhost:5000 server<br><br>
In case the server is changed, please change the base url in the compare.js react file in general views folder


<h3>NOTE: Do change the debugging mode to false in the script at the time of hosting on actual server as debugging mode is only meant to be used while testing</h3>

<h2>test.py</h2>
This is a script to test whether or not HostApi1.py is functioning correctly<br>
When hosting on actual server, do change the URL in the code
