import sys
import subprocess

if(sys.argv[1] == "setup"):
    subprocess.call(['python3', 'setup.py', *sys.argv[2:]])
elif(sys.argv[1] == "send"):
    subprocess.call(['python3', 'send_message.py', *sys.argv[2:]])
elif(sys.argv[1] == "receive"):
    subprocess.call(['python3', 'receive_message.py'])
elif(sys.argv[1] == "help"):
    print("setup:")
    print("  termchatter setup [channel]")
    print("    Changes/sets the pusher channel you want to broadcast and receive messages to and from\n")
    print("  termchatter setup [channel] [username]")
    print("    Changes/sets both the pusher channel and username you want to use\n")
    print("  termchatter setup pusher [app id] [app key] [secret] [cluster]")
    print("    Sets up pusher\n")
    print("chat:")
    print("  termchatter send [message]")
    print("    Broadcasts a message to the pusher channel you've selected\n")
    print("  termchatter receive")
    print("    Run a listener to the pusher channel you've selected\n")
    print("Run 'termchatter receive' on a separate console")
else:
    print("Type 'termchatter help' for guidance")