# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur

class concertspage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      self.content_from_file("myconcertshtml.html")
      self.title=title
      self.params=title
      sql="select * from concerts"
      sqlargs=()
      templatename="_concert.html"
      errormessage="pas de concerts"
      tablename="concerts"
      self.content+= self.display_collection_with_current_path(sql,sqlargs,templatename,errormessage,tablename)
      try:
        userid=params["userid"][0]
      except:
        userid=None
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/concerts")

