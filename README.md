# interactive_plots

Code to accompany my blog post on [Interactive Plots with Chemical Structures](https://practicalcheminformatics.blogspot.com/2019/11/interactive-plots-with-chemical.html)

## Installation 

Linux
```shell 
conda create -f environment_linux.yml
```
OS-X
```shell
conda create -f environment_osx.yml 
```

You can also do this:
```shell
conda create -n rdkit_env -c rdkit rdkit
conda activate rdkit_env
pip install dash==1.6.0
pip install dash-daq==0.2.1
```


## Running the application
Once installed you should just be able to type
```shell
./chem_scatter.py
```
or if you work on an OS that doesn't enable you to make python scripts executable, you can do 
```:
python chem_scatter.py
```
Once the script starts, you should see something like this
```shell
Running on http://127.0.0.1:8050/
Debugger PIN: 056-419-733
```
The IP address will be different, it should be your IP address.  You should now be able to copy the web address and paste it into your favorite browser to run the program. 

