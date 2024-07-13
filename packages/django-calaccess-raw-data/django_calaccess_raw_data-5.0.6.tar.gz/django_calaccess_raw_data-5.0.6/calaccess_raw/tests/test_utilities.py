"""
Tests for the utilities storied in app's __init__.py file.
"""
# Testing
from django.test import TestCase
from django.test.utils import override_settings

# Stuff to test
import calaccess_raw

# Logging
import logging

logger = logging.getLogger(__name__)


class UtilityTestCase(TestCase):
    """
    Tests related to our hodgepodge of utilities.
    """

    multi_db = True

    @override_settings(CALACCESS_DATA_DIR=None)
    @override_settings(BASE_DIR=None)
    def test_dir_errors(self):
        """
        Test error expected when download directory is missing.
        """
        with self.assertRaises(ValueError):
            calaccess_raw.get_data_directory()

    @override_settings(CALACCESS_DATA_DIR="/foo/bar/")
    def test_dir_configured(self):
        """
        Tests for directory functions __init__.py file.
        """
        calaccess_raw.get_data_directory()

    @override_settings(CALACCESS_DATA_DIR=None)
    @override_settings(BASE_DIR="/foo/bar/")
    def test_dir_basedir(self):
        """
        Tests for directory functions __init__.py file with different settings.
        """
        calaccess_raw.get_data_directory()

    def test_model_methods(self):
        """
        Test the methods that hook up with our models.
        """
        calaccess_raw.get_model_list()
