import gumtree
import olx
import sys
print "***************************STARTUP***************************"
with open ('scrapelist.cfg', 'r') as f:
    for line in f:
	print ("Now handling line \""+line.strip()+"\"")
        if (line.split(' ')[3].strip()=='gumtree'):
            gumtree.main(line.split(' ')[2],line.split(' ')[1],int(line.split(' ')[0]))
        elif (line.split(' ')[3].strip()=='olx'):
            olx.main(line.split(' ')[2],line.split(' ')[1],int(line.split(' ')[0]))
