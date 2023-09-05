# Task 2

# Write tests for the Phonebook application, which you have
# implemented in module 1. Design tests for this solution and
# write tests using unittest library

from unittest import TestCase, main
from src.manager import create, update, delete

class TestPhoneFunctions(TestCase):

    def test_create(self):
        data = {"0762729401": {"first_name": "Andrii", "last_name": "Dorokhov",
                               "city": "Kharkiv", "country": "Ukraine"}}
        data_to_update = {"13109179191": {"first_name": "Christina",
                                          "last_name": "Aguilera", "city": "Los Angeles", "country": "USA"}}
        result = create(data, data_to_update)
        dict_test = {"0762729401": {"first_name": "Andrii", "last_name": "Dorokhov", "city": "Kharkiv", "country": "Ukraine"},
                     "13109179191": {"first_name": "Christina", "last_name": "Aguilera", "city": "Los Angeles", "country": "USA"}}
        self.assertEqual(result, dict_test)

    def test_delete(self):
        data = {"0762729401": {"first_name": "Andrii", "last_name": "Dorokhov",
                               "city": "Kharkiv", "country": "Ukraine"}}
        ph_number_to_delete = "0762729401"
        result = delete(data, ph_number_to_delete)
        self.assertEqual(result, {})

    def test_update(self):
        data = {"0762729401": {"first_name": "Andrii"}}
        data_to_update = {"0762729401": {"first_name": "Christina"}}
        result = update(data, data_to_update)
        dict_test = {"0762729401": {"first_name": "Christina"}}
        self.assertEqual(result, dict_test)


if __name__ == '__main__':
    main()
