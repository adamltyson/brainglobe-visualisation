# brainglobe-visualisation
Data visualisation in brainglobe


## To install everything needed for visualisation
_Assumes that conda was installed for brainreg/cellfinder. If this is not 
the case, please see the 
[cellfinder installation](https://docs.brainglobe.info/cellfinder/installation)._
```
conda create --name brainglobe-vis python=3.8
conda activate brainglobe-vis
pip install brainrender napari[all] allensdk tables
```

### To check everything is installed properly, run:

* `napari` A window should open up
* `brainrender` A brain should pop up