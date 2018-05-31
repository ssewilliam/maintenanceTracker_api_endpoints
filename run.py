from flask import Flask, request, jsonify, abort

app = Flask(__name__)
# list data storage with fake data that would be used for get requests
request_data_list = [
    {
        'request_id':'1',
        'request_type':'repair',
        'request_title':'Fix the navigation bar',
        'request_body':'The navigation bar is not sticky for the mobile devices.You should repair it so that it remains sticky'
    },
    {
        'request_id':'2',    
        'request_type':'maintenance',    
        'request_title':'change the background color',
        'request_body':'The background color is not set as specified please change it so that is matches as specified'
    },
    {
        'request_id':'3',    
        'request_type':'repair',    
        'request_title':'Fix the navigation bar',
        'request_body':'The navigation bar is not sticky for the mobile devices.You should repair it so that it remains sticky'
    }
]

@app.route('/api_v_1/users/requests',methods=['GET'])
def get_all_requests():
    """
        This endpoint returns all maintance request tickets
    """    
    # 1. check if the data storage has some data
    if len(request_data_list) < 1:
        abort(404)
    # 2. return all data stored
    return jsonify({
        'status':'OK',
        'requests':request_data_list
    }),200

@app.route('/api_v_1/users/requests/<requestId>',methods=['GET'])
def get_single_request(requestId):
    """
        This endpoint returns a single maintance request ticket based on the id parsed
    """
    # 1. fetch data from storage and check if the id passed matches storage id
    request_data = [
            request_data for request_data in request_data_list
            if request_data['request_id'] == requestId
        ]
    # 2. check if there is data already stored        
    if len(request_data) == 0:
        abort(404)
    return jsonify({ # 3. return the found request id details
        'request_data':request_data[0]
    }),200

@app.route('/api_v_1/users/requests' ,methods= ['POST'])
def create_request():
    """
        This endpoint creates a maintance request ticket
    """
    # 1. force getting json data from a request
    request_data = request.get_json(force=True)
    # 2. validate the data checkking if its of examples of strings
    if isinstance(request_data['request_type'], str) and  isinstance(request_data['request_title'], str) and isinstance(request_data['request_body'], str):
        
        # 3. store the data
        request_last_id = len(request_data_list) #  count how many maintance requests are already saved
        request_last_id += 1 
        request_datas = {
            'request_id':request_last_id,
            'request_title':request_data['request_title'],
            'request_type': request_data['request_type'],
            'request_body':request_data['request_body']
        }
        # create an instance of request and immitate the saving of data
        request_data_list.append(request_datas)  #  Save request in the list
        
        return jsonify({
            'results':request_datas
        }), 201
        
    return jsonify({
        'status': 'FAIL',
        'message': 'Failed to create a request. Invalid data',
    }), 400


if __name__ == "__main__":
    app.run(debug=True)