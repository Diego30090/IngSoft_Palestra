class ElementoMercato (elemento):
    def __init__(self, name, owner_id, owner_name, owner_cell, description, photo):
        super().__init__(name, description, photo)
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_cell = owner_cell

        pass
