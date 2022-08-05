import mimetypes
from flask import request, Response, json
from flask import jsonify

from src import app
from  ..controllers import accountController
from ..controllers import notificationController

#route tester
@app.route("/tester-dois")
def tester():
	##chamar função da controller
	return "Hello! Teste executado com sucesso. Rota em funcionamento!"

@app.route("/account", methods=['POST', 'PUT'])
def account():
    dataResponse = None
    statusResponse = 200
    if not request.data:
        dataResponse = {
            'message': 'bad request',
            'error': ['Attribrutes are required']
        }
        return json.dumps(dataResponse), 402, {'content-type': 'application/json'}

    if request.method == 'POST':
        # call controller
        controllerResponse = accountController.saveAccount(request.json)
        statusResponse = controllerResponse['status']
        dataResponse = controllerResponse
    elif request.method == 'PUT':
        controllerResponse = accountController.updateAccount(request.json)
        statusResponse = controllerResponse['status']
        dataResponse = controllerResponse
    
    return json.dumps(dataResponse), statusResponse, {'content-type': 'application/json'}

@app.route("/account/<accountId>", methods=['GET', 'DELETE'])
def getAccountById(accountId):
    dataResponse = []
    statusResponse = 200
    if not accountId:
        # chamar função para listar contas
        statusResponse = 403
    else:
        if request.method == 'GET':
            # call controller 
            controllerResponse = accountController.getAccountById(accountId)
            statusResponse = controllerResponse['status']
            dataResponse = controllerResponse

    return json.dumps(dataResponse), statusResponse, {'content-type': 'application/json'}

@app.route("/notification", methods=['POST', 'PUT'])
def saveNotification():
    dataResponse = None
    statusResponse = 200
    if not request.data:
        dataResponse = {
            'message': 'bad request',
            'error': ['Attribrutes are required']
        }
        return json.dumps(dataResponse), 402, {'content-type': 'application/json'}

    if request.method == 'POST':
        # call controller
        controllerResponse = notificationController.saveNotification(request.json)
        statusResponse = controllerResponse['status']
        dataResponse = controllerResponse

    return json.dumps(dataResponse), statusResponse, {'content-type': 'application/json'}

@app.route("/notification/<notificationId>", methods=['GET', 'DELETE'])
def getNotificationById(notificationId):
    dataResponse = []
    statusResponse = 200
    if not notificationId:
        statusResponse = 403
    else:
        if request.method == 'GET':
            # call controller 
            controllerResponse = notificationController.getNotificationById(notificationId)
            statusResponse = controllerResponse['status']
            dataResponse = controllerResponse

    return json.dumps(dataResponse), statusResponse, {'content-type': 'application/json'}
