class ComponentMemory:
    def __init__(self):
        self.last_component = None

    def update(self, component):
        self.last_component = component

    def get(self):
        return self.last_component