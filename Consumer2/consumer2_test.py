import unittest
import atexit
from pact import Consumer, Provider
from consumer2 import getCustomersWithProductBalanceSum

pact = Consumer('Consumer 2').has_pact_with(Provider('Provider'), host_name='localhost',  port=7070)
pact.start_service()
atexit.register(pact.stop_service)

class GetCustomersContract(unittest.TestCase):
  def test_get_customers(self):
    expected = [
        {
            'name': 'Alice',
            'financialProducts': [
                {
                    'balance': 4,
                },
                {
                    'balance': 5,
                }
            ]
        },
        {
            'name': 'Bob',
            'financialProducts': [
                {
                    'balance': 4,
                },
                {
                    'balance': 6,
                }
            ]
        },
        {
            'name': 'Charlie',
            'financialProducts': [
                {
                    'balance': 6,
                },
                {
                    'balance': 5,
                }
            ]
        }
    ]

    (pact
     .given('customers exist and have financialProducts with balances')
     .upon_receiving('a request for all customers and the balances of their financial products')
     .with_request('get', '/customers')
     .will_respond_with(200, body=expected))

    with pact:
      result = getCustomersWithProductBalanceSum('localhost:7070')

    self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()