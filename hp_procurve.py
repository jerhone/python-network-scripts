#!/usr/bin/python2.7
#
# created by Jerhone
# email: jerhone.valledor@gmail.com

import pexpect

# Switch Credentials

sw_ip = '192.168.10.253'
sw_pass = 'password'

# Spawn Telnet 
radius_child = pexpect.spawn('telnet ' + sw_ip)
# Send a key to prompt password
radius_child.send('\x1b[A')
radius_child.expect('Password: ')
radius_child.sendline(sw_pass)
radius_child.expect ('# ')
radius_child.sendline('conf t')
radius_child.expect('\(config\)#')
radius_child.sendline('aaa authentication telnet login radius')
radius_child.expect('\(config\)#')
radius_child.sendline('aaa authentication telnet enable radius')
radius_child.expect('\(config\)#')
radius_child.sendline('radius-server retransmit 2')
radius_child.expect('\(config\)#')
radius_child.sendline('radius-server key S3creTkey')
radius_child.expect('\(config\)#')
radius_child.sendline('radius-server host 192.168.10.254 key S3creTkey acct-port 1813 auth-port 1812')
radius_child.expect('\(config\)#')
radius_child.sendline('exit')
radius_child.expect('# ')
radius_child.sendline('write memory')
radius_child.expect('# ')
radius_child.sendline('logout')
radius_child.expect('.*n]?')
radius_child.sendline('y')
print("switch has been successfully configured...")
