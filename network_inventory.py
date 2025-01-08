#!/usr/bin/python3

import yaml

def inventory():

  router_list = {}
  router_list['Local_Switch'] = '0cc05e660000'
  router_list['User_Network'] = '0ce0f20b0000'
  router_list['ACCT_Network'] = '0c4034070000'
  router_list['MGMT_Networ'] = '0ccc785d0000'
  router_list['IT_Network'] = '0c1cb2850000'

  inventory = dict(all = dict (
    children = dict(
      EXOS = dict(
        hosts = router_list,
        vars = dict(
            RAM = '512',
            vCPUs = '1',
            QEMU = '/usr/bin/qemu-system-x86_64(v4.2.1)',
            BootPriority = 'CD/DVD-ROM or HDD',
            OnClose = 'Power off the VM',
            ConsoleType = 'telnet',
            Adapters = '13',
            Type = 'Realtek 8139 Ethernet (rtl8139)',
            ReplicateNetworkConnectionStatesInQEMU = 'True'
          )
        )
      )
    )
  )

  return inventory

def main():
  with open('/home/student/ansible/D417/inventory_exos.yml', 'w') as outfile:
    yaml.dump(inventory(), outfile, default_flow_style=False)

if __name__ == "__main__":
    main()
