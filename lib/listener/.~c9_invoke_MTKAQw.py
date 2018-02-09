import pymongo
import falcon

class AgentJobActiveListener:
  def on_get(self, req, res):
    # Buat client untuk connect to database
    client = pymongo.MongoClient("mongodb://35.187.233.55:27017/ardegra")
    try:
      # buat var db untuk lakukan CRUD
      db = client["ardegra"]
      
      # Ambil data spiders dari database
      documents = db.agentJobs.find({})
      result    = []
      for document in documents:
        if document["status"] == "s":
          result.append({
            "spiderName": str(document["spiderName"]),
            "imageName": str(document["imageName"]),
            "status": str(document["status"])
          })
        
      res.context["result"] = {"data": result, "error": {"message": "success", "code": 200}}
      res.status            = falcon.HTTP_200
    except Exception as err:
      res.context["result"] = {"error": {"message": str(err), "code": 404}}
      res.status            = falcon.HTTP_404
    finally:
      client.close()