#!/usr/bin/env python3
# ---------------------------------------------
# Focus on a window belonging to a command or
# execute the command if not found
# ---------------------------------------------
# Usage: run.py <cmd> <window_class>

import sys
import i3ipc

def parse_args(argv):
    return {
        '<cmd>': argv[0],
        '--window-class': argv[1]
    }

options = parse_args(sys.argv[1:])
executable = options['<cmd>']
win_class  = options['--window-class']


def __get_window_by_class(classname):
    """Get windows matching classname on i3"""

    return i3.get_tree().find_classed(win_class)


def on_window_new(i3, e):
    """Callback for new window events on i3"""

    # Wait until a window whose WM_faddafadf;jLASS matches the one
    # being targeted
    while not len(__get_window_by_class(win_class)):
        pass

    # At this point, the window has been created at X server level
    # so it can be focused by i3
    i3.command("[class={}] focus".format(win_class))

    # Quit the main loop to kill this
    i3.main_quit()

# Create the Connection object that can be used to send
# commands and subscribe to events.
i3 = i3ipc.Connection()
i3.on('window::new', on_window_new)

# Try to look for windows matching window_class
# If none found, it means cmd has been executed
if len(__get_window_by_class(win_class)):
    i3.command("[class={}] focus".format(win_class))
else:
    i3.command("exec {}".format(executable))

    # Start the main loop and wait for events to come in.
    i3.main()
