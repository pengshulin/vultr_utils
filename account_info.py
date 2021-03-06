#!/usr/bin/env python
# coding:utf8
# display account infomation
# Peng Shulin <trees_peng@163.com> 2018
import os
import sys
import vultr
import pprint

VULTR_API=os.getenv('VULTR_API','')
if len(VULTR_API) != 36:
    print('VULTR_API error')
    sys.exit(1)

v = vultr.vultr.Vultr(VULTR_API)

info = v.account_info()
pprint.pprint(info)

