
Functional Requirements:
1. Support 3 types of notif: EMAIL, SMS, PUSH
2. Exponential Backoff on failed deliveries
3. Async delivery. System should not block while sending notif
4. Send one notif. No bulk notif

NFR:
1. OOPs
2. extensible
3. non blocking

Entities
1. ENUM -> NotificationType
2. Notification - Core Data Class - Builder Class
3. NotificationGateway - Interface -- send() method iss defined which is to be implemented
4. EmailGateway, SMSGateway, PushGateway
5. RetryGateway - Decorator class for exponential backoff 
6. NotificationFactory - Will have a map of notification type and gateway
7. Recipient - Data class 
8. Notification Service
9. Main Class
