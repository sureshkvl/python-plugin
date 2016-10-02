class Simple(object):
    def readfile(self, path):
        fo = open(path, "r+")
        str = fo.read(100)
        fo.close()
        return str
