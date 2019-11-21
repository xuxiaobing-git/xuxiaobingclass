import unittest

from app.business_action.login import LoginAction


class MyTestCase(unittest.TestCase):

	def test_01(self):
		case = LoginAction()
		case.into_lucky()
		self.assertEqual(True, False)


if __name__ == '__main__':
	unittest.main()
