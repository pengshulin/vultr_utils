#!/usr/bin/env python
# coding:utf8
# sync all startup_*.sh with remote vultr
# Peng Shulin <trees_peng@163.com> 2018
import os
import sys
import glob
import vultr

VULTR_API=os.getenv('VULTR_API','')
if len(VULTR_API) != 36:
    print('VULTR_API error')
    sys.exit(1)

scripts_list=glob.glob('startup_*.sh')
v = vultr.vultr.Vultr(VULTR_API)
original_list = v.startupscript_list()
for sid in original_list:
    name = original_list[sid]['name']
    remote_script = original_list[sid]['script']
    #print sid, name
    if not 'startup_'+name in scripts_list:
        print 'Deleting remote script %s ...'% (name)
        v.startupscript_destroy( sid )
    else:
        local_script=open('startup_'+name,'r').read()
        if local_script == remote_script:
            print 'Ignore script %s'% (name)
        else:
            print 'Updating script %s'% (name)
            v.startupscript_update( sid, name, local_script )
        scripts_list.remove('startup_'+name)
           
for name in scripts_list:
    print 'Uploading new script %s'% name[8:]
    local_script=open(name,'r').read()
    v.startupscript_create( name[8:], local_script )

