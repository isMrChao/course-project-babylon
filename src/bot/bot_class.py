import alpaca_trade_api as tradeapi

class BOT:
    """ 
    --Tass created Feb 16 2023--
    last update Feb 28 2023
    
    A class used to 
    - get trading bot information and working status
    - read data from Alpaca market
    - place, change, cancel orders
    
    """
    def __init__(self):
        self.status = 0
        self.id = 0
    
    def printURL(self):
        return print("Base URL: ", self.BASE_URL)
    
    def set_status(self, status): self.status = status
    def get_status(self) : return self.status
    
    # dir (1 is buy, 0 is sell)
    def submit_order(self, symb, qty, dir):
        move = 'buy'
        if dir == 0: move = 'sell'
        
        self.api.submit_order(
            symbol=symb, # Replace with the ticker of the stock you want to buy
            qty=qty,
            side= move,
            type='market', 
            time_in_force='gtc'
        )
            
        
           
    def cancel_order(self):
        return
    
    def read_1min_data(self, symbol):
        market_data = self.api.get_barset(symbol, 'minute', limit=1)
        return market_data
        