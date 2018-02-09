import pymongo
import falcon
from lib.config import Config

class AgentJobLatestListener:
  def on_get(self, req, res, numberOfJob):
    # Buat client untuk connect to database
    client = pymongo.MongoClient("mongodb://{}/ardegra".format(Config.DATABASE_ADDRESS))
    try:
      # buat var db untuk lakukan CRUD
      db = client["ardegra"]
      # Ambil data spiders dari database
      documents = db.agentJobs.find({}).sort("$natural", -1).limit(int(numberOfJob))
      result    = []
      for document in documents:
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