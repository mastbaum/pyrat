Tools
=====

ratinfo
-------

The ``ratinfo`` command line program that collects various simple tools for extracting information from output ROOT files produced by the outroot.  It saves you the trouble of having to write a full-blown ROOT macro to get some pieces of information.

**log**::

    ratinfo log [rootfile]

Prints the log contents from the RAT session that produced this output ROOT file.

**macro**::

    ratinfo macro [rootfile]

Prints the RAT macro commands that produced this output ROOT file.  Does not include any commands typed interactively.

**db**::

    ratinfo db [rootfile]

Prints a full trace of all the RATDB values that were accessed during the RAT job that produced this file.  The trace is actually a valid RATDB file with a validity range set to "user override" that can be redirected to a file and used in another job.

Example output fragment::

    drl129:rat-trunk stan$ ratinfo db miniCLEAN_20keV_shellfit.root

    {
      name: "PMT",
      index: "r1408",
      valid_begin: [-1, -1],
      valid_end: [-1, -1],

      pmt_vacuum_material: "pmt_vacuum",
      dynode_top: -30,
      [snip, snip]

**status**::

    ratinfo status [rootfile1] [rootfile2] [...]

Prints the filename and status description for one or more output ROOT files.  Example::

    drl129:rat-trunk stan$ ratinfo status miniCLEAN_20keV_shellfit.root 
    miniCLEAN_20keV_shellfit.root: ABORT

The possible status codes are:

OK
  Job ran to completion
ABORT
  Job was aborted partway through by user pressing Ctrl-C once.  File was closed properly, but may have fewer events than requested in macro file.
CRASH
  Job was terminated ungracefully using multiple Ctrl-C or possibly a segmentation fault.  The output file was not closed and may produce ROOT warnings.
UNKNOWN
  The status value stored in the file has an unexpected value.  The file might have been produced by a newer RAT version.
UNSUPPORTED
  This ROOT file contains no status information.  It either was not created by RAT, or was created by a very old version.
NOTROOT
  The file specified on the command line is not a ROOT file at all.

**var**::

    ratinfo var [rootfile] [expression] [optional:cut]

Scan through the events in a ROOT file and print the mean, standard deviation and uncertainty on the mean for a given selector expression.  If the optional cut is supplied, then only events where the cut expression evaluates to true are accumulated.  The uncertainty on the mean is defined to be:
$$ \Delta \bar{x} =  \frac{\bar{x}}{\sqrt{\sigma_x}}. $$

The expression and cut syntax is exactly that of the TTree::Draw() command, but the expression should evaluate to a 1D histogram.  For example, one can request a simple variable::

    drl129:rat-trunk stan$ ratinfo var miniCLEAN_20keV_shellfit.root numPE
    selector = "numPE", cut = ""
    # of events = 106
    mean = 116.669811, rms = 11.456828, uncert_mean = 1.112785

or a more complex expression::

    drl129:rat-trunk stan$ ratinfo var miniCLEAN_20keV_shellfit.root numPE 'numPE/particle.ke'
    selector = "numPE", cut = "numPE/particle.ke"
    # of events = 106
    mean = 117.794857, rms = 11.618573, uncert_mean = 1.128496

It is usually a good idea to enclose expressions with symbols in single quotes to protect them from interpretation by the shell.

The number of events printed is the number of events passing the cut expression.  Using the same file as above::

    drl129:rat-trunk stan$ ratinfo var miniCLEAN_20keV_shellfit.root numPE 'numPE>105'
    selector = "numPE", cut = "numPE>105"
    # of events = 87
    mean = 120.126437, rms = 9.472045, uncert_mean = 1.015510

