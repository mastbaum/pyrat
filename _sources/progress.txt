Port Progress
=============
A summary of tasks remaining for porting RAT to Python. Only parts that are generally useful will be ported; experiment-specific packages will extend RAT to fill in the rest.

To-do
-----
bin
```
* rat: similar to chroma-sim

data
````
Convert to strict JSON.

test
````
Update macros.

src/core
````````
* BurstProc: supernova burst trigger, should go in processors
* CutProc: depends on DS
* EventInfo: exists only to contain a DS::Calib object? why in core?
* Gsim, GLG4*: replaced by g4py interface
* PruneProc: depends on DS
* RunManager
* Version: easy

src/daq
```````
All heavily dependent on DS. This should be modular.

src/db
``````
* DBLink

src/ds
``````
Seriously need to figure something out here.

src/fit
```````
* FitterProcessor, framework bits

src/gen
```````
These will be re-implemented as python generators. For Decay0, generate a wrapper with f2py.

src/geo
```````
How to flip between G4 CSG and chroma meshes?

src/io
``````
These depend on input and output DS.

* DispatchEvents
* G4Stream: copy mute from chroma, move to core
* InNetProducer
* OutNetProc
* OutROOTProc
* Pack
* PackEvents
* TrackCursor, TrackNav, TrackNode

src/physics
```````````
Perhaps some of this will stay in C++.

* EmPhysicsListV*
* G4Cerenkov
* GLG4NeutronDiffusionAndCapture
* GLG4OpAttenuation
* GLG4PMTOpticalModel: deprecated
* GLG4Scint
* HadronicPhysicsListV*
* PhotonThinning
* PhysicsList

src/util
````````
* BitManip: mostly trivial, maybe do not port
* Factory
* getopt - replace with python optparse

Done
----
bin
```
* ratci: unchanged
* ratdb: unchanged
* ratinfo: unchanged
* rattest: unchanged

src/calib
`````````
Mostly experiment-specific, will not be ported into main project.

src/cmd
```````
* Messengers: trivial when macros are python scripts
* ProcBlockManager: done -- rat.core.processor

src/core
````````
* CountProc: done -- rat.processors.stats
* Log: done -- replaced with python logging module, rat.core.log
* ProcBlock: done -- rat.core.processor
* Processor: done -- rat.core.processor
* Producer: replaced by python generators
* SignalHandler: done -- signal module, rat.core.signal_handler
* Trajectory: needed on top of g4 tracking?
* WriteVarProc: deprecated in RAT, depends on DS

src/db
``````
* DB: done? -- dict subclass, rat.core.ratdb
* DBExceptions: done -- use python exceptions
* DBFieldCallback: done? -- did this ever work in rat?
* DBJsonLoader: done -- json module
* DBTable: done -- dict subclass, rat.core.ratdb
* DBTextLoader: deprecated, will not port
* HTTPDownloader: use httplib + json
* json_*: replaced by json module

src/fit
```````
* QPDF: deprecated, will not port
* FitLike: deprecated, will not port

src/io
``````
* DSReader: done -- rat.generators.rootfile
* FillRCHProc: deprecated, will not port
* InDispatchProducer: wip -- rat.generators.dispatch
* InPackedProducer: done -- rat.generators.rootfile
* InROOTProducer: done -- rat.generators.rootfile

src/util
````````
* Extensible: deprecated
* HashFunc: use hash() builtin or hashlib
* LinearInterp: use numpy.interp
* MultivariateInterp: use numpy.interp
* RadicalInverse: rat.util.math.radical_inverse

