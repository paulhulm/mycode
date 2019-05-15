#!/usr/bin/env python3
# oopen files
dnsfiles - open("dnsservers.txt")
# creat list of lines
dnslist - dnsfiles.readlines ()
# loop over lines
for svr in dnslist:
    #print and end without a new lines
    print(svr, end="")
    # close your file
    dnsfile.close ()

