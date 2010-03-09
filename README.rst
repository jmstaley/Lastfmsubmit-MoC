===============================
Last.fm Music on Console script
===============================

A simple script put together for MoC to submit tracks to lastfm and provide song notifications.

The script depends on lastfmsubmitd and pynotify.


=====
Usage
=====

The script was designed to be used in connection with Music On Console and the last.fm submission daemon. The script also depends on pynotify.

Download the script from::

 http://cloud.github.com/downloads/jmstaley/Lastfmsubmit-MoC/lastfmsubmit_notify_songchange.py

This will create a Lastfmsubmit-MoC directory, inside this is the script. The script needs to be made executable::

 chmod +x lastfmsubmit_notify_songchange.py. 
 
This then needs to be put somewhere that MoC can find it. For example I have a bin folder in my home directory so I place it there /home/jon/bin/.

Now you need to add the command to moc. In you moc config, which should be located in::

 ~/.moc/config 
 
find the line that starts with OnSongChange. Uncomment this line and change it so that it reads::

 OnSongChange = "/home/jon/bin/lastfmsubmit_notify_songchange.py -a %a -t %t -l %d -r %r" 

replacing /home/jon/bin/ for the place you have put the file.

There are two extra options that can be added

 * -q – suppresses the notification
 * -n – suppresses the lastfm submi
