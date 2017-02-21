#PYTHON SCRIPT FOR CHOOSING LUNCH
#STEP 1: IMPORT ALL THE THINGS
import sys
import random
import string
import pycurl
import json

#STEP 2 INIT BOOLS
josh=False
bcheap = False
ncheap = False

#STEP 3 CHECK ARGS, WARN FOR SHIT INPUT
if len(sys.argv) > 2:
	if (sys.argv[1] == 'cheap' and sys.argv[2] == 'ncheap') or (sys.argv[1] == 'ncheap' and sys.argv[2] == 'cheap'):
		print "ugh wtf are you doing?  I am not writing the error handling for stupidity.  You're gonna get cheap food"

if len(sys.argv) > 1 and sys.argv[1]=='josh':
	josh = True
elif len(sys.argv) > 1 and sys.argv[1]=='cheap':
	bcheap = True
elif len(sys.argv) > 1 and sys.argv[1]=='ncheap':
	ncheap = True

#STEP 4 KEEP CHECKING ARGS
if len(sys.argv) > 2:
	if sys.argv[2]=='cheap':
		bcheap=True
	elif sys.argv[2] == 'ncheap':
		ncheap=True
	else:
		print "You fucked up... discarding arg " + sys.argv[2]

#OPEN THEM DATA FILES FOR READ/READ+
Cheap = open("cheapeats.txt","r")
NotCheap = open("notcheapeats.txt","r")
Veto = open("vetolist.txt","r")
AteThere = open("atethere.txt","r+")

#READ THEM DATAFILES, FILL THEM LISTS
cheapeats = Cheap.readlines()
notcheapeats = NotCheap.readlines()
veto = Veto.readlines()
atethere = AteThere.readlines()

#CHECK AGAINST LAST 5 PLACES EATEN AT
if len(atethere) > 5:
	AteThere.close()
	AteThere = open("atethere.txt",'w')
	i = 1
	for item in range(1,6):
		AteThere.write(atethere[i])
		i=i+1

#CLEAR THE DATAFILE, REWRITE LAST PLACES EATEN AT FROM LIST
AteThere.close()
NotAgain = open("atethere.txt","r")
notagain = NotAgain.readlines()

#CHECK CASES FOR CHEAP OR NOT CHEAT OPTIONS, CONCATENATE LISTS
if not bcheap and not ncheap:
	eats = cheapeats+notcheapeats
elif (bcheap):
	eats = cheapeats
elif (ncheap):
	eats = notcheapeats

#REMOVE ANYTHING IN LIST THAT WAS CHOSEN LAST 5 TIMES
eats = [x for x in eats if x not in notagain]

#IF JOSH IS COMING, SCRUB ENTRIES THAT HE DOESN'T LIKE
if (josh):
	eats = [x for x in eats if x not in veto]

#SEED RANDOM FUNCTION
secure_random = random.SystemRandom()

#SELECT LUNCH SPOT
lunch = secure_random.choice(eats)

#ADD CHOICE TO ATE THERE LIST
AteThere=open("atethere.txt","a")
AteThere.write(lunch)
AteThere.close()

#RUN AND TELL DAT TO CONSOLE
print lunch

#RUN AND TELL DAT TO SLACK
#DEFINE JSON MESSAGE:
data = json.dumps({"username": "LUNCH WILL BE AT:", "icon_emoji": ":hamburger:", "text": lunch})

#DEFINE SLACK WEBHOOK URL:
slackurl='https://hooks.slack.com/services/PUT/YOUR/URLHERE'

#Create CURL object
c = pycurl.Curl()
#Define CURL Paramters
c.setopt(c.URL, slackurl)
c.setopt(c.HTTPHEADER, [
			'Content-Type: application/json'
		]) 
c.setopt(c.POSTFIELDS, data)
c.setopt(pycurl.POST, 1)
#POST TO SLACK
c.perform()
