import json
import falcon
from json import dumps
from buildProcessor import BuildProcessor
import logging

class BuildRequestService:

    def on_get(self, req, resp, id): 
        logging.info(req.path, req.uri, req.url, req.query_string)  
        logging.info(id)   
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        resp.body = quote

    def on_post(self, req, resp):
        try:
            result = req.media    
            processor = BuildProcessor()
            processor.queueBuild(result.get("id"))
            resp.body = dumps(result)
            resp.status = falcon.HTTP_200
        except:
            resp.status = falcon.HTTP_500
       
    def on_put(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'PUT'
        }
        resp.body = quote

    

