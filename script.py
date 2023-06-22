# coding: utf-8 -*-
from audio_save import audio_savepage
import audio_save
import random
import string
global Program
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str



global audio_save
from audio_save import audio_savepage
import audio_save
global audio_save
from concert import concertpage
import concert
global concert
from about import aboutpage
import about
global about
from concerts import concertspage
import concerts
global concerts
from home import homepage
import home
global home
from redirect import redirectaction
def findaudio(n):
  return n.split("/")[0] == "audio"
def findimages(n):
  return n.split("/")[0] == "image"
def returnend(n):
  return n.split("/")[1]




from directory import directory
import json
import psutil
import logging
import binascii
import random as rand
import smtplib
import datetime
import sys
import requests
from jsoncontent import jsoncontent
global session
import sqlite3
global copy
global reloadmymodules
global connection
global get_file
global switcher
__mots__={
    "/audio_save":{"partiedemesmots":"audio_save"},
    r"/concert/\d+":{"partiedemesmots":"concert"},
    "/about":{"partiedemesmots":"about"},
    "/concerts":{"partiedemesmots":"concerts"},
    "/":{"partiedemesmots":"home"},
}

myredirect=["codepage"]
switcher={
'html':'text/html',
'css':'text/css',
'json':'application/json',
'js':'text/javascript',
'jpg':"image/jpg",
'jpeg':"image/jpeg",
'wav':"audio/wav",
'png':"image/png",
'gif':"image/gif",
'ico':'image/vnd.microsoft.icon'
}


connection = sqlite3.connect("mesburgers1.db")

# cursor
global crsr
crsr = connection.cursor()

myusers=crsr.execute("PRAGMA table_info([users])")
table_users = myusers.fetchall()
global force_to_unicode
global decode_any_string
def decode_any_string(text):
    try:
        print("..."+text[0:60]+"...")
        return force_to_unicode(text)
    except UnicodeEncodeError as e:
        print(type(e))
        print('gerer cette erreur')
        return text.encode('utf-8')
    except UnicodeDecodeError as e:
        print(type(e))
        print('gerer cette erreur')
        return text

def force_to_unicode(text):
    "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding"
    return text if isinstance(text, unicode) else text.decode('utf-8')
session = requests.Session()
try:
    if len(sys.argv) == 4: 
        session.current_user=[sys.argv[3]]
except:
    print("no arg")
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from os.path import exists
from urlparse import urlparse, parse_qs
import os



global path1
path1=os.getcwd()
import codecs
import re

global Program
global get_file
global get_file_dir

global mycard


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

import random
def render_figure(pathname,Program):
    try:
        global path1
        path1=os.getcwd()
        print(pathname,Program,"<== pathname, pgrm")
        Program.set_filename(pathname)
        print("render figure")
        print('ok')
        p1=Program.get_path
        p2=Program.get_filename
        print("okdac")
        #print(p1())
        print("okokdac")
        #print(p2())
        #print(p1()+p2())
        #print('dac')
        title=Program.get_title
        try:
            print(session.current_user)
            Program.set_path("./mespages")
            h=get_file("mynavsignedin.html")
            Program.set_menu(h.read())
        except:
            h=open("./mespages/mynav.html",'r')
            Program.set_menu(h.read())
        header=Program.get_header
        content=Program.get_content
        footer=Program.get_footer
        layout=Program.get_layout()
        print(Program.__class__.__name__, "my html page action name")
        print((Program.__class__.__name__ in myredirect), "my redirect is like codepage")
        print(Program.get_redirect(), "my html redirect url link")
        print(Program.get_redirect() != "", "my redirect is not ''")

        if isinstance(Program,jsoncontent):
            html=Program
        elif Program.__class__.__name__ in myredirect and Program.get_redirect() != "":
            html=redirectaction(Program.get_redirect())
        elif isinstance(Program,redirectaction):
            html=Program
        elif layout == False:
            print("content")
            try:
                html=decode_any_string(content())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=content().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                html=content()
        else:
            title=title()
            css=Program.get_css()
            body=""
            js=""
            header1=""
            main1=""
            footer1=""
            print("header")
            try:
                header1+=decode_any_string(header().decode('utf-8'))
            except UnicodeEncodeError as e:
                print(type(e)[0:50])
                print('header gerer cette erreur')
                header1=header().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e)[0:50])
                print('gerer cette erreur')
                header1=header()
            print("content")
            try:
                main1=decode_any_string(content().decode('utf-8'))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                main1=content().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                main1=content()
            print("footer")
            print("type footer")

            print(type(force_to_unicode(footer())))

            try:
                footer1=decode_any_string(footer().decode('utf-8'))
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                footer1=footer().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                footer1=footer()
            print("footer ajouté")
            print("type menu")
            print(type(Program.get_menu()))
            try:
                body+=force_to_unicode(Program.get_menu())
            except UnicodeEncodeError as e:
                print(type(e))
                print('gerer cette erreur')
                body+=Program.get_menu().encode('utf-8')
            except UnicodeDecodeError as e:
                print(type(e))
                print('gerer cette erreur')
                body+=Program.get_menu()
            print("meu ajouté")
            j=open(path1+"/mespages/jstag.html").read()    
            js+=j % ("/js/jquery.js",)
            #print(js)
            js+=j % ("/js/js.js",)
            #print(js)
            print(Program.get_js(),"=js")
            js+=Program.get_js().decode('utf-8')

            j=open(path1+"/myapppage.html","r").read().decode('utf-8')
            #print(j)
            #print(title.decode('utf-8'),"=title")
            #print(css.decode('utf-8'),"=css")
            #print(js.decode('utf-8'),"=js")
            #print(header1.decode('utf-8'),"header1")
            #print(main1,"=main1")
            print("erreur")
            print(footer1[0:30],"=footer")
            print(js.decode('utf-8')[0:30],"==js")
            print(js.decode('utf-8')[-30:-1],"==fin js")
            print(main1.decode('utf-8')[0:30],"==main1")
            print(header1[0:30],"==js")
            print("erreur")
            html=j % (title.decode('utf-8'),css.decode('utf-8'),header1,main1.decode('utf-8'),footer1,js)
            #print(html)
            print("fin balise")
        #mychemin=p1()+("" if (p1()[-1]=="/" or p2()[0] == "/") else "/")+p2()
        #print(mychemin)
        #print(type(html))
        if isinstance(html,str):
            s1=html
        elif isinstance(html,directory):
            s1=html
        else:
            s1=html.encode('utf-8')
        #Program.sethtml(s1)    
        return s1
    except Exception as e:
        print(e,'erreru')


# SQL command to create a table in the database
f=open(path1+"/mespages/dump.sql",'rb')
sql_command = f.read().decode('utf-8')
global myroutes

for sql in sql_command.split(";"):
    print(sql)
    try:
        crsr.execute(sql)
    except Exception as e:
        print(e)

connection.commit()




def reloadmymodules(params = None):
    reload(audio_save)
    reload(audio_save)
    reload(concert)
    reload(about)
    reload(concerts)
    reload(home)
def copy(params = None):
    #restart_program()
    #os.execv(sys.argv[0], sys.argv)
    #os.execv(sys.executable, ['python'] + sys.argv)
    os.system("cp "+path1+"/mespages/js.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/css/css.css "+path1+"/css/css.css")
    os.system("cp "+path1+"/mespages/css/signin.css "+path1+"/css/signin.css")
    os.system("cp "+path1+"/mespages/css/*.css "+path1+"/css")
    os.system("cp "+path1+"/mespages/*.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/userconnecte.js "+path1+"/js")
    os.system("cp "+path1+"/mespages/signin.js "+path1+"/js")

#Program.path("./")


global erreur404
def erreur404(params = None):
    try:
        print("erreur 202")
        Program.set_path("./mespages")
        j=get_file("404.html")
        print("my file")
        text=j.read()
        Program.set_path("./css")
        Program.add_css("404.css")

        Program.edit_title("Page non trouvée")
        Program.set_content(text)
        print("my path")
        set_my_header("")
        print("my footer")
        set_my_footer("")
        print("my path1")
        Program.set_path("./erreur")
        print("my path")
        return render_figure("404.html")

    except Exception as e:
        print("errur my 404",e)
global addgiftcard
def addgiftcard(params = None):
    Program.set_path("./mespages")
    j=open(Program.get_filename_path("addgiftcard.html"),'rb')
    Program.add_css("signin.css")
    Program.add_js("addcard.js")
    Program.add_css("addgiftcard.css")
    text=j.read().decode('utf-8')
    Program.set_content(force_to_unicode(text))
    Program.set_path("./mespages")
    k=open(Program.get_filename_path("headeroverlay.html"),'rb')
    headertext=k.read().decode('utf-8')
    Program.set_header(headertext)

    return render_figure("ma page.html")





def homefunc(params):
  Program=homepage("./myhomedirectory","super website",params)
  return render_figure("myhomehtml.html",Program)


def concertsfunc(params):
  Program=concertspage("./myconcertsdirectory","super website",params)
  return render_figure("myconcertshtml.html",Program)


def aboutfunc(params):
  Program=aboutpage("./myaboutdirectory","super website",params)
  return render_figure("myabouthtml.html",Program)


def concertfunc(params):
  Program=concertpage("./myconcertdirectory","super website",params)
  return render_figure("myconcerthtml.html",Program)


def audio_savefunc(params):
  Program=audio_savepage("./myaudio_savedirectory","super website",params)
  return render_figure("myaudio_savehtml.html",Program)


def audio_savefunc(params):
  Program=audio_savepage("./myaudio_savedirectory","super website",params)
  return render_figure("myaudio_savehtml.html",Program)

class S(BaseHTTPRequestHandler):
    def _mon_erreur(self,e):
        print("erreur get",e)
        file="404.html"
        dir="./erreur"
        Program.set_path(dir)
        k= open(Program.get_path()+"/"+file,'rb').read()
        print(k)
        self._set_headers(switcher.get("html"))
        self.wfile.write(force_to_unicode(k.decode('utf-8')))
    def _mon_erreur_text(self,e):
        print("erreur get",e)
        file="404.html"
        dir="./erreur"
        Program.set_path(dir)
        k= "mon erreur"
        print(k)
        self._set_headers(switcher.get("html"))
        self.wfile.write(force_to_unicode(k.decode('utf-8')))
    def _set_headers(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()
    def set_header(self,myheader='text/html'):
        self.send_response(200)
        self.send_header('Content-type', myheader)
        self.end_headers()
    def do_GET(self):
        print("=========new route GET=========["+self.path+"]===========")
        try:
            copy()
            reloadmymodules()
            urlpath=self.path
            myurlpath=urlpath.split("?")[0]
            routetrouve=None
            #f = open("index.html", "r")
            query_components = parse_qs(urlparse(urlpath).query)
            try:
                query_components["userid"]=[session.current_user[0]]
                print("-- user connecté --")
            except:
                print("aucun user connecté")
            print('path',myurlpath , query_components,"what params")
            query_components["routeids"]=re.findall(r'\d+', myurlpath)
            #x=searchmyparams(query_components,myurlpath)
            for path in myroutes:
                #simple=path.split("?")[0]
                #print("le chemin est %s et la route %s" % (myurlpath,path))
                #print("la route a été trouvée ?%r" % (re.match(path, myurlpath) != None))
                mysimplefunc=myroutes[path]


                kk=re.match(path, myurlpath)
                if kk:
                    for x in range(len(kk.groups())):
                        print(kk.group(0),x,kk.group(x))
                        query_components["param"+str(x)] = kk.group(x)
                    routetrouve=path
                    code=mysimplefunc(query_components)
                    #code=Program.gethtml()
                    print("le code récupéré")    
                    break

            if routetrouve:
                print("La route a été trouvée ? %r, c'est %s" % (routetrouve is not None, routetrouve))
            else:
                print("La route n'a pas été trouvée ?  %r" % (routetrouve is None,))
            try:
                print(isinstance(code,redirectaction))
            except:
                code=""
            if isinstance(code,redirectaction):
                self.send_response(301)
                myred=code.get_redirect()
                print("vous serez redirigée à %s " % myred)
                self.send_header('Location',myred)
            elif isinstance(code,jsoncontent):
                print("return json")
                data=code.get_json()
                code.set_json(None)

                self._set_headers(switcher.get("json"))
                self.wfile.write(str(data).replace("'",'"'))
            elif myurlpath.split(".")[-1] in ["css","scss"]:
                print("le mimetype est %s et la réponse est %s" % ("css",200))
                self._set_headers(switcher["css"])

                code=open(os.getcwd()+myurlpath, "rb").read().decode('utf-8')
                self.wfile.write(code)
            elif myurlpath.split(".")[-1] in map(returnend, filter(findaudio,switcher.values())):
                print("le mimetype est %s et la réponse est %s" % ("audio",200))
                self._set_headers(switcher[myurlpath.split(".")[-1]])

                code=open(os.getcwd()+myurlpath, "rb").read()
                self.wfile.write(code)
            elif myurlpath.split(".")[-1] in map(returnend, filter(findimages,switcher.values())):
                print("le mimetype est %s et la réponse est %s" % ("png",200))
                self._set_headers(switcher[myurlpath.split(".")[-1]])

                code=open(os.getcwd()+myurlpath, "rb").read()
                self.wfile.write(code)
            elif myurlpath.split(".")[-1] in ["js"]:
                print("le mimetype est %s et la réponse est %s" % ("js",200))
                self._set_headers(switcher["js"])

                code=open(os.getcwd()+myurlpath, "rb").read()
                self.wfile.write(code)
            elif routetrouve:
                
                try:
                    dic=__mots__[routetrouve]
                    if dic["partiedemesmots"]:
                        print("une partie de mes mots a été cherchée?vrai")
                        try:
                            if code.index(dic["partiedemesmots"]):
                                print("la route est html")

                                print("le mimetype est %s et la réponse est %s" % ("html",200))
                                self._set_headers(switcher["html"])


                                self.wfile.write(code)
                                print("les mots ed la page ont été reconnus?vrai")
                        except:
                            print("la route nest pas html")
                except Exception as e:
                        print("les mots ed la page ont été reconnu?faux",code)
                        self._mon_erreur_text(e)
            else:
                self._mon_erreur("ni une erreur ni css js ou image")
        except UnboundLocalError as e:
            self._mon_erreur(e)
        return

    def do_HEAD(self):
        self._set_headers()
    def deal_myid_data(self,b):
        boundary = b
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False, "Content NOT begin with boundary","")
        line = self.rfile.readline()
        remainbytes -= len(line)
        fn = re.findall(r'Content-Disposition.*name="myid"([\d.]*\d+)', line)
        if not fn:
            return (False, "Can't find out myid...","")
        print(self.path)

        myfilename=get_random_string(8)+".wav"
        
        fn = "./myfilename"
        value=""
        print(fn)
        line = self.rfile.readline()
        remainbytes -= len(line)
        line = self.rfile.readline()
        remainbytes -= len(line)
        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?","")
                
        preline = self.rfile.readline()
        remainbytes -= len(preline)
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith('\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, "number '%s' found success!" % preline,preline)
            else:
                out.write(preline)
                preline = line
        return (False, "Unexpect Ends of data.","")
    def deal_post_data(self):
        boundary = self.headers.plisttext.split("=")[1]
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            return (False, "Content NOT begin with boundary","","")
        line = self.rfile.readline()
        remainbytes -= len(line)
        fn = re.findall(r'Content-Disposition.*name="recording"; filename="(.*)"', line)
        if not fn:
            return (False, "Can't find out file name...","","")
        print(self.path)
        path = "./uploads"

        myfilename=get_random_string(8)+".wav"
        
        fn = os.path.join(path, myfilename)
        print(fn)
        line = self.rfile.readline()
        remainbytes -= len(line)
        try:
            out = open(fn, 'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?","","")
        preline = self.rfile.readline()
        remainbytes -= len(preline)
        recordingnotfound=True
        myidnotfound=True
        inline="recording"
        myparams=["myid","recording"]
        params=[]
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            print("boundary in line %s" % (boundary in line))
            print("Content-Disposition in line %s" % ("Content-Disposition" in line))
            print("recording in line %s" % ("recording" in line))
            print("myid in line %s" % ("myid" in line))
            print("=====")
            if boundary in line:
                print("preline : %s" % preline)
                print("out : %s" % out)

                if inline=="recording":
                     preline = preline[0:-1]
                     if preline.endswith('\r'):
                         preline = preline[0:-1]
                     out.write(preline)
                     out.close()
                     out=""
                     print("recording in line")
                     params.append(myfilename)

                elif inline =="myid":
                     myid=re.search(r'(\d+)', preline).group(1)
                     params.append(myid)
                     myidnotfound=False
                if len(myparams)==len(params):
                    return (True, "upload %s and find my id %s success!" % tuple(params))+tuple(params)
            elif "recording" in line:
                inline="recording"
                out.write(preline)
                preline = line
            elif "myid" in line:
                inline="myid"
                out+=preline
                preline = line
            elif inline == "recording":
                inline="recording"
                out.write(preline)
                preline = line
            elif inline == "myid":
                inline="myid"
                out+=preline
                preline = line


        return (False, "Unexpect Ends of data.","","")
    def do_POST(self):
        print("=========new route POST====================")
        try:
            if self.path=="/audio_save":
              r, info,myfilename,myid = self.deal_post_data()
              print(info,myfilename)
              query_components={"myid":myid, "myfilename":myfilename}
            else:
              self.data_string = self.rfile.read(int(self.headers['Content-Length']))
              query_components = parse_qs(self.data_string)
            print("tyui")
            Program=directory("Burger King")
            Program.set_url(self.path)
            urlpath=Program.get_url()
            try:
              query_components["routeids"]=re.findall(r'\d+', urlpath)
            except:
              print("azazaz")
            print("tyui")
            x=query_components
            fields=query_components
            print("tyui")
            try:
                query_components["userid"]=[session.current_user[0]]
                print("-- user connecté --")
            except:
                print("aucun user connecté")
            print("in post method")
            myurlpath=urlpath.split("?")[0]
            print(myurlpath)
            try:
                print('my path')
                print(myurlpath)
                print("tyui")
                print(route_post.get(myurlpath))
                if route_post.get(myurlpath) is not None:
                    print("route trouve")
                    print(fields)
                    res=route_post.get(myurlpath)(query_components)
                    if isinstance(res,str):
                        codehtml = res
                        print("is code HTML")
                        #print(codehtml)
                    elif isinstance(res,jsoncontent):
                        Program=res
                    elif isinstance(res,directory):
                        print("is object")
                        print(res)
                        Program=res
                        try:
                            if isinstance(Program,setuserpage):
                                session.current_user=Program.get_session()
                        except:
                            print("pas de session")
                        if Program.get_current_user() is not None and Program.get_current_user() != ():
                            print("current_user")
                            print(Program.get_current_user())
                            session.current_user=Program.get_current_user()
            except KeyError:
                print("erreur 6")


        #self.data_string = params
            urlpath=self.path
            print("redirect post:")
            print(Program.get_redirect())
            copy()
            reloadmymodules()
            #render_pages()
            #myaccountinfo()
            #home()
            try:
                mytype=Program.get_mimetype() or self.path.split(".")[-1]
                print(urlpath)
                print("my type")
                print(mytype)
                print("Program.get json")
                print(Program.get_json() is not None)
                print(Program.get_json())
                print(route_post.get(myurlpath))
            except:
                print("no mimetype(redirect)")
            print("redirect")
            if Program and isinstance(Program,redirectaction):
                myred=Program.get_redirect()
                print("vous serez redirigée à %s " % myred)

                self.send_response(301)
                self.send_header('Location',myred)
            elif isinstance(Program,jsoncontent):
                print("return json")
                data=Program.get_json()
                Program.set_json(None)

                self._set_headers(switcher.get("json"))
                self.wfile.write(str(data).replace("'",'"'))
            elif mytype is not None:
                if mytype != "html":
                    if switcher.get(mytype) is not None:
                        if myroutes.get(urlpath) is not None:
                            self._set_headers(switcher.get(mytype))
                            self.wfile.write(codehtml)
            else:
                print(mytype)
                self._set_headers(switcher.get(mytype))
                self.wfile.write(codehtml)
            session.neworder=None
            self.end_headers()
        except UnboundLocalError as e:
            code=directory("Burger King")
            code.__class__ = erreur
            code.set_erreur(str(e))
            code.set_title({marouteget})

            self._set_headers(switcher.get("html"))
            self.wfile.write(k.read().decode('utf-8'))

        return


def run(server_class=HTTPServer, handler_class=S, port=8000,host="localhost"):
    server_address = ('', port)
    print("run erver")
    httpd = server_class(server_address, handler_class)
    #print 'http://localhost:8000'
    if len(argv) == 2:
        print('http://'+host+':'+argv[1])
    else:
        print('http://'+host+':'+str(port))
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
#rewards()
#offers()


global route_post
myroutes = {

r"/concert/\d+":concertfunc,
"/about":aboutfunc,
"/concerts":concertsfunc,
"/":homefunc,
}
global menu
# POST routes
route_post={
"/audio_save":audio_savefunc,

}
if len(argv) == 3:
    run(port=int(argv[1]),host=argv[2])
elif len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
