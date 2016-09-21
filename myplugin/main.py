from stevedore import driver


def main():
    mydriver = driver.DriverManager(namespace="mydrivers", name="driver2")
    #print mydriver.driver
    print mydriver.driver().getname()


if __name__ == "__main__":
    main()
