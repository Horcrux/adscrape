import gumtree
import sys
with open ('scrapelist.cfg', 'r') as f:
    for line in f:
        gumtree.main(line.split(' ')[2],line.split(' ')[1],int(line.split(' ')[0]))
