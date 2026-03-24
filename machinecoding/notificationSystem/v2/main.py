from entities.Notification import Notification
from entities.enums import *
from entities.Recipient import Recipient
from NotificationService import NotifService

def main():

    service = NotifService(10)
    rc1 = Recipient('Adi', 'adi@gmail.com', "12345")
    rc2 = Recipient("Anu", "anu@gmail.com")

    notif1 = Notification.Builder(type=NotifType.EMAIL, recipient=rc1).set_subject("Email 1").set_message("This is an Email").build()
    notif2 = Notification.Builder(type=NotifType.EMAIL, recipient=rc2).set_subject("Email 2").set_message("This is an Email 2").build()

    notif3 = Notification.Builder(type=NotifType.SMS, recipient=rc1).set_message("This is an SMS 1").build()

    print("---------Sending Notificaiton---------")
    service.send_notif(notification=notif1)
    service.send_notif(notification=notif2)
    service.send_notif(notification=notif3)
    service.shutdown()


if __name__ == '__main__':
    main()