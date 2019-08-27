import glob
import csv
import datetime
import os

#path in jupyter
filedate = (datetime.datetime.today().strftime('%Y-%m-%d')) 
path = r'/home/jovyan/fileconsolidator/files'
outputpath = r'/home/jovyan/fileconsolidator/files/output'
print(path)
files = [os.path.basename(f) for f in glob.glob(path + "**/*.csv", recursive=False)]
excelfiles = [f for f in glob.glob(path + "**/*.csv", recursive=False)]

print('file only')
print(files)
print('full path')
print(excelfiles)

csvuploadfile = outputpath+'/orderconsolidated-'+filedate+'.csv'  
 
#create new csv file
with open(outputpath+'/orderconsolidated-'+filedate+'.csv', 'wt') as file:
    filewriter = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE,escapechar=' ')
    rownumber = 0
    print('fileopened')
    #go through all excel files
    for f in excelfiles:
        #open, go through each row in excel file, and read)
        filename = os.path.basename(f)
        with open(f,newline='',encoding="utf8", errors='ignore') as sourcefile:
            csvreader=csv.reader(sourcefile,delimiter=',')                    
            for row in csvreader:
                #escapes extra characters
                cleanrow = str(row)
                escapechars = "'[]'`‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
                for c in escapechars:
                    cleanrow = cleanrow.replace(c,"")
                row=cleanrow
                print(row,filename)
                filewriter.writerow([row,filename,""]) 
                #filewriter.write(f)
                rownumber += 1                

                

filecount = rownumber
print('LOG DONE')           
print(filecount)
