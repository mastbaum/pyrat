RAT is an Analysis Tool, Python edition
=======================================
A Python implementation of RAT.

Overview
--------
RAT is a simulation and analysis package built with [GEANT4](http://geant4.cern.ch), [ROOT](http://root.cern.ch), and C++, originally developed by S. Seibert for the Braidwood Collaboration. It is now being used (and developed) by the miniCLEAN, DEAP-3600, and SNO+ collaborations.

Bindings for ROOT (PyROOT) and GEANT4 (g4py) permit rebuilding RAT in Python, where the extensive standard library and contructs like generators allow great simplications to the implementation. Python also makes modularity easier -- the core code may be open-source and collaboratively developed by various user collaborations, while experiment-specific parameters and analysis code may be implemented in other separate packages.

