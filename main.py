import gumtree
import olx
import sys
print "***************************STARTUP***************************"
with open ('scrapelist.cfg', 'r') as f:
    for line in f:
        print line.split(' ')[2].strip().split('/')[2]
	print ("Now handling line \""+line.strip()+"\"")
        if (line.split(' ')[2].strip().split('/')[2].split('.')[1]=='gumtree'):
            gumtree.main(line.split(' ')[2].strip(),line.split(' ')[1],int(line.split(' ')[0]))
        elif (line.split(' ')[2].strip().split('/')[2].split('.')[1]=='olx'):
            olx.main(line.split(' ')[2].strip(),line.split(' ')[1],int(line.split(' ')[0]))
