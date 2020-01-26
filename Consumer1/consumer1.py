from bottle import route, run, template
import requests

def getCustomers(hostname):
    url = 'http://' + hostname + '/customers'
    return requests.get(url).json()

@route('/')
def index():
    customers = getCustomers('localhost:8080')
    return template('consumer1', customers = customers)

if __name__ == '__main__':
    run(host = 'localhost', port = 8081, debug = True)
