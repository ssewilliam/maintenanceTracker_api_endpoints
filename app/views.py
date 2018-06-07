# app/views.py 
from flask import request, jsonify, abort
import json
from app import app
from app.models import *

@app.route('/api_v_1/users/requests',methods=['GET'])
def get_all_requests():
    """
        This endpoint returns all maintance request tickets
    """    
    if len(total_requests) < 1:
        return jsonify({
            'status':'FAIL',
            'response_message':"you have no requests"
        }),404
    return jsonify({
        'status':'OK',
        'requests':total_requests,
        'response_message':'Successfully returned request',
    }),200

@app.route('/api_v_1/users/requests/<requestId>',methods=['GET'])
def get_single_request(requestId):
    """ This endpoint returns a single request by id """
    results = request_model.get_single_request_by_id(requestId)
    if results:
        return jsonify({        
            'results':results,
            'status':'OK',
            'response_message':'Successfully returned request',
        }),200
    else:
        return jsonify({        
            'response_message':'request does not exist',
            'status':'FAIL'
        }),200        
 
@app.route('/api_v_1/users/requests' ,methods= ['POST'])
def create_request():
    """
        This endpoint creates a maintance request ticket
    """
    request_data = request.get_json(force=True)
      
    if not request.json:
        abort(400)        

    if 'request_type' not in request.json:
        abort(400) 
    
    if 'request_title' not in request.json:
        abort(400) 

    if 'request_body' not in request.json:
        abort(400) 

    if isinstance(request_data['request_type'], str) and  isinstance(request_data['request_title'], str) and isinstance(request_data['request_body'], str):
        
        new_request = request_model(request_data['request_type'],request_data['request_title'],request_data['request_body'])
        new_request.post_request()
        if new_request:            
            return jsonify({
                'status':'OK',
                'response_message': 'Request successfully created',
                'request_id':new_request.get_id()
            }), 201
        else:
            return jsonify({ 
                'status':'FAIL',
                'response_message': 'Request was not created'
            }), 400            
                   
    return jsonify({
        'status': 'FAIL',
        'response_message': 'Failed to create a request. Invalid data',
    }), 400

@app.route('/api_v_1/users/requests/<requestId>',methods=['PUT'])
def modify_request(requestId):
    
    update_request_data = request.get_json(force=True)
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

    update_request = request_model(update_request_data['request_type'],update_request_data['request_title'],update_request_data['request_body'])
    result = update_request.update_request(requestId)
    if result:
        return jsonify({
            'status':'OK',
            'response_message':'Successfully updated request',
            'results':result
        }), 200
    return jsonify({
        'status':'FAIL',
        'response_message':'request id doesnot exist'
    }),400
