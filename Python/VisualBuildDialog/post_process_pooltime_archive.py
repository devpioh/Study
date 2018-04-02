'''
Created on 2013. 9. 11.

@author: azzrael
'''



import os
import sys
from sys import argv

import subprocess
#import plistlib
import shutil

sys.path.insert(0,'../Build/')


class XcodeBuilder:
    

    # delete *.meta file recursively
    @classmethod
    def delete_unity_meta_file( thisClass ):
        
        print("delete unity .meta files - start")
        
        exts = ["meta"]
        found = {x:[] for x in exts}
        
        for dirPath, dirNames, files in os.walk(thisClass.xcodeProjPath):
            for name in files:
                ext = name.lower().rsplit(".", 1)[-1]
                
                if ext in exts:
                    found[ext].append(os.path.join(dirPath, name))
                    
        for search in found:
            for delfile in found[search]:
                os.remove(delfile)
                
        print("delete unity .meta files - end")
        
    
    
    
    '''
    # update info.plist   
    @classmethod 
    def update_info_plist( thisClass ):
        
        print("update plist info - start")
        
        if os.path.isfile(thisClass.infoPlistPath):
            info = plistlib.readPlist(thisClass.infoPlistPath)
            info["CFBundleURLTypes"] = [{"CFBundleURLTypes":thisClass.urlName, 
                                         "CFBundleTypeRole":"Editor",
                                         "CFBundleURLSchemes":["kakao"+thisClass.kakaoClientID]}]
            
            info["CFBundleVersion"] = thisClass.versionCode            
            info["CFBundleShortVersionString"] = thisClass.versionNum
            info["UIStatusBarHidden"] = True
            info["UIStatusBarHidden~ipad"] = True
            info["UIViewControllerBasedStatusBarAppearance"] = False
            info["UIRequiresFullScreen"] = True
            
            # for Xcode 7
            info["NSAppTransportSecurity"] = {"NSAllowsArbitraryLoads":True}
            
            try:
                outfile = open(thisClass.infoPlistPath, "wb")
                plistlib.writePlist(info, outfile)
            except:
                print('can not open info.plist file to write new contents or data corrupted!!!')
                sys.exit(1)
            finally:
                outfile.close()                
                
        print("update plist info - end")
    '''
    
    '''        
    @classmethod        
    def update_app_controller(thisClass):
        
        print("update application controller - start")
        
        # modify main.mm
        strOut = ""
        try:                
            mainFile = open( thisClass.mainMMPath, "r" )
            for line in mainFile:
                newLine = line
                if thisClass.appControllerKeyword in line:
                    newLine = line.replace(thisClass.appControllerKeyword, thisClass.appControllerChangeKeyword)
                strOut += newLine               
        except:
            print('can not open ' + thisClass.mainMMPath + ' file to write new contents or data corrupted!!!')
            sys.exit(1)        
        finally:
            mainFile.close()
        
        try:
            outFile = open(thisClass.mainMMPath, "w")
            outFile.write(strOut)
        except:
            print('can not open ' + thisClass.mainMMPath + ' file to write new contents or data corrupted!!!')
            sys.exit(1)
        finally:
            outFile.close()
        
        print("update application controller - end")
    '''
            
    
    
    '''
    @classmethod
    def update_xcode_proj( thisClass ):
        
        print( "update xcode project file - start" )
        project = XcodeProject.Load(thisClass.pbxProjName)
        
        #update build configuration
        project.add_build_setting(thisClass.clientIDStr, thisClass.kakaoClientID, thisClass.clientIDForAddOption)
        project.add_build_setting(thisClass.preProcessorDefStr, thisClass.preProcessorDefValue)
        #project.add_build_setting("CODE_SIGN_RESOURCE_RULES_PATH", "$(SDKROOT)/ResourceRules.plist")

        #for xcode 7
        project.add_build_setting("ENABLE_BITCODE","No")

        # code signing
        # if exist key already modify it
        #project.add_build_setting_for('Release', "CODE_SIGN_IDENTITY[sdk=iphoneos*]", thisClass.signID[thisClass.profileType])
        #project.add_build_setting_for('Ad-Hoc', "CODE_SIGN_IDENTITY[sdk=iphoneos*]", thisClass.signID[thisClass.profileType])
        #project.add_build_setting_for('Distribution', "CODE_SIGN_IDENTITY[sdk=iphoneos*]", thisClass.signID[thisClass.profileType])
        
        # add Frameworks
        project.add_file("System/Library/Frameworks/ImageIO.framework", None, tree="SDKROOT", weak=False)
        project.add_file("System/Library/Frameworks/MessageUI.framework", None, tree="SDKROOT", weak=False)
        project.add_file("System/Library/Frameworks/AddressBook.framework", None, tree="SDKROOT", weak=False)
        project.add_file("System/Library/Frameworks/AssetsLibrary.framework", None, tree="SDKROOT", weak=False)
        project.add_file("System/Library/Frameworks/CoreData.framework", None, tree="SDKROOT", weak=False)
        project.add_file("System/Library/Frameworks/Security.framework", None, tree="SDKROOT", weak=False)
        
        # add other linker flags
        for currFlag in thisClass.otherLDFlags:
            project.add_other_ldflags(currFlag)      
        
        if project.modified:    
            project.backup()
            project.saveFormat3_2()
            #project.save()
            
        print( "update xcode project file - end" )
    '''
            

        
     
    
    @classmethod
    def build_archive( thisClass ):        
        
        print("build archive - start")      
        
        try:
            saveCurrWokingDir = os.getcwd()            
            os.chdir(thisClass.xcodeProjPath)  
                                                       
            if thisClass.isAutomaticSigning :
                #codeSigningIdentityOpt = "CODE_SIGN_IDENTITY=" + thisClass.signIDs["development"]
                developmentTeamOpt = "DEVELOPMENT_TEAM=" + thisClass.developmentTeamID
                output = subprocess.Popen( ["/usr/bin/xcodebuild", "-project", thisClass.xcodeProjName, "-scheme", "Unity-iPhone", "-configuration", thisClass.buildConfiguration, "-sdk", "iphoneos",
                                            developmentTeamOpt,                                                      
                                            "clean", "archive", "-archivePath", thisClass.archivePath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
                
                outstream, errstream = output.communicate()
            
                print(outstream)
                print(errstream)
                
            else : 
                for profile in thisClass.profiles :
                    codeSigningIdentityOpt = "CODE_SIGN_IDENTITY=" + thisClass.signIDs[profile]
                    provisioningProfileOpt = "PROVISONING_PROFILE_SPECIFIER=" + thisClass.provisionProfiles[profile]
                               
                    output = subprocess.Popen( ["/usr/bin/xcodebuild", "-project", thisClass.xcodeProjName, "-scheme", "Unity-iPhone", "-configuration", thisClass.buildConfiguration, "-sdk", "iphoneos",
                                                codeSigningIdentityOpt, provisioningProfileOpt,                                                          
                                                "clean", "archive", "-archivePath", thisClass.archivePath[profile]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
                    
                    outstream, errstream = output.communicate()
                
                    print(outstream)
                    print(errstream)
            
            
                
        except subprocess.CalledProcessError:       
            print('can not build xcode(.xcarchive)!!!')      
            sys.exit(3)
            
        finally:
            os.chdir(saveCurrWokingDir)
        
        print("build archive - end")   
    
    
    @classmethod
    def build_ipa(thisClass):        
        
        print("build ipa - start")
        
        try:  
            saveCurrWokingDir = os.getcwd()            
            os.chdir(thisClass.xcodeProjPath)  
            
            for profile in thisClass.profiles :
                
                if profile == "distribution" and thisClass.serverToConnect != "REAL" :
                    continue
                
                exportOptionPlistFile = "exportDevelopment.plist"               
                if(profile == "development") : exportOptionPlistFile = "exportDevelopment.plist"
                elif(profile == "adhoc") : exportOptionPlistFile = "exportAdhoc.plist"
                elif(profile == "distribution") : exportOptionPlistFile = "exportDistribution.plist"
                else : exportOptionPlistFile = "exportEnterprise.plist"
                exportOptionPlistPath = thisClass.scriptRootPath + "/ExportOptionPList/" + exportOptionPlistFile
                   
                if thisClass.isAutomaticSigning :
                    output = subprocess.Popen( ["/usr/bin/xcodebuild", "-exportArchive", "exportFormat", "ipa", "-archivePath", thisClass.archivePath, "-exportPath", thisClass.outIPAPaths[profile],
                                                "-exportOptionsPlist", exportOptionPlistPath],
                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
                else :
                    output = subprocess.Popen( ["/usr/bin/xcodebuild", "-exportArchive", "exportFormat", "ipa", "-archivePath", thisClass.archivePath[profile], "-exportPath", thisClass.outIPAPaths[profile],
                                                "-exportOptionsPlist", exportOptionPlistPath],
                                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True )
                                       
                outstream, errstream = output.communicate()            
                
                print(outstream)
                print(errstream)   
                
                #rename ipa file name
                outFullIPAPaths = thisClass.outIPAPaths[profile] + "Unity-iPhone.ipa"
                destOutFullIPAPaths = thisClass.outIPAPaths[profile] + profile + thisClass.versionIdentifier.split(".")[-2] + ".ipa"
                os.rename(outFullIPAPaths, destOutFullIPAPaths)
                
        except subprocess.CalledProcessError:       
            print('can not build xcode(.xcarchive)!!!')      
            sys.exit(3)      
            
        finally:
            os.chdir(saveCurrWokingDir)
        
        #print(thisClass.archivePath)        
        #shutil.rmtree(thisClass.archivePath)    
    
        print("build ipa - end")
     
    
    @classmethod
    def Build(thisClass):
        
        print('----- prepare for excuting our magic scripts to tweak our xcode -----')
        
        # command arguments
        thisClass.assetsPath = argv[1]
        thisClass.xcodeProjPath = argv[2]
        thisClass.scriptRootPath = thisClass.xcodeProjPath[:-12]
        thisClass.srcPluginPath = argv[3]        
        thisClass.versionIdentifier = argv[4]
        thisClass.versionNum = argv[5]
        thisClass.versionCode = argv[6]        
        if argv[7].lower() == "automatic" : thisClass.isAutomaticSigning = True
        else : thisClass.isAutomaticSigning = False
        thisClass.serverToConnect = argv[8]
        thisClass.buildConfiguration = argv[9]
        thisClass.isCommandLineBuild = argv[10].lower()
        thisClass.developmentTeamID = argv[11]
        strProfiles = argv[12]
        thisClass.profiles = strProfiles.split(",")    
        strDevSignID = argv[13]
        strAdhocSignID = argv[14]
        strDistSignID = argv[15]
        strDevProvisionProfile = argv[16]
        strAdhocProvisionProfile = argv[17]
        strDistProvisionProfile = argv[18]
        
        thisClass.signIDs = {"development":strDevSignID,
                             "adhoc":strAdhocSignID,
                             "distribution":strDistSignID} 
        
        thisClass.provisionProfiles = {"development":strDevProvisionProfile,
                                       "adhoc":strAdhocProvisionProfile,
                                       "distribution":strDistProvisionProfile}         
                    
        # various path
        #thisClass.srcKAAuthBundlePath = thisClass.srcPluginPath + '/KAAuth.bundle'
        #thisClass.dstKAAuthBundlePath = thisClass.xcodeProjPath + '/Libraries/KAAuth.bundle'
        thisClass.xcodeProjName = thisClass.xcodeProjPath + "/Unity-iPhone.xcodeproj"
        thisClass.pbxProjName = thisClass.xcodeProjPath +'/Unity-iPhone.xcodeproj/project.pbxproj'
        
        if thisClass.isAutomaticSigning :
            thisClass.archivePath = thisClass.xcodeProjPath + "/build/Release-iphoneos/" + thisClass.versionIdentifier.split(".")[-2] + thisClass.buildConfiguration +".xcarchive"
        else :
            for profile in thisClass.profiles : 
                thisClass.archivePath[profile] = thisClass.xcodeProjPath + "/build/Release-iphoneos/" + profile +".xcarchive"
                
        thisClass.outIPAPaths = {"development":"", "adhoc":"", "distribution":""}
        
        for profile in thisClass.profiles :                
            thisClass.outIPAPaths[profile] = thisClass.xcodeProjPath + "/build/Release-iphoneos/"       
        
        # signing and provision profile
        
       
        print("command line argument : assets path --> " + thisClass.assetsPath)
        print("command line argument : xcode build path --> " + thisClass.xcodeProjPath)
        print("command line argument : unity ios pluggin path --> " + thisClass.srcPluginPath)        
        print("command line argument : version identifier --> " + thisClass.versionIdentifier)
        print("command line argument : version num --> " + thisClass.versionNum)
        print("command line argument : version code --> " + thisClass.versionCode)
        print("command line argument : is CommandLine Build ?--> " + thisClass.isCommandLineBuild)
        
        if thisClass.isAutomaticSigning :
            print("command line argument : thisClass.archivePath --> " + thisClass.archivePath)     
        
        print("command line argument : development sign id --> " + thisClass.signIDs["development"])
        print("command line argument : adhoc sign id --> " + thisClass.signIDs["adhoc"])
        print("command line argument : distribution sign id --> " + thisClass.signIDs["distribution"])
        print("command line argument : development provisionProfile --> " + thisClass.provisionProfiles["development"])
        print("command line argument : adhoc provisionProfile --> " + thisClass.provisionProfiles["adhoc"])
        print("command line argument : distribution provisionProfile --> " + thisClass.provisionProfiles["distribution"])      
        
        for profile in thisClass.profiles :        
            print("command line argument : provision profile --> " + profile)  
             
            if not thisClass.isAutomaticSigning : 
                print("command line argument : thisClass.archivePath --> " + thisClass.archivePath[profile])
                                      
            print("command line argument : thisClass.outIPAPaths --> " + thisClass.outIPAPaths[profile])        
        
              
        thisClass.delete_unity_meta_file()
        #thisClass.update_xcode_proj()     
        #thisClass.update_info_plist()       
        #thisClass.update_app_controller()
        
        if( thisClass.isCommandLineBuild == "true" ):   
            thisClass.build_archive()       
            thisClass.build_ipa()
        
        
        print('------ end for excuting our magic scripts to tweak our xcode -----')
    



# if __name__ == '__main__':
#     XcodeBuilder.Build()