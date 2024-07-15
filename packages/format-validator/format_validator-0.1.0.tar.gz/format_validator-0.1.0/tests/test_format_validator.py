import unittest
from format_validator import validate_phone_number, validate_date

class TestFormatValidator(unittest.TestCase):

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number('(123) 456-7890'))
        self.assertTrue(validate_phone_number('123-456-7890'))
        self.assertTrue(validate_phone_number('123.456.7890'))
        self.assertTrue(validate_phone_number('1234567890'))
        self.assertTrue(validate_phone_number('+31636363634'))
        self.assertTrue(validate_phone_number('075-63546725'))
        self.assertFalse(validate_phone_number('123-4567-890'))

    def test_validate_date(self):
        self.assertTrue(validate_date('12/31/2020'))
        self.assertTrue(validate_date('31/12/2020'))
        self.assertTrue(validate_date('2020-12-31'))
        self.assertTrue(validate_date('31-Dec-2020'))
        self.assertFalse(validate_date('31/13/2020'))
        self.assertFalse(validate_date('2020/12/31'))

if __name__ == '__main__':
    unittest.main()
