#PYTHON SCRIPT FOR CHOOSING LUNCH
import sys
import random
import string
import subprocess
import pycurl
import json

josh=False
bcheap = False
ncheap = False

if len(sys.argv) > 1 and sys.argv[1]=='josh':
	josh = True
elif len(sys.argv) > 1 and sys.argv[1]=='cheap':
	bcheap = True
elif len(sys.argv) > 1 and sys.argv[1]=='ncheap':
	ncheap = True

if len(sys.argv) > 2:
	if sys.argv[2]=='cheap':
		bcheap=True
	elif sys.argv[2] == 'ncheap':
		ncheap=True
	else:
		print "You fucked up... discarding arg " + sys.argv[2]
		
if josh:
	print "JOSH"
if bcheap:
	print "CHEAP"
if ncheap:
	print "NOT CHEAP"

Cheap = open("cheapeats.txt","r")
NotCheap = open("notcheapeats.txt","r")
Veto = open("vetolist.txt","r")
AteThere = open("atethere.txt","r+")

cheapeats = Cheap.readlines()
notcheapeats = NotCheap.readlines()
veto = Veto.readlines()
atethere = AteThere.readlines()

if len(atethere) > 5:
	AteThere.close()
	AteThere = open("atethere.txt",'w')
	i = 1
	for item in range(1,6):
		AteThere.write(atethere[i])
		i=i+1

AteThere.close()
NotAgain = open("atethere.txt","r")
notagain = NotAgain.readlines()

print "NOTAGAIN: "
print notagain

if not bcheap and not ncheap:
	eats = cheapeats+notcheapeats
elif (bcheap):
	eats = cheapeats
elif (ncheap):
	eats = notcheapeats

eats = [x for x in eats if x not in notagain]
if (josh):
	eats = [x for x in eats if x not in veto]

secure_random = random.SystemRandom()

lunch = secure_random.choice(eats)

AteThere=open("atethere.txt","a")
AteThere.write(lunch)
AteThere.close()
print lunch

data = json.dumps({"username": "LUNCH WILL BE AT:", "icon_emoji": ":hamburger:", "text": lunch})

c = pycurl.Curl()
c.setopt(c.URL, 'https://hooks.slack.com/services/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')
c.setopt(c.HTTPHEADER, [
			'Content-Type: application/json'
		]) 
c.setopt(c.POSTFIELDS, data)
c.setopt(pycurl.POST, 1)
c.perform()
