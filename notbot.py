#!/usr/bin/env python

import sys
import socket
import yaml
from random import choice

HOST = "irc.bne.redhat.com"
PORT = 6667
CHANNEL = '#test4bot'
NICK = "notbot"
IDENT = "notbot"
REALNAME = "NotBot"
SOURCEFILE = "voice.yaml"

voice = yaml.load(open(SOURCEFILE))

s = socket.socket()
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s\r\n" % CHANNEL)
s.send("PRIVMSG %s :Hi everybody!  No way I'm not a notbot.\r\n" % CHANNEL)

while True:
    data = s.recv (1024)
    if data.find('PING') != -1:
        s.send('PONG ' + data.split()[1] + '\r\n')
    elif data.find(NICK) != -1 and data.find('PRIVMSG') != -1:
        print data
        found = False
        for command in voice:
            if data.find(command) != -1:
                found = True
                response = choice(voice[command])
                s.send('PRIVMSG %s :%s\r\n' % (CHANNEL, response))
                if command == 'quit' or command == 'bye':
                    s.close()
        if found == False: # need to account for invalid commands without spamming the list
            response = choice(voice['badcommand'])
            s.send('PRIVMSG %s :%s\r\n' % (CHANNEL, response))