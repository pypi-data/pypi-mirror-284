import unittest
from  pkg1 import validate

class ValidateGreater(unittest.TestCase):

	def test_validate(self):
		self.assertEqual(validate.is_eligible(12), False)
		self.assertEqual(validate.is_eligible(19), True)

unittest.main()
