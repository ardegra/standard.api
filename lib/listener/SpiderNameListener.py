import pymongo
import falcon

from lib.spider.ForumSpider1 import ForumSpider1
from lib.spider.NewsSpider1 import NewsSpider1
from lib.spider.NewsSpider2 import NewsSpider2
from lib.spider.NewsSpider34 import NewsSpider34
from lib.config import Config

class SpiderNameListener:
  def on_get(self, req, res, spiderName):
    # Buat client untuk connect to database
    client = pymongo.MongoClient("mongodb://{}/ardegra".format(Config.DATABASE_ADDRESS))
    try:
      # buat var db untuk lakukan CRUD
      db = client["ardegra"]
      
      # Ambil data spiders dari database
      documents = db.spiders.find({"name": spiderName})
      result    = []
      for document in documents:
        if document["type"]["name"] == "Forum Spider 1":
          spider = ForumSpider1()
          spider.from_document(document)
        elif document["type"]["name"] == "News Spider 1":
          spider = NewsSpider1()
          spider.from_document(document)
        elif document["type"]["name"] == "News Spider 2":
          spider = NewsSpider2()
          spider.from_document(document)
        else:
          spider = NewsSpider34()
          spider.from_document(document)
        result.append(spider.to_dict())
        
      res.context["result"] = {"data": result, "error": {"message": "success", "code": 200}}
      res.status            = falcon.HTTP_200
    except Exception as err:
      res.context["result"] = {"error": {"message": str(err), "code": 404}}
      res.status            = falcon.HTTP_404
    finally:
      client.close()
      
  def on_patch(self, req, res, spiderName):
    client = pymongo.MongoClient("mongodb://{}/ardegra".format(Config.DATABASE_ADDRESS))
    db = client["ardegra"]
    try:
      doc   = req.context["doc"]
      if "country" in doc:
        if doc["country"]:country = doc["country"]
        else:raise Exception("error country")
      if "category" in doc:
        if doc["category"]:category = doc["category"]
        else:raise Exception("error category")
      if "type" in doc:
        doc["type"]["description"]= ""
        if doc["type"]:type = doc["type"]["name"]
        else:raise Exception("error type")
      if "xpath" in doc:
        if doc["xpath"]:xpath = doc["xpath"]
        else:raise Exception("error xpath")
        
        
      if doc["type"]["name"] == "Forum Spider 1":
        if "categoryList" in doc:
          if doc["categoryList"]: categoryList = doc["categoryList"]
          else:raise Exception("error categoryList")
        
      elif doc["type"]["name"] == "News Spider 1":
        if "indexUrl" in doc:
          if doc["indexUrl"]:indexUrl = doc["indexUrl"]
          else:raise Exception("error indexUrl")
        if not "ignoreDomainList" in doc:raise Exception("error ignoreDomainList")
        if "entryDateParser" in doc:
          if doc["entryDateParser"]:entryDateParser = doc["entryDateParser"]
          else:raise Exception("error entryDateParser")
        if "indexMaxPageNumber" in doc:
          if doc["indexMaxPageNumber"]:indexMaxPageNumber = int(doc["indexMaxPageNumber"])
          else:raise Exception("error indexMaxPageNumber")
        
      elif doc["type"]["name"] == "News Spider 2":
        if "indexUrl":
          if doc["indexUrl"]:indexUrl = doc["indexUrl"]
          else:raise Exception("error indexUrl")
        if not "ignoreDomainList":raise Exception("error ignoreDomainList")
        if "entryDateParser":
          if doc["entryDateParser"]:entryDateParser = doc["entryDateParser"]
          else:raise Exception("error entryDateParser") 
        if "indexStartDate":
          if doc["indexStartDate"]:indexStartDate = doc["indexStartDate"]
          else:raise Exception("error indexStartDate")  
        if "indexEndDate":
          if doc["indexEndDate"]:indexEndDate = doc["indexEndDate"]
          else:raise Exception("error indexEndDate")
          
      else:
        if "categoryList" in doc:
          if doc["categoryList"]: categoryList = doc["categoryList"]
          else:raise Exception("error categoryList")
        if "indexUrl" in doc:
          if doc["indexUrl"]:indexUrl = doc["indexUrl"]
          else:raise Exception("error indexUrl")
        if not "ignoreDomainList" in doc: raise Exception("error ignoreDomainList")
        if "entryDateParser" in doc:
          if doc["entryDateParser"]:entryDateParser = doc["entryDateParser"]
          else:raise Exception("error entryDateParser")
        if "indexStartDate" in doc:
          if doc["indexStartDate"]:indexStartDate = doc["indexStartDate"]
          else:raise Exception("error indexStartDate")
        if "indexEndDate" in doc:
          if doc["indexEndDate"]:indexEndDate = doc["indexEndDate"]
          else:raise Exception("error indexEndDate")
        if "indexOffsetIncrement" in doc:
          if doc["indexOffsetIncrement"]:indexOffsetIncrement = doc["indexOffsetIncrement"]
          else:raise Exception("error indexOffsetIncrement")
          
      db.spiders.update({"name": spiderName}, doc)
      res.context["result"] = {"error": {"message": "success", "code": 200}}
      res.status            = falcon.HTTP_200
    except Exception as err:
      res.context["result"] = {"error": {"message": str(err), "code": 404}}
      res.status            = falcon.HTTP_404