import zmq
import sys

msgport = "5556"

if len(sys.argv) > 1:
    msgport = sys.argv[1]
    msgport = int(msgport)

context = zmq.Context()
msgsocket = context.socket(zmq.REP)
msgsocket.bind("tcp://*:{}".format(msgport))

pubport = "5557"

if len(sys.argv) > 2:
    pubport = sys.argv[2]
    pubport = int(pubport)

pubsocket = context.socket(zmq.PUB)
pubsocket.bind("tcp://*:{}".format(pubport))

while True:
    message = msgsocket.recv_json()
    print("Got message: ", message)
    pubsocket.send_string(message["topic"] + " " + message["from"] + " " + message["contents"])
    msgsocket.send_json("OK")