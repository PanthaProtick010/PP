import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--physics",help="Physics")
parser.add_argument("--chemistry",help="Chemistry")
parser.add_argument("--maths",help="Mathematics")
arg=parser.parse_args()

if arg.physics:
    ph=int(arg.physics) 
else:
    ph=0
if arg.chemistry:
    ch=int(arg.chemistry)
else:
    ch=0
if arg.maths:
    math=int(arg.maths)
else:
    math=0

print(str((ph+ch+math)/3))