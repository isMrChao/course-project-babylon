import alpaca_trade_api as tradeapi

class BOT:
    """ 
    --Tass created Feb 16 2023--
    last update Feb 16 2023
    
    A class used to 
    - get trading bot information and working status
    - read data from Alpaca market
    - place, change, cancel orders
    
    """
    def __init__(self):
        self.SEC_KEY = ''
        self.PUB_KEY = ''
        self.BASE_URL = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(key_id= self.PUB_KEY, secret_key=self.SEC_KEY, base_url=self.BASE_URL)
        self.status = 0
    
    def setKEY(self, seckey, pubkey):
        self.SEC_KEY = seckey
        self.PUB_KEY = pubkey
        
    def printKEY(self):
        print("Secret KEY: ", self.SEC_KEY)
        print("Public KEY: ", self.PUB_KEY)
    
    def printURL(self):
        return print("Base URL: ", self.BASE_URL)
    
    def set_status(self, status): self.status = status
    def get_status(self) : return self.status
    
    # dir (1 is buy, 0 is sell)
    def submit_order(self, symb, quant, dir):
        move = 'buy'
        if dir == 0: move = 'sell'
        
        self.api.submit_order (
            symbol=symb; # Replace with the ticker of the stock you want to buy
            qty=quant,
            side= move,
            type='market', 
            time_in_force='gtc' # Good 'til cancelled
        )
           
    def cancel_order(self):
        return
    
    def read_data(self, symbol):
        market_data = self.api.get_barset(symbol, 'minute', limit=1)
        
    