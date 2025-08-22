import unittest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from intellihome.devices import SmartDevice, SmartLight
from intellihome.manager import DeviceManager

class TestDeviceManager(unittest.TestCase):
    """Tests for the DeviceManager class."""

    def setUp(self):
        """Set up a new DeviceManager and some devices before each test."""
        self.manager = DeviceManager()
        self.device1 = SmartDevice("Lamp")
        self.light1 = SmartLight("Overhead Light")
        self.manager.add_device(self.device1)
        self.manager.add_device(self.light1)

    def test_add_device(self):
        # The setUp method already adds devices, so we just check them
        self.assertEqual(len(self.manager.list_devices()), 2)
        # Test adding another device
        device3 = SmartDevice("Fan")
        self.manager.add_device(device3)
        self.assertEqual(len(self.manager.list_devices()), 3)
        self.assertIn(device3, self.manager.list_devices())

    def test_get_device(self):
        retrieved_device = self.manager.get_device(self.device1.device_id)
        self.assertIs(retrieved_device, self.device1)

    def test_get_nonexistent_device(self):
        self.assertIsNone(self.manager.get_device("nonexistent-id"))

    def test_list_devices(self):
        devices = self.manager.list_devices()
        self.assertEqual(len(devices), 2)
        self.assertIn(self.device1, devices)
        self.assertIn(self.light1, devices)

    def test_list_devices_empty(self):
        manager = DeviceManager()
        self.assertEqual(manager.list_devices(), [])

    def test_remove_device(self):
        device_id = self.device1.device_id
        self.assertTrue(self.manager.remove_device(device_id))
        self.assertIsNone(self.manager.get_device(device_id))
        self.assertEqual(len(self.manager.list_devices()), 1)

    def test_remove_nonexistent_device(self):
        self.assertFalse(self.manager.remove_device("nonexistent-id"))
        self.assertEqual(len(self.manager.list_devices()), 2)

if __name__ == '__main__':
    unittest.main()
