import os
import dbm
import argparse
import logging

logging.getLogger('paramiko.transport').setLevel(logging.WARN)

class AnyDBMManager(object):
    '''
    Manage Anydbm db
    '''
    def __init__(self, args):
        self.dbfile = args.path
        if args.list:
            self.list_entries()
        elif args.set:
            for k,v in args.set:
                self.set_entry(k,v)
        elif args.delete:
            self.delete_entry(args.delete)
        else:
            print('No operation chosen. Check help')
    # end __init__

    def list_entries(self):
        try:
            db_h = dbm.open(self.dbfile, 'r')
            for k in db_h.keys():
                print(k,db_h[k])
        finally:
            db_h.close()

    def set_entry(self, key, value):
        try:
            db_h = dbm.open(self.dbfile, 'c')
            db_h[key] = value
        finally:
            db_h.close()

    def delete_entry(self, key):
        try:
            db_h = dbm.open(self.dbfile, 'w')
            del db_h[key]
        finally:
            db_h.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description='''
Manage dbm db
Example : to add/delete testcase run-times in testrepository

python3 anydbm-manage.py -p /tmp/times.dbm -d scripts.pbb_evpn.test_pbb_evpn.TestPbbEvpnMacLearning.test_mac[cb_sanity,sanity]

python3 anydbm-manage.py -p /tmp/times.dbm -s scripts.pbb_evpn.test_pbb_evpn.TestPbbEvpnMacLearning.test_mac[cb_sanity,sanity] 306.15
''')
    ap.add_argument('-p', '--path', type=str,
                    help='path to anydbm db file')
    ap.add_argument('-l', '--list', action='store_true', default=False,
                    help='list entries in th db')
    ap.add_argument('-s', '--set', nargs=2, action='append',
                    help='Add/update a testtag and run-time(secs) to db')
    ap.add_argument('-d', '--delete', type=str,
                    help='Delete a testtag key from db', default='')
    args = ap.parse_args()
    dbm_handler = AnyDBMManager(args)
