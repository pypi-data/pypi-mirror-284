import sys

def main(args):
    print(args)
    id_config = './.appid'
    key_config = './.appkey'
    secret_config = './.secret'
    cluster_config = './.cluster'
    channel_name = './.channel'
    user_name = './.username'
    channel = ''
    username = ''
    if(not len(args) <= 0):
        if(args[0] == 'pusher'):
            if(len(args) == 5):
                app_id = args[1]
                app_key = args[2]
                secret = args[3]
                cluster = args[4]
                file = open(id_config, 'w')
                file.write(app_id)
                file = open(key_config, 'w')
                file.write(app_key)
                file = open(secret_config, 'w')
                file.write(secret)
                file = open(cluster_config, 'w')
                file.write(cluster)
                exit()
        elif(len(args) == 1):
            channel = args[0]
            file = open(channel_name, 'w')
            file.write(channel)
            exit()
        elif(len(args) == 2):
            channel = args[0]
            username = args[1]
            file = open(channel_name, 'w')
            file.write(channel)
            file = open(user_name, 'w')
            file.write(username)
            exit()
    print("Type 'chat help' for guidance")