#!/usr/bin/env python3

def main():
    firewalldict = {'sip':'5060', 'ssh':'22', 'http':'80'}

    ## Display the current state of our dictionary
    print(firewalldict)

    ## Add another entry to the dict
    ## Notice that https maps to an INT, not a STRING
    firewalldict['https'] = 443

    ## Display the dict with the new entry for host4
    print(firewalldict)

    ## Display some dictionary data
    print('The print statement can be passed multiple items, provided they are separate by commas')
    print("The port in use for HTTP Secure is:", firewalldict['https'])

    ## This SHOULD fail but it will not because we are using the .get method
    print("A safer way to recall that data is to use the .get method:", \
      firewalldict.get('razzledazzlerootbeer'))

    ## Use the .keys method to return a list of keys
    print(firewalldict.keys())

    ## Use the .values method to return a list of values
    print(firewalldict.values())

main()
