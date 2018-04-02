'''
Created on 2013. 8. 29.

@author: azzrael
'''


import sys
import os
import subprocess
import datetime
import ftplib
import shutil

# import buildMsgMailTo
# import unicodedata

from BuildConfig import BuildConfig
from _overlapped import NULL



class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()
    


# class for command line build
class AosBuildParam:    
    
    #user build setting param start!!!!
    excutablePath = r"C:/Program Files/Unity561f1/Editor/Unity.exe"
    svnPath = r"D:/Study/Unity/" #r"D:/Work/PoolTime10"
    svnProjectPath = svnPath + r"/PoolTimeSourceCode"
    
    bundleVersion = "1.0.0.0"
    bundleVersionCode = "200"
    
    serverToConnect = "DEV"
    # serverToConnect = "ALPHA"
    # serverToConnect = "REAL"
    serverPort = "9190"  # fixed!!!!
    #user setting param end!!!!    
    
    # build define
    serverModeDefinePrefix = "COMMAND_LINE_BUILD_"
    userScriptBaseDefine = r"BUILD_POCKET;USE_ASSET_BUNDLE_AUX;MOCAA;NO_GPGS;UNITY_ADS;FORCE_CHECK_CLIENT_ABUSE;"
    userScriptServerModeDefine = serverModeDefinePrefix + "DEV"
    userScriptDebugLogDefine = r"DEBUG_ASSERT;DEBUG_LOG;"
    userScriptAdjustDefine = r"ADJUST;"
    userScriptGPrestoDefine = r"G_PRESTO;"
    userScriptDefine = userScriptBaseDefine;
    # build option, debug mode => Development
    buildOption = "Release";
    # debug mode => Development
    # buildOption = "Development";
    
        
    
    # unity android build param
    bundleIdentifier = "com.webzen.pocket.google"    
    keystorePass = "pocket5566"
    keyaliasPass = "pocket5566"
    
    buildFunction = "CommandLineBuild.PerformAndroidBuild" 
        
    # build path       
    @classproperty
    def buildPath(self) :
        return self.svnPath + "/PoolTime/AOS"#r"/Build/PoolTime/AOS"  
    
    @classproperty
    def logPath(self) :        
        return os.path.abspath(self.buildPath + "/unitylog.txt") 
    
    @classproperty
    def apkPath(self) :        
        return os.path.abspath(self.buildPath + "/APK")   
    
    apkFileName = apkPath
    apkFullPath = apkPath    
    
    # etc info         
    
    # shared upload folder
    sharedDrive = "\\\\10.101.56.242\\b-adshare"
    sharedDirectory = "\\PocketBuild\\AOS\\"
    sharedDriveUserName = r"username"
    sharedDrivePassword = r"password"
    
    # ftp info    
    ftpServerIP = "61.249.229.70"
    ftpPort = 14151
    ftpUserID = "hancue_npt"
    ftpUserPass = r"gkszb&&djqfhem^"
    ftpDirectory = "/Hancue_NPLUTO/APK/"  
    
    
    



# class for build log
class BuildLog:   
    
    # constructor
    def __init__(self, strBuildPath):
        self.buildLogFile = open(strBuildPath + "/buildlog.txt", "w")
        # make default console output to utf8 encoding!!!
        try:
            subprocess.check_call(["cmd", "/C", "chcp", "65001"], stderr=subprocess.STDOUT)
            
        except subprocess.CalledProcessError:          
            sys.exit()
    
    # log for both file and stdout   
    def writeLog(self, strLog, consoleOut=True) :    
        stringLog = strLog
        if type(strLog) is bytes:                    
            stringLog = strLog.decode(encoding="utf8", errors="ignore")
            # stringLog = unicodedata.normalize("NFKD", strLog).encode("utf8","ignore") 
            # stringLog = strLog.decode(encoding="utf8",errors="ignore")           
        if consoleOut: print(stringLog)
            
        self.buildLogFile.write(stringLog)     
   
    def writeLogAndFinalize(self, strLog, consoleOut=True) :
        self.writeLog(strLog, consoleOut)
        self.buildLogFile.flush()
        self.buildLogFile.close()  
    
    
        

# class for command line build
class AosBuild:
        
    svnRevision = "-1"
    #log = BuildLog(AosBuildParam.buildPath)   
    _log = "none"
    @classproperty
    def log(self) :
        if self._log == "none" :
            self._log = BuildLog(AosBuildParam.buildPath)
            
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
            output = subprocess.Popen(["svn.exe", "info", AosBuildParam.svnProjectPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outstream, errstream = output.communicate()           
            strOutStream = outstream.decode("utf8", "ignore")   
            tokens = strOutStream.split()       
            revisionNumIdx = next(tokenIdx for tokenIdx, currToken in enumerate(tokens) if currToken == "Revision:")         
            thisClass.svnRevision = tokens[revisionNumIdx + 1]
        
        except StopIteration:
            thisClass.Quit("---svn revision corrupt!!! - please retry after fix svn revision problem first!!---\n")            
    
    @classmethod
    def PerformSVNUpdate(thisClass, SvnUpdateRevision=-1):        
        # svn update
        thisClass.log.writeLog("[1, svn update start!!!]\n\n")       
        
        try: 
            
            # get current working copy version
            if(SvnUpdateRevision != -1) :
                thisClass.GetRevisionNumber()                     
                currRevisionNum = int(thisClass.svnRevision)
                if(SvnUpdateRevision > currRevisionNum) :
                    thisClass.Quit("---svn update to revision error occured!!! - cannot update to revision if target revision is greater than current revision!!---\n")                   
            
            svnCmd = ["svn.exe", "update", AosBuildParam.svnProjectPath]
            if(SvnUpdateRevision != -1) :
                svnCmd = ["svn.exe", "update", "-r" + str(SvnUpdateRevision), AosBuildParam.svnProjectPath]          
            output = subprocess.Popen(svnCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outstream, errstream = output.communicate()
            thisClass.log.writeLog(outstream)
            thisClass.log.writeLog(errstream)
            
            # check Conflict
            output = subprocess.Popen(["svn.exe", "status", AosBuildParam.svnProjectPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outstream, errstream = output.communicate()
            strOutStream = outstream.decode("utf8", "ignore")
            if strOutStream.find("Summary of conflicts:") >= 0 : 
                thisClass.Quit("---svn Conflicted!!! - please retry after fix svn conflict problem first!!---\n")                
            
            if SvnUpdateRevision == -1 :
                thisClass.GetRevisionNumber()           
            
            # print("\n\nFounded Revision : " + thisClass.svnRevision)           
                        
        except subprocess.CalledProcessError:
            thisClass.Quit("---svn update failed!!! - please retry after fix svn update problem first!!---\n")        
            
        thisClass.log.writeLog("[1, svn update end!!!]\n\n")      
    
    
    
    @classmethod
    def PerformSVNCommit(thisClass, CommitFileDictionary=None):             
        # svn update
        thisClass.log.writeLog("[4, svn commit start!!!]\n\n")       
        
        try:
            cmdAdd = ["svn.exe", "add", AosBuildParam.apkFullPath]
            if CommitFileDictionary != None :
                cmdAdd = ["svn.exe", "add"]
                for keyApkFileName in CommitFileDictionary :
                    cmdAdd.append(CommitFileDictionary[keyApkFileName])
          
                            
            output = subprocess.Popen(cmdAdd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outstream, errstream = output.communicate()
            thisClass.log.writeLog(outstream)
            thisClass.log.writeLog(errstream) 
            
            cmdCommit = ["svn.exe", "commit", "-m", "add apk : " + AosBuildParam.apkFileName, AosBuildParam.apkFullPath]
            if CommitFileDictionary != None :                
                cmdCommit = ["svn.exe", "commit", "-m"]
                commitMsg = "add apk : "
                for keyApkFileName1 in CommitFileDictionary :
                    commitMsg = commitMsg + keyApkFileName1 + " "
                
                cmdCommit.append(commitMsg)
                
                for keyApkFileName2 in CommitFileDictionary :
                    cmdCommit.append(CommitFileDictionary[keyApkFileName2])
                    
                                      
            output = subprocess.Popen(cmdCommit, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outstream, errstream = output.communicate()
            thisClass.log.writeLog(outstream)
            thisClass.log.writeLog(errstream)
            
            # check Conflict
            output = subprocess.Popen(["svn.exe", "status", AosBuildParam.svnPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
            
            if not os.path.exists("y:") :    
                if AosBuildParam.sharedDriveUserName == "none" or AosBuildParam.sharedDrivePassword == "none" :                                                            
                    cmdMount = "net use y: " + AosBuildParam.sharedDrive   
                    output = subprocess.Popen(cmdMount, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    outstream, errstream = output.communicate()
                    thisClass.log.writeLog(outstream)
                    thisClass.log.writeLog(errstream)                      
                else :
                    cmdMount = "net use y: " + AosBuildParam.sharedDrive + " /user:" + AosBuildParam.sharedDriveUserName + " " + AosBuildParam.sharedDrivePassword    
                    output = subprocess.Popen(cmdMount, stdout=subprocess.PIPE, stderr=subprocess.PIPE)                    
                    outstream, errstream = output.communicate()
                    thisClass.log.writeLog(outstream)
                    thisClass.log.writeLog(errstream)              
                    
                
                                                                                        
            
            sharedFolderName = str(datetime.datetime.now().date()).replace("_", "") 
            dstPath = "y:\\" + AosBuildParam.sharedDirectory + sharedFolderName + "\\" 
            if not os.path.exists(dstPath) :
                os.mkdir(dstPath)          
            shutil.copy2(AosBuildParam.apkFullPath, dstPath);
          
        except subprocess.CalledProcessError:
            thisClass.Quit("---upload to shared directory failed!!!!---\n")    
        except IOError as e:            
            thisClass.log.writeLog("copy failed : " + e)             
            
        thisClass.log.writeLog("[3, upload to shared folder end!!!]\n\n")
        
        
    @classmethod
    def PerformFTPUpload(thisClass):        
        # ftp upload
        thisClass.log.writeLog("[3, FTP upload start!!!]\n\n")        
        
        try:            
            ftpSession = ftplib.FTP()
            ftpSession.connect(AosBuildParam.ftpServerIP, AosBuildParam.ftpPort)
            ftpSession.login(AosBuildParam.ftpUserID, AosBuildParam.ftpUserPass)
            ftpSession.cwd(AosBuildParam.ftpDirectory)            
            saveDir = AosBuildParam.bundleVersion
            if saveDir not in ftpSession.nlst():
                ftpSession.mkd(saveDir)            
            ftpSession.cwd(AosBuildParam.ftpDirectory + saveDir)
            
            file = open(AosBuildParam.apkFullPath, 'rb')  # file to send
            ftpSession.storbinary("STOR " + AosBuildParam.apkFileName, file)  # send the file
            
            
        except ftplib.all_errors:
            thisClass.Quit("---ftp upload failed!!! - please retry after fix ftp upload problem first!!---\n")             
                        
        except IOError:
            thisClass.Quit("---ftp target file open failed!!! - please retry after fix target file open problem first!!---\n")               
                   
        finally:            
            file.close()  # close file and FTP
            ftpSession.quit()    
            
        thisClass.log.writeLog("[3, FTP upload end!!!]\n\n")        
    
    
    
    @classmethod
    def PerformUnityBuild(thisClass):
        
        # unity build
        thisClass.log.writeLog("[2, unity build start!!!]\n\n")        
        
        thisClass.buildTime = str(datetime.datetime.now().date()).replace("-", "") + "_" + str((datetime.datetime.now().time().isoformat().replace("/", "").replace(":", ""))[0:4])
        # print(thisClass.buildTime)
        # print(thisClass.svnRevision)
        # print(AosBuildParam.serverToConnect.lower())        
        
        buildOpt = "release"
        if "development" in AosBuildParam.buildOption.lower() :
            buildOpt = "debug"
            
        AosBuildParam.apkFileName = "PoolTime_d" + thisClass.buildTime + "_v" + AosBuildParam.bundleVersionCode + "_r" + thisClass.svnRevision + "_p" + AosBuildParam.serverPort + "_" + AosBuildParam.serverToConnect.lower() + "_" + buildOpt + ".apk"  
        AosBuildParam.apkFullPath = AosBuildParam.apkPath + "/" + AosBuildParam.apkFileName
              
        try:  
            
            # caution!!! last two parameter == unity's user #define arguments
            subprocess.check_call([AosBuildParam.excutablePath, "-quit", "-batchmode", "-projectPath", AosBuildParam.svnProjectPath, "-logFile", AosBuildParam.logPath,
                                  "-executeMethod", AosBuildParam.buildFunction, AosBuildParam.buildOption, AosBuildParam.userScriptDefine, AosBuildParam.bundleIdentifier, AosBuildParam.bundleVersion, AosBuildParam.bundleVersionCode,
                                  AosBuildParam.keystorePass, AosBuildParam.keyaliasPass, AosBuildParam.apkFullPath], stderr=subprocess.STDOUT)
                                    
        except subprocess.CalledProcessError:           
                                  
            for logline in open(AosBuildParam.logPath, "r") : print(logline)
            thisClass.log.writeLogAndFinalize("---unity build error occurred!!! - please retry after fix unity build error first!!---\n")
            input()
            sys.exit()
        
        #for logline in open(AosBuildParam.logPath, "r", encoding="utf-8") : print(logline)
        #for logline in open(AosBuildParam.logPath, "r") : print(logline)
       
        thisClass.log.writeLog("[2, unity build end!!!]\n\n") 
    
    
    
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
            
        # strMailDesc += "Output File Location(Ftp) : " + AosBuildParam.ftpDirectory + AosBuildParam.bundleVersion + "\n"
        strMailDesc += "Output File Location(Shared Folder) : " + AosBuildParam.sharedDirectory + AosBuildParam.bundleVersion + "\n"
        return strMailDesc
    
    
    
    @classmethod
    def PerformBuild(thisClass, SvnSourceUpdate=True, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnApkCommit=True):    
        
        logBuildMode = "Release"
        if "Development" in AosBuildParam.buildOption : logBuildMode = "Debug"
        
        thisClass.log.writeLog("\n[{0}-{1} build start!!!]\n\n".format(AosBuildParam.serverToConnect, logBuildMode))
        
        # svn update relation
        if SvnSourceUpdate : 
            AosBuild.PerformSVNUpdate(SvnUpdateRevision)
        else :
            AosBuild.GetRevisionNumber()
           
        AosBuild.PerformUnityBuild()
        if UploadToSharedFolder : AosBuild.PerformUploadToSharedFoler()
        if SvnApkCommit : AosBuild.PerformSVNCommit()   
           
        thisClass.log.writeLog("\n[{0}-{1} build End!!!]\n\n".format(AosBuildParam.serverToConnect, logBuildMode))        
               
       
   
    
        


# class for command line build
class AosBuildManager:     
    
    # alpha, beta, real all build, ftp upload, svn commit
    @classmethod    
    def BuildAll(thisClass, SvnSourceUpdate=True, SvnUpdateRevision=-1, UploadToSharedFolder=True, SvnApkCommit=True, MailTo=True):        
                
        #setting ios build param
        AosBuildParam.bundleVersion = BuildConfig.bundleVersion
        AosBuildParam.bundleVersionCode = BuildConfig.bundleVersionCode
        AosBuildParam.excutablePath = BuildConfig.excutablePath
        AosBuildParam.svnPath = BuildConfig.svnPath
        AosBuildParam.svnProjectPath = BuildConfig.svnProjectPath 
               
        AosBuildParam.sharedDrive = BuildConfig.sharedDrive
        AosBuildParam.sharedDirectory = BuildConfig.sharedDirectory
        AosBuildParam.sharedDriveUserName = BuildConfig.sharedDriveUserName
        AosBuildParam.sharedDrivePassword = BuildConfig.sharedDrivePassword
          
        AosBuild.log.writeLog("\n[Master Build Start!!!]\n\n")
        
               
        for mode in BuildConfig.serverModes :
                        
            AosBuildParam.serverToConnect = mode
            AosBuildParam.userScriptServerModeDefine = AosBuildParam.serverModeDefinePrefix + AosBuildParam.serverToConnect + ";"
               
            if mode in BuildConfig.debugModes :           
                AosBuildParam.buildOption = "Development" 
                AosBuildParam.userScriptDefine = AosBuildParam.userScriptBaseDefine + AosBuildParam.userScriptServerModeDefine + AosBuildParam.userScriptDebugLogDefine
                if mode in BuildConfig.adjustServerMode :
                    if "DEBUG" in BuildConfig.adjustBuildMode :
                        AosBuildParam.userScriptDefine = AosBuildParam.userScriptDefine + AosBuildParam.userScriptAdjustDefine
                        
                if mode in BuildConfig.gPrestoServerMode :
                    if "DEBUG" in BuildConfig.gPrestoBuildMode :
                        AosBuildParam.userScriptDefine = AosBuildParam.userScriptDefine + AosBuildParam.userScriptGPrestoDefine
                        
                #AosBuild.PerformBuild(SvnSourceUpdate, SvnUpdateRevision, UploadToSharedFolder, SvnApkCommit)                
                print( "Debug : " + AosBuildParam.userScriptDefine )
                
            if mode in BuildConfig.releaseModes :
                AosBuildParam.buildOption = "Release"
                AosBuildParam.userScriptDefine = AosBuildParam.userScriptBaseDefine + AosBuildParam.userScriptServerModeDefine
                
                if mode in BuildConfig.adjustServerMode :
                    if "RELEASE" in BuildConfig.adjustBuildMode :
                        AosBuildParam.userScriptDefine = AosBuildParam.userScriptDefine + AosBuildParam.userScriptAdjustDefine
                        
                if mode in BuildConfig.gPrestoServerMode :
                    if "RELEASE" in BuildConfig.gPrestoBuildMode :
                        AosBuildParam.userScriptDefine = AosBuildParam.userScriptDefine + AosBuildParam.userScriptGPrestoDefine
                        
                #AosBuild.PerformBuild(SvnSourceUpdate, SvnUpdateRevision, UploadToSharedFolder, SvnApkCommit)                
                print( "RELEASE : " + AosBuildParam.userScriptDefine )
                 
        if SvnApkCommit : AosBuild.PerformSVNCommit()
        
        # if MailTo and UploadToSharedFolder : buildMsgMailTo.MailManager.send_via_gmail_all(AosBuild.GetCompletedMailTitle("APK All"),  AosBuild.GetCompletedMailDesc("APK All", buildSuccessApkPath))
        sys.stdout.writelines('/a')
        sys.stdout.flush()
            
        AosBuild.Quit("\n[Master Build End!!!]\n\nbye!!!\n\n")        
    

'''
if __name__ == '__main__':
    
    AosBuild.PerformBuild()
'''
    
