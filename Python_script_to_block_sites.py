# Let's start building the python script that can run at system startup to block the access to the particular websites.

# Setting up the variables

# Here, the host_path is set to the path to the hosts file. In our case, it is located under /etc. In python, r is used to represent the raw string.

from time import *
from datetime import *

host_path = r"C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
websites = ["http://www.facebook.com", "www.facebook.com", "http://www.instagram.com", "www.instagram.com"]

# We need while loop to make our file run ate every 5 seconds.

while True:
    


    ''' Determining the time
In the process to build our desired python script, we need to check the current time whether it is working time or fun time since the application will block the website access during the working time.

To check the current time, we will use the datetime module. We will check whether the datetime.now() is greater than the datetime object for 9 AM of the current date and is lesser than the datetime object for 5 PM of the current date.

The open() method opens the file stored as host_path in r+ mode. First of all, we read all the content of the file by using the read() method and store it to a variable named content.

The for loop iterates over the website list (websites) and we will check for each item of the list whether it is already present in the content.

If it is present in the hosts file content, then we must pass. Otherwise, we must write the redirect-website mapping to the hosts file so that the website hostname will be redirected to the localhost.
'''
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 7)<datetime.now()<datetime(datetime.now().year, datetime.now().month, datetime.now().day, 17):
        print("Working Hours")
        with open(host_path, "r+") as fileptr:
            content = fileptr.read()
            for website in websites:
                if website in content:
                    pass 
                else:
                    fileptr.write(redirect+" "+website+"\n")
    else:
        ''' Removing from the hosts file
Our script is working fine for the working hours, now lets add some features for the fun hours also. In the fun hours (not working hours) we must remove the added lines from the hosts file so that the access to the blocked websites will be granted.
'''
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Fun Hours")    
    sleep(5)