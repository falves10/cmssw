import FWCore.ParameterSet.Config as cms

# Trigger Primitive Producer
from SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_mc_cfi import *
# esmodule creating  records + corresponding empty essource
from SimCalorimetry.EcalTrigPrimProducers.ecalTrigPrimESProducer_mc_cff import *

#Common
from Configuration.StandardSequences.Eras import eras
eras.phase2_common.toModify( simEcalTriggerPrimitiveDigis, BarrelOnly = cms.bool(True) )
