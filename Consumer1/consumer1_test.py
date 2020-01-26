import unittest
import atexit
from pact import Consumer, Provider
from consumer1 import getCustomers

pact = Consumer('Consumer 1').has_pact_with(Provider('Provider'), host_name='localhost',  port=7070)
pact.start_service()
atexit.register(pact.stop_service)

class GetCustomersContract(unittest.TestCase):
  def test_get_customers(self):
    expected = [
      {
          'name': 'Alice',
          'email': 'alice@mail.com',
          'status': 'married'
      },
      {
          'name': 'Bob',
          'email': 'bob@mail.com',
          'status': 'married'
      },
            {
          'name': 'Charlie',
          'email': 'charlie@mail.com',
          'status': 'single'
      }
    ]

    (pact
     .given('customers exist')
     .upon_receiving('a request for all customers')
     .with_request('get', '/customers')
     .will_respond_with(200, body=expected))

    with pact:
      result = getCustomers('localhost:7070')

    self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()