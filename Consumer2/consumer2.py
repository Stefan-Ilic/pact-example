from bottle import route, run, template
import requests

def getCustomersWithProductBalanceSum(hostname):
    url = 'http://' + hostname + '/customers'
    return requests.get(url).json()

@route('/')
def index():
    customers = getCustomersWithProductBalanceSum('localhost:8080')
    customerDict = {}
    for customer in customers:
        products = customer['financialProducts']
        balances = [product['balance'] for product in products]
        sumOfProducts = sum(balances)
        customerDict[customer['name']] = sumOfProducts

    return template('consumer2', customers = customerDict)

if __name__ == '__main__':
    run(host = 'localhost', port = 8082, debug = True)
