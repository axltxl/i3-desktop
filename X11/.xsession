#################################
# Set keyboard settings on X11 session
#################################

# Make sure the xprofile has been sourced
# regardless of how i3 is gonna be spawned
[ -f ~/.xprofile ] && . ~/.xprofile

# # Load Xresources database
xrdb -merge ~/.Xresources

# Set initial background
xsetroot -solid `xrdb -query | grep color_base00 | awk '{print $2}'`

# Finally, get i3 going
exec i3
