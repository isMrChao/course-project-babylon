class Event:
    """ 
    --Tass created Feb 15 2023--
    
    A class used to 
    - dump timestamp from trading book
    - help frontend recieve bot ececution records, graph, and related information.
    
    """
    def __init__(self):
        self._HIST_PATH = None
    
    def dump_history(self, timestamp):
        return
           
    def display_model():
        return
        
    def get_book():
        return
    
    def print_latest_order():
        return
        
    def print_all_orders():
        return
        
    def update_model():
        return
        
    def update_book():
        return
        
        
            


class Execution:
    """ 
    --Tass created Feb 15 2023--
    
    A class used to 
    - add, delete stocks products that bot controlled
    - start, pause the bot
    
    """
    def __init__(self, apikey, secret):
        self._STOCKS = []
        self._BOTS = []
        self._API_KEY = apikey
        self._SECRET = secret
        
    def add_stock(self, stock:str):
        valid_stock = self.check_stock(stock)
        if valid_stock==None:
            return None
        self._STOCKS.append(valid_stock)
        
    def get_stocks(self, stock:str):
        return self._STOCKS
    
    def check_stock(self, stock: str) ->str:
        # Check if there's invalid characters in symbol
        if not stock.replace(" ", "").isalnum(): 
            print("INVALID SYMBOL: %s\n", stock)
            return None
        
        # Valid, uniform format
        valid_stock = stock.replace(" ", "").upper()
        return valid_stock
        
    
    def delete_stock(self, stock:str):
        valid_stock = self.check_stock(self, stock)
        if valid_stock not in self._STOCKS: 
            print("stock not found in buckets\n")
            return None
        self._STOCKS.remove(stock)
    
    def start_bot(self, bot: Bot):
        bot.set_status(1)
    
    def pause_bot(self, bot: Bot):
        bot.set_status(0)
        
    def start_all_bots(self):
        for bot in self._BOTS: self.start_bot(bot)
    
    def pause_all_bots(self):
        for bot in self._BOTS: self.pause_bot(bot)
    
    def get_bot_infomation(self, bot: Bot):
        return bot.get_info()
    
    
    def get_user_info(self):
        return [self._API_KEY, self._SECRET]
    
    def set_user_info(self, new_key, new_secret):
        self._API_KEY = new_key
        self._SECRET = new_secret
    
    def clear_user_info(self):
        self._API_KEY = None
        self._SECRET = None
    
        
    
    