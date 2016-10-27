import os 
import mimetypes

index ={}

# currentAbsDirectory = os.path.abspath('/home')
# print currentAbsDirectory

def crawlDirectory(folderPath):

    for folderName, subfolders, filenames in os.walk(folderPath):
        for subfolder in subfolders:
           
            if subfolder not in index.keys():
                index[subfolder] = [folderName+"/"+subfolder]
            else: 
                index[subfolder].append(folderName+"/"+subfolder)
        for filename in filenames:
            mime = mimetypes.guess_type(filename)
             
            if mime[0]:
                print('FILE INSIDE ' + folderName + ': '+ filename)
                # print "woah"
                if filename not in index.keys():
                    index[filename] = [folderName+'/'+filename]
                else: 
                    index[filename].append(folderName+'/'+filename)
                with open(folderName+'/'+filename) as file:
                    line = file.read()
                    for word in line.split():
                        if word not in index.keys():
                            index[word] = [folderName+'/'+filename]
                        else:
                            index[word].append(folderName+'/'+filename)
        


searchFolder = raw_input("Enter folder to crawl: ")
crawlDirectory(searchFolder)
query = raw_input("Enter word/file/ folder name: ")

for key in index[query]:
    print key
    print index[key]
