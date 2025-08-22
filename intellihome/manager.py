from typing import Dict, Optional
from intellihome.devices import SmartDevice

class DeviceManager:
    """Manages all smart devices in the home."""

    def __init__(self):
        self._devices: Dict[str, SmartDevice] = {}

    def add_device(self, device: SmartDevice):
        """Adds a new device to the manager."""
        self._devices[device.device_id] = device

    def get_device(self, device_id: str) -> Optional[SmartDevice]:
        """Retrieves a device by its ID."""
        return self._devices.get(device_id)

    def list_devices(self) -> list[SmartDevice]:
        """Lists all devices."""
        return list(self._devices.values())

    def remove_device(self, device_id: str) -> bool:
        """Removes a device by its ID. Returns True if successful."""
        if device_id in self._devices:
            del self._devices[device_id]
            return True
        return False
