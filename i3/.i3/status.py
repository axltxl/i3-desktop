################################
# i3pystatus configuration file.
################################
import os
from i3pystatus import Status
from i3pystatus.weather import weathercom

# Base16 Dracula
base00 = "#282936"
base01 = "#3a3c4e"
base02 = "#4d4f68"
base03 = "#626483"
base04 = "#62d6e8"
base05 = "#e9e9f4"
base06 = "#f1f2f8"
base07 = "#f7f7fb"
base08 = "#ea51b2"
base09 = "#b45bcf"
base0A = "#ebff87"
base0B = "#00f769"
base0C = "#a1efe4"
base0D = "#62d6e8"
base0E = "#b45bcf"
base0F = "#00f769"

# Get status bar
status = Status(standalone=True)

##############
#color palette
##############
color_good  = base0B
color_warn  = base0A
color_bad   = base08
color_white = base07

# Displays clock
status.register("clock",
                color=color_white,
                hints= {'markup': 'pango'},
                format= "%m<b>%d</b>|%H<b>%M</b>")

# Weather
status.register("weather",
                format="{icon} {current_temp:>2}{temp_unit}",
                colorize=True,
                backend=weathercom.Weathercom(
                    units="metric",
                    location_code="DAXX0009"
                ))

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
                color_unmuted=color_white,
                format=" {volume:>3}%",
                format_muted=" [MUTE]")

# show battery status
status.register("battery",
        full_color=color_good,
        format=" {percentage:>3.0f}%",
        alert=True,
        alert_percentage=20,
        critical_color=color_bad,
        not_present_text="",
        charging_color=color_good)

# What I'm currently listening to
status.register("now_playing",
                hints={'markup': 'pango'},
                format="<span background=\"" + base0B + "\"><b> {status} {artist}</b> - {title} </span>",
                color=base00)

# run the thing!
status.run()
