#!/usr/bin/env python

import os, sys, getopt, argparse, fnmatch, errno, subprocess, shlex
import subprocess
from subprocess import call


#inputFilePath  = "/store/group/phys_egamma/EgammaRegression/94X/cluster/DoubleElectron_FlatPt-1To300/crab_SCElectronPt1To300PerfectIC/180219_223030/0000/" 
inputFilePath  = "/store/group/phys_egamma/EgammaRegression/94X/electron/DoubleElectron_FlatPt-300To6500/crab_ElectronPt300To6500RealIC/180305_150951/0000/" 
#outputFilePath = "/store/group/phys_egamma/EgammaRegression/94X/cluster/DoubleElectron_FlatPt-1To300/"
outputFilePath = "/store/group/phys_egamma/EgammaRegression/94X/electron/DoubleElectron_FlatPt300To6500-RealIC/"

prefix = "root://eoscms/"

#eosls = "eos ls" + prefix + inputFilePath

#proc = subprocess.Popen("ls" + ".", stdout=subprocess.PIPE).communicate()[0]
#proc = subprocess.Popen(eosls, stdout=subprocess.PIPE).communicate()[0]

#print proc

def getListofFiles(inPath):
ls = subprocess.Popen(["eos, ls", inputFilePath],  
                     stdout=subprocess.PIPE,
                     )
## define the grep command
grep = subprocess.Popen(["grep", ".root"],  
                        stdin=ls.stdout,
                        stdout=subprocess.PIPE,
                       )

# read from the end of the pipe (stdout)
endOfPipe = ls.stdout
print endOfPipe
return endOfPipe


 
#getListofFiles(inputFilePath)

#print getListofFiles(inputFilePath)

#for iFiles in getListofFiles(inputFilePath)
#    print iFiles 

#print getoutput("xrdcp root://eoscms//store/group/phys_egamma/EgammaRegression/94X/cluster/DoubleElectron_FlatPt-1To300/crab_SCElectronPt1To300PerfectIC/180219_223030/0000/tree_2.root root://eoscms//store/group/phys_egamma/EgammaRegression/94X/cluster/DoubleElectron_FlatPt-1To300/tree_2.root")

