def sercher():
    try:
        book = open('kiran.txt',)

        import  time
        time.sleep(3)
    except Exception as e:
        print(e)
    finally:
        while True:
            text = (yield )
            if text in book.readline():
                print(" yes your content match")
            else:
                print("your search is not match ")
            book.close()

search = sercher()
print("start")
next(search)
print("send ")
search.send("kiran")