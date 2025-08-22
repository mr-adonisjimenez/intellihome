import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from intellihome.devices import SmartDevice, SmartLight

class TestSmartDevice(unittest.TestCase):
    """Tests for the SmartDevice class."""

    def setUp(self):
        """Set up a new SmartDevice before each test."""
        self.device = SmartDevice("Test Device")

    def test_initial_status_is_off(self):
        self.assertEqual(self.device.status, "off")

    def test_turn_on(self):
        self.device.turn_on()
        self.assertEqual(self.device.status, "on")

    def test_turn_off(self):
        self.device.status = "on"  # Start with the device on
        self.device.turn_off()
        self.assertEqual(self.device.status, "off")

    def test_get_status(self):
        self.assertEqual(self.device.get_status(), "Test Device: off")
        self.device.turn_on()
        self.assertEqual(self.device.get_status(), "Test Device: on")

class TestSmartLight(unittest.TestCase):
    """Tests for the SmartLight class."""

    def setUp(self):
        """Set up a new SmartLight before each test."""
        self.light = SmartLight("Test Light")

    def test_initial_brightness(self):
        self.assertEqual(self.light.brightness, 100)

    def test_set_valid_brightness(self):
        self.light.set_brightness(50)
        self.assertEqual(self.light.brightness, 50)
        self.light.set_brightness(0)
        self.assertEqual(self.light.brightness, 0)
        self.light.set_brightness(100)
        self.assertEqual(self.light.brightness, 100)

    def test_set_invalid_brightness(self):
        with self.assertRaises(ValueError):
            self.light.set_brightness(101)
        with self.assertRaises(ValueError):
            self.light.set_brightness(-1)

    def test_get_status_with_brightness(self):
        self.assertEqual(self.light.get_status(), "Test Light: off, Brightness: 100%")
        self.light.turn_on()
        self.light.set_brightness(75)
        self.assertEqual(self.light.get_status(), "Test Light: on, Brightness: 75%")

if __name__ == '__main__':
    unittest.main()
