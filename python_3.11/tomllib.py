"""
# This is a TOML document.
title = "TOML Example"

[owner]
name = "Tom Preston-Werner'
dob = 1979-05-27T07:32:00-08:00 # First class dates
[database]
server = "192.168.1. 1"
ports = [ 8000, 8001, 8002 ]
connection_max = 5000
enabled = true

[servers]
# Indentation (tabs and/or spaces) is allowed but not required
[servers. alpha]
ip = "10.0.0.1"
dc = "eqdc10"
[servers. beta]
ip = "10.0.0.2"
dc = "eqdc10"

[clients]
"""

import tomllib

def main () -> None:
    with open("settings.toml", "rb") as f:
        data = tomllib. load (f)
    print(data)

if __name__ == '__main__':
    main()

# output
"""
{'title': 'TOML Example', 'owner': {'name'; 'Tom Preston-Werner', 'dob': datetime.datetime(1979, 5, 27, 7 ,32, tzinfo=datetime. timezone(datetime.timedelta(days=-1, seconds=57600)))}, 
'database': {'server': '192.168.1.1', 'ports': [8000, 8001, 80021], 'connection_max': 5000, 'enabled': True'}, 
'servers': {'alpha': {'ip': '10.0.0.1', 'dc': 'eqdc10}, 'beta': {'ip': '10.0.0.2', 'dc': 'eqdc10'}},
'clients': {'data': [['gama', 'delta'], [1,2]], 'hosts': ['alpha', 'omega']}}
"""