from ftplib import FTP
import parameters as param
import yaml

def UploadFileToFTP ():
    try:
        file = open(param.FTP_INFO_FILE, "r")
        #ftpinfo = []
        #for line in file:
        #    ftpinfo.append(line.rstrip())
        #print(ftpinfo)
        #session = FTP(host = ftpinfo[0], user = ftpinfo[1], passwd=ftpinfo[2])
        with open(param.FTP_INFO_FILE, 'r') as stream:
            try:
                ftpinfo = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)        
        session = FTP(host = ftpinfo['host'], user = ftpinfo['login']['un'], passwd=ftpinfo['login']['pw'])
        session.cwd(ftpinfo['dir'])
        UploadFile(param.HTML_REPORT_FILENAME, session)
        UploadFile(param.HTML_PORTOFOLIO_REPORT_FULLNAME, session)
        UploadFile(param.HTML_TREND_REPORT_FILENAME, session)
        UploadFile(param.BUYLIST, session)
        UploadFile(param.SELLLIST,session)        
        session.quit()
    except Exception as err:        
        print("FTP load failed: {0}".format(err))
    
    
def UploadFile(filename, session):        
    file = open(filename,'rb')                  # file to send
    cmd = "STOR " + filename
    session.storbinary(cmd, file)     # send the file
    file.close()