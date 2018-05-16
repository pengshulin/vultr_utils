#!/usr/bin/env python
# coding:utf8
# destroy all remote servers
# Peng Shulin <trees_peng@163.com> 2018
import os
import sys
import vultr

VULTR_API=os.getenv('VULTR_API','')
if len(VULTR_API) != 36:
    print('VULTR_API error')
    sys.exit(1)

v = vultr.vultr.Vultr(VULTR_API)
server_list = v.server_list()
for sid in server_list:
    #print server_list[sid]
    location = server_list[sid]['location']
    main_ip = server_list[sid]['main_ip']
    print 'Destroying server %s, %s'% (location, main_ip)
    v.server_destroy( sid )

