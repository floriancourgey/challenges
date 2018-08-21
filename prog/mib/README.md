installer les outils snmp
télécharger (wget) le MIB de newbiecontest (NC-MIB.txt) dans /usr/share/snmp/mibs
à la ligne 9 il dit avoir besoin de SNMPv2-SMI, donc il faut le télécharger (https://opensource.apple.com/source/net_snmp/net_snmp-7/net-snmp/mibs/SNMPv2-SMI.txt?txt) dans /usr/share/snmp/mibs
`snmptranslate -m NC-MIB -IR -Onf {OID}`
où {OID} est un identifiant, comme pid, descr ou contact
On a par exemple
`snmptranslate -m NC-MIB -IR -Onf processEntry.pid`
qui donne
`.iso.org.dod.internet.private.enterprises.newbiecontest.processTable.processEntry.pid`
`snmptranslate -m NC-MIB -Tp -OS`
affiche le tree
