'''
Created on 2017. 6. 2.

@author: webzen_BW
'''


class BuildConfig: 
    
    serverModes = ["DEV", "ALPHA", "REAL"]
    profiles = ["development", "adhoc", "distribution"]
    debugModes = ["DEV", "ALPHA", "REAL"]
    releaseModes = ["DEV", "ALPHA", "REAL"]
    adjustServerMode = ["REAL"]
    adjustBuildMode = ["DEBUG", "RELEASE"]
    gPrestoServerMode = ["ALPHA","REAL"]
    gPrestoBuildMode = ["RELEASE"]
    
    
    #version
    bundleVersion = "2.0.3"
    bundleVersionCode = "203"
    
    #unity executable path
    excutablePath = r"C:/Program Files/Unity/Editor/Unity.exe"
    #master svn path
    svnPath = r"D:\PoolTime"
    #svn project path
    svnProjectPath = svnPath + r"/SourcesNeoBilliards"
    
    developmentTeamID = "U473ZJ736G"    
    
    signIDs = {"development":"iPhone Developer: pocket developer (T8BM668FTX)",
               "adhoc":"iPhone Distribution: WEBZEN INC. (U473ZJ736G)",
               "distribution":"iPhone Distribution: WEBZEN INC. (U473ZJ736G)"}
    
    provisionProfiles = {"development":"/Users/webzen_BW/Desktop/PoolTime/SourcesNeoBilliards/Pocket_IOS_Certificate/pocket/Pocket_iOS_Development_provisioning.mobileprovision",
                         "adhoc":"/Users/webzen_BW/Desktop/PoolTime/SourcesNeoBilliards/Pocket_IOS_Certificate/pocket/Pocket_iOS_Adhoc_provisioning.mobileprovision",
                         "distribution":"/Users/webzen_BW/Desktop/PoolTime/SourcesNeoBilliards/Pocket_IOS_Certificate/pocket/Pocket_iOS_Distribution_provisioning.mobileprovision"}
    
    
    # shared upload folder
    sharedDrive = r"//10.101.56.242/B-ADSHARE"
    sharedDirectory = r"/PocketBuild/IOS/" 
    sharedDriveUserName = r"none"
    sharedDrivePassword = r"none*"

    
    
