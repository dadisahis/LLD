from mediator import *

def main():
    mediator = LoginMediator()

    username_field = TextField(mediator)
    password_field = TextField(mediator)    
    login_button = Button(mediator)

    mediator.set_username_field(username_field)
    mediator.set_password_field(password_field) 
    mediator.set_login_button(login_button)
    print("Attempt with wrong credentials:")
    username_field.set_text("user1")
    password_field.set_text("")
    login_button.click()

    print("\nAttempt with correct credentials:")
    username_field.set_text("admin")
    password_field.set_text("password")
    login_button.click()


if __name__ == "__main__":
    main()