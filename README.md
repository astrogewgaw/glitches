# glitches

[![Code style: black][black-badge]][black]

this is my own copy of the database of pulsar glitches maintained [**here**][table] by the Jodrell Bank Centre for Astrophysics at the University of Manchester. if you end up using the data from the original table or from this repository, please cite [**Espinoza et al. (2011)**][paper] (a BibTeX style citation for the same is given in the [**CITATION.md**](CITATION.md) file) and refer to the original [**url**][glitches]. the data, in all of its JSON glory, is available in the [**glitches.json**](glitches.json) file. the whole scraping code resides in the [**scrap.py**](scrap.py) file. the data is updated on every Friday, at midnight (in UTC time). this repository will eventually power the [**koshka**][koshka] package, which aims to make accessing all pulsar and radio transient related catalogues easier.

[black]: https://github.com/psf/black
[koshka]: https://github.com/astrogewgaw/koshka
[glitches]: http://www.jb.man.ac.uk/pulsar/glitches.html
[paper]: http://adsabs.harvard.edu/abs/2011MNRAS.414.1679E
[table]: http://www.jb.man.ac.uk/pulsar/glitches/gTable.html
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
