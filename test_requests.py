# test_requests.py

import unittest
import json
from app import app

class TestRequestsEndPoint(unittest.TestCase):
    def setUp(self):
        # This is the requests test json data with predefined values
        self.request_data = {
            'title':'request title',
            'type':'request type',
            'description': 'this is request description'
        }
        self.request_data2 = {
            'title':'This was a request title',
            'type':'request type',
            'description': 'this was a request description'
        }
        # initialize the test client
        self.client = app.test_client()
    # test if the creation of a new request works correctly
    def test_create_request(self):
        response = self.client.post('/api/v1/create_request',data=self.request_data)
        # get the results returned in json format
        results = json.loads(response.data.decode())
        # assert that the request contains a success message
        self.assertEqual(results['response'],'Request successfully Published')
        # assert that the request contains a 201 status code
        self.assertTrue(response.status_code, 201)
    # test_if the user can modify a request
    def test_modify_request(self):
        pass
        

if __name__ == "__main__":
    unittest.main()