#!/bin/bash -e
echo "installing cpm..."
mkdir ~/.cpm
git clone --recursive https://github.com/castisdev/cpm.git ~/.cpm/cpm
sudo ln -sf ~/.cpm/cpm/cpm.py /usr/local/bin/cpm
echo "...done."
