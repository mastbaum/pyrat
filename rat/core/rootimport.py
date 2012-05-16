'''Import ROOT-related modules.

This instance of ROOT should be used throughout rat.
'''
import os
import ROOT

G4SYSTEM = os.enivron["G4SYSTEM"]
ROOT.gSystem.Load("libRATEvent_" + G4SYSTEM)

import ROOT.RAT

