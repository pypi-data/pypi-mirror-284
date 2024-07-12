# showquota
`showquota` is a utility for checking linux user and projects(secondary groups) storage quota on the system. Useful on HPC infrastructures where each user have a home quota folder and a project quota folder on an external source like beegfs.

 showquota currently supports xfs and beegfs checks but it's higly customizable via config file.
 
 ```
[test@localhost ~]$ showquota
Home folder:
--------------------------------------------------
User quota on /home (/dev/mapper/rl_nfs--srv-home)
                        Blocks
User ID      Used   Soft   Hard Warn/Grace
---------- ---------------------------------
userA        3.8M   9.8G   9.8G  00 [------]
--------------------------------------------------

Project(s) folder:
------------------------------------------------------------------------
Group: projectA
Quota information for storage pool Default (ID: 1):

      user/group      ||           size          ||    chunk files
     name      |  id  ||    used    |    hard    ||  used   |  hard
--------------|------||------------|------------||---------|---------
projectA      | 1010 ||      0 Byte|    4.88 GiB||        0|unlimited
------------------------------------------------------------------------
```



# Installation
```
pip install showquota
```


# Configuration

The tool require a config file `/opt/showquota/config.cfg`, if the file doesn't exists it will be created on the first run.
You need to edit it and set the storage server(s).


config.cfg:
```
#showquota configfile
#by Giulio Librando
home_server_ip: 'x.x.x.x'
home_server_command: 'xfs_quota -x -c 'report -h' /home'
beegfs_server_ip: 'x.x.x.x'
beegfs_server_command: 'beegfs-ctl --getquota --gid %GID%'
```

`home_server_ip` and `beegfs_server_ip` can be both set to **ip** or **localhost**

If you use xfs for the /home folder and beegfs for the projects folder leave the default commands. 
`%GID%` is dinamically replaced with real values inside the tool



