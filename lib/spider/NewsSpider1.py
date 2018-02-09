import json

import pymongo
import falcon

from bson import json_util

class NewsSpider1:
  def __init__(self, **kwargs): 
    self.name = kwargs.get("name", None)
    self.country = kwargs.get("country", None)
    self.category = kwargs.get("category", None)
    self.entryDateParser = kwargs.get("entryDateParser", None)
    self.ignoreDomainList = kwargs.get("ignoreDomainList", None)
    self.indexMaxPageNumber = kwargs.get("indexMaxPageNumber", None)
    self.indexUrl = kwargs.get("indexUrl", None)
    self.type = kwargs.get("type", None)
    self.xpath = kwargs.get("xpath", None)
    
  def from_document(self, document):
    self.name = document["name"]
    self.country = document["country"]
    self.category = document["category"]
    self.entryDateParser = document["entryDateParser"]
    self.ignoreDomainList = document["ignoreDomainList"]
    self.indexMaxPageNumber = document["indexMaxPageNumber"]
    self.indexUrl = document["indexUrl"]
    self.type = document["type"]
    self.xpath = document["xpath"]

  def to_dict(self):
    return {
      "name": self.name,
      "country": self.country,
      "category": self.category,
      "entryDateParser": self.entryDateParser,
      "ignoreDomainList": self.ignoreDomainList,
      "indexMaxPageNumber": self.indexMaxPageNumber,
      "indexUrl": self.indexUrl,
      "type": self.type,
      "xpath": self.xpath,
      
    }