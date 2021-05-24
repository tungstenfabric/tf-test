echo "qwe123QWE" | kinit admin > /dev/null
ipa host-find | grep  "Host name" | grep -v "overcloud" | grep -v "freeipa" | cut -d : -f 2
