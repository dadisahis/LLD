from PubSubService import PubSubService
from entities.Message import Message
from entities.Subscribers import *
from entities.Topic import Topic


def main():
    service = PubSubService.get_instance()

    spts_sbc1= AdSubscriber("Sports Sub 1")
    spts_sbc2= AdSubscriber("Sports Sub 2")
    tech_sbc= AdSubscriber("Tech Sub")


    SPORT_TOPIC = "SPORT_TOPIC"
    TECH_TOPIC = "TECH_TOPIC"

    service.create_topic(SPORT_TOPIC)
    service.create_topic(TECH_TOPIC)

    service.subscribe(SPORT_TOPIC, spts_sbc1)
    service.subscribe(SPORT_TOPIC, spts_sbc2)
    service.subscribe(TECH_TOPIC, tech_sbc)

    service.publish(SPORT_TOPIC, Message("Sport AD 1"))
    service.publish(SPORT_TOPIC, Message("Sport AD 2"))
    service.publish(SPORT_TOPIC, Message("Sport AD 3"))


    service.publish(TECH_TOPIC, Message("Tech AD 1"))

    service.unsubscribe(SPORT_TOPIC, spts_sbc2)
    service.publish(SPORT_TOPIC, Message("Sport AD 4"))

    service.shutdown()

if __name__ == '__main__':
    main()