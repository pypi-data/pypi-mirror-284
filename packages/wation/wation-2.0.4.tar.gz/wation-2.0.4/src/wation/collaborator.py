from wation import Wation

def enpoint_request():
    wation = Wation.instance()
    response = wation.request('/collaborator/endpoint', 'get')
    if response['status'] != True:
        raise ValueError(response['message'])

    return response['data']['endpoint']

def enpoint_refresh():
    wation = Wation.instance()
    response = wation.request('/collaborator/endpoint/refresh', 'get')
    return response['status']

def requests_logs():
    wation = Wation.instance()
    response = wation.request('/collaborator/requests/logs', 'get')
    if response['status'] != True:
        raise ValueError(response['message'])
    return response['data']['items']

def requests_clear():
    wation = Wation.instance()
    response = wation.request('/collaborator/requests/clear', 'get')
    return response['status']