#!/bin/bash
set -eux
echo "setting 27 inch 4K monitor"
xrandr --output DisplayPort-0 --mode 3840x2160 --scale "1.5x1.5" --rate 60 --primary
echo "setting 24 inch 1080p monitor"
xrandr --output HDMI-A-0 --mode 1920x1080 --scale 2x2 --pos 5760x0
echo "setting global scaling to 2x" 
gsettings set org.gnome.desktop.interface scaling-factor 2
