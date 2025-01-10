#!/usr/bin/python3

import yaml

def inventory():

  windows_list = {}
  windows_list['WindowsDesktop-1'] = '0c4b3c0a0000'
  windows_list['WindowsDesktop-2'] = '0c59fd860000'
  windows_list['WindowsDesktop-3'] = '0ce20ff30000'
  windows_list['WindowsDesktop-4'] = '0c4674350000'

  inventory = dict(all = dict (
    children = dict(
      Windows = dict(
        hosts = windows_list,
        vars = dict(
            RAM = '4096',
            vCPUs = '2',
            QEMU = '/usr/bin/qemu-system-x86_64(v4.2.1)',
            BootPriority = 'HDD',
            OnClose = 'Send the shutdown signal (ACPI)',
            ConsoleType = 'vnc',
            Adapters = '1',
            Type = 'Intel Gigabit Ethernet (e1000)',
            ReplicateNetworkConnectionStatesInQEMU = 'True'
          )
        )
      )
    )
  )

  return inventory

def main():
  with open('/home/student/ansible/D417/inventory_windows.yml', 'w') as outfile:
    yaml.dump(inventory(), outfile, default_flow_style=False)

if __name__ == "__main__":
    main()
