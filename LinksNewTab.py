#!/usr/bin/python

import re
import glob
from string import Template

print "This script will change all links to html version which can be opened in the NEW tab.\n"

fileList = glob.glob("*.md")
if len(fileList) == 0:
	print "No markdown file here.Exit -o-"
	exit(0)
print "Your markdown file are these:\n"

for f in fileList:
	print f

for f in fileList:
	print "\nStart convert: " + f
	fileObject = file(f)
	
	try:
		fileText = fileObject.read()
		
		markdownReg = re.compile("(.*)\[(.*)\]\((.*)\)",re.M)
		urlTemplate = Template("<a href='${linkUrl}' target='_blank'>${linkName}</a>")
		
		def mdToUrl(matchobj):
			itself = matchobj.group(0)
			beforeLink = matchobj.group(1)
			linkName = matchobj.group(2)
			linkUrl = matchobj.group(3)
			
			if len(beforeLink) > 0:
				if beforeLink[len(beforeLink)-1] == '!':
					urlReg = itself #escape '![]()'
				else:
					urlReg = beforeLink + urlTemplate.safe_substitute(linkUrl = linkUrl,linkName = linkName) # .*[]()
			else:
				urlReg = urlTemplate.safe_substitute(linkUrl = linkUrl,linkName = linkName) # []()
			return urlReg
		
		result = re.sub(markdownReg, mdToUrl, fileText)
		
		newFile = f.replace(".md","_new.md")
		output = open(newFile, 'w')
		output.write(result)
		print "OK!\n"
	
	finally:
		fileObject.close( )

print "Mission all over! Check all the generate *_new.md files"