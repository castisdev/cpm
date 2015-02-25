#!/bin/bash -e
echo "installing cpm..."
mkdir -p ~/.cpm/bin
git clone --recursive https://github.com/castisdev/cpm.git ~/.cpm/cpm
ln -sf ~/.cpm/cpm/cpm.py ~/.cpm/bin/cpm
echo 'export PATH="~/.cpm/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
echo "...done."
