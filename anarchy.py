# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib
import re,string,os,shutil,urllib2,urllib3,subprocess
from urllib import urlopen
import requests,tempfile

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = kd = ke = kf = cl

print "Anarchy Team Bots"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
 A⃣n⃣a⃣r⃣c⃣h⃣y⃣ T⃣e⃣a⃣m⃣ B⃣o⃣t⃣s⃣ 
═══════════════════════
⇰ Me
⇰ /mid @
⇰ /apakah [Text]
⇰ /say [Text]
⇰ /pp @
⇰ /cover @
⇰ /midpict [MID]
⇰ /ambil qr: [MID]
⇰ /cek [Lurks]
⇰ /read [Lurkers]
⇰ /youtube [Text]
⇰ /music [CONTOH] ⇰ NAMA PENYANYI-JUDUL
⇰ /wikipedia [Text]
⇰ /lyric [Text]
⇰ /gn: [Text]
⇰ /gcreator:inv
⇰ /mimic on/off
⇰ /taget @
⇰ /del target @
⇰ /targetlist
⇰ /mimic target
⇰ /buka
⇰ /tutup
⇰ /infconfig
⇰ /system
⇰ /karnel
⇰ /cpu
⇰ Sp
⇰ Speedbot
⇰ /runtime
⇰ Contact:on/off
═══════════════════════
NEW TEAM ↓↓↓ 
A⃣n⃣a⃣r⃣c⃣h⃣y⃣ T⃣e⃣a⃣m⃣ B⃣o⃣t⃣s⃣ 
═══════════════════════ 
 """

helpAdmin ="""
A⃣n⃣a⃣r⃣c⃣h⃣y⃣ T⃣e⃣a⃣m⃣ B⃣o⃣t⃣s⃣ 
═══════════════════════
⇰ Glist
⇰ Admin on @
⇰ Qr:on/off
⇰ Blockinvite:on/off
⇰ Namelock:on/off
⇰ Protection:on/off
⇰ Cleanse.
⇰ Kill ban
⇰ Auto like:on/off
⇰ Mycop @
⇰ Mybackup
⇰ Bcast
⇰ Myname:
⇰ Mybio:
⇰ Ban @
⇰ Unban @
⇰ Clear ban
⇰ Adminlist
═══════════════════════
 """

KAC=[cl,ki,kk,kc,kd,ke,kf]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
admin = ["","",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
owner = ["YOUR MID",mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    "kickJoin":False,
    "alwayRead":False,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks For Add Contact Me line.me/ti/p/~@cmi5964z",
    "lang":"JP",
    "comment":"AutoLike by line.me/ti/p/~@cmi5964z",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
	aa = ""
	bb = ""
	strt = int(0)
	akh = int(0)
	nm = nama
	print nm
	for mm in nm:
		akh = akh + 3
		aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M","""+json.dumps(mm)+"),"""
		strt = strt + 4
		akh = akh + 1
		bb += "@x \n"
	aa = (aa[:int(len(aa)-1)])
	msg = Message()
	msg.to = to
	msg.from_ = admin
	msg.text = bb
	msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
	print msg
	try:
		cl.sendMessage(msg)
	except Exception as error:
		print error

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = kd.getGroup(op.param1)
				    except:
					try:
                                            G = ke.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        kd.updateGroup(G)
                                    except:
                                        try:
                                            ke.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Nama Grup dikunci")
                                        ki.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        kk.sendText(op.param1,"Wkwkkww mampus")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = kd.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kd.updateGroup(X)
                        Ti = kd.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Nmid:
                        G = kn.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kn.updateGroup(G)
                        Ticket = kn.reissueGroupTicket(op.param1)

                if op.param3 in Nmid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)

                if op.param3 in Omid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                if op.param3 in Pmid:
                    if op.param2 in Qmid:
                        X = kq.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                        kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kq.updateGroup(X)
                        Ti = kq.reissueGroupTicket(op.param1)
                if op.param3 in Qmid:
                    if op.param2 in Rmid:
                        X = kr.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                        kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kr.updateGroup(X)
                        Ti = kr.reissueGroupTicket(op.param1)
                if op.param3 in Rmid:
                    if op.param2 in Smid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Smid:
                    if op.param2 in Tmid:
                        X = kt.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)


                if op.param3 in mid:
                    if op.param2 in Fmid:
                        X = kf.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kf.updateGroup(X)
                        Ti = kf.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Gmid:
                        X = kg.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kg.updateGroup(X)
                        Ti = kg.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Omid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Pmid:
                        X = kp.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kp.updateGroup(X)
                        Ti = kp.reissueGroupTicket(op.param1)
#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,kk,kc,kd,ke,kf]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 55:
             if not op.param2 in Bots and admin:
                if wait["alwayRead"] == True:
                    try:
                         klist=[ki,kk,kc,kd,ke,kf]
                         kicker = random.choice(klist)
                         G = kicker.getGroup(op.param1)
                         kicker.kickoutFromGroup(op.param1,[op.param2])
                    except Exception, e:
                         print e
        if op.type == 17:
             if not op.param2 in Bots and admin:
                  if wait["kickJoin"] == True:
                     try:
                         klist=[ki,kk,kc,kd,ke,kf]
                         kicker = random.choice(klist)
                         G = kicker.getGroup(op.param1)
                         kicker.kickoutFromGroup(op.param1,[op.param2])
                     except Exception, e:
                         print e
                          
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.sendText(msg.to,"WAJIB ADD OA DI BAWAH UNTUK MELIHAT COMMAND SILAHKAN KETIK HELP")
			    cl.sendText(msg.contentMetadata = {'mid': "uf8c45b9ad0e8027405bdda71534a1eed"}
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if Bmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki,kk,kc,kd,ke,kf]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki,kk,kc,kd,ke,kf]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki,kk,kc,kd,ke,kf]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki,kk,kc,kd,ke,kf]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ticket = kk.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kd.updateGroup(X)
                    Ti = kd.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ticket = kc.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kd.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kd.updateGroup(X)
                    Ticket = kd.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ticket = ke.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kg.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kf.updateGroup(X)
                    Ticket = kf.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True



                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kf.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kf.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kn.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    kp.acceptGroupInvitationByTicket(op.param1,Ti)
                    kq.acceptGroupInvitationByTicket(op.param1,Ti)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kg.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kg.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kp.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kp.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kf.updateGroup(X)
                    Ti = kp.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                        
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        
                        wait["dblacklist"] = False
                        
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    #cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: Trevor ───")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: Trevor")
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help admin"]:
               if msg.from_ in admin:
                 print "\nHelp admin...."
                 if wait["lang"] == "JP":
                 	cl.sendText(msg.to, helpAdmin + "")
                 else:
                 	cl.sendText(msg.to,helpt)
            elif msg.text in ["Key","key","Help"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
                    
            elif ("/gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("/gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: "," ")
                klist=[kt,ks,kr,kq,kp,ko,kn,kj,kh,kg,kf,ke,kd,kc,kk,ki,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: "," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
                
            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)

            elif msg.text in ["Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Allgift","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
            elif "Myname:" in msg.text:
               if msg.from_ in owner or admin:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names Menjadi : " + string + "")
#==================================================
            elif '/lyric ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif '/wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == '/reboot':
               if msg.from_ in owner or admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == '/ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == '/system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == '/kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == '/cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif '/music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            elif msg.text in ["/Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["/cancel"]:
                if msg.toType == 2:
                    klist=[kj,kh,kg,kf,ke,kd,kc,kk,ki,kn,ko,kp,kq,kr,ks,kt]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kicker.sendText(msg.to,"No one is inviting")
                        else:
                            kicker.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kicker.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kicker.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["/buka"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["/tutup"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == '/ginfo':
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text in ["Glist"]:
               if msg.from_ in owner or admin:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)
            elif "Myid" == msg.text:
                cl.sendText(msg.to,msg.from_)			
            elif "/say " in msg.text:
				bctxt = msg.text.replace("/say ","")
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
				cl.sendText(msg.to,(bctxt))
#======================================
            elif "Tl: " in msg.text:
                tl_text = msg.text.replace("Tl: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Protect:on","Protect on"]:
               if msg.from_ in owner or admin: 
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:off","Qr off"]:
               if msg.from_ in owner or admin:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:on","Qr on"]:
               if msg.from_ in owner or admin:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:off","Protect off"]:
               if msg.from_ in owner or admin: 
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
               if msg.from_ in owner or admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
               if msg.from_ in owner or admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
#=======================================================
            elif msg.text in ["Sensi on","S:on"]:
              if msg.from_ in owner:   
                 wait["alwayRead"] = True
                 cl.sendText(msg.to,"Sensi on Tuan")
            elif msg.text in ["Sensi off","S:off"]:
              if msg.from_ in owner:
                 wait["alwayRead"] = False
                 cl.sendText(msg.to,"Sensi off Tuan")
            elif msg.text in ["Kickjoin on"]:
               if msg.from_ in owner:  
                 wait["kickJoin"] = True
                 cl.sendText(msg.to,"Kita kick yang join")
            elif msg.text in ["Kickjoin off"]:
               if msg.from_ in owner:
                 wait["kickJoin"] = False
                 cl.sendText(msg.to,"Selesai Tugas Astro")
#=======================================================
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Protect invite on")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Protect invite off")
				except:
					pass
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " Done")
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif msg.text in ["K on","Contact:on","Contact on","K:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on"]:
               if msg.from_ in admin:    
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off"]:
               if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave:on","Auto leave on","Auto leave:on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Leave:off","Auto leave off","Auto leave:off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")

            elif msg.text in ["共有:オン","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["共有:オフ","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Auto like:on"]:
              if msg.from_ in owner or admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Auto like:off"]:
              if msg.from_ in owner or admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")


            elif msg.text in ["Set Group"]:
            	print "Setting pick up..."
                md = "Settings\n"
                
                
                if wait["likeOn"] == True: md+="��Auto like : on\n"
                else:md+="��Auto like : off\n"
                if wait["copy"] == True: md+="��Mimic : on\n"
                else:md+="��Mimic : off\n"
                if wait["winvite"] == True: md+="��Invite : on\n"
                else:md+="��Invite : off\n"
                if wait["pname"] == True: md+="��Namelock : on\n"
                else:md+="��Namelock : off\n"
                if wait["contact"] == True: md+="��Contact : on\n"
                else: md+="��Contact : off\n"
                if wait["autoJoin"] == True: md+="��Auto join : on\n"
                else: md +="��Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="��Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "��Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="��Auto leave : on\n"
                else: md+="��Auto leave : off\n"
                if wait["timeline"] == True: md+="��Share : on\n"
                else:md+="��Share : off\n"
                if wait["clock"] == True: md+="��Clock Name : on\n"
                else:md+="��Clock Name : off\n"
                if wait["autoAdd"] == True: md+="��Auto add : on\n"
                else:md+="��Auto add : off\n"
                if wait["commentOn"] == True: md+="��Comment : on\n"
                else:md+="��Comment : off\n"
                if wait["Backup"] == True: md+="��Backup : on\n"
                else:md+="��Backup : off\n"
                if wait["qr"] == True: md+="��Protect QR : on\n"
                else:md+="��Protect QR : off\n"
                if wait["protectionOn"] == True: md+="��Protection : on\n\n"+ datetime.today().strftime('%H:%M:%S')
                else:md+="��Protection : off\n\n"+ datetime.today().strftime('%H:%M:%S')
                cl.sendText(msg.to,md)
#========================================
#------------------------------------------------
            elif msg.text in ["/gcreator:inv"]:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif msg.text in ["Backup:on","Backup on"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["/rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Add:on","Auto add on","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah on Bosqu")
            elif msg.text in ["Add:off","Auto add off","Auto add:off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah off Bosqu")
#========================================
#========================================
            elif "Message: " in msg.text:
                wait["message"] = msg.text.replace("Message: ","")
                cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message: " in msg.text:
                wait["message"] = msg.text.replace("Add message: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Message"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Comment: " in msg.text:
                c = msg.text.replace("Comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Comment on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Comment off","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Comment"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["/getqr"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        uye.updateGroup(x)
                    gurl = uye.reissueGroupTicket(msg.to)
                    uye.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================
            elif msg.text.lower() == '/respons':
                profile = cl.getProfile()
                text = profile.displayName + "Anarchy"
                cl.sendText(msg.to, text)
            elif "/ambil qr: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("/ambil qr: ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
#========================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif "/cover @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("/cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "/midpict " in msg.text:
                umid = msg.text.replace("/midpict ","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "/pp " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("/pp ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")

#===============================================
            elif msg.text in ["Speedbot"]:
                start = time.time()                   
                cl.sendText(msg.to, "「SPEED BOTS ANARCHY LOADING.....」")                    
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed asli executed"

             elif msg.text.lower() == '/runtime':
                 eltime = time.time() - mulai
                 van = "Bot sudah berjalan selama "+waktu(eltime)
                 cl.sendText(msg.to,van)
#===============================================
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in owner or admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#=================================================
            elif msg.text in ["Mybackup"]:
              if msg.from_ in owner or admin:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#=================================================
            elif msg.text == "/cek":
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "/read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik kau dulu Cek baru Sider")
						
#========================================
           elif "Bcast " in msg.text:
               if msg.from_ in admin or owner:
                   bc = msg.text.replace("Bcast ","")
                   gid = cl.getGroupIdsJoined()
                   for i in gid:
                       cl.sendText(i,"======[BROADCAST]======\n\n"+bc+"\n\n#BROADCAST!!")
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
            elif "Cleanse." in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse.","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    cl.sendText(msg.to,"☠ Just Casual Some Cleansing. ☠")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    ks.sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Dark Spear")
                    else:
                        for target in targets:
                          if target not in Bots:
                            try:
                                klist=[cl,ki,kk,kc,kd,ke,kf]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kl.sendText(msg.to,"Group Cleansed")
#================================================
#========================================
            elif msg.text.lower() == ["welcome","Wc","Welkam","Welcome"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#=======================================
#-------------------Fungsi spam start--------------------------
            elif "/spam change: " in msg.text:
                wait["spam"] = msg.text.replace("/spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "/spam add: " in msg.text:
                wait["spam"] = msg.text.replace("/spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "/spam: " in msg.text:
                strnum = msg.text.replace("/spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

#-------------------Fungsi spam finish----------------------------
#-----------------------------------------------
#-----------------------------------------------
            elif "/apakah " in msg.text:
                tanya = msg.text.replace("/apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi"," Capek aku pantek!")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
#================================================
#===============================================
#=================================================
            elif "/spam " in msg.text:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif "/mid @" in msg.text:
                _name = msg.text.replace("/mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#========================================
            elif msg.text in ["/jonall"]:
                if msg.from_ in owner or admin: 
					G = cl.getGroup(msg.to)
					info = cl.getGroup(msg.to)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ticket = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kk.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kd.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ke.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					kf.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					cl.updateGroup(G)

            elif msg.text in ["Pergi"]:                
                 if msg.toType == 2:                
                   X = cl.getGroup(msg.to)
                 try:
                     ki.leaveGroup(msg.to)
                     kk.leaveGroup(msg.to)
                     kc.leaveGroup(msg.to)
                     kd.leaveGroup(msg.to)
                     ke.leaveGroup(msg.to)
                     kf.leaveGroup(msg.to)
                 except:
                       pass
                    
            elif msg.text in ["/out"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     cl.sendText(msg.to,"Bye Bye")
                     cl.leaveGroup(msg.to)
                except:
                     pass
            elif "Mk:" in msg.text:
                  if msg.from_ in admin:                                        
                       mk0 = msg.text.replace("Hallo:","")
                       mk1 = mk0.lstrip()
                       mk2 = mk1.replace("@","")
                       mk3 = mk2.rstrip()
                       _name = mk3
                       gs = ki.getGroup(msg.to)
                       targets = []
                       for h in gs.members:
                           if _name in h.displayName:
                              targets.append(h.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                               try:
                                 if msg.from_ not in target:
                                   ki.kickoutFromGroup(msg.to,[target])
                               except:
								   random.choice(KAC).kickoutFromGroup(msg.to,[target])
								
#==========================================
            elif "/youtube " in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
#==========================================
            elif msg.text in ["/mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["/mimic off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["/targetlist"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "/mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("/mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "/target @" in msg.text:
                        target = msg.text.replace("/target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "/del target @" in msg.text:
                        target = msg.text.replace("/del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#==========================================
            elif msg.text in ["Killban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Dasar Kamvret")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc,kd,ke,cl,kf]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Dark Spear" in msg.text:
                if msg.from_ in admin:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    klist=[ki,kk,kc,kd,ke,cl,kf]
                    kicker = random.choice(klist)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    kicker.sendText(msg.to,"Dark Spear!")
                    kicker.sendText(msg.to,"Dark Spear!")
                    kicker.sendText(msg.to,"Dark Spear!")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                               klist=[ki,kk,kc,kd,ke,cl,kf]
                               kicker = random.choice(klist)
                               kicker.kickoutFromGroup(msg.to,[target])
                               print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Dark Spear Terus")
                                kk.sendText(msg,to,"Dark Spear Terus")
                            pass
            elif ("Keluar " in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")
							
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kl.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
							
            elif "Tk " in msg.text:
                       nk0 = msg.text.replace("Tk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       km.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    km.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    km.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Bunuh " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")            	    
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kk.sendText(msg.to,"Success Boss")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear ban"]:
              if msg.from_ in owner:
				wait["blacklist"] = {}
				cl.sendText(msg.to,"clear")
				
            elif msg.text in ["Ban"]:
               if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
			
            elif msg.text in ["Banlist"]:
               if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
               if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]: 
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                        kd.kickoutFromGroup(msg.to,[jj])
                        ke.kickoutFromGroup(msg.to,[jj])
                        kf.kickoutFromGroup(msg.to,[jj])
                        
                    cl.sendText(msg.to,"Blacklist user")
            elif "Admin on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"succes add to adminlist")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
            elif msg.text.lower() == 'Adminlist':
              if msg.from_ in admin:
                if admin == []:
                       cl.sendText(msg.to,"The adminlist is empty")
                else:
                        cl.sendText(msg.to,"loading...")
                        mc = ""
                        gh = ""
                        for mi_d in owner:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
		        for mi_d in admin:
			    gh += "->" +cl.getContact(mi_d).displayName + "\n"				
                        cl.sendText(msg.to,"════════════════\nOWNER\n════════════════\n\n" + mc + "\n════════════════\nADMIN\n════════════════\n\n" + gh +"\n════════════════\n")
                        print "[Command]Stafflist executed"
        
#=============================================
#=============================================
#=============================================
            elif "Info @" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#=============================================
            elif msg.text in ["Speed","Sp","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Loading")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sSPEEDBOTS" % (elapsed_time))
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Bl " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned Bos")
                   except:
                      pass        
#============================================
            #elif msg.text in ["Clear"]:
                #if msg.toType == 2:
                    #group = cl.getGroup(msg.to)
                    #gMembMids = [contact.mid for contact in group.invitee]
                    #for _mid in gMembMids:
                        #random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    #cl.sendText(msg.to,"Clear boss!!!")
            elif msg.text in ["/tagall"]:
				if msg.toType == 2:
					if msg.contentType == 0:
						group = cl.getGroup(msg.to)
						nama = [contact.mid for contact in group.members]
						nm1, nm2, jml = [], [], len(nama)
						if jml <= 100:
							mention(msg.to, nama)
						if jml > 100 and jml < 200:
							for i in range(0.99):
								nm1 += [nama[i]]
							mention(msg.to, nm1)
							for j in range(100, len(nama)-1):
								nm2 += [nama[j]]
							mention(msg.to, nm2)
						if jml > 200 and jml < 300:
							for i in range(0.99):
								nm1 += [nama[i]]
							mention(msg.to, nm1)
							for j in range(100, 199):
								nm2 += [nama[j]]
							mention(msg.to, nm2, jml)
							for k in range(200, len(nama)-1):
								nm3 += [nama[k]]
							mention(msg.to, nm3, jml)
						if jml > 300:
							print " terlalu banyak mem 300+"
						cnt = message()
						cnt.text =  "Done:"+str(jml)
						cont.to = msg.to
						cl.sendMessage(cnt)
					
#===========================================
        if op.param3 == "Namelock on":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = "ua87810961d8822889217ef0eb64262cf"
			if op.param2 in OWN:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				kd.kickoutFromGroup(op.param1,[op.param2])
				ke.kickoutFromGroup(op.param1,[op.param2])
				kf.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#===========================================
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n╠" + Name
						wait2['ROM'][op.param1][op.param2] = "╠" + Name
				else:
					cl.sendText
            except:
                pass
						
						
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
