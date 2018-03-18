#!/bin/bash
qbfile=~/.config/qutebrowser/bookmarks/urls
if [ -f $qbfile ]; then
    if [ -f $qbfile.bak ]; then
        i=0
        while :
        do
            if [ ! -f $qbfile.bak.$i ]; then
                cp $qbfile $qbfile.bak.$i
                echo "qutebrowser bookmarks successfully backed up as " $qbfile.bak.$i
                break
            fi
            let i=$i+1
        done
    else
        cp $qbfile $qbfile.bak
        echo "qutebrowser bookmarks successfully backed up as " $qbfile.bak
    fi
fi
buku -p -f 40 | awk -F '\t' '{print $1" "$2}' > ~/.config/qutebrowser/bookmarks/urls
