- installer les outils snmp
- télécharger (wget) le MIB de ACME (ACME-MIB.txt) dans /usr/share/snmp/mibs
- à la ligne 9 il dit avoir besoin de SNMPv2-SMI, donc il faut le télécharger (https://opensource.apple.com/source/net_snmp/net_snmp-7/net-snmp/mibs/SNMPv2-SMI.txt?txt) dans /usr/share/snmp/mibs
- `snmptranslate -m ACME-MIB -IR -Onf {OID}`
- où {OID} est un identifiant, comme pid, descr ou contact
- On a par exemple
- `snmptranslate -m ACME-MIB -IR -Onf processEntry.pid`
- qui donne
- `.iso.org.dod.internet.private.enterprises.ACME.processTable.processEntry.pid`
- `snmptranslate -m ACME-MIB -Tp -OS`
- affiche le tree

1.3.6.1.2.1  .1.1.0
|iso
  |org
    |dod
      |internet
        |
          |enterprise
```bash
$ ./test.py
# SNMPv2-MIB::sysDescr.0 = Linux zeus 4.8.6.5-smp #2 SMP Sun Nov 13 14:58:11 CDT 2016 i686
```

## Understand the file
```bash
NC-MIB DEFINITIONS ::= BEGIN # the MIB name is NC-MIB
IMPORTS
    MODULE-IDENTITY, enterprises FROM SNMPv2-SMI; # import the MIB "SNMPv2-SMI"
descr OBJECT IDENTIFIER ::= {newbiecontest 1} # the descr variable = newbiecontest
comment OBJECT-TYPE # object comment
	SYNTAX      	String
	MAX-ACCESS  	read-only
	STATUS      	current
	DESCRIPTION 	Website description
	::= \{ descr 1 \} # located at descr 1
```

## Convert to OID
With NC-MIB.txt in the current folder `pwd`:
```bash
$ snmptranslate -M $(pwd) -m NC-MIB -IR comment # look for the comment node
MIB search path: /var/www/vhosts/floriancourgey.com/work/
Cannot find module (SNMPv2-SMI): At line 9 in /var/www/vhosts/floriancourgey.com/work/NC-MIB.txt
Cannot adopt OID in NC-MIB: processEntry ::= \{ processTable 1 }
Cannot adopt OID in NC-MIB: contact ::= \{ descr 3 }
Cannot adopt OID in NC-MIB: hostname ::= \{ descr 2 }
[...]
```

We have `Cannot find module (SNMPv2-SMI)`, so let's download it from `net-snmp.org` and place it in the same folder
```bash
$ wget http://www.net-snmp.org/docs/mibs/SNMPv2-SMI.txt
$ snmptranslate -M $(pwd) -m NC-MIB -IR comment
NC-MIB::comment
$ snmptranslate -M `pwd` -m NC-MIB -Pu -Tz
"org"                   "1.3"
"dod"                   "1.3.6"
"internet"                      "1.3.6.1"
"directory"                     "1.3.6.1.1"
"mgmt"                  "1.3.6.1.2"
"mib-2"                 "1.3.6.1.2.1"
"experimental"                  "1.3.6.1.3"
"private"                       "1.3.6.1.4"
"enterprises"                   "1.3.6.1.4.1"
"newbiecontest"                 "1.3.6.1.4.1.9999"
"descr"                 "1.3.6.1.4.1.9999.1"
"comment"                       "1.3.6.1.4.1.9999.1.1"
"hostname"                      "1.3.6.1.4.1.9999.1.2"
"contact"                       "1.3.6.1.4.1.9999.1.3"
"processTable"                  "1.3.6.1.4.1.9999.2"
"processEntry"                  "1.3.6.1.4.1.9999.2.1"
"pid"                   "1.3.6.1.4.1.9999.2.1.1"
"cmd"                   "1.3.6.1.4.1.9999.2.1.2"
"cpu"                   "1.3.6.1.4.1.9999.2.1.3"
"state"                 "1.3.6.1.4.1.9999.2.1.4"
"security"                      "1.3.6.1.5"
"snmpV2"                        "1.3.6.1.6"
"snmpDomains"                   "1.3.6.1.6.1"
"snmpProxys"                    "1.3.6.1.6.2"
"snmpModules"                   "1.3.6.1.6.3"
```
