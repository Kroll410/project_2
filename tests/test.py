import unittest
from app import app


class FlaskHTTPTests(unittest.TestCase):

    def setUp(self) -> None:
        self.tester = app.test_client(self)

    def test_get(self):
        """Test GET HTTP requests to server"""

        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/show_tables', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/edit/Customers/2', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/edit/Orders/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/edit/Platforms/3', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/edit/Platformtypes/4', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/edit/Customers/100', content_type='html/text')
        self.assertEqual(response.status_code, 500)

        response = self.tester.get('/edit/Platforms/100', content_type='html/text')
        self.assertEqual(response.status_code, 500)

        response = self.tester.get('/edit/Orders/100', content_type='html/text')
        self.assertEqual(response.status_code, 500)

        response = self.tester.get('/edit/Platformtypes/100', content_type='html/text')
        self.assertEqual(response.status_code, 500)

        response = self.tester.get('/add/Customers', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/add/Orders', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/add/Platforms', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        response = self.tester.get('/add/Platformtypes', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_post_(self):
        """Test POST HTTP requests to server"""

        """Test POST requests with invalid data
            Table - `Orders`
        """
        # Current platform id is not presented in db
        response = self.tester.post('/orders', data={
            'play_time': '2',
            'Customers.id': '1',
            'Platforms.id': '9'
        })
        self.assertEqual(response.status_code, 500)

        # Invalid data passed to `play_time`
        response = self.tester.post('/orders', data={
            'play_time': 'example',
            'Customers.id': '1',
            'Platforms.id': '9'
        })
        self.assertEqual(response.status_code, 500)

        # Good
        response = self.tester.post('/orders', data={
            'play_time': '4',
            'Customers.id': '1',
            'Platforms.id': '8'
        })
        self.assertEqual(response.status_code, 302)

        """
            Table - `Customers`
        """
        # Invalid login name
        response = self.tester.post('/customers', data={
            'login_name': 123
        })
        self.assertEqual(response.status_code, 500)
        # Login name too short
        response = self.tester.post('/customers', data={
            'login_name': 'Fal'
        })
        self.assertEqual(response.status_code, 500)
        # Good
        response = self.tester.post('/customers', data={
            'login_name': 'Fallout boy'
        })
        self.assertEqual(response.status_code, 302)

        """
            Table - `Platforms`
        """
        # Platformtypes.id is not presented in db
        response = self.tester.post('/platforms', data={
            'price': '10',
            'Platformtypes.id': 10,
        })
        self.assertEqual(response.status_code, 500)
        # Invalid price value
        response = self.tester.post('/platforms', data={
            'price': 'ab',
            'Platformtypes.id': 3,
        })
        self.assertEqual(response.status_code, 500)

        # Good
        response = self.tester.post('/platforms', data={
            'price': 100,
            'Platformtypes.id': 3,
        })
        self.assertEqual(response.status_code, 302)
        """
            Table - `Platformtypes`
        """

        # Good
        response = self.tester.post('/platformtypes', data={
            'type': 'Nintendo Switch',
        })
        self.assertEqual(response.status_code, 302)

    def test_delete(self):
        """Test DELETE HTTP requests to server"""

        # Good
        self.tester.delete('/orders/2')
        response = self.tester.get('/orders/2')
        self.assertEqual(response.json, {})

        self.tester.delete('/customers/4')
        response = self.tester.get('/customers/4')
        self.assertEqual(response.json, {})

        self.tester.delete('/platforms/4')
        response = self.tester.get('/platforms/4')
        self.assertEqual(response.json, {})

        self.tester.delete('/platformtypes/2')
        response = self.tester.get('/platformtypes/2')
        self.assertEqual(response.json, {})

        # Invalid
        self.tester.delete('/customers/1')
        response = self.tester.get('/customers/1')
        self.assertNotEqual(response.json, {})

        self.tester.delete('/platformtypes/3')
        response = self.tester.get('/platformtypes/3')
        self.assertNotEqual(response.json, {})

        self.tester.delete('/platforms/5')
        response = self.tester.get('/platforms/5')
        self.assertNotEqual(response.json, {})
