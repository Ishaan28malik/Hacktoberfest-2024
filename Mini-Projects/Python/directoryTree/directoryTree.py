import os
import sys
import argparse


# Python program\to print 
# colored text and background 
class colors: 
    #to make ansci colour coding work even in windows
    from platform import system
    if "win" in system().lower(): #works for Win7, 8, 10 ...
        from ctypes import windll
        k=windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11),7)
    
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'


class Node:
    '''This class represents a directory'''
    def __init__(self, baseDir):
        baseDir=os.path.split(baseDir)
        if len(baseDir) == 1:
            baseName=baseDir[0]
        else:
            baseName=baseDir[1]
        baseLoc=baseDir[0]
        self.dirName=baseName
        self.dirLoc=baseLoc
        self.children=[]

    def findChildDirectories(self):
        '''this functioin finds all child directories of current node'''
        path=os.path.join(self.dirLoc, self.dirName)
        if not os.path.isdir(path):
            return
        subs=os.listdir(path)
        for sub in subs:
            tempNode=Node(os.path.join(path, sub))
            self.children.append(tempNode)


def createDirectoryTree(rootNode, maxDepth=99999):
    '''this function creates a tree of directories with first parameter as root of tree and maxDepth is maximum depth given tree can have.'''
    if rootNode == None or maxDepth < 1:
        return None
    rootNode.findChildDirectories()
    for child in rootNode.children:
        if os.path.isdir(os.path.join(rootNode.dirLoc, rootNode.dirName)):
            createDirectoryTree(child, maxDepth - 1)

def getDirectoryTree(rootNode, maxDepth=99999, tabCount=1, onlyDir=False, extensions=None, search=None, takeImage=False):
    '''this function traverses the directory tree and returns tree in string format.
It uses follows given colour coding in its output:
    directory - blue
    executable - green
    compressed file - red
    other file - white'''
    if rootNode == None or maxDepth < 1:
        return None
    str="|    " * (tabCount-1)
    fullPath=os.path.join(rootNode.dirLoc, rootNode.dirName)
    finalOutput=""
    if onlyDir == True or os.path.isdir(fullPath):
        if os.path.isdir(fullPath):
            if rootNode.dirName == search:
                finalOutput+="{}|===={}{}{}{}\n".format(str, colors.fg.orange, colors.bold, rootNode.dirName, colors.fg.lightgrey)
            else:
                finalOutput+="{}|===={}{}{}\n".format(str, colors.fg.blue, rootNode.dirName, colors.fg.lightgrey)
    else:
        extension=fullPath.split(".", -1)[-1]
        executables=["exe", "sh", "py", "cpp"]
        compressed=["zip", "tar", "gz"]
        if rootNode.dirName == search:
                finalOutput+="{}|===={}{}{}{}\n".format(str, colors.fg.orange, colors.bold, rootNode.dirName, colors.fg.lightgrey)
        elif search != None:
            pass
        elif extensions != None:
            if extension in extensions:
                finalOutput+="{}|----{}{}{}\n".format(str, colors.fg.lightgrey, rootNode.dirName, colors.fg.lightgrey)
        elif extension in executables:
        #if os.access(fullPath, os.X_OK):
            finalOutput+="{}|----{}{}{}\n".format(str, colors.fg.green, rootNode.dirName, colors.fg.lightgrey)
        elif extension in compressed:
            finalOutput+="{}|----{}{}{}\n".format(str, colors.fg.red, rootNode.dirName, colors.fg.lightgrey)
        else:
            finalOutput+="{}|----{}{}{}\n".format(str, colors.fg.lightgrey, rootNode.dirName, colors.fg.lightgrey)
    for child in rootNode.children:
        output=getDirectoryTree(child, maxDepth-1, tabCount+1, onlyDir=onlyDir, extensions=extensions, search=search)
        if output != None or output.strip() != "":
            finalOutput+=(output)
    return finalOutput


#Parse the arguments
def getArguments():
    '''this function parses the arguments passed to script and validates them
Following parameters affect the output of this function:
    1) -d", "--dir : this is the base directory from which to print/search sub-directories
    2) -m or --max-depth :  this parameter tells the maxmimum depth of sub-directories to explore
    3) -e or --extensions : this parameter makes function to print only files with given extension
    4) -s or --search : this parameter takes a filename as input and if the given file is found then prints it in orange colour
    5) --onlyDir : This is a boolean variable which makes it print only directories in tree
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Base directory location",dest="path",action="store",required=True)
    parser.add_argument("-m", "--max-depth", help="Maximum depth to go from base directory",dest="maxDepth",action="store", default=5,required=False)
    parser.add_argument("-i", "--image", help="To take image of output",dest="image", default=False, action="store",required=False)
    parser.add_argument("--only-dir", help="To print only directories in output",dest="onlyDir",action="store", type=strToBool, default=False, required=False)
    parser.add_argument("-e", "--extensions", help="To print only files with given output",dest="extensions", default=None, nargs="*", action="store",required=False)
    parser.add_argument("-s", "--search", help="To search a given file",dest="search", default=None, action="store",required=False)
    args = parser.parse_args()
    args.path=os.path.realpath(args.path)
    if not os.path.isdir(args.path):
        print("Given directory does not exists")
        sys.exit(1)
    if args.onlyDir==True and args.extensions!=None:
        print("Please provide either --only-dir true or --extensions")
        sys.exit(1)
    if args.extensions!=None and len(args.extensions) == 1:
        args.extensions=args.extensions[0].split(",")
    return args


def strToBool(value):
    '''this function takes a string and check if the string is string for a binary value'''
    if value.lower() in {'false', 'f', '0', 'no', 'n'}:
        return False
    elif value.lower() in {'true', 't', '1', 'yes', 'y'}:
        return True
    raise ValueError(f'{value} is not a valid boolean value')


args=getArguments()
rootDir=args.path
maxDepth=int(args.maxDepth)
onlyDir=args.onlyDir
extensions=args.extensions
search=args.search
rootNode=Node(rootDir)
createDirectoryTree(rootNode, maxDepth=maxDepth)
outputTree=getDirectoryTree(rootNode, onlyDir=onlyDir, extensions=extensions, search=search)
print(outputTree)
