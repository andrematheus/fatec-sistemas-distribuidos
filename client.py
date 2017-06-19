import sys
import zmq
import threading

name = sys.argv[1]

topic = sys.argv[2]

port = "5557"

context = zmq.Context()
subsocket = context.socket(zmq.SUB)

subsocket.connect("tcp://localhost:{}".format("5557"))

subsocket.setsockopt_string(zmq.SUBSCRIBE, topic)


sendsocket = context.socket(zmq.REQ)
sendsocket.connect("tcp://localhost:{}".format("5556"))


def receive_messages():
    print("Starting receive thread")
    while True:
        message = subsocket.recv_string()
        fr, message = message.split(" ", 2)[1:]
        if fr.strip() != name:
            print("{}: {}".format(fr, message))


t = threading.Thread(target=receive_messages)


t.start()


def send(contents):
    sendsocket.send_json({
        "topic": topic,
        "from": name,
        "contents": contents
    })
    msg = sendsocket.recv_json()
    if msg != "OK":
        print("Error sending: ", msg)


for line in sys.stdin:
    send(line.strip())