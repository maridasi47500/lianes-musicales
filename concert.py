#  coding=utf-8
import sqlite3
import traceback
import sys
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur

class concertpage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)

      self.title=title
      print(params)
      sql="select * from concerts where id = ?"
      sqlargs=(params["routeids"][0])
      templatename="_concert.html"
      errormessage="pas de concerts"
      tablename="concerts"


      x1=self.display_collection_with_current_path(sql,sqlargs,templatename,errormessage,tablename)
      sql="select * from recordings where concert_id = ?"
      sqlargs=(params["routeids"][0])
      templatename="_recording.html"
      errormessage="pas de concerts"
      tablename="recordings"


      x2=self.display_collection_with_current_path(sql,sqlargs,templatename,errormessage,tablename)
      self.myyield(x1+x2)
      self.content_from_yield("myconcerthtml.html")
      self.params=title
      self.add_css("myconcert.css")
      self.add_js("myconcert.js")
      self.add_js_link("https://code.jquery.com/jquery-3.7.0.js")
      self.add_js_link("/js/audiodisplay.js")
      self.add_js_link("/js/recorderjs/recorder.js")
      self.add_js_link("/js/main.js")

      try:
        userid=params["userid"][0]
      except:
        userid=None
    except Exception as e:
      self.__class__ = erreur
      #self.set_erreur(str(e))

      print(traceback.format_exc())
      self.set_erreur(str(traceback.format_exc()))
      # or
      #print(sys.exc_info()[2])
      self.set_title(str(e)+"/concert")

