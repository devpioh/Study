'''
Created on 2013. 9. 9.

@author: azzrael
'''


from BuildConfig import BuildConfig
from IosBuildMain import IosBuildManager

if __name__ == '__main__':
    
    BuildConfig.serverModes = ["DEV"]
    #BuildConfig.profiles = ["development", "adhoc"]
    BuildConfig.profiles = ["adhoc"]
    BuildConfig.debugModes = ["DEV"]
    BuildConfig.releaseModes = ["DEV"]
    BuildConfig.adjustServerMode = ["REAL"]
    BuildConfig.adjustBuildMode = ["DEBUG", "RELEASE"]
    BuildConfig.gPrestoServerMode = ["REAL"]
    BuildConfig.gPrestoBuildMode = ["RELEASE"]
    
    IosBuildManager.BuildAll(SvnSourceUpdate=True, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnIPACommit=False, MailTo=True)