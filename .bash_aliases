alias l1="ls -1a"
alias dc="docker-compose"
alias ccat="pygmentize -g -O style=solarized-dark"
alias df="df -h"
alias du="du -h"

function setuiscale() {
	xrandr --output DP-0 --scale $1x$1 &> /dev/null
	xrandr --output DisplayPort-0 --scale $1x$1 &> /dev/null
	xrandr --output HDMI-0 --scale $1x$1 &> /dev/null
	gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "[{'Gdk/WindowScalingFactor', <2>}]" &> /dev/null
}

function setscale() {
	gsettings set org.gnome.desktop.interface text-scaling-factor $1 &> /dev/null
}

