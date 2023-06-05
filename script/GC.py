import sys
import os
import subprocess
import argparse

parser=argparse.ArgumentParser("GC content in 20(default) bases before and after call position (GC_20) .")
parser.add_argument("-l","--list",help="first cloumn is Chr and Second cloumn is Pos.",required=True)
parser.add_argument("-f","--fna",help="human genome sequence",required=True)
parser.add_argument("-n","--num",help="number bases before and after call position",default=20)
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
args=parser.parse_args()
infile=open(args.list,"r")
outfile=open("%s/%s.bed"%(args.outdir,args.num),"w")

for line in infile:
    start,end=0,0
    line=line.strip()
    pos=int(line.split("\t")[1])
    if pos>20:
        outfile.write("")

infile.close()
outfile.close()
