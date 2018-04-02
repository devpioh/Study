'''
Created on 2013. 9. 9.

@author: azzrael
'''


import sys
import os
import subprocess
import ftplib
import datetime

import shutil

#import buildMsgMailTo
#import unicodedata
from BuildConfig import BuildConfig


class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


#class for command line build
class IosBuildParam:    
    
    #user build setting param start!!!!
    excutablePath = r"/Applications/Unity/Unity.app/Contents/MacOS/Unity"
    svnPath = r"/Users/webzen_BW/Desktop/PoolTime"
    svnProjectPath = svnPath + r"/SourcesNeoBilliards"
    
    bundleVersion = "2.0.3"
    bundleVersionCode = "203"
    
    serverToConnect = "DEV" 
    ServerPort = "9190" 
    profiles = ["development"]
    #user setting param end!!!!    
    
    
    #build define
    serverModeDefinePrefix = "COMMAND_LINE_BUILD_"   
    userScriptBaseDefine = r"BUILD_POCKET;USE_ASSET_BUNDLE_AUX;MOCAA;NO_GPGS;UNITY_ADS;FORCE_CHECK_CLIENT_ABUSE;"
    userScriptServerModeDefine = serverModeDefinePrefix + "DEV"
    userScriptDebugLogDefine = r"DEBUG_ASSERT;DEBUG_LOG;"
    userScriptAdjustDefine = r"ADJUST;"
    userScriptGPrestoDefine = r"G_PRESTO;"
    userScriptDefine = userScriptBaseDefine;
    #build option, debug mode => Development
    buildOption = "Release";
    #debug mode => Development
    #buildOption = "Development";   
    
    # unity android build param
    bundleIdentifier = "com.webzen.pocket.iOS"    
    
    buildFunction = "CommandLineBuild.PerformIOSBuild" 
    
    # build path   
    @classproperty
    def buildPath(self) :
        return self.svnPath + r"/Build/PoolTime/IOS"
    
    @classproperty
    def outputXcodePath(self) :        
        return os.path.abspath(self.buildPath + r"/OutputXcode") 
    
    @classproperty
    def logPath(self) :        
        return os.path.abspath(self.buildPath + "/unitylog.txt")
    
    ipaPath = buildPath   
    ipaFileNames = {"development":"", 
                    "adhoc":"", 
                    "distribution":""}
    
    ipaFullPaths = {"development":"", 
                    "adhoc":"", 
                    "distribution":""}
      
    # provisioning profile
    developmentTeamID = "WEBZEN INC."
    # signing and provision profile
    signIDs = {"development":"iPhone Developer: pocket developer (T8BM668FTX)",
               "adhoc":"iPhone Distribution: WEBZEN INC. (U473ZJ736G)",
               "distribution":"iPhone Distribution: WEBZEN INC. (U473ZJ736G)"}
    
    provisionProfiles = {"development":"/Users/webzen_BW/Desktop/PoolTime/SourcesNeoBilliards/Pocket_IOS_Certificate/pocket/Pocket_iOS_Development_provisioning.mobileprovision",
                         "adhoc":"/Users/webzen_BW/Desktop/PoolTime/SourcesNeoBilliards/Pocket_IOS_Certificate/pocket/Pocket_iOS_Adhoc_provisioning.mobileprovision",
                         "distribution":"/Users/webzen_BW/Desktop/PoolTime/SourcesNeoBilliards/Pocket_IOS_Certificate/pocket/Pocket_iOS_Distribution_provisioning.mobileprovision"}

    # etc info         
    
    # shared upload folder
    sharedDrive = r"//10.101.56.242/B-ADSHARE"
    sharedDirectory = r"PocketBuild/IOS/"      
    sharedDriveUserName = r"username"
    sharedDrivePassword = r"password"
    
    #ftp info
    ftpServerIP = "61.249.229.70"
    ftpPort = 14151
    ftpUserID = "hancue_npt"
    ftpUserPass = r"gkszb&&djqfhem^"
    ftpDirectory = "/Hancue_NPLUTO/IPA/"   
    
    
        
    
    
    
    
    @classmethod
    def setOutputFilePath(thisClass, strDate, strRevision):
        
        thisClass.ipaPath = thisClass.buildPath + "/IPA/"
        
        buildOpt = "release"
        if "development" in thisClass.buildOption.lower() :
            buildOpt = "debug"
            
        for profile in thisClass.profiles :   
            filename = "PoolTime" "_d" + strDate + "_v" + thisClass.bundleVersion + "_r" + strRevision + "_p" + thisClass.ServerPort + "_" + thisClass.serverToConnect.lower() + "_" + buildOpt + "_" + profile
            thisClass.ipaFileNames[profile] = filename + ".ipa"
            thisClass.ipaFullPaths[profile] = thisClass.ipaPath + thisClass.ipaFileNames[profile] 



#class for build log
class BuildLog:   
    
    # constructor
    def __init__(self, strBuildPath):
        self.buildLogFile = open(strBuildPath + "/buildlog.txt", "w")
        # make default console output to utf8 encoding!!!
        try:
            output = subprocess.Popen( "export LANG=ko_KR.UTF-8", shell=True, stderr=subprocess.STDOUT )
            outstream, errstream = output.communicate()
            
        except subprocess.CalledProcessError:          
            sys.exit()
    
    # log for both file and stdout   
    def writeLog(self, strLog, consoleOut = True) :    
        stringLog = strLog
        if type(strLog) is bytes:                    
            #stringLog = strLog.decode(encoding="ascii",errors="ignore")
            stringLog = strLog.decode(encoding="utf8",errors="ignore")
                    
        if consoleOut: print(stringLog)
            
        self.buildLogFile.write(stringLog)     
   
    def writeLogAndFinalize(self, strLog, consoleOut = True) :
        self.writeLog(strLog, consoleOut)
        self.buildLogFile.flush()
        self.buildLogFile.close()  
    
    
        

#class for command line build
class IosBuild:
        
    svnRevision = "-1"
    #log = BuildLog(IosBuildParam.buildPath)
    _log = "none"
    @classproperty
    def log(self) :
        if self._log == "none" :
            self._log = BuildLog(IosBuildParam.buildPath)
            
        return self._log   
    
    
        
    
    
    @classmethod
    def Quit(thisClass, quitMessage): 
        thisClass.log.writeLogAndFinalize(quitMessage)
        
        try:
            while True:
                pass
        except KeyboardInterrupt:
            sys.exit()     
     
    
    @classmethod
    def GetRevisionNumber(thisClass):
        # get revision number
        try:
            output = subprocess.Popen( ["svn", "info", IosBuildParam.svnProjectPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            outstream, errstream = output.communicate()           
            strOutStream = outstream.decode("utf8", "ignore")   
            tokens = strOutStream.split()       
            revisionNumIdx = next( tokenIdx for tokenIdx, currToken in enumerate(tokens) if currToken == "Revision:" )         
            thisClass.svnRevision = tokens[revisionNumIdx+1]
        
        except StopIteration:
            thisClass.Quit("---svn revision corrupt!!! - please retry after fix svn revision problem first!!---\n")            
    
    @classmethod
    def PerformSVNUpdate(thisClass, SvnUpdateRevision=-1):        
        #svn update
        thisClass.log.writeLog("[1, svn update start!!!]\n\n")       
        
        try: 
            
            # get current working copy version
            if( SvnUpdateRevision != -1 ) :
                thisClass.GetRevisionNumber()                     
                currRevisionNum = int(thisClass.svnRevision)
                if( SvnUpdateRevision > currRevisionNum ) :
                    thisClass.Quit("---svn update to revision error occured!!! - cannot update to revision if target revision is greater than current revision!!---\n")                   
            
            svnCmd = ["svn", "update", IosBuildParam.svnProjectPath]
            if( SvnUpdateRevision != -1 ) :
                svnCmd = ["svn", "update", "-r" + str(SvnUpdateRevision), IosBuildParam.svnProjectPath]          
            output = subprocess.Popen( svnCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            outstream, errstream = output.communicate()
            thisClass.log.writeLog(outstream)
            thisClass.log.writeLog(errstream)
            
            # check Conflict
            output = subprocess.Popen( ["svn", "status", IosBuildParam.svnProjectPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            outstream, errstream = output.communicate()
            strOutStream = outstream.decode("utf8", "ignore")
            if strOutStream.find("Summary of conflicts:") >= 0 : 
                thisClass.Quit("---svn Conflicted!!! - please retry after fix svn conflict problem first!!---\n")                
            
            if SvnUpdateRevision == -1 :
                thisClass.GetRevisionNumber()           
            
            #print("\n\nFounded Revision : " + thisClass.svnRevision)           
                        
        except subprocess.CalledProcessError:
            thisClass.Quit("---svn update failed!!! - please retry after fix svn update problem first!!---\n")        
            
        thisClass.log.writeLog("[1, svn update end!!!]\n\n")      
    
    
    
    @classmethod
    def PerformSVNCommit(thisClass, CommitFileDictionary=None):             
        #svn update
        thisClass.log.writeLog("[4, svn commit start!!!]\n\n")       
        
        try:
            
            cmdAdd = ["svn", "add"] 
                       
            if CommitFileDictionary != None :                    
                for keyIPAFileName in CommitFileDictionary :
                    cmdAdd.append(CommitFileDictionary[keyIPAFileName])
            else :
                for profile in IosBuildParam.profiles :           
                    cmdAdd.append(IosBuildParam.ipaFullPaths[profile])         
                            
            output = subprocess.Popen( cmdAdd, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            outstream, errstream = output.communicate()
            thisClass.log.writeLog(outstream)
            thisClass.log.writeLog(errstream) 
            
            
            cmdCommit = ["svn", "commit", "-m"]
            commitMsg = "add ipa : "
                    
            if CommitFileDictionary != None :               
                for keyIPAFileName1 in CommitFileDictionary :
                    commitMsg = commitMsg + keyIPAFileName1 + " "
                
                cmdCommit.append(commitMsg)
                
                for keyIPAFileName2 in CommitFileDictionary :
                    cmdCommit.append(CommitFileDictionary[keyIPAFileName2])
            else :
                for profile in IosBuildParam.profiles :
                    commitMsg = commitMsg + IosBuildParam.ipaFileNames[profile] + " "
                    
                cmdCommit.append(commitMsg)
                
                for profile in IosBuildParam.profiles :
                    cmdCommit.append(IosBuildParam.ipaFullPaths[profile])
                    
            output = subprocess.Popen( cmdCommit, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            outstream, errstream = output.communicate()
            thisClass.log.writeLog(outstream)
            thisClass.log.writeLog(errstream)
            
            # check Conflict
            output = subprocess.Popen( ["svn", "status", IosBuildParam.svnPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            outstream, errstream = output.communicate()
            strOutStream = outstream.decode("utf8", "ignore")
            if strOutStream.find("Summary of conflicts:") >= 0 : 
                thisClass.Quit("---svn Conflicted!!! - please retry after fix svn conflict problem first!!---\n")                            
                        
        except subprocess.CalledProcessError:
            thisClass.Quit("---svn update failed!!! - please retry after fix svn update problem first!!---\n")                   
            
        thisClass.log.writeLog("[4, svn commit end!!!]\n\n")            
        
    
    
    @classmethod
    def PerformUploadToSharedFoler(thisClass):        
        # ftp upload
        thisClass.log.writeLog("[3, upload to shared folder start!!!]\n\n")        
        
        try : 
                       
            for profile in IosBuildParam.profiles :
                
                if profile == "distribution" and IosBuildParam.serverToConnect != "REAL" :
                    continue
                
                remoteVolume = "/Volumes/B-ADSHARE/"                
                if not os.path.exists(remoteVolume) : 
                    
                    os.mkdir(remoteVolume)                    
                    
                    if IosBuildParam.sharedDriveUserName == "none" or IosBuildParam.sharedDrivePassword == "none" :                              
                        cmdMount = r"/sbin/mount -t smbfs //" + IosBuildParam.sharedDrive + " " +  remoteVolume 
                        output = subprocess.Popen(cmdMount, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        
                        outstream, errstream = output.communicate()
                        thisClass.log.writeLog(outstream)
                        thisClass.log.writeLog(errstream)
                        
                    else :                        
                        cmdMount = r"/sbin/mount -t smbfs //" + IosBuildParam.sharedDriveUserName + ":" + IosBuildParam.sharedDrivePassword + "@" + IosBuildParam.sharedDrive + " " +  remoteVolume 
                        output = subprocess.Popen(cmdMount, stdout=subprocess.PIPE, stderr=subprocess.PIPE)                       
                        
                        outstream, errstream = output.communicate()
                        thisClass.log.writeLog(outstream)
                        thisClass.log.writeLog(errstream)
                                          
            
                sharedFolderName = str(datetime.datetime.now().date()).replace("_", "") 
                dstPath = remoteVolume + IosBuildParam.sharedDirectory + sharedFolderName + "/" 
                if not os.path.exists(dstPath) :
                    os.mkdir(dstPath)
                                               
                shutil.copy2(IosBuildParam.ipaFullPaths[profile], dstPath);           
            
        except subprocess.CalledProcessError:  
            thisClass.Quit("---upload to shared directory failed!!!---\n") 
        except IOError as e:            
            thisClass.log.writeLog("copy failed : " + str(e))       
           
            
        thisClass.log.writeLog("[3, upload to shared folder end!!!]\n\n")
    
    @classmethod
    def PerformFtpUpload(thisClass):        
        # ftp upload
        thisClass.log.writeLog("[3, ftp upload start!!!]\n\n")
        
        try:            
            ftpSession = ftplib.FTP()
            ftpSession.connect( IosBuildParam.ftpServerIP, IosBuildParam.ftpPort )
            ftpSession.login( IosBuildParam.ftpUserID, IosBuildParam.ftpUserPass )
            ftpSession.cwd( IosBuildParam.ftpDirectory )
            saveDir = IosBuildParam.bundleVersion
            if saveDir not in ftpSession.nlst():
                ftpSession.mkd( saveDir )            
            ftpSession.cwd( IosBuildParam.ftpDirectory + saveDir )
            
            for profile in IosBuildParam.profiles :
                file = open( IosBuildParam.ipaFullPaths[profile], 'rb' )               # file to send
                ftpSession.storbinary( "STOR " + IosBuildParam.ipaFileNames[profile], file )     # send the file
            
            
        except ftplib.all_errors:
            thisClass.Quit("---ftp upload failed!!! - please retry after fix ftp upload problem first!!---\n")             
                        
        except IOError:
            thisClass.Quit("---ftp target file open failed!!! - please retry after fix target file open problem first!!---\n")               
                   
        finally:            
            file.close()                                       # close file and FTP
            ftpSession.quit()    
            
        thisClass.log.writeLog("[3, ftp upload end!!!]\n\n")       
    
    
    
    @classmethod
    def PerformUnityBuild(thisClass):
        
        #unity build
        thisClass.log.writeLog("[2, unity build start!!!]\n\n")
        
        thisClass.buildTime = str(datetime.datetime.now().date()).replace("-", "") + "_" + str((datetime.datetime.now().time().isoformat().replace("/", "").replace(":", ""))[0:4])
        #print(thisClass.buildTime)
        #print(thisClass.svnRevision)
        #print(AosBuildParam.serverToConnect.lower())       
        
        IosBuildParam.setOutputFilePath(thisClass.buildTime, thisClass.svnRevision)
        
        try :
            
            strProfiles = ""
            for profile in IosBuildParam.profiles :
                strProfiles = strProfiles + profile + ","
            
            strProfiles = strProfiles[:-1]
                
            #thisClass.log.writeLog("strProfiles : " + strProfiles)
            
            # caution!!! last two parameter == unity's user #define arguments            
            subprocess.check_call( [IosBuildParam.excutablePath, "-quit", "-batchmode", "-projectPath", IosBuildParam.svnProjectPath, "-logFile", IosBuildParam.logPath,
                                  "-executeMethod", IosBuildParam.buildFunction, IosBuildParam.serverToConnect, IosBuildParam.buildOption, IosBuildParam.userScriptDefine, IosBuildParam.bundleIdentifier, 
                                  IosBuildParam.bundleVersion, IosBuildParam.bundleVersionCode,
                                  IosBuildParam.outputXcodePath, strProfiles,
                                  IosBuildParam.developmentTeamID,
                                  IosBuildParam.signIDs["development"], IosBuildParam.signIDs["adhoc"], IosBuildParam.signIDs["distribution"],
                                  IosBuildParam.provisionProfiles["development"], IosBuildParam.provisionProfiles["adhoc"], IosBuildParam.provisionProfiles["distribution"]
                                  ], stderr=subprocess.STDOUT )       
                    
            
        except subprocess.CalledProcessError:              
                      
            for logline in open(IosBuildParam.logPath, "r") : print( logline )
            thisClass.log.writeLogAndFinalize("---unity build error occurred!!! - please retry after fix unity build error first!!---\n")
            input()
            sys.exit()
            
            
        thisClass.UpdateOutputFile()        
       
        thisClass.log.writeLog("[2, unity build end!!!]\n\n") 
    

    @classmethod
    def UpdateOutputFile(thisClass): 
        
        for profile in IosBuildParam.profiles : 
            
            if profile == "distribution" and IosBuildParam.serverToConnect != "REAL" :
                continue
                                 
            strOutputIpaFilename = profile + IosBuildParam.bundleIdentifier.split(".")[-2] + ".ipa"
            strOutputIpaPath = IosBuildParam.outputXcodePath + "/build/Release-iphoneos/"
            strOriOutputIpaFullPath = strOutputIpaPath + strOutputIpaFilename            
            strDestIpaPath = strOutputIpaPath + IosBuildParam.ipaFileNames[profile]
            
            os.rename(strOriOutputIpaFullPath, strDestIpaPath)            
            shutil.copy2(strDestIpaPath, IosBuildParam.ipaPath)
            os.remove(strDestIpaPath)    
    
    @classmethod
    def GetCompletedMailTitle(thisClass, buildType):
        strMailTitle = "Build Completed - " + buildType + " : " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n"
        return strMailTitle
    
    @classmethod
    def GetCompletedMailDesc(thisClass, buildType, outputFilenameDic):
        strMailDesc = "Build Type : " + buildType + "\n"
        strMailDesc += "Time : " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n"
        for outputFilename in outputFilenameDic :
            strMailDesc += "Output File : " + outputFilename + "\n"   
        
        strMailDesc += "Output File Location(Ftp) : " + IosBuildParam.ftpDirectory + IosBuildParam.bundleVersion + "\n"          
        return strMailDesc
    
    
    @classmethod
    def PerformBuild(thisClass, SvnSourceUpdate=True, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnIPACommit=True):    
                
        logBuildMode = "Release"
        if "Development" in IosBuildParam.buildOption : logBuildMode = "Debug"
        thisClass.log.writeLog( "\n[{0}-{1} build start!!!]\n\n".format( IosBuildParam.serverToConnect, logBuildMode ) )
        
        # svn update relation
        if SvnSourceUpdate : 
            IosBuild.PerformSVNUpdate(SvnUpdateRevision)
        else :
            IosBuild.GetRevisionNumber()
           
        IosBuild.PerformUnityBuild()
        if UploadToSharedFolder : IosBuild.PerformUploadToSharedFoler()
        if SvnIPACommit : IosBuild.PerformSVNCommit()   
           
        thisClass.log.writeLog( "\n[{0}-{1} build End!!!]\n\n".format( IosBuildParam.serverToConnect, logBuildMode ) )        
               
       
   
    
        


#class for command line build
class IosBuildManager:    
    
    # alpha, beta, real all build, ftp upload, svn commit
    @classmethod    
    def BuildAll(thisClass, SvnSourceUpdate=True, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnIPACommit=True, MailTo=True):        
                
        #setting ios build param
        IosBuildParam.bundleVersion = BuildConfig.bundleVersion
        IosBuildParam.bundleVersionCode = BuildConfig.bundleVersionCode
        IosBuildParam.excutablePath = BuildConfig.excutablePath
        IosBuildParam.svnPath = BuildConfig.svnPath
        IosBuildParam.svnProjectPath = BuildConfig.svnProjectPath
        IosBuildParam.profiles = BuildConfig.profiles
        IosBuildParam.signIDs = BuildConfig.signIDs        
        IosBuildParam.provisionProfiles = BuildConfig.provisionProfiles
        IosBuildParam.developmentTeamID = BuildConfig.developmentTeamID
        
        IosBuildParam.sharedDrive = BuildConfig.sharedDrive
        IosBuildParam.sharedDirectory = BuildConfig.sharedDirectory        
        IosBuildParam.sharedDriveUserName = BuildConfig.sharedDriveUserName
        IosBuildParam.sharedDrivePassword = BuildConfig.sharedDrivePassword
        
        IosBuild.log.writeLog( "\n[Master build Start!!!]\n\n" )               
                    
        for mode in BuildConfig.serverModes :                        
            IosBuildParam.serverToConnect = mode 
            IosBuildParam.userScriptServerModeDefine = IosBuildParam.serverModeDefinePrefix + IosBuildParam.serverToConnect + ";"
            
            if mode in BuildConfig.debugModes :           
                IosBuildParam.buildOption = "Development" 
                IosBuildParam.userScriptDefine = IosBuildParam.userScriptBaseDefine + IosBuildParam.userScriptServerModeDefine + IosBuildParam.userScriptDebugLogDefine
                if mode in BuildConfig.adjustServerMode :
                    if "DEBUG" in BuildConfig.adjustBuildMode :
                        IosBuildParam.userScriptDefine = IosBuildParam.userScriptDefine + IosBuildParam.userScriptAdjustDefine
                        
                if mode in BuildConfig.gPrestoServerMode :
                    if "DEBUG" in BuildConfig.gPrestoBuildMode :
                        IosBuildParam.userScriptDefine = IosBuildParam.userScriptDefine + IosBuildParam.userScriptGPrestoDefine
                        
                #IosBuild.PerformBuild(SvnSourceUpdate, SvnUpdateRevision, UploadToSharedFolder, SvnIPACommit)
                print( "debug serverMode : " + IosBuildParam.userScriptServerModeDefine )
                print( "debug userDefine : " + IosBuildParam.userScriptDefine )
                                
            if mode in BuildConfig.releaseModes :
                IosBuildParam.buildOption = "Release"
                IosBuildParam.userScriptDefine = IosBuildParam.userScriptBaseDefine + IosBuildParam.userScriptServerModeDefine #+ IosBuildParam.userScriptDebugLogDefine
                
                if mode in BuildConfig.adjustServerMode :
                    if "RELEASE" in BuildConfig.adjustBuildMode :
                        IosBuildParam.userScriptDefine = IosBuildParam.userScriptDefine + IosBuildParam.userScriptAdjustDefine
                        
                if mode in BuildConfig.gPrestoServerMode :
                    if "RELEASE" in BuildConfig.gPrestoBuildMode :
                        IosBuildParam.userScriptDefine = IosBuildParam.userScriptDefine + IosBuildParam.userScriptGPrestoDefine
                        
                #IosBuild.PerformBuild(SvnSourceUpdate, SvnUpdateRevision, UploadToSharedFolder, SvnIPACommit)                
                print( "release serverMode : " + IosBuildParam.userScriptServerModeDefine )
                print( "release userDefine : " + IosBuildParam.userScriptDefine )
        
        #if SvnIPACommit : IosBuild.PerformSVNCommit()
        
        #if MailTo and UploadToSharedFolder : buildMsgMailTo.MailManager.send_via_gmail_all(IosBuild.GetCompletedMailTitle("IPA All"),  IosBuild.GetCompletedMailDesc("IPA All", buildSuccessIPAPath))
        sys.stdout.writelines('/a')
        sys.stdout.flush()
        
        IosBuild.Quit( "\n[Master build End!!!]\n\nbye!!!\n\n" )    
   
        
   
    
    
            
