from datetime import datetime
class ShortenURL:
    def __init__(self, builder: 'Builder'):
        self.long_url = builder.long_url
        self.short_key = builder.short_key
        self.creation_dt =  builder.creation_dt


    def get_long_url(self):
        return self.long_url

    def get_short_key(self):
        return self.short_key
    
    def get_creation_dt(self):
        return self.creation_dt
    

    class Builder:
        def __init__(self, long_url, short_key):
            self.long_url = long_url
            self.short_key = short_key
            self.creation_dt = datetime.now()

        def creation_date(self, creation_dt):
            self.creation_dt = creation_dt
            return self
        
        def build(self):
            return ShortenURL(self)