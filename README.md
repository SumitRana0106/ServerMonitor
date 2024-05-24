# ServerMonitor
Script to monitor server RAM, CPU and Disk usage and send critical email notifications on daily basis. Developed it for monitoring aws EC2 instance , as aws does not provide disk usage metric in cloudwatch metrics.

## Usage
1. Most effecient way to use the script is use it as a cron service.


## Dependencies
1. Python3
2. python library "psutil". Install it using command "pip install psutil"
3. **crond** service



## Important Note :
1. For email notification like gmail, password should be app password as less secured authentication is disabled by google.


