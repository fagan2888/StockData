## This file is an alternative implemention of FTP. 
## It is a practise of transion to oop programing
##


from myFTP import myFTP
import parameters as param
import yaml

def doUpload ():
    try:
        ftp = myFTP()
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
        session = ftp.Create(host = ftpinfo['host'], user = ftpinfo['login']['un'], passwd=ftpinfo['login']['pw'])
        session.cwd(ftpinfo['dir'])
        ftp.Upload(param.HTML_REPORT_FILENAME, session)
        ftp.Upload(param.HTML_PORTOFOLIO_REPORT_FULLNAME, session)
        ftp.Upload(param.HTML_TREND_REPORT_FILENAME, session)
        ftp.Upload(param.BUYLIST, session)
        ftp.Upload(param.SELLLIST,session)     
        ftp.quit(session)
    except Exception as err:        
        print("FTP load failed: {0}".format(err))

