## This file is an alternative implemention of FTP. 
## It is a practise of transion to oop programing
##

from ftplib import FTP


class myFTP(object):
    def __init__(self):
        raise NotImplementedError
    
    def Create(self, host, user, pw):
        session = FTP(host=self.host, user=self.user, passwd=self.pw)
        return session

    def Upload(self,filename, session):        
        file = open(filename,'rb')                  # file to send
        cmd = "STOR " + filename
        session.storbinary(cmd, file)     # send the file
        file.close()
    def Quit(self, session):
        session.quit()

    def main():
        suite

if __name__ == '__main__':
    sys.exit(int(main() or 0))



    

        
        
    