#!/bin/bash -e
echo "installing cpm..."
mkdir -p ~/.cpm/bin
git clone --recursive https://github.com/castisdev/cpm.git ~/.cpm/src/cpm
ln -sf ~/.cpm/src/cpm/cpm.py ~/.cpm/bin/cpm
echo 'export PATH="~/.cpm/bin:$PATH"' >> ~/.bashrc
export PATH="~/.cpm/bin:$PATH"
echo "...done."
