from NotificationService import NotificationService
from entities.Recipient import Recipient
from entities.Notification import *
def main():
    notif_service = NotificationService(10)

    rec1 = Recipient("123",'adi@mail.com', 'pushToken123', None)
    rec2 = Recipient("345",'anu@mail.com', None, '9992229929')


    welcome_email =  Notification.Builder(rec1, NotificationType.EMAIL).set_subject("Welcome").set_message("Hi, WEclome to the platform").build()
    notif_service.send_notif(welcome_email)


    sms_notif =  Notification.Builder(rec2, NotificationType.SMS).set_message("Hi, This is a push notif to the platform").build()
    notif_service.send_notif(sms_notif)


    push_notif =  Notification.Builder(rec2, NotificationType.PUSH).set_message("Hi, This is a push notif to the platform").build()
    notif_service.send_notif(push_notif)


    print("Shutdown")
    notif_service.shutdown()

if __name__ == '__main__':
    main()


