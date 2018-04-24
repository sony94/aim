
import os
import vlc
import sys
import webbrowser
from pygame import mixer


def pulpit():
    print ("Przechodze na pulpit.\n")

def google():
    webbrowser.open('http://google.com')  # Go to example.com



def argumenty(arg, cos):
	print cos
	print "dzial"
	print arg
	#print opcja
	return cos

def nmap(target, opcja):
	opcja = argumenty("szybko", opcja)

	print "udalo sie" 
	print opcja
		



def numbers_to_strings(argument):
    switcher = {
        0: pulpit(),
        1: google(),
    }


nmap(sys.argv[2], sys.argv[3:])