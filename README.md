# AS400Scripts
Useful scripts for AS400 testing


## AS400 Users Enumeration

:warning: Each attempt does a login tentative. Be careful with the script for lockout.

```
python as400_enum_users.py -h                                                         

Enumerate Users on AS400 using telnet

usage: as400_enum_users.py [-h] [-v] [-o OUTPUT] -i IP -f FILENAME

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increase output verbosity
  -o OUTPUT, --output OUTPUT
                        Write valid users to an output file

required arguments:
  -i IP, --ip IP        Ip address of the host
  -f FILENAME, --filename FILENAME
                        File that contain the users to enumerate
```
