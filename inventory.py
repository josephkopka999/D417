#!/usr/bin/env python3

# import configparser

#import configparser


#config = configparser.ConfigParser()

#config.add_section('Switches')
#config.set('Local_Switch','512 MB','1','/usr/bin/qemu-system-x86_64(v4.2.1)','CD/DVD-ROM or HDD','Power off the VM','telnet','13','0c:c0:5e:66:00:00','Realtek 8139 Ethernet (rtl8139)','True')
#config.set('User_Network','512 MB','1','/usr/bin/qemu-system-x86_64(v4.2.1)','CD/DVD-ROM or HDD','Power off the VM','telnet','13','0c:e0:f2:0b:00:00','Realtek 8139 Ethernet (rtl8139)','True')
#config.set('ACCT_Network','512 MB','1','/usr/bin/qemu-system-x86_64(v4.2.1)','CD/DVD-ROM or HDD','Power off the VM','telnet','13','0c:40:34:07:00:00','Realtek 8139 Ethernet (rtl8139)','True')
#config.set('MGMT_Network','512 MB','1','/usr/bin/qemu-system-x86_64(v4.2.1)','CD/DVD-ROM or HDD','Power off the VM','telnet','13','0c:cc:78:5d:00:00','Realtek 8139 Ethernet (rtl8139)','True')
#config.set('IT_Network','512 MB','1','/usr/bin/qemu-system-x86_64(v4.2.1)','CD/DVD-ROM or HDD','Power off the VM','telnet','13','0c:1c:b2:85:00:00','Realtek 8139 Ethernet (rtl8139)','True')


#config.add_section('Computers')
#config.set('WindowsDesktop-1','4096','2','/usr/bin/qemu-system-x86_64(v4.2.1)','HDD','Send the shutdown signal (ACPI)','vnc','1','0c:4b:3c:0a:00:00','Intel Gigabit Ethernet (e1000)','true')
#config.set('WindowsDesktop-2','4096','2','/usr/bin/qemu-system-x86_64(v4.2.1)','HDD','Send the shutdown signal (ACPI)','vnc','1','0c:59:fd:86:00:00','Intel Gigabit Ethernet (e1000)','true')
#config.set('WindowsDesktop-3','4096','2','/usr/bin/qemu-system-x86_64(v4.2.1)','HDD','Send the shutdown signal (ACPI)','vnc','1','0c:e2:0f:f3:00:00','Intel Gigabit Ethernet (e1000)','true')
#config.set('WindowsDesktop-4','4096','2','/usr/bin/qemu-system-x86_64(v4.2.1)','HDD','Send the shutdown signal (ACPI)','vnc','1','0c:46:74:35:00:00','Intel Gigabit Ethernet (e1000)','true')

#with open('inventory.ini', 'w') as f:
#    config.write(f)


import yaml

def inventory():

  router_list = {}
  router_list['Local_Switch'] = '0c:c0:5e:66:00:00'
  router_list['User_Network'] = '0c:e0:f2:0b:00:00'
  router_list['ACCT_Network'] = '0c:40:34:07:00:00'
  router_list['MGMT_Networ'] = '0c:cc:78:5d:00:00
  router_list['IT_Network'] = '0c:1c:b2:85:00:00'

  inventory = dict(all = dict (
    children = dict(
      EXOS = dict(
        hosts = router_list,
        vars = dict(
            RAM = '512',
            vCPUs = '1',
            QEMU = '/usr/bin/qemu-system-x86_64(v4.2.1)'
            Boot_Priority = 'CD/DVD-ROM or HDD'
            On_close = 'Power off the VM'
            Console_type = 'telnet'
            Adapters = '13'
            Type = 'Realtek 8139 Ethernet (rtl8139)'
            ReplicateNetworkConnectionStatesInQEMU = 'True'
          )
        )
      )
    )
  )

  return inventory

def main():
  with open('/home/student/ansible/D417/inventory.yml', 'w') as outfile:
    yaml.dump(inventory(), outfile, default_flow_style=False)

if __name__ == "__main__":
    main()