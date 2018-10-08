#!/bin/tcsh


#
setenv InputDir "/store/group/phys_egamma/EgammaRegression/94X/photon/DoublePhoton_FlatPt-1500To3000/crab_PhotonPt1500To3000RealIC/180622_161125/0000/"
setenv OutputDir "/store/group/phys_egamma/EgammaRegression/94X/photon/DoublePhoton_FlatPt1500To3000-RealIC"
#setenv InputDir ${1}
#setenv OutputDir ${2}
 
setenv prefix "root://eoscms/"

if( -f files_to_copy.txt ) then
rm files_to_copy.txt
endif
 
eos ls ${InputDir} | grep ".root" > files_to_copy.txt
#ls ${InputDir} > files_to_copy.txt
 
set count = 0
foreach i (`cat files_to_copy.txt`)
 
@ count = ${count} + 1
echo "--->> copying xrdcp ${prefix}${InputDir}/${i} TO ${prefix}${OutputDir}/${i}"
 
#xrdcp root://cmseos.fnal.gov/${InputDir}/${i} ${OutputDir}/${i}
#xrdcp ${InputDir}/${i} root://cmseos.fnal.gov/${OutputDir}/${i} 
#xrdcp root://cmseos.fnal.gov/${InputDir}/${i} root://cmseos.fnal.gov/${OutputDir}/${i}

xrdcp ${prefix}${InputDir}/${i} ${prefix}${OutputDir}/${i}

end
 
echo " Total ${count} files copied "
rm files_to_copy.txt

