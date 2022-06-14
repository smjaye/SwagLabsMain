import unittest
import swaglabs_locators as locators
import swaglabs_methods as methods


class SwagLabsAppPositiveTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs @classmethod)
    def test_main_swag_labs_app():
        methods.setUp()
        methods.log_in()
        methods.my_cart()
        methods.check_out()
        methods.log_out()
        methods.tearDown()













