import falcon

from falcon_cors import CORS

from lib.middleware.JSONTranslator import JSONTranslator
from lib.middleware.RequireJSON import RequireJSON

from lib.listener.SpiderListener import SpiderListener
from lib.listener.SpiderNameListener import SpiderNameListener
from lib.listener.AgentJobLatestListener import AgentJobLatestListener
from lib.listener.AgentJobActiveListener import AgentJobActiveListener
from lib.listener.AgentJobCrawling import AgentJobCrawling

cors = CORS(
  allow_all_origins=True,
  allow_all_headers=True,
  allow_all_methods=True
)
api  = falcon.API(middleware=[cors.middleware, RequireJSON(), JSONTranslator()])


api.add_route("/spider", SpiderListener())
api.add_route("/spider/{spiderName}", SpiderNameListener())
api.add_route("/agentJob/latest/{numberOfJob}", AgentJobLatestListener())
api.add_route("/agentJob/active", AgentJobActiveListener())
api.add_route("/agentJob", AgentJobCrawling())
