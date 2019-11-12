#!/usr/bin/env python3

def main():
    vendordict = {'cisco': True, 'juniper': False, 'artista': True, 'netgear': True}
    custlist = ['acme', 'globex corporation', 'soylent green', 'initech', 'umbrella corporation']

    ## Display the current state of our dictionary
    print(vendordict)

    ## Display all of the dictionary methods
    ## Focus on the ones without underscores
    ## Dict is a special word that Python treats as a dictionary
    ## FYI -- dict would be a terrible variable name
    print(dir(dict))
    # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', \
    # 'update', 'values']

    ## Use a few dictionary methods
    vendordict.keys()
    vendordict.values()
    vendordict.get('juniper')
    ## Remove the key:Value pair for NetGear
    vendordict.pop('netgear')
    ## Notice that 'NetGear' no longer returns a value (the key:value pair is gone)
    vendordict.get('netgear')

    ## Display all of the list methods -- focus on the ones without underscores
    ## List is a special word that Python treats as a list
    ## FYI -- list would be a terrible variable name
    print(dir(list))
    # ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', \
    # 'reverse', 'sort']
    custlist.append('cyberdyne')

    ## CyberDyne should now be part of the list
    print(custlist)


main()

