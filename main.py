def task1():
    dz = int(input("Donne moi tes infos"))
    try:
        value = input(f"""
        Enter an integer de {dz}""")
        #print('The half of'+ value+ 'is'+ value\2)


        var1=654
        var2=int(input('Give me a num : '))
        print(var1/var2)
    except ZeroDivisionError:
        print
    except ValueError:
        pass
    except TypeError:
        pass


def task2():
    ll = [325,3,57,2146,19604]
    print(ll[1] )
def task3():
    dic = {"qd":845,"sdfv":6845,"d^fpskv":6845}
    print(dic["qoehfde"])


def task4():
    f= open("test.txt")
    f.write()
