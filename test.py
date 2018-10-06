from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

	#Ensure that flask was sett up correctly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure that login page loads correctly
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertFalse(b'Please try again.' in  response.data)

	# Ensure that login correctly
	def test_correct_login(self):
		tester = app.test_client(self)
		response = tester.post(
				'/login',
					data=dict(username="admin", password="admin"),
					follow_redirects=True
		)
		self.assertIn(b'You are just login', response.data)

	# Test Wrong credentails
	def test_incorrect_login(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
				data=dict(username="wrong", password="wrong"),
				follow_redirects=True
		)
		self.assertIn(b'Invalid credentials. Please try again', response.data)

	# test loggout 
	def test_logout(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
				data=dict(username="admin", password="admin"),
				follow_redirects=True
		)
		self.assertIn(b'You were just Logged out', response.data)

		#Ensure that main page requires login
	def test_main_route_requires_login(self):
		tester = app.test_client(self)
		response = tester.get('/', follow_redirects=True)
		self.assertTrue(b'You need to first Login', response.data)


	def test_post_show_up(self):
		tester = app.test_client(self)
		response = tester.post(
			'/login',
				data=dict(username="admin", password="admin"),
				follow_redirects=True
		)
		self.assertIn(b'He loves Hiphop', response.data)



if __name__ =='__main__':
	unittest.main()