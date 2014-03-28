import sys
import socket
#import string

HOST="irc.freenode.net"
PORT=6667
CHANNEL='#test4notbot'
NICK="notbot"
IDENT="notbot"
REALNAME="NotBot"

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
   if data.find('!notbot quit') != -1:
      s.send("PRIVMSG %s :Fine, if you don't want me here, I'll go where I'm appreciated.\r\n" % CHANNEL)
      s.send('QUIT\r\n')
      sys.exit()
   if data.find('hi notbot' ) != -1:
      s.send('PRIVMSG %s :I already said hi...\r\n' % CHANNEL)
   if data.find('hello notbot' ) != -1:
      s.send('PRIVMSG %s :I already said hi...\r\n' % CHANNEL)
   if data.find('KICK') != -1:
      s.send ('JOIN %s\r\n' % CHANNEL)
   if data.find('cheese') != -1:
      s.send('PRIVMSG %s :Cheese? WHERE?!?!?!?!?!\r\n' % CHANNEL)
   if data.find('slaps notbot') != -1:
      s.send('PRIVMSG %s :That was totally unnecessary!\r\n' % CHANNEL)