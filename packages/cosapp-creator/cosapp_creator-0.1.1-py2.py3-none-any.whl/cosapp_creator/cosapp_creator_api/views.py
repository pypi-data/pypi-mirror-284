from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser, ParseError
from .serializers import detectConnectionErrorSerializer
from .validateConnections import detectConnError, checkLoops

def checkData(request):
    error = ''
    data = {}
    try:
        data = JSONParser().parse(request)
        serializer = detectConnectionErrorSerializer(data=data)
        if not serializer.is_valid():
            error = 'Systems, connections and packages needed.'
    except ParseError:
        error = 'Error while decoding JSON'
    except Exception as err:
        error = f'Error : {str(err)}'
    return data, error



@api_view(('PUT', ))
def detectConnectionErrorView(request):
    try:
        data, error = checkData(request)
        if not error:
            errors = detectConnError(data['systemList'], data['packages'], data['connectionList'])['errors']
        else:
            errors = [{ 'kind': 'data', 'message': error }]
    except Exception as err:
        errors = [{ 'kind': 'data' , 'message': f'Error : {str(err)}'}]
    return Response(errors)


@api_view(('PUT', ))
def getLoops(request):
    try:
        loops = []
        data, error = checkData(request)
        if not error:
            result = detectConnError(data['systemList'], data['packages'], data['connectionList'])
            errors = result['errors']
            assembly = result['assembly']
            if len(errors) == 0 and assembly:
                loops = checkLoops(assembly)
        else:
            errors = [{ 'kind': 'data', 'message': error }]
    except Exception as error:
        errors = [{ 'kind': 'data', 'message': f'Error : {str(error)}' }]
    return Response({ 'loops': loops, 'errors': errors })