class ElementoInventario (elemento):
    def __init__(self, name, description, photo):
        super().__init__(name, description, photo)
        self.stock = 1
        self.available = 1


    def add_one(self):
        self.stock = stock + 1
        self.available = available + 1

    def reduce_one(self):
        if self.stock > 1:
            self.stock = stock - 1
            self.available = available - 1
        else:
            ##TOGLI QUESTO ELEMENTO DAL FILE
            self._del_()
