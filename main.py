from intellihome.devices import SmartDevice, SmartLight
from intellihome.manager import DeviceManager

def print_help():
    """Prints the available commands."""
    print("\nAvailable commands:")
    print("  add light <name>      - Adds a new smart light.")
    print("  add device <name>     - Adds a new generic smart device.")
    print("  list                  - Lists all devices.")
    print("  turn on <device_id>   - Turns a device on.")
    print("  turn off <device_id>  - Turns a device off.")
    print("  brightness <device_id> <level> - Sets the brightness of a light (0-100).")
    print("  remove <device_id>    - Removes a device.")
    print("  help                  - Shows this help message.")
    print("  exit                  - Exits the application.")

def main():
    """Main function to run the CLI."""
    manager = DeviceManager()
    print("Welcome to Intellihome!")
    print_help()

    while True:
        try:
            command = input("\nEnter command > ").strip().lower()
            parts = command.split()

            if not parts:
                continue

            action = parts[0]

            if action == "add":
                if len(parts) >= 3:
                    device_type = parts[1]
                    name = " ".join(parts[2:])
                    if device_type == "light":
                        light = SmartLight(name)
                        manager.add_device(light)
                        print(f"Added light '{name}' with ID: {light.device_id}")
                    elif device_type == "device":
                        device = SmartDevice(name)
                        manager.add_device(device)
                        print(f"Added device '{name}' with ID: {device.device_id}")
                    else:
                        print("Unknown device type. Use 'light' or 'device'.")
                else:
                    print("Usage: add <light|device> <name>")

            elif action == "list":
                devices = manager.list_devices()
                if not devices:
                    print("No devices found.")
                else:
                    print("\n--- All Devices ---")
                    for device in devices:
                        print(f"  ID: {device.device_id} | {device.get_status()}")
                    print("--------------------")

            elif action == "turn" and len(parts) == 3:
                sub_action, device_id = parts[1], parts[2]
                device = manager.get_device(device_id)
                if device:
                    if sub_action == "on":
                        device.turn_on()
                        print(f"Turned on {device.name}.")
                    elif sub_action == "off":
                        device.turn_off()
                        print(f"Turned off {device.name}.")
                    else:
                        print("Usage: turn <on|off> <device_id>")
                else:
                    print("Device not found.")

            elif action == "brightness" and len(parts) == 3:
                device_id, level_str = parts[1], parts[2]
                device = manager.get_device(device_id)
                if isinstance(device, SmartLight):
                    try:
                        level = int(level_str)
                        device.set_brightness(level)
                        print(f"Set brightness for {device.name} to {level}%.")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Device not found or is not a light.")

            elif action == "remove" and len(parts) == 2:
                device_id = parts[1]
                if manager.remove_device(device_id):
                    print(f"Device {device_id} removed.")
                else:
                    print("Device not found.")

            elif action == "help":
                print_help()

            elif action == "exit":
                print("Goodbye!")
                break

            else:
                print("Unknown command. Type 'help' for a list of commands.")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
