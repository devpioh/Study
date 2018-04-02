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
    gPrestoServerMode = ["REAL"]
    gPrestoBuildMode = ["RELEASE"]
    
    
    #version
    bundleVersion = "2.4.0"    
    bundleVersionCode = "240"
    
    #unity executable path
    excutablePath = r"C:/Program Files/Unity/Editor/Unity.exe"
    #master svn path
    svnPath = r"D:/Study/PiohStudy/Python/VisualBuildDialog" #r"D:\PoolTime"
    #svn project path
    #svnProjectPath = svnPath + r"/SourcesNeoBilliards"
    #svnProjectPath = svnPath + r"/SL2_SourcesNeoBilliards"
    svnProjectPath = svnPath + r"/PoolTime"
    
    sharedDrive = "\\\\10.101.56.242\\b-adshare"
    sharedDirectory = "\\PocketBuild\\AOS\\"
    
    sharedDriveUserName = r"username"
    sharedDrivePassword = r"password"
    