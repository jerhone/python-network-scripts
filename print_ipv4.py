#!/usr/bin/python


import socket, sys

foo = open(sys.argv[1])
hosts = [ host.strip() for host in foo.readlines() ]

for host in hosts:
    fqdn = socket.gethostbyname(host)
    print 'The IP Address of %s is %s' % (host, fqdn)

