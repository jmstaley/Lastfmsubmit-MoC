#!/usr/bin/env python
import subprocess
import pynotify

from optparse import OptionParser

if __name__ == '__main__':

    # setup parser
    parser = OptionParser()

    # set default to show notification
    parser.set_defaults(quiet=False)

    parser.add_option('-q', action='store_true', dest='quiet')
    parser.add_option('-n', action='store_true', dest='no_submit')
    parser.add_option('-a', '--artist', dest='artist')
    parser.add_option('-t', '--title', dest='title')
    parser.add_option('-l', '--length', dest='length')
    parser.add_option('-r', '--album', dest='album')

    (options, args) = parser.parse_args()

    if not options.no_submit:
        # call lastfmsubmit
        subprocess.call(['/usr/lib/lastfmsubmitd/lastfmsubmit', 
                         '--artist', '%s' % options.artist,
                         '--title', '%s' % options.title, 
                         '--length', '%s' % options.length, 
                         '--album', '%s' % options.album])

    # send notification to libnotify
    if not options.quiet:
        if pynotify.init('Notify MoC'):
            n = pynotify.Notification('%s' % options.artist, '%s' % options.title)
            n.set_timeout(5000)
            n.show()
