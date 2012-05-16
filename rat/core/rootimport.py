'''Import ROOT-related modules.'''

import os
import ROOT

G4SYSTEM = os.getenv("G4SYSTEM")

if G4SYSTEM is not None:
    ROOT.gSystem.Load("libRATEvent_" + G4SYSTEM)
    import ROOT.RAT

