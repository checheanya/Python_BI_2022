This repo is designed for the proper installation and running of the *ultraviolence.py* script. In order to run the script follow the instructions below.
The instructions were checked and created on the **Ubuntu 18.04.6 LTS (bionic)**.

The ultraviolence.py file could be downloaded by running the command:
```console
$  git clone --branch HW3 https://github.com/checheanya/Python_BI_2022/
```

## Python 3.11.0rc2 installation

The program was made using Python 3.11.0rc2 version that is currently under development. To install this version you can follow the instruction below which is inspired by (https://www.the-analytics.club/python-3-11-ubuntu).

First, we have to add add-apt repository to the system:
```console
$ sudo apt install software-properties-common
```

Then we can use this utility to install the deadsnakes repository and updating the installed packages.
```console
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
```

This command will install the new version of Python3.11
```console
$ sudo apt install python3.11
```

Then we can set this version of python as the main one (remember which python are you changing to python3.11: python or python3, and use proper command to run the script later):
```console
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
$ python --version
```

Install required packages for the correct work of this version:
```console
$ sudo apt install python3.11-dev python3.11-venv python3.11-distutils python3.11-gdbm python3.11-tk python3.11-lib2to3
```

For downloading other packages we have to install pip:
```console
$ python -m ensurepip --default-pip
```

## Environment 

From now on we will work in a new environment to set up all packages with the version needed to run the script.
To create a new Python environment use:
```console
$ python -m venv violent_env
$ source violent_env/bin/activate
```

## Packages

This file requires special versions of some packages:
* aiohttp==3.8.3
* beautifulsoup4==4.11.1
* biopython==1.77
* google-api-python-client==2.65.0
* lxml==4.9.1
* opencv-python==4.6.0.66
* pandas==1.4.3 (it takes a while to install it but it works, you just have to wait for a bit)

You can install them by running (you might need to change the locations of the folder):
```console
$ pip install -r ./Python_BI_2022/HW3/requirements.txt
```

And finally you can run the *ultraviolence.py* by running this command:
```console
$ python ./Python_BI_2022/HW3/ultraviolence.py
```
Enjoy the output :)

