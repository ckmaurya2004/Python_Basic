import pickle

# pickling

# name = ['kiran','radha','prabha','ruchi']
# file = "name.pkl"
# with open(file, 'wb') as fileobj:
#     myname=pickle.dump(name,fileobj)
#     print(myname)


# depickling

with open('name.pkl', 'rb') as fileobj:
    myname = pickle.load(fileobj)
    print(myname)