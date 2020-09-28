#!/bin/bash
set -x
# 1080p HDMI right of 4K DisplayPort-0
xrandr --output DisplayPort-0 --mode 3840x2160 --scale "1.5x1.5" --rate 60 --primary
xrandr --output HDMI-A-0 --mode 1920x1080 --scale 2x2 --pos 5760x0
gsettings set org.gnome.desktop.interface scaling-factor 2

# 1680x1050 DVI left of 4K DP-0
# xrandr --output DVI-D-0 --mode 1680x1050 --scale 2x2 --pos 0x0
# xrandr --output DP-0 --mode 3840x2160 --scale "1.25x1.25" --rate 60 --primary --pos 3360x0
# gsettings set org.gnome.desktop.interface scaling-factor 2
