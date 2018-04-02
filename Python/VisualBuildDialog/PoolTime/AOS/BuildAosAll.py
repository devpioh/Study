'''
Created on 2013. 9. 2.

@author: azzrael
'''

from AosBuildMain import AosBuildManager
from BuildConfig import BuildConfig

if __name__ == '__main__':  
    
    BuildConfig.serverModes = ["DEV", "ALPHA", "REAL"]
    BuildConfig.debugModes = ["DEV", "ALPHA", "REAL"]
    BuildConfig.releaseModes = ["DEV", "ALPHA", "REAL"]
    BuildConfig.adjustServerMode = ["REAL"]
    BuildConfig.adjustBuildMode = ["DEBUG", "RELEASE"]
    BuildConfig.gPrestoServerMode = ["REAL"]
    BuildConfig.gPrestoBuildMode = ["RELEASE"]   
     
    AosBuildManager.BuildAll(SvnSourceUpdate=True, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnApkCommit=False, MailTo=True)