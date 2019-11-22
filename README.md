# AS400Scripts
Useful scripts for AS400 testing

```

                                   Sign On           
                                               System  . . . . . :   TEST 
                                               Subsystem . . . . :   TEST     
                                               Display . . . . . :   TEST 

                User  . . . . . . . . . . . . . .              
                Password  . . . . . . . . . . . .              
                Program/procedure . . . . . . . .              
                Menu  . . . . . . . . . . . . . .              
                Current library . . . . . . . . .              

            +-------------------------------------------------------------------+                     
            |  Unauthorized access is stricly prohibited and subject to legal   |           
            |             proceedings before courts of law.                     |  
            +-------------------------------------------------------------------+                                                                                                                                                                                                                                                                                                                                                                                                                    


                                        (C) COPYRIGHT IBM CORP. 1980, 2015.
```


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

### Example 
```
python as400_enum_users.py -i 10.0.0.1 -f potential-users.txt -o valid-users.txt -v

Enumerate Users on AS400 using telnet

[+] 6 Users loaded
[+] Enumeration started. Each attempt does a login tentative.
[*] PSOUAA is a valid user
[+] Writing valid user to file
```

