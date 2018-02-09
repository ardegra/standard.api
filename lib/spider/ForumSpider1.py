import pymongo
import falcon

class ForumSpider1:
  def __init__(self, **kwargs):
    self.name = kwargs.get("name", None)
    self.country = kwargs.get("country", None)
    self.category = kwargs.get("category", None)
    self.category_list = kwargs.get("categoryList", None)
    self.type = kwargs.get("type", None)
    self.xpath = kwargs.get("xpath", None)
    
  def from_document(self, document):
    self.name = document["name"]
    self.country = document["country"]
    self.category = document["category"]
    self.category_list = document["categoryList"]
    self.type = document["type"]
    self.xpath = document["xpath"]

  def to_dict(self):
    return {
      "name": self.name,
      "country": self.country,
      "category": self.category,
      "categoryList": self.category_list,
      "type": self.type,
      "xpath": self.xpath
    }
    
    
  # def on_get(self, req, res):
  #   # Buat client untuk connect to database
  #   client = pymongo.MongoClient("mongodb://35.187.233.55:27017/ardegra")
  #   try:
  #     # buat var db untuk lakukan CRUD
  #     db = client["ardegra"]
      
  #     # Ambil data spiders dari database
  #     documents = db.spiders.find({})
  #     result    = []
  #     for document in documents:
  #       result.append({
  #         "_id": str(document["_id"]),
  #         "name": str(document["name"]),
  #         "country": str(document["country"]),
  #         "category": str(document["category"]),
  #         "categoryList": document["categoryList"],
  #         "type": {
  #           "description": document["type"]["description"],
  #           "name": document["type"]["name"]
  #         },
  #         "xpath": {
  #             "post": {
  #               "authorName": str(document["xpath"]["post"]["authorName"]),
  #               "id": str(document["xpath"]["post"]["id"]),
  #               "authorId": str(document["xpath"]["post"]["authorId"]),
  #               "item": str(document["xpath"]["post"]["item"]),
  #               "firstPostId": str(document["xpath"]["post"]["firstPostId"]),
  #               "entryDate": str(document["xpath"]["post"]["entryDate"]),
  #               "content": str(document["xpath"]["post"]["content"]),
  #               "permalink": str(document["xpath"]["post"]["permalink"]),
  #               "authorUrl": str(document["xpath"]["post"]["authorUrl"])
  #             },
  #             "category": {
  #                 "lastPage": str(document["xpath"]["category"]["lastPage"]),
  #                 "prevPage": str(document["xpath"]["category"]["prevPage"])
  #             },
  #             "thread": {
  #                 "url": str(document["xpath"]["thread"]["url"]),
  #                 "lastPage": str(document["xpath"]["thread"]["lastPage"]),
  #                 "nextPage": str(document["xpath"]["thread"]["nextPage"]),
  #                 "title": str(document["xpath"]["thread"]["title"]),
  #                 "prevPage": str(document["xpath"]["thread"]["prevPage"])
  #             }
  #         }
  #       })

  #     res.context["result"] = {"data": result, "error": {"message": "success", "code": 200}}
  #     res.status            = falcon.HTTP_200
  #   except Exception as err:
  #     res.context["result"] = {"error": {"message": str(err), "code": 404}}
  #     res.status            = falcon.HTTP_404
  #   finally:
  #     client.close()