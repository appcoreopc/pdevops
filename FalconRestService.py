# command to run
# gunicorn --bind 0.0.0.0:8888 FalconRestService:api

import falcon 
from RestService.BuildRequestService import BuildRequestService

api = falcon.API()
api.add_route('/buildrequest/{id}', BuildRequestService())
