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
        'request_title':'Add an about page',
        'request_body':'We need an about us page on the app where we can find out more about you'
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
        'status':'OK',
        'request_data':request_data[0]
    }),200

@app.route('/api_v_1/users/requests' ,methods= ['POST'])
def create_request():
    """
        This endpoint creates a maintance request ticket
    """
    # 1. force getting json data from a request
    request_data = request.get_json(force=True)
    
    if not request.json:
        abort(400)        

    if 'request_type' not in request.json:
        abort(400) 
    
    if 'request_title' not in request.json:
        abort(400) 

    if 'request_body' not in request.json:
        abort(400) 
    # 2. validate the data checking if its of examples of strings,all fields exist

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
            'status':'OK',
            'results':request_datas,
            'response_message': 'Request ticket successfully created'
        }), 201
        
    return jsonify({
        'status': 'FAIL',
        'message': 'Failed to create a request. Invalid data',
    }), 400

@app.route('/api_v_1/users/requests/<requestId>',methods=['PUT'])
def modify_request(requestId):
    # 1. force getting json data from a request
    put_request_data = request.get_json(force=True)

    """
        2. (Using List comprehension)
            from the data stored in the temp storage check if the id passed matches the stored id
           to verify that the request id does exist
    """

    if not request.json:
        abort(400)

    if 'request_type' not in request.json:
        abort(400)

    if type(request.json['request_type']) is not str or request.json['request_type'] == '':
        abort(400)
    if 'request_type' not in request.json:
        abort(400)

    if type(request.json['request_type']) is not str or request.json['request_type'] == '':
        abort(400)

    request_data = [request_dat for request_dat in request_data_list if request_dat['request_id'] == requestId]
    if len(request_data) < 1:
        abort(404)

    # 3 create a new dictionary with the data that has been passed
    new_put_request = {
        'request_id':put_request_data['request_id'],
        'request_type':put_request_data['request_type'],
        'request_title':put_request_data['request_title'],
        'request_body':put_request_data['request_body']
    }
    # 4 Save the changes to the temp storage
    request_data_list.append(new_put_request)
    return jsonify({
        'status':'OK',
        'new_request_data':new_put_request
    }), 200
# customise 400,404,403,500 html response errors with json response
@app.errorhandler(400)
def page_bad_request(e):
    return jsonify({
        'status':'BAD REQUEST',
        'response_message':'the request was bad'
    }),400
  
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'status':'FAIL',
        'response_message':'page not found'
    }),404
    
@app.errorhandler(403)
def page_forbidden(e):
    return jsonify({
        'status':'DENIED',
        'response_message':'You have no access to this page'
    }),403

@app.errorhandler(405)
def page_forbidden(e):
    return jsonify({
        'status':'NOT ALLOWED',
        'response_message':'This method is not allowed'
    }),405

@app.errorhandler(500)
def page_serverdown(e):
    return jsonify({
        'status':'SERVER DOWN',
        'response_message':'The server is unable to handle the request'
    }),500
    
if __name__ == "__main__":
    app.run(debug=True)