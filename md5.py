from hashlib import md5

class MD5:
    def __init__(self, data):
        if data == None:
            self.data = ''
            self.hash = ''
            return
        self.data = str(data)
        self.hash = md5(self.data.encode()).hexdigest()

    def __str__(self) -> str:
        return f"{self.data}({self.hash})"
    def __repr__(self) -> str:
        return self.hash
    def __call__(self):
        return self.data
    def __add__(self, val2):
        if val2.data == None:
            return self
        return MD5(self.data + val2.data)
    def encode(self):
        return self.hash.encode()
