from ConfigReader import read

v = read()


def getHost():
    d=v["rabbitmq"]["host"]
    print(d)
    return d
