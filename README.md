# interactive_plots

Code to accompany my blog post on [Interactive Plots with Chemical Structures](https://practicalcheminformatics.blogspot.com/2019/11/interactive-plots-with-chemical.html)

# Installation 
```shell
Linux - conda create -f environment_linux.yml
OS-X - conda create -f environment_osx.yml 
```

You can also do this: ```
conda create -n rdkit_env -c rdkit rdkit
conda activate rdkit_env
pip install dash==1.6.0
pip install dash-daq==0.2.1
```

# Running the application
Once installed you should just be able to type: 
```./chem_scatter.py```
or if you work on an OS that doesn't enable you to make python scripts executate, you can do 
```python chem_scatter.py```
