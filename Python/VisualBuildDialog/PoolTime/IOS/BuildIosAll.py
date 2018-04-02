'''
Created on 2013. 9. 9.

@author: azzrael
'''


from BuildConfig import BuildConfig
from IosBuildMain import IosBuildManager


if __name__ == '__main__':    
    
    '''
    BuildConfig.serverModes = ["DEV", "ALPHA", "REAL"]
    BuildConfig.profiles = ["development", "adhoc", "distribution"]
    BuildConfig.debugModes = ["DEV", "ALPHA", "REAL"]
    BuildConfig.releaseModes = ["DEV", "ALPHA", "REAL"]
    BuildConfig.adjustServerMode = ["REAL"]
    BuildConfig.adjustBuildMode = ["DEBUG", "RELEASE"]
    BuildConfig.gPrestoServerMode = ["REAL"]
    BuildConfig.gPrestoBuildMode = ["RELEASE"]
    '''
    
    BuildConfig.serverModes = ["ALPHA", "REAL"]
    #BuildConfig.profiles = ["development", "adhoc", "distribution"]
    BuildConfig.profiles = ["adhoc", "distribution"]
    BuildConfig.debugModes = []
    BuildConfig.releaseModes = ["ALPHA", "REAL"]
    BuildConfig.adjustServerMode = ["REAL"]
    BuildConfig.adjustBuildMode = ["DEBUG", "RELEASE"]
    BuildConfig.gPrestoServerMode = ["REAL"]
    BuildConfig.gPrestoBuildMode = ["RELEASE"]
    
    IosBuildManager.BuildAll(SvnSourceUpdate=False, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnIPACommit=False, MailTo=True)