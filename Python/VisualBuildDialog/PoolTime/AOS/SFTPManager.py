'''
Created on 2015. 3. 30.

@author: azzrael

'''

''' 

import sys
import os      
import pysftp

from sys import argv


class SFTPUploadManager(object):
    
    IP = "61.249.230.200"
    ID = "sr_mobile"
    PW = r"ahqkdlf*vocl##"
    PORT = 18181
    PLATFORM_PATH = r"Android/"
    TO_AB_PATH = r"HanPocket/"
    FROM_AB_PATH = r"../../../SourcesHanPocket8/AssetBundle/" + PLATFORM_PATH    
     
    
    def __init__(self):
        pass
        
    
    @classmethod  
    def upload(cls):
        
        try:
            TO_AB_PATH = cls.TO_AB_PATH + argv[1] + "/AssetBundles/" + cls.PLATFORM_PATH
            with pysftp.Connection(cls.IP, username=cls.ID, password=cls.PW, port=cls.PORT) as sftp:
                with sftp.cd(TO_AB_PATH):
                    normAbsSrcPath = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), cls.FROM_AB_PATH))
                    
                    cur_local_dir = os.getcwd()                    
                    os.chdir(normAbsSrcPath)                   
                    
                    print("src directory : ", normAbsSrcPath)
                    print("dst directory : ", sftp.pwd)                    
                    
                    wtcb = pysftp.WTCallbacks()                    
                   
                    pysftp.walktree('.', wtcb.file_cb, wtcb.dir_cb, wtcb.unk_cb, recurse=False)
                    for fname in wtcb.flist:                                        
                        fname = fname.replace( ".\\", "" )                                            
                        sftp.put(fname, fname)                        
                        print(fname, "uploaded")

                    # restore local directory
                    os.chdir(cur_local_dir)
                    
        except Exception as e:
            print(e)
            sys.exit("shit sftp upload failed!!!")
            
                
'''   
    
    

        