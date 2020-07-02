import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth


app = Flask(__name__)
setup_db(app)

CORS(app, resources={r"/api/*": {"origins": "*"}})
'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()


# ROUTES
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization,true')
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET,PATCH,POST,DELETE,OPTIONS')
    return response


'''

@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks')
def drinks_get():
    try:
        container = Drink.query.all()
        drinks = [drink.short() for drink in container]
        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except BaseException:
        abort(404)


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def drinks_details(token):
    try:
        container = Drink.query.all()
        drinks = [drink.long() for drink in container]
        if len(drinks) == 0:
            abort(404)
        else:    
            return jsonify({
                "success": True,
                'drinks': drinks
            })
    except BaseException:
        abort(404)


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth("post:drinks")
def create_drinks(token):
    try:
        title = request.json['title']
        recipe = request.json['recipe']
        if title and recipe:    
            posted_drink = Drink(title=title, recipe=json.dumps(recipe))
            posted_drink.insert()
        else:
            abort(422)
        container = Drink.query.all()
        drinks = [drink.short() for drink in container]
        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except BaseException:
        abort(422)


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:drinks_id>', methods=['PATCH'])
@requires_auth("patch:drinks")
def edit_drinks(token, drinks_id):
    try:
        title = request.json['title']
        recipe = request.json['recipe']
        drink = Drink.query.filter(Drink.id == drinks_id).one_or_none()
        if drink is None:
            abort(404)
        else:    
            drink.title = title
            drink.recipe = json.dumps(recipe)
            drink.update()
        container = Drink.query.all()
        drinks = [drink.long() for drink in container]
        return jsonify({
            'success': True,
            'drinks': drinks
        })
    except BaseException:
        abort(404)


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:drinks_id>', methods=['DELETE'])
@requires_auth("delete:drinks")
def delete_drinks(token, drinks_id):
    try:
        drink = Drink.query.get(drinks_id)
        if drink:
            drink.delete()
        else:
            abort(404)
        return jsonify({
            'success': True,
            'delete': drinks_id
        })
    except BaseException:
        abort(404)


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(401)
def not_authorizated(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "not authorizated"
    }), 401
