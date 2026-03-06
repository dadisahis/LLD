from abc import ABC, abstractmethod

# Mediator interface
class UIMEdator(ABC):
    @abstractmethod
    def component_changed(self, component):
        pass

class UIComponent(ABC):
    def __init__(self, mediator):
        self.mediator = mediator
    def notify_mediator(self):
        self. mediator.component_changed(self)


class TextField(UIComponent):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.text = ""

    def set_text(self, text):
        self.text = text
        print(f"TextField: Setting text to '{self.text}'")
        self.notify_mediator()

    def get_text(self):
        return self.text
    
class Button(UIComponent):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.enabled = False
    
    def click(self):
        if self.enabled:
            print("Button: Clicked!")
            self.notify_mediator()
        else:
            print("Button: Disabled, cannot click.")

    def set_enabled(self, enabled):
        self.enabled = enabled
        state = "enabled" if enabled else "disabled"
        print(f"Button: Now {state}.")

class LoginMediator(UIMEdator):
    def __init__(self):
        self.username_feild = None
        self.password_feild = None
        self.login_button = None
    
    def set_username_field(self, field):
        self.username_feild = field
    def set_password_field(self, field):
        self.password_feild = field

    def set_login_button(self, button):
        self.login_button = button
    
    def component_changed(self, component):
        if component == self.username_feild or component == self.password_feild:
            enable = self.username_feild.get_text() != "" and self.password_feild.get_text() != ""
            self.login_button.set_enabled(enable)
        elif component == self.login_button:
            username = self.username_feild.get_text()
            password = self.password_feild.get_text()
            if username == "admin" and password == "password":
                print("LoginMediator: Login successful!")
            else:
                print("LoginMediator: Login failed!")