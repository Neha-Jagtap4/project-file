from sys import *
import os
from pathlib import Path
import time
import hashlib
import datetime
import schedule
import psutil
from urllib.request import urlopen
import smtplib
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Periodic Process Logger with Auto Scheduled Log Report 
#Delete the duplicate files
def DeleteFiles(dict1):
    
    results = list(filter(lambda x: len(x)>1,dict1.values()))

    icnt = 0
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0
    else:
        print("No duplicate files found")

 
def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

#Finding duplicate files and removing 
def findDup(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups

    else:
        print("Invalid Path")

#Finding duplicate result
def printResults(dict1):
    results = list(filter(lambda x: len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates found")
        print("The following files are duplicate")
        for  result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
    else:
        print("No duplicate files found")

#Finding path and Duplicate files 
def ProcessMemory(dict1,log_dir="Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separtor = "-" * 80
    log_path =os.path.join(log_dir,"Marvellous")    
    f= open(log_path,'w')   
    f.write(separtor+"\n")  
    f.write("Process Logger " +time.ctime()+ "\n")
    f.write(separtor+"\n")

    results = list(filter(lambda x: len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates files are Sucessfully copied")
        for  result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
                listprocess.append(subresult)
    else:
        print("No duplicate files found")

    for element in listprocess:
        f.write("%s\n"%element)

    #Sending email 
    print("Log file is successfully generated at location : ",log_path)

    sender_email = "njagtap368@gmail.com"
    receiver_email = "nehajagtapc@gmail.com"

    message = MIMEMultipart()

    message["From"] = sender_email
    message['To'] = receiver_email

    message['Subject'] = "sending mail using python"

    file = "Demo.txt"
    attachment = open(file,'rb')
    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)
    message.attach(obj)

    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com',587)
    email_session.starttls()
    email_session.login(sender_email,'Neha@7261')
    email_session.sendmail(sender_email,receiver_email,my_message)
    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")

def main():
    print("---- Periodic Process Logger with Auto Scheduled Log Report  -----")

    print("Application name : " +argv[0])
    print("Directory is: "+argv[1])
    print("File created : "+argv[2])
    
    
    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[2] == "-h") or (argv[2] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[2] == "-u") or (argv[2] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    cwd = os.getcwd() # Print the current working  directory
    print("Current working directory:")
    print(cwd)

    print(cwd+"\\"+argv[1])
    source_folder = cwd+"\\"+argv[1]

    arr={}
    startTime = time.time()
    arr = findDup(argv[1])
    printResults(arr)
    DeleteFiles(arr)
    ProcessMemory(arr,argv[2])
    endTime = time.time()

    print("Took %s seconds to evaluate "%(endTime - startTime))
    
if __name__ == "__main__":
    main()