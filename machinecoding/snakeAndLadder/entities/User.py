class User:
    def __init__(self, name):
        self._name = name
        self._position = 0
    
    def get_name(self):
        return self._name
    
    def get_position(self):
        return self._position

    def set_position(self, pos):
        self._position = pos