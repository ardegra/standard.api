import pymongo
import falcon
from lib.config import Config

class AgentJobCrawling:
  def on_post(self,req,res):
    client = pymongo.MongoClient("mongodb://{}/ardegra".format(Config.DATABASE_ADDRESS))
    db = client["ardegra"]
    try:
      doc   = req.context["doc"]
      if "spiderName" in doc:
        if doc["spiderName"]:spiderName = doc["spiderName"]
        else:raise Exception("error spiderName")
      if "imageName" in doc:
        if doc["imageName"]:imageName = doc["imageName"]
        else:raise Exception("error imageName")
      doc["status"] = "queueing"

      db.agentJobs.insert_one(doc)
      res.context["result"] = {"error": {"message": "success", "code": 200}}
      res.status            = falcon.HTTP_200
    except Exception as err:
      res.context["result"] = {"error": {"message": str(err), "code": 404}}
      res.status            = falcon.HTTP_404