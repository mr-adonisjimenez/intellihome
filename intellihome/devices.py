import uuid

class SmartDevice:
    """A base class for all smart devices."""

    def __init__(self, name: str):
        self.device_id = str(uuid.uuid4())
        self.name = name
        self.status = "off"  # Default status is off

    def turn_on(self):
        """Turns the device on."""
        self.status = "on"

    def turn_off(self):
        """Turns the device off."""
        self.status = "off"

    def get_status(self) -> str:
        """Returns the current status of the device."""
        return f"{self.name}: {self.status}"


class SmartLight(SmartDevice):
    """A smart light that can be turned on/off and have its brightness adjusted."""

    def __init__(self, name: str):
        super().__init__(name)
        self.brightness = 100

    def set_brightness(self, brightness: int):
        """Sets the brightness of the light."""
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            raise ValueError("Brightness must be between 0 and 100.")

    def get_status(self) -> str:
        """Returns the current status of the light, including brightness."""
        status = super().get_status()
        return f"{status}, Brightness: {self.brightness}%"
