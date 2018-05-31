from flask import Flask, request, jsonify, abort

app = Flask(__name__)
# list data storage with fake data
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
    # check if the data storage has some data
    if len(request_data_list) < 1:
        abort(404)
    # return all data stored
    return jsonify({
        'status':'OK',
        'requests':request_data_list
    }),200

@app.route('/api_v_1/users/requests/<requestId>',methods=['GET'])
def get_single_request(requestId):
    # fetch data from storage and check if the id passed matches storage id
    request_data = [
            request_data for request_data in request_data_list
            if request_data['request_id'] == requestId
        ]
    if len(request_data) == 0:
        abort(404)
    return jsonify({
        'request_data':request_data[0]
    })

if __name__ == "__main__":
    app.run(debug=True)