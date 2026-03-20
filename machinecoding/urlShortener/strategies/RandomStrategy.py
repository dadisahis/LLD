from .KeyGenStrategy import KeyGenStrategy
import random
class RandomStrategy(KeyGenStrategy):
    CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPPQRSTUVWXYZ0123456789'
    KEY_LENGTH = 6

    def gen_key(self, id):
        return ''.join(random.choice(self.CHARACTERS) for i in range(self.KEY_LENGTH))
    

    