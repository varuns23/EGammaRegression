from CRABClient.UserUtilities import config

doUserFiles = True

from CRABAPI.RawCommand import crabCommand
from dbs.apis.dbsClient import DbsApi
dbs = DbsApi('https://cmsweb.cern.ch/dbs/prod/global/DBSReader')

config = config()
#General
config.General.workArea                 = './'
config.General.transferOutputs          = True
config.General.transferLogs             = True
#JobType
config.JobType.pluginName               = 'Analysis'
config.JobType.psetName                 = 'runAnalyzer.py'
#config.JobType.allowUndistributedCMSSW  = True
#Data
config.Data.inputDBS                    = 'global'
config.Data.splitting                   = 'FileBased'
config.Data.unitsPerJob                 = 100
#config.Data.totalUnits                  = 1
config.Data.publication                 = False

#config.Site.storageSite                 = 'T3_US_FNALLPC'
config.Site.storageSite                 = 'T2_CH_CERN'

if __name__ == '__main__':

    datasets_p = { #'PhotonPt5To300RealIC' : '/DoublePhoton_FlatPt-5To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
                   #'PhotonPt300To1000RealIC' : '/DoublePhoton_FlatPt-300To1000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
		   #'PhotonPt1000To1500RealIC': '/DoublePhoton_FlatPt-1000To1500/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
		   'PhotonPt1500To3000RealIC': '/DoublePhoton_FlatPt-1500To3000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
		   #'PhotonPt3000To4000RealIC': '/DoublePhoton_FlatPt-3000To4000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
		   #'PhotonPt4000To5000RealIC': '/DoublePhoton_FlatPt-4000To5000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',

		   #'PhotonPt5To300PerfectIC' : '/DoublePhoton_FlatPt-5To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM',
		   #'PhotonPt300To1000PerfectIC' : '/DoublePhoton_FlatPt-300To1000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM',
		   #'PhotonPt1000To1500PerfectIC' : '/DoublePhoton_FlatPt-1000To1500/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM',
		   'PhotonPt1500To3000PerfectIC' : '/DoublePhoton_FlatPt-1500To3000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM',
		   #'PhotonPt3000To4000PerfectIC' : '/DoublePhoton_FlatPt-3000To4000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM',
		   #'PhotonPt4000To5000PerfectIC' : '/DoublePhoton_FlatPt-4000To5000/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM'
    }

    datasets_e = { #'ElectronPt1To300RealIC'    : '/DoubleElectron_FlatPt-1To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
                   #'ElectronPt300To6500RealIC' : '/DoubleElectron_FlatPt-300To6500/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
                   #'ElectronPt1To300PerfectIC' : '/DoubleElectron_FlatPt-1To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM',
		   #'ElectronPt300To6500PerfectIC' : '/DoubleElectron_FlatPt-300To6500/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM'
    }

    datasets_c = { #'SCElectronPt1To300RealIC' : '/DoubleElectron_FlatPt-1To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
                   #'SCElectronPt300To6500RealIC' : '/DoubleElectron_FlatPt-300To6500/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_v10-v1/AODSIM',
                   #'SCElectronPt1To300PerfectIC' : '/DoubleElectron_FlatPt-1To300/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM'
		   #'SCElectronPt300To6500PerfectIC' : '/DoubleElectron_FlatPt-300To6500/RunIIFall17DRStdmix-FlatPU0to60_94X_mc2017_realistic_withECAL_IdealIC-v1/AODSIM'
    }

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    # for name, dataset in datasets_p2.iteritems():
    #     config.General.requestName = name
    #     if not doUserFiles:
    #         config.Data.inputDataset = dataset
    #     else:
    #         fileDictList=dbs.listFiles(dataset=dataset)
    #         lfnList = [ dic['logical_file_name'] for dic in fileDictList ]
    #         config.Data.userInputFiles = lfnList

    #     config.JobType.psetName = 'runAnalyzer_p.py'
    #     submit(config)

    #for name, dataset in datasets_c.iteritems():
    #    config.General.requestName = name
    #    config.Data.inputDataset   = dataset
    #    config.Data.outLFNDirBase  = '/store/group/phys_egamma/EgammaRegression/94X/cluster'
    #    config.JobType.psetName    = 'runAnalyzer_c.py'
    #    submit(config)

    for name, dataset in datasets_p.iteritems():
        config.General.requestName = name
        config.Data.inputDataset   = dataset
        config.Data.outLFNDirBase  = '/store/group/phys_egamma/EgammaRegression/94X/photon'
        config.JobType.psetName    = 'runAnalyzer_p.py'
        submit(config)

    #for name, dataset in datasets_e.iteritems():
    #    config.General.requestName = name
    #    config.Data.inputDataset   = dataset
    #    config.Data.outLFNDirBase  = '/store/group/phys_egamma/EgammaRegression/94X/electron'
    #    config.JobType.psetName    = 'runAnalyzer_e.py'
    #    submit(config)
