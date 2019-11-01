# command to run
# gunicorn --bind 0.0.0.0:8888 FalconRestService:api

# curl command 
# curl -d '{"id":"123456"}' -H "Content-Type: application/json" -X POST http://localhost:8888/queuebuildrequest


import falcon 
from restService.buildRequestService import BuildRequestService

api = falcon.API()

api.add_route('/buildrequest/{id}', BuildRequestService())

api.add_route('/queuebuildrequest', BuildRequestService())