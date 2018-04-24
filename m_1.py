import os
import sys
import webbrowser
from ldtp import *
import time
import subprocess
from subprocess import call


def katalog():
	

	print ("Przechodze na pulpit.\n")
	os.chdir("/home/danielubi/Pulpit/")
	print ("Tworze plik\n")
	subprocess.call("touch test", shell=True)


def otworz(target, opcja):
	if not opcja:
		webbrowser.open('https://'+target+'.com') 

def nmap(target, opcja):

	print len(opcja)



	if target != "hosty":

		porty = "1-65535"
		szybkosc = "-T4"

		if not opcja:
			subprocess.call("nmap -sF -n "+szybkosc+" -p "+porty+" -A -v -Pn --version-all -oX /home/danielubi/python_nauka/temp/"+target+".xml " + target, shell=True)
			subprocess.call("xsltproc /home/danielubi/python_nauka/temp/"+target+".xml -o /home/danielubi/python_nauka/temp/"+target+".html" , shell=True)
			print ("udalo sie")


		elif opcja[0] == "szybko":
			
			subprocess.call("nmap -sF -n -T4 -p 1-1000 -A -v -Pn --version-all -oX "+target+".xml " + target, shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True)
			print "szybko poszlo"

	 
		elif opcja[0] == "wolno":
			subprocess.call("nmap -sF -n -T1 -p 137-139,445,22123,22222  -A -v -Pn --version-all -oX "+target+".xml " + target, shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True) 	
			print "wolno szlo"


		elif opcja[0] == "":
			subprocess.call("nmap -sT -n -p 1-1000 -A -v -Pn --version-all -oX "+target+".xml " + target, shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True)
			print "dzien dobry"

	elif target == "hosty":

		if len(opcja) == 1:
			print (opcja[0])
			subprocess.call("nmap -sT -n -T3 -p 1-1000 -A -v -Pn --version-all -oX "+target+".xml -iL " + opcja[0], shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True)
			print ("udalo sie")

		elif opcja[1] == "szybko":
			subprocess.call("nmap -sT -n -T4 -p 1-1000 -A -v -Pn --version-all -oX "+target+".xml -iL " + opcja[0], shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True)
			print "szybko poszlo"

	 
		elif opcja[1] == "wolno":
			subprocess.call("nmap -sT -n -T1 -p 1-1000 -A -v -Pn --version-all -oX "+target+".xml -iL " + opcja[0], shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True) 	
			print "wolno szlo"


		elif opcja[1] == "":
			subprocess.call("nmap -sT -n -p 1-1000 -A -v -Pn --version-all -oX "+target+".xml -iL " + opcja[0], shell=True)
			subprocess.call("xsltproc "+target+".xml -o "+target+".html" , shell=True)
			print "dzien dobry"

 	else:
		print "Bledna komenda nmap"


def zadanie(argument):
	if argument == 'katalog':
		katalog(sys.argv[2], sys.argv[3:])
	elif argument == 'otworz':
		otworz(sys.argv[2], sys.argv[3:])
	elif argument == 'nmap':
		nmap(sys.argv[2], sys.argv[3:])
	else:
		print "Bledna komenda"


zadanie(sys.argv[1])