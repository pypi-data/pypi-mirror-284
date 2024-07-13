import sys

id_config = './.appid'
key_config = './.appkey'
secret_config = './.secret'
cluster_config = './.cluster'
channel_name = './.channel'
user_name = './.username'
channel = ''
username = ''
if(not len(sys.argv) <= 1):
    if(sys.argv[1] == 'pusher'):
        if(len(sys.argv) == 6):
            app_id = sys.argv[2]
            app_key = sys.argv[3]
            secret = sys.argv[4]
            cluster = sys.argv[5]
            file = open(id_config, 'w')
            file.write(app_id)
            file = open(key_config, 'w')
            file.write(app_key)
            file = open(secret_config, 'w')
            file.write(secret)
            file = open(cluster_config, 'w')
            file.write(cluster)
            exit()
    elif(len(sys.argv) == 2):
        channel = sys.argv[1]
        file = open(channel_name, 'w')
        file.write(channel)
        exit()
    elif(len(sys.argv) == 3):
        channel = sys.argv[1]
        username = sys.argv[2]
        file = open(channel_name, 'w')
        file.write(channel)
        file = open(user_name, 'w')
        file.write(username)
        exit()
print("Type 'chat help' for guidance")