from WMCore.Configuration import Configuration

config = Configuration()

config.section_('General')
config.General.requestName = 'PhiSymStep1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'phisym-cfg.py'
config.JobType.outputFiles = ['etsum_barl_1.dat','etsum_endc_1.dat','k_barl.dat','k_endc.dat','Espectra_plus.root','PhiSymmetryCalibration_kFactors.root']

config.section_('Data')
config.Data.inputDataset = '/AlCaPhiSym/Run2012D-v1/RAW'
config.Data.lumiMask = 'jsonls-alcaphisym.txt'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.outLFN = '/store/group/dpg_ecal/alca_ecalcalib/bmarzocc/PhiSymmetryStep1/'
config.Data.ignoreLocality = True
config.Data.publication = True

config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
