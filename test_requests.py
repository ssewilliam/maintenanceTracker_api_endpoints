# test_requests.py

import unittest
import json
from run import *

class TestRequestsEndPoint(unittest.TestCase):
    def setUp(self):
        # This is the requests test json data with predefined values
        self.request_data = {
            'request_title':'fix the login button',
            'request_type':'repair',
            'request_body': 'When you click the login button it only returns you to the same page'
        }
        self.request_data2 = {
            'request_title':'',
            'request_type' :'maintenance',
            'request_body' : 'This button does not look good you should consider removing it'
        }
        self.request_data3 = {
            'request_id':'1',
            'request_title':'Replace the retina display',
            'request_type' :'maintenance',
            'request_body' : 'This button does not look good you should consider removing it'
        }
        self.request_data4 = {
            'request_id':1,
            'request_title':'Replace the retina display',
            'request_type' :1,
            'request_body' : 'This button does not look good you should consider removing it'
        }
        self.request_data5 = {
            'request_id':1,
            'request_title':'Replace the retina display',
            'request_type' :1
        }
        # initialize the test client
        self.client = app.test_client()

    def test_get_all_requests(self):
        """
            This test checks if the endpoint route can return all requests
        """
        # check for the status code returned when getting all requests
        res = self.client.get('/api_v_1/users/requests')
        self.assertEqual(res.status_code, 200)

        # check if the status response key matches ok when fetching all requests
        response = self.client.get('/api_v_1/users/requests')
        data = json.loads(response.data.decode())
        self.assertEqual(data['status'], 'OK')

    def test_get_single_request(self):
        """
            This test checks for the status code returned for fetching a single request
        """
        # check if the status response key matches ok when fetching a single
        response = self.client.get('/api_v_1/users/requests/1')
        data = json.loads(response.data.decode())
        self.assertEqual(data['status'], 'OK')        

    def test_create_request(self):
        """
            This test checks whether the api can create requests
        """
        # check for the status response from the api endpoint
        response = self.client.post('/api_v_1/users/requests',data=json.dumps(self.request_data) ,content_type='application/json')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'OK')

        # check for the status code from the response returned
        self.assertEqual(response.status_code,201)
    
    def test_modify_request(self):
        """
            This test checks whether the api can modify requests
        """
        # check for the status response from the api endpoint
        response = self.client.put('/api_v_1/users/requests/1',data=json.dumps(self.request_data3), content_type='application/json')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'OK')

        # check for the status code from the response returned
        response = self.client.put('/api_v_1/users/requests/1',data=json.dumps(self.request_data3) ,content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_modify_with_empty_values(self):
        """
            This test checks whether the api can modify requests with some empty values
        """
        # check for the status response from the api endpoint
        response = self.client.put('/api_v_1/users/requests/1',data=self.request_data2)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'BAD REQUEST')

        # check for the status code from the response returned
        response = self.client.put('/api_v_1/users/requests/1',data=self.request_data2)
        self.assertEqual(int(response.status_code),400)

    def test_modify_with_numerical_values(self):
        """
            This test checks whether the api can modify requests with some numeric values
        """
        # check for the status response from the api endpoint
        response = self.client.put('/api_v_1/users/requests/1',data=self.request_data4)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'BAD REQUEST')

        # check for the status code from the response returned
        response = self.client.put('/api_v_1/users/requests/1',data=self.request_data4)
        self.assertEqual(int(response.status_code),400)

    def test_modify_without_some_fields(self):
        """
            This test checks whether the api can modify requests with some numeric values
        """
        # check for the status response from the api endpoint
        response = self.client.put('/api_v_1/users/requests/1',data=self.request_data5)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['status'],'BAD REQUEST')

        # check for the status code from the response returned
        response = self.client.put('/api_v_1/users/requests/1',data=self.request_data5)
        self.assertEqual(int(response.status_code),400)

if __name__ == "__main__":
    unittest.main()