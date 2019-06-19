#################################
# Set keyboard settings on X11 session
#################################

#
xrdb -merge ~/.Xresources

# Set keyboard mappings
xmodmap ~/.Xmodmap

# Set keyboard rates
xset r rate 200 60
