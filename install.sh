#!/bin/bash
if [[ $EUID -ne 0 ]]; then
    echo "Please run as root" 
    echo "like this 'sudo bash $0'"
    exit 1
fi
    sudo pip3 install opencv-python pyzbar
    chmod +x qrcan.py
    sudo cp qrcan.py /usr/bin/qrcan
    echo ""
    echo ""
    echo "Now you can run qrcan."
    echo "qrcan filename.png"
