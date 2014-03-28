#!/usr/bin/env python

import sys
import socket
import yaml
from random import choice

HOST = "irc.bne.redhat.com"
PORT = 6667
CHANNEL = '#test4notbot'
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
   elif data.find(NICK):
      for command in voice:
         if data.find(command) != -1:
            response = voice[command][0]
            s.send('PRIVMSG %s :%s\r\n' % (CHANNEL, response))
   
   # need to account for invalid commands
   # s.send('PRIVMSG %s :Unknown command\r\n' % (CHANNEL))