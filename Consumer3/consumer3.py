from bottle import route, run, template, request
import requests

def getCustomer(hostname, customerID):
    url = 'http://' + hostname + '/customers'
    return requests.get(url + '/' + customerID).json()

@route('/')
def index():
    customerID = request.query.customerID
    if customerID:
        customer = getCustomer('localhost:8080', customerID)
        customerName = customer['name']
        products = customer['financialProducts']
    else:
        products = []
        customerName = ''

    return template('consumer3', customerName = customerName, products = products)

if __name__ == '__main__':
    run(host = 'localhost', port = 8083, debug = True)