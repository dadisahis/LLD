from machinecoding.pubsubSystem.v1.PubSubService import PubSubService
from entities.SubscrberStrategy import *
def main():
    service = PubSubService.get_instance()
   

    # create subscriber
    spts_1 = NewsSubscriber("spts_1")
    spts_2 = NewsSubscriber("spts_2")
    tech_1 = NewsSubscriber("tech_1")
    sys_admin = AlertSubscriber("SysAdmin")

    SPORT_TOPIC = "SPORTS"
    TECH_TOPIC = "TECH"
    SYSTEM_TOPIC = "SYSTEM"

    service.create_topic(SPORT_TOPIC)
    service.create_topic(TECH_TOPIC)
    service.create_topic(SYSTEM_TOPIC)

    service.subscribe(SPORT_TOPIC, spts_1)
    service.subscribe(SPORT_TOPIC, spts_2)
    service.subscribe(TECH_TOPIC, tech_1)
    service.subscribe(SYSTEM_TOPIC, sys_admin)


    print("Publishing message")
    service.publish(SPORT_TOPIC, Message("Team a wins"))
    service.publish(TECH_TOPIC, Message("New Iphone Launched"))
    service.publish(SPORT_TOPIC, Message("Chelsea Win"))
    service.publish(SYSTEM_TOPIC, Message("Server crash"))


    service.unsubscribe(SPORT_TOPIC, spts_2)
    service.publish(SPORT_TOPIC, Message("Arsenal Win"))
    

    service.shutdown()


if __name__ == '__main__':
    main()