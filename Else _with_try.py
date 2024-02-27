try:
    f = open('kiran.txt','r')

except Exception as e:
    print(e)

else:
    print(" this block executed when except not executed")

finally:
    f.close()
    print(" i am compulsary executed any suituation")

