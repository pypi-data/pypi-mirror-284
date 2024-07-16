[![BSD license](https://img.shields.io/badge/License-BSD-orange.svg)](https://lbesson.mit-license.org/)
[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8-brightgreen)](https://www.python.org/downloads/release/python-370/)
[![PyPI](https://img.shields.io/pypi/v/emmer.svg?style=flat)](https://pypi.org/project/emmer/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/emmer)](https://pypi.org/project/emmer/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6652013.svg)](https://doi.org/10.5281/zenodo.6652013)

# EMmer

![emmer](resources/emmer.jpg)

This is a python package to collect important functions related to cryo EM data processing. Broadly, EMmer tools are divided based on the input data type: either a coordinate file (PDB) or a map data (as a numpy array). They are structured as follows: 

## Structuring

* emmer
    * ndimage
        * filter (Low-pass, high-pass, band-pass filters and FSC filters)
        * mask (Compute FDR confidence masks and atomic model masks) 
        * radial_profile (Compute radial profile from a map, estimate bfactors from radial profile) 
        * fsc (compute FSC between two maps)
        * contour (compute properties of a contour at a given threshold like surface area, volume, number of segments)
        * sharpen (modify maps by rescaling the amplitudes)
        * general tools: 
            * average half maps
            * compute real space correlation
            * estimate center of mass of a map
            * I/O operations 
            * Trim map between residues 

    * pdb
        * SSE (Secondary Structure Estimation using DSSP algorithm)
        * convert (to convert PDB to map)
        * General tools: 
            * perturb PDB 
            * Compute RMSD between two PDB
            * Get bfactors of all atoms 
            * Set bfactors of all atoms to a uniform value
            * Neighbor analysis (estimate number of neighbors at a given position)

# Installation

You can install using pip

```
pip install emmer
```
Recommended python version: > 3.6 

## Usage
You can load modules inside your python script like this: 

1) Convert PDB to map
```
from emmer.pdb.convert.convert_pdb_to_map import convert_pdb_to_map
simulated_map = convert_pdb_to_map(input_pdb="/path/to/pdb.pdb", apix=1.1, size=(256,256,256)) # Returns a numpy.ndarray of shape: (256,256,256)
```

2) Compute FSC curve from two halfmaps
```
from emmer.ndimage.fsc.calculate_fsc_curve import calculate_fsc_curve
fsc_curve = calculate_fsc_curve(halfmap1, halfmap2)
```

3) Compute real space correlation between map and model
```
from emmer.pdb.convert.convert_pdb_to_map import convert_pdb_to_map
from emmer.ndimage.compute_real_space_correlation import compute_real_space_correlation as rsc
simulated_map = convert_pdb_to_map(input_pdb="/path/to/pdb.pdb", apix=1.1, size=(256,256,256))
emmap_path = "/path/to/emmap.mrc"
real_space_correlation = rsc(simulated_map, emmap_path)  # Input can either be a path to a map or a numpy.ndarray of shape:(N,N,N) 
```

# Conventions

Some suggestions:
* emmap density data is named "emmap"
* Pixel size is named 'apix'
* Distances are measured in Angstrom.

## Etymology

Refers to a person doing EM: an EM-mer 

Is also a bucket in [Dutch](https://nl.wikipedia.org/wiki/Emmer)... 
"Een emmer is een waterdicht vat dat aan een hengsel gedragen en meestal gebruikt wordt voor het vervoer van vloeistoffen."

It is also a type of wheat.

Acronym for:
Electron Microscopy Mightier (than) Ex Rays

# Feature requests

WRITE THEM HERE
