# CMU 18731 HW2
# Code referenced from:git@bitbucket.org:huangty/cs144_bufferbloat.git
# Edited by: Deepti Sunder Prakash

#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: `basename $0` {experiment_name}"
exit
fi

exp=$1

# Change the -i argument based on your network configuration to plot the bandwidth of hl1, hl2 and a1.
# You can additionally plot bandwidth of other hosts as well in the similar way.
python plot_rate.py -f ${exp}_bw.txt -o ${exp}_hl1_bw.png --xlabel time-100units=1sec --ylabel bandwidth-Mbps -i s1-eth2
python plot_rate.py -f ${exp}_bw.txt -o ${exp}_hl2_bw.png --xlabel time-100units=1sec --ylabel bandwidth-Mbps -i s1-eth3
python plot_rate.py -f ${exp}_bw.txt -o ${exp}_a1_bw.png --xlabel time-100units=1sec --ylabel bandwidth-Mbps -i s1-eth4

python plot_rate.py -f ${exp}_bw.txt -o ${exp}_hr1_bw.png --xlabel time-100units=1sec --ylabel bandwidth-Mbps -i s1-eth2
python plot_rate.py -f ${exp}_bw.txt -o ${exp}_hr2_bw.png --xlabel time-100units=1sec --ylabel bandwidth-Mbps -i s1-eth3
python plot_rate.py -f ${exp}_bw.txt -o ${exp}_a2_bw.png --xlabel time-100units=1sec --ylabel bandwidth-Mbps -i s1-eth4

#Congestion Window
python plot_cwd.py -f ${exp}_tcpprobe.txt -o ${exp}_hl1_cwd.png
python plot_cwd.py -f ${exp}_tcpprobe.txt -o ${exp}_hl2_cwd.png 
python plot_cwd.py -f ${exp}_tcpprobe.txt -o ${exp}_a1_cwd.png 

python plot_cwd.py -f ${exp}_tcpprobe.txt -o ${exp}_hr1_cwd.png
python plot_cwd.py -f ${exp}_tcpprobe.txt -o ${exp}_hr2_cwd.png
python plot_cwd.py -f ${exp}_tcpprobe.txt -o ${exp}_a2_cwd.png


echo "Use xdg-open to see figures"
echo "Figure Names"
echo "Bandwidth-hl1 : ${exp}_hl1_bw.png"
echo "Bandwidth-hl2 : ${exp}_hl2_bw.png"
echo "Bandwidth-a1 : ${exp}_a1_bw.png"
echo "Bandwidth-hr1 : ${exp}_hr1_bw.png"
echo "Bandwidth-hr2 : ${exp}_hr2_bw.png"
echo "Bandwidth-a2 : ${exp}_a2_bw.png"
echo "Congestion Window-hl1 : ${exp}_hl1_cwd.png"
echo "Congestion Window-hl2 : ${exp}_hl2_cwd.png"
echo "Congestion Window-a1 : ${exp}_a1_cwd.png"
echo "Congestion Window-hr1 : ${exp}_hr1_cwd.png"
echo "Congestion Window-hr2 : ${exp}_hr2_cwd.png"
echo "Congestion Window-a2 : ${exp}_a2_cwd.png"
