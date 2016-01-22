import sys, os

if len(sys.argv) < 2:
    msg  = '\n'
    msg += "Usage 1: %s $INPUT_ROOT_FILE\n" % sys.argv[0]
    msg += '\n'
    sys.stderr.write(msg)
    sys.exit(1)

from seltool import ertool
from larlite import larlite as fmwk
from ROOT import flashana
from ROOT import gSystem
gSystem.Load('libKalekoAna_ERToolStuff.so')
# Create ana_processor instance
my_proc = fmwk.ana_processor()

# Set input root file
for x in xrange(len(sys.argv)-1):
    my_proc.add_input_file(sys.argv[x+1])

# Specify IO mode
my_proc.set_io_mode(fmwk.storage_manager.kREAD)

# Specify output root file name
my_proc.set_ana_output_file("flashmashvalidation_anaout.root")

# Create ERTool algorithm
fm_algo = ertool.ERAlgoFlashMatch()

# Create ERTool analysis
my_ana = ertool.ERAnaFlashMatchValidation()

# Create larlite interfce analysis unit for ERTool
my_anaunit = fmwk.ExampleERSelection()
my_anaunit.setDisableXShift(False)
my_anaunit._mgr._mc_for_ana = True

# Set Producers
# First Argument: True = MC, False = Reco
# Second Argument: producer module label
my_anaunit.SetShowerProducer(True,"mcreco")
my_anaunit.SetTrackProducer(True,"mcreco")
my_anaunit.SetFlashProducer("opflash")


my_anaunit._mgr.AddAlgo(fm_algo)
my_anaunit._mgr.AddAna(my_ana)
my_ana._mode =True # True = Select. False = Fill mode
my_proc.add_process(my_anaunit)

# run!
my_proc.run(0,10)

# done!
print
print "Finished running ana_processor event loop!"
print

#fm_algo.StoreParams()
sys.exit(0)

