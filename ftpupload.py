from ftplib import FTP
import parameters as param

def UploadFileToFTP ():
    try:
        file = open(param.FTP_INFO_FILE, "r")
        ftpinfo = []
        for line in file:
            ftpinfo.append(line.rstrip())
        print(ftpinfo)
        session = FTP(host = ftpinfo[0], user = ftpinfo[1], passwd=ftpinfo[2])
        file = open(param.HTML_PORTOFOLIO_REPORT_FULLNAME,'rb')                  # file to send
        cmd = "STOR " + param.HTML_PORTOFOLIO_REPORT_FULLNAME
        session.storbinary(cmd, file)     # send the file
        file.close()                                    # close file and FTP
        file = open(param.HTML_REPORT_FILENAME,'rb')                  # file to send
        cmd = "STOR " + param.HTML_REPORT_FILENAME
        session.storbinary(cmd, file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()
    except Exception as err:        
        print("FTP load failed: {0}".format(err))
        
