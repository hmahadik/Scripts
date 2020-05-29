alias l1="ls -1a"
alias sshmv="ssh -X harshad@192.168.100.143"
alias ivyking="ssh -X harshad@ivyking.arcturusnetworks.com"
alias ivymike="ssh -X harshad@ivymike.arcturusnetworks.com"
alias sshmx="ssh root@192.168.100.114"
alias ccat="pygmentize -g -O style=solarized-dark"
alias aty="cd ~/Developer/yocto/fsl-arm-yocto-bsp/ && source setup-environment bld-xwayland"
alias yoctodocker="docker run -it -v ~/Developer:/home/harshad/Developer -u root yocto-imx bash"
alias vae='cd ~/Developer/yocto/fsl-arm-yocto-bsp/sources/meta-arc-vision/recipes-vae/vae'
alias yocto='docker run -it -v ~/Developer:/home/harshad/Developer -v /opt/fsl-imx-xwayland:/opt/fsl-imx-xwayland -w /home/harshad/Developer/yocto/fsl-arm-yocto-bsp -u harshad yocto-imx bash'

function setuiscale() {
	xrandr --output DP-0 --scale $1x$1
	xrandr --output DisplayPort-0 --scale $1x$1
	xrandr --output HDMI-0 --scale $1x$1
	gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "[{'Gdk/WindowScalingFactor', <2>}]"
}

function setscale() {
	gsettings set org.gnome.desktop.interface text-scaling-factor $1
}

