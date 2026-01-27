from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light:
    def on(self):
        print("Light is ON")

    def off(self):
        print("Light is OFF")

class Thermostat:
    def __init__(self):
        self.temperature = 20  # Default temperature in Celsius
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Thermostat set to {self.temperature}°C")

    def get_temperature(self):
        return self.temperature
    

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.on()
    
    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.off()
    
    def undo(self):
        self.light.on()

class SetTemperatureCommand(Command):
    def __init__(self, thermostat: Thermostat, temperature: int):
        self.thermostat = thermostat
        self.temperature = temperature
        self.prev_temperature = None
    
    def execute(self):
        self.prev_temperature = self.thermostat.get_temperature()
        self.thermostat.set_temperature(self.temperature)
    def undo(self):
        self.thermostat.set_temperature(self.prev_temperature)


    
class RemoteControl:
    def __init__(self):
        self.curr_command = None
        self.history = []
    
    def set_command(self, command:Command):
        self.curr_command = command

    def press_execute(self):
        if self.curr_command:
            self.curr_command.execute()
            self.history.append(self.curr_command)
        else:
            print("No command set.")
    def press_undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("No command to undo.")


