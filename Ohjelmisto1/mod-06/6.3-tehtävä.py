def bensiinimaara():
    return galloonat*3.1785

galloonat = 1
while galloonat > 0:
    galloonat = int(input("Anna galloonamäärä: "))
    if galloonat < 0:
        break
    print(bensiinimaara())
