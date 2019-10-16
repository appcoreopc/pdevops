import falcon 
from RestService.BuildRequestService import BuildRequestService

api = falcon.API()
api.add_route('/quote', BuildRequestService())
