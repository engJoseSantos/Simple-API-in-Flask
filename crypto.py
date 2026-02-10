class Crypto:
    def __init__(self, id, name, code, value_to_usd):
        self.id = id
        self.name = name
        self.code = code
        self.value_to_usd = value_to_usd
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" :self.name,
            "code" :self.code.upper(),
            "price_usd" :self.value_to_usd
        }