#!/bin/bash

# STEP 1: Confirm the directory of where venv will be installed (or is already installed).
if [[ -z "$1" ]];then
    echo No Virtual Environment path specified.
    echo If there is not a directory in $PWD/.venv, a new venv will be created.
    read -p "Continue creating venv at $PWD/.venv ? (y/n)" choice
    if ! [[ "$choice" == [yY] || "$choice" == [yY][eE][sS] ]];then
        echo "Terminating process" 
        exit 1
    fi
    echo Continuing Installation at "$PWD/.venv" ...
else
    echo Changing directory to "$1" ...
    cd "$1"
fi

# STEP 2: install libusb if not installed.
sudo apt-get install libusb-1.0 -y

ruleDest="/etc/udev/rules.d/11-ftdi.rules"
# STEP2: create the rules file.
cat << EOF | sudo tee "$ruleDest"
# /etc/udev/rules.d/11-ftdi.rules
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6001", GROUP="plugdev", MODE="0666"
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6011", GROUP="plugdev", MODE="0666"
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6010", GROUP="plugdev", MODE="0666"
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6014", GROUP="plugdev", MODE="0666"
SUBSYSTEM=="usb", ATTR{idVendor}=="0403", ATTR{idProduct}=="6015", GROUP="plugdev", MODE="0666"
EOF
echo Rules file created at "$ruleDest"

# STEP 4: install python if not installed.
if [[ ! "which python3" ]]; then
    echo "You must have python installed, installing python from apt..."
    sudo apt-get install python3 -y
fi

# STEP 5:
# Install the virtual environment if not already installed.
if [[ ! -e ".venv/" ]]; then
    python3 -m venv .venv
fi
# Ensure that the virtual environment is indeed activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    source .venv/bin/activate
# In case you have a different venv activated.
elif [[ "$PWD/.venv" != "$VIRTUAL_ENV" ]]; then
    deactivate
    # Just in case you did something funky with your venv.
    source deactivate
    source .venv/bin/activate
fi
echo Virtual Environment Successfully Activated ...

# STEP 6: Install the pip dependencies from requirements file
## Freely using pip now that we know that we are in the virtual environment.
echo Install requirements ...
cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null
python3 -m pip install -r VanillaReqs/requirements.txt

# STEP 7: Insert the BLINKA_FT232H=1 into bashrc if it's not already there
rcFile=~/".bashrc"

prop="BLINKA_FT232H"
val="1"
if grep -q "^export $prop=" "$rcFile"; then
    # Look for a string with the words export prop=value in ~/.bashrc
    sed -i "s/^export $prop=.*$/export $prop=$val/" "$rcFile" &&
    echo "Updated new bashrc value $prop=$val"
else
    echo -e "export $prop=$val" >> "$rcFile"
    echo "Inserted bashrc export $prop=$val"
fi

source ~/.bashrc

echo Install complete!
