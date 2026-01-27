from command import *

def main():
    light = Light()
    thermostat = Thermostat()

    lighon = LightOnCommand(light)
    lightoff = LightOffCommand(light)
    thermostat_set_25 = SetTemperatureCommand(thermostat, 25)

    remote = RemoteControl()

    print("Pressing Light on")
    remote.set_command(lighon)
    remote.press_execute()
    
    print("Pressing Light off")
    remote.set_command(lightoff)
    remote.press_execute()

    print("Pressing Thermostat set to 25")
    remote.set_command(thermostat_set_25)
    remote.press_execute()

    print("Undoing last command")
    remote.press_undo()

    print("Undoing last command")
    remote.press_undo()

    print("Undoing last command")
    remote.press_undo()


if __name__ == "__main__":
    main()