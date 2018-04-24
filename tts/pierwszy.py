# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tempfile import NamedTemporaryFile
import pyttsx3;
import gtts
from gtts import gTTS
import os
import subprocess
from subprocess import call
import vlc

# debian
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(
    '/etc/ssl/certs/',
    'ca-certificates.crt')


tts = gTTS(text='Ą, Ę, hehe żółw', lang='pl', slow=False)
f = NamedTemporaryFile(delete=False)
tts.write_to_fp(f)
#os.chdir('/home/danielubi/python_nauka/tts/')
#subprocess.call("ls -l" , shell=True)
player = vlc.MediaPlayer("czesc.mp3")

print (f.name)
player.play()
player.stop()
#f.close()