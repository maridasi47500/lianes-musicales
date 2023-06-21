# coding=utf-8
import sqlite3
from datetime import datetime
from jsoncontent import jsoncontent
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur

class audio_savepage(jsoncontent):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      self.content=""
      self.title=title
      self.params=title
      self.mysql("insert into recordings (filename,concert_id, date) values (?,?,?)",(params["myfilename"], params["myid"][0],str(datetime.now().date())))
      self.set_json({"result":"ok"})
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/audio_save")
      self.set_json({"result":"erreur"})
