#!/usr/bin/env python3

def main():
    hostipdict = {'host01':'10.0.2.3', 'host02':'192.168.3.3', 'host03':'72.4.23.22'}

    ## Display the current state of our dictionary
    print(hostipdict)

    ## add another entry to the dict
    hostipdict['host04'] = '10.23.43.224'

    ## Display the dict with the new entry for host04
    print(hostipdict)

    ## rewrite the value for host02
    hostipdict['host02'] = '192.168.70.55'

    ## Display the dict with the new entry applied
    print(hostipdict)

    ## recall from the dict
    ## 'host02' should now point to '192.168.70.55'
    hostipdict['host02']

    ## This will cause a key error
    ## toast01 is not a key
     hostipdict['toast01']

main()
