import pymongo
import falcon
import arrow

class NewsSpider2:
  def __init__(self, **kwargs):
    self.name = kwargs.get("name", None)
    self.country = kwargs.get("country", None)
    self.category = kwargs.get("category", None)
    self.indexUrl= kwargs.get("indexUrl", None)
    # self.indexMaxPageNumber= kwargs.get("indexMaxPageNumber", None)
    self.indexStartDate= kwargs.get("indexStartDate", None)
    self.indexEndDate= kwargs.get("indexEndDate", None)
    self.ignoreDomainList= kwargs.get("ignoreDomainList", None)
    self.entryDateParser= kwargs.get("entryDateParser", None)
    self.type = kwargs.get("type", None)
    self.xpath = kwargs.get("xpath", None)
    
  def from_document(self, document):
    self.name = document["name"]
    self.country = document["country"]
    self.category = document["category"]
    self.indexUrl= document["indexUrl"]
    # self.indexMaxPageNumber= document["indexMaxPageNumber"]
    self.indexStartDate=  arrow.get(document["indexStartDate"]).isoformat()
    self.indexEndDate= arrow.get(document["indexEndDate"]).isoformat()
    self.ignoreDomainList= document["ignoreDomainList"]
    self.entryDateParser= document["entryDateParser"]
    self.type = document["type"]
    self.xpath = document["xpath"]

  def to_dict(self):
    return {
      "name": self.name,
      "country": self.country,
      "category": self.category,
      "indexUrl": self.indexUrl,
      # "indexMaxPageNumber": self.indexMaxPageNumber,
      "indexStartDate": self.indexStartDate,
      "indexEndDate": self.indexEndDate,
      "ignoreDomainList": self.ignoreDomainList,
      "entryDateParser": self.entryDateParser,
      "type": self.type,
      "xpath": self.xpath
    }