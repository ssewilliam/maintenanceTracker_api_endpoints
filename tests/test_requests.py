# test_requests.py

# from app.views
import unittest
import json
from app import app
from app.views import *

class TestRequestsEndPoint(unittest.TestCase):
    def setUp(self):
        """ This is the requests test predefined values """
        self.request_data = {
            'request_title':'fix the login button',
            'request_type':'repair',
            'request_body': 'When you click the login button it only returns you to the same page'
        }
        self.request_data2 = {
            'request_title':'fix the login button',
            'request_type' :'maintenance',
            'request_body' : 'This button does not look good you should consider removing it'
        }

        # initialize the test client
        self.client = app.test_client()

    def test_get_all_requests(self):
        """
            This test checks if the endpoint route can return all requests
        """
        response = self.client.post('/api_v_1/users/requests',data=json.dumps(self.request_data) ,content_type='application/json')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'OK')

        response_2 = self.client.get('/api_v_1/users/requests')
        response_data_2 = json.loads(response_2.data.decode())
        self.assertEqual(response_data_2['status'],'OK')
        self.assertEqual(response_2.status_code, 200)

        # # check if the status response key matches ok when fetching all requests
        # response = self.client.get('/api_v_1/users/requests')
        # data = json.loads(response.data.decode())
        # self.assertEqual(data['status'], 'OK')

    def test_get_single_request(self):
        """
            This test checks for the status code returned for fetching a single request
        """
        response = self.client.post('/api_v_1/users/requests',data=json.dumps(self.request_data) ,content_type='application/json')
        response_data = json.loads(response.data.decode())

        self.assertEqual(response_data['status'],'OK')
        self.assertEqual(response.status_code,201)

        response_2 = self.client.get('/api_v_1/users/requests/1')
        response_data_2 = json.loads(response_2.data.decode())
        self.assertEqual(response_data_2['status'], 'OK') 

    def test_create_request(self):
        """
            This test checks whether the api can create requests
        """

        response = self.client.post('/api_v_1/users/requests',data=json.dumps(self.request_data) ,content_type='application/json')
        response_data = json.loads(response.data.decode())

        self.assertEqual(response_data['status'],'OK')
        self.assertEqual(response.status_code,201)
    
    def test_modify_request(self):
        """
            This test checks whether the api can modify requests
        """

        response = self.client.post('/api_v_1/users/requests',data=json.dumps(self.request_data), content_type='application/json')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'OK')

        response = self.client.put('/api_v_1/users/requests/1',data=json.dumps(self.request_data2) ,content_type="application/json")
        self.assertEqual(response.status_code,200)

if __name__ == "__main__":
    unittest.main()