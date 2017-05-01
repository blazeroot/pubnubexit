
import time
import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration, PNHeartbeatNotificationOptions
from pubnub.pubnub import PubNub

import keys.keys as keys

my_channel = "my_channel_1234"

pnconfig = PNConfiguration()
pnconfig.subscribe_key = keys.SUBSCRIBE_KEY
pnconfig.publish_key = keys.PUBLISH_KEY
# pnconfig.heartbeat_notification_options = PNHeartbeatNotificationOptions.ALL

my_pubnub = PubNub(pnconfig)


def my_publish_callback(envelope, status):
    print('my_publish_callback', status.is_error(), datetime.datetime.now())


class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        print('presence', pubnub, presence)

    def status(self, pubnub, status):
        print('status.category', status.category, datetime.datetime.now())

    def message(self, pubnub, message):
        print('message', pubnub.timestamp(), message.message, datetime.datetime.now())

print()
print('*** start ***')
my_listener = MySubscribeCallback()
my_pubnub.add_listener(my_listener)
my_pubnub.subscribe().channels(my_channel).execute()
my_pubnub.publish().channel(my_channel).message(['hello', 'there', my_channel]).async(my_publish_callback)
time.sleep(5)  # long enough for message to be received
my_pubnub.remove_listener(my_listener)
my_pubnub.unsubscribe().channels(my_channel).execute()
my_pubnub.stop()
print('done!', datetime.datetime.now())
