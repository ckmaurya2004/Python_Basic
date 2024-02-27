client_list = { 1:"kiran", 2:"Shikha", 3:"Ruchi"}
log_list = {1:"Excersize", 2:"Food"}

def gatetime():
    import datetime
    return datetime.datetime.now()

try:
    print("Select  Client Name:")
    for key ,value in client_list.items():
        print("press " , key ,"for",value, "\n", end="")
    client_name = int(input())
    
    print("Selected name is :",client_list[client_name],"\n", end="")

    print("Press  1 for log")
    print("Press 2 for retrive")
    op = int(input())

    if op is 1:
        for key,value in log_list.items():
            print("press",key , "to log" , value, "\n", end="")
        log_name = int(input())
        print("Selected job  is",log_list[log_name],"\n", end="")
        f = open(f"{client_list[client_name]}_{log_list[log_name]}.txt" ,"a")
        k= 'y'
        while(k is not 'n'):
            print("Enter",log_list[log_name],"\n",end="")
            mytext = input()
            f.write(f"[{gatetime()}]: {mytext} \n" )
            k = input("ADD MORE?(y/n)")
            continue
        f.close()
    elif op is 2:
        for key,value in log_list.items():
            print("press",key , "to retrive" , value, "\n", end="")
        log_name = int(input())
        print("Retrive job  is",log_list[log_name],"\n", end="")
        f = open(f"{client_list[client_name]}_{log_list[log_name]}.txt" ,"rt")
        contents = f.readlines()
        for line in contents:
            print(line ,end="")
        f.close()
    else:
        print("invalid client")


    
except:
    print("worng input")