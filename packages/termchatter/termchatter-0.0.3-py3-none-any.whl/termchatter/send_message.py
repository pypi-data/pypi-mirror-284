import os.path
import pusher
import sys
sys.dont_write_bytecode = True
import pusher_checker

key_config = './.appkey'
cluster_config = './.cluster'
channel_name = './.channel'
user_name = './.username'
app_key = ''
cluster = ''
if(not os.path.exists(channel_name) or not os.path.exists(user_name) or not pusher_checker.checker()):
    print("Channel, username, or Pusher not setup")
    exit()
else:
    file = open(channel_name, 'r')
    channel = file.read().replace('\n', '')
    file = open(user_name, 'r')
    username = file.read().replace('\n', '')
    file = open(key_config, 'r')
    app_key = file.read().replace('\n', '')
    file = open(cluster_config, 'r')
    cluster = file.read().replace('\n', '')
    

pusher_client = pusher.Pusher(
  app_id='1833217',
  key=app_key,
  secret='bf0a41c17f86bd5baaca',
  cluster=cluster,
  ssl=True
)

if(len(sys.argv) == 2):
    message = sys.argv[1]
else:
    print("Put your message as argument, use quotes to send messages with spaces")
    exit()

pusher_client.trigger(channel, 'message', {'username': username, 'message': message})