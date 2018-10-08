from WMCore.Configuration import Configuration                                            
config = Configuration()
#General
config.section_('General')
config.General.requestName     = 'job_Electron'
config.General.workArea        = './'
config.General.transferLogs    = True
config.General.transferOutputs = True
#JobType
config.section_('JobType')
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'runAnalyzer_c.py'
config.JobType.outputFiles = ['ElectronTree.root']
config.JobType.allowUndistributedCMSSW  = True
#Data
config.section_('Data')
config.Data.inputDataset = '/DoubleElectron_FlatPt-1To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM'
config.Data.splitting    = 'EventAwareLumiBased'
config.Data.unitsPerJob  = 10
config.Data.publication  = False
config.Data.totalUnits   = 10
#config.Data.ignoreLocality = True
config.Data.outLFNDirBase  ='/store/group/phys_egamma/EgammaRegression/94X/TEST'
#User
config.section_('User')
#Site
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.blacklist = ["T2_US_Wisconsin"]
#config.Site.whitelist = ['T1_US_FNAL']
#config.Site.whitelist = ['T3_US_FNALLPC']

