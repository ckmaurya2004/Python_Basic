import datetime
import time

end_time = datetime.datetime(2024,2,8)
site_block  = ['www.w3schools.com','www.codewithharry.com']
host_path = "/media/kiran/F61E7C131E7BCADF/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"


while True:
    if datetime.datetime.now() < end_time:
        print("start blocking")
        with open(host_path,'r+') as host_file:
           content =  host_file.read()
           for web in content:
                if web not in content:
                   host_file.write(f"{redirect} {web} \n")
                else:
                   pass

    else:
        with open(host_path,'r+') as host_file:
            content =  host_file.readlines()
            host_file.seek(0)
            for line in content:
               if not any(web in line for web in site_block):
                   host_file.write(line)

            host_file.truncate()
        time.sleep(5)

       
