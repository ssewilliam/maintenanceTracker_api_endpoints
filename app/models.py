# app/models.py
total_requests = []
class request_model:
    def __init__(self, request_type, request_title, request_body ):
        """ _request class """
            
        request_last_id = len(total_requests)
        request_last_id += 1
        self.request_id = request_last_id
        self.request_type = request_type
        self.request_title = request_title
        self.request_body = request_body        
        self.total_requests = []

    def get_id(self):
        return self.request_id
    
    def get_type(self):
        return self.request_type

    def get_title(self):
        return self.request_title
    
    def get_body(self):
        return self.request_body
    
    def post_request(self):
        """post anew request by the user"""

        new_request = {
            'request_id':self.request_id,
            'request_title':self.request_title,
            'request_type': self.request_type,
            'request_body':self.request_body
        }

        total_requests.append(new_request)
        return new_request
    
    @staticmethod
    def get_requests():
        """ Returns the list empty or not"""
        return total_requests

    @staticmethod
    def get_single_request_by_id(requestId):
        """ returns a dictionary at the list's index"""
        requestId = int(requestId) 
        if len(total_requests) > 0 and requestId <= len(total_requests):
            result_data = {
                'request_id': total_requests[requestId-1]['request_id'],
                'request_type': total_requests[requestId-1]['request_type'],
                'request_title': total_requests[requestId-1]['request_title'],
                'request_body': total_requests[requestId-1]['request_body']
            }
            return result_data  
      
    def update_request(self,requestId):
        requestId = int(requestId) 
        new_put_request = {}
        if len(total_requests) > 0 and requestId <= len(total_requests):
            new_put_request = {
                'request_id':requestId,
                'request_title':self.request_title,
                'request_type': self.request_type,
                'request_body':self.request_body
            }
            total_requests[requestId-1] = new_put_request
            return new_put_request
        return new_put_request