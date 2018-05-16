#!/usr/bin/env python
# coding:utf8
# create one remote server
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

print('Gathering info ...')

print('===================')
print('1. region list')
regions = v.regions_list()
pprint.pprint( regions )

print('===================')
print('2. plan list')
plans = v.plans_list()
pprint.pprint( plans )

print('===================')
print('3. os list')
oss = v.os_list()
pprint.pprint( oss )

print('===================')
print('4. sshkey list')
sshkeys = v.sshkey_list()
pprint.pprint( sshkeys )

print('===================')
print('5. startupscript list')
scripts = v.startupscript_list()
pprint.pprint( scripts )


DEFAULT_REGION='Tokyo'
#DEFAULT_REGION='Seattle'
#DEFAULT_REGION='Sydney'
#DEFAULT_REGION='Singapore'
#DEFAULT_REGION='Silicon Valley'
DEFAULT_PLAN='1024 MB RAM,25 GB SSD,1.00 TB BW'
DEFAULT_OS='Ubuntu 16.04 x64'
DEFAULT_SSHKEY='trees-ThinkPad-E570'
DEFAULT_SCRIPT='ubuntu_postinst.sh'

# name/id transform
for i in regions:
    if regions[i]['name'] == DEFAULT_REGION:
        DEFAULT_REGION = int(i)
for i in plans:
    if plans[i]['name'] == DEFAULT_PLAN:
        DEFAULT_PLAN = int(i)
for i in oss:
    if oss[i]['name'] == DEFAULT_OS:
        DEFAULT_OS = int(i)
for i in sshkeys:
    if sshkeys[i]['name'] == DEFAULT_SSHKEY:
        DEFAULT_SSHKEY = i
for i in scripts:
    if scripts[i]['name'] == DEFAULT_SCRIPT:
        DEFAULT_SCRIPT = int(i)


# recheck for available region
if not DEFAULT_REGION in plans[str(DEFAULT_PLAN)]['available_locations']:
    print( "regions not available for default plan" )
    print( 'required %s'% DEFAULT_REGION )
    print( 'available %s'% plans['DEFAULT_PLAN']['available_locations'] )
    sys.exit(1)


# get formal ID
dcid=int(regions[str(DEFAULT_REGION)]['DCID'])
vpsplanid=plans[str(DEFAULT_PLAN)]['VPSPLANID']
osid=oss[str(DEFAULT_OS)]['OSID']
sshkeyid=sshkeys[DEFAULT_SSHKEY]['SSHKEYID']
scriptid=scripts[str(DEFAULT_SCRIPT)]['SCRIPTID']

print('===================')
print( 'DCID:      %s'% dcid )
print( 'VPSPLANID: %s'% vpsplanid )
print( 'OSID:      %s'% osid )
print( 'SSHKEYID:  %s'% sshkeyid )
print( 'SCRIPTID:  %s'% scriptid )

print('===================')
print('Creating server ...')
v.server_create( dcid, vpsplanid, osid, 
        scriptid=scriptid, sshkeyid=sshkeyid )
        

