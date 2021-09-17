# sublogger

## About

I use the Python subprocess constructor frequently and find myself having to rewrite the bits to print Popen to STDOUT and write to a log when needed.  I thought it would be nice to have a module that standardizes this action across my projects.  If you find yourself doing the same, give it a try!  The examples.py script will produce a log with default name, a log file with user specified name, and the third pass will print in terminal without writing to a log.  That should give you a good idea of how to use it.  The log files are time/date stamped, record username, log the command that was run, and the output.  It also displays the output in your terminal when ran.


### Example

$ import sublogger<br/>
$ log = sublogger.sublogger('test.log')<br/>
$ cmd = "ls -lha"<br/>
$ log.cmd_out(cmd)<br/>

[$] total 36K
[$] drwxr-xr-x 4 m4xx3d0ut m4xx3d0ut 4.0K Sep 17 14:17 .<br/>
[$] drwxr-xr-x 4 m4xx3d0ut m4xx3d0ut 4.0K Sep 17 09:47 ..<br/>
[$] drwxr-xr-x 8 m4xx3d0ut m4xx3d0ut 4.0K Sep 17 14:16 .git<br/>
[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut   12 Sep 17 14:16 .gitignore<br/>
[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut 1.1K Sep 17 09:47 LICENSE<br/>
[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut  309 Sep 17 09:59 README.md<br/>
[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut 1.5K Sep 17 15:02 sublogger.py<br/>
[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut   45 Sep 17 15:02 test.log<br/>


### Example Log File

17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] ls -lha<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] total 36K<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] drwxr-xr-x 4 m4xx3d0ut m4xx3d0ut 4.0K Sep 17 14:17 .<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] drwxr-xr-x 4 m4xx3d0ut m4xx3d0ut 4.0K Sep 17 09:47 ..<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] drwxr-xr-x 8 m4xx3d0ut m4xx3d0ut 4.0K Sep 17 14:16 .git<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut   12 Sep 17 14:16 .gitignore<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut 1.1K Sep 17 09:47 LICENSE<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut  309 Sep 17 09:59 README.md<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut 1.5K Sep 17 15:02 sublogger.py<br/>
17-Sep-2021 (15:02:48)-m4xx3d0ut-[$] -rw-r--r-- 1 m4xx3d0ut m4xx3d0ut 1002 Sep 17 15:02 test.log<br/>
