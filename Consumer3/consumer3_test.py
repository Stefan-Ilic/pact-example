import unittest
import atexit
from pact import Consumer, Provider
from consumer3 import getCustomer

pact = Consumer('Consumer 3').has_pact_with(Provider('Provider'), host_name='localhost',  port=7070)
pact.start_service()
atexit.register(pact.stop_service)

class GetCustomersContract(unittest.TestCase):
  def test_get_customer(self):
    expected = {
            'name': 'Alice',
            'financialProducts': [
                {
                    'name': 'Share',
                    'balance': 4,
                    'productCode': 'ABC1',
                    'interestRate': 1.2
                },
                {
                    'name': 'Bond',
                    'balance': 5,
                    'productCode': 'ABC2',
                    'interestRate': 1.3
                }
            ]
        }

    (pact
     .given('customer 1 exists and has financialProducts')
     .upon_receiving('a request for customer 1 and their financialProducts')
     .with_request('get', '/customers/1')
     .will_respond_with(200, body=expected))

    with pact:
      result = getCustomer('localhost:7070', '1')

    self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()