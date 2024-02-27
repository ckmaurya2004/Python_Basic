def doc1(func1):
    def nowexe():
        print("Executing now")
        func1()
        print("Executed")
    return nowexe
@doc1
def who_is_kiran():
    print("kiran is a good girl")

who_is_kiran()

    