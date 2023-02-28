import unittest
from api_class import *
class Test_API_CLASS(unittest.TestCase):
    def test_print(self):
        user = Execution()
        self.assertEqual(user.test_print(), "i can print!")

    def test_check_symbols(self):
        user = Execution()
        a1 = user.check_symbol("BTC USDT")
        a2 = user.check_symbol("btc eTh ")
        a3 = user.check_symbol("e t h s py")
        a4 = user.check_symbol("    ###")
        a5 = user.check_symbol(" BTCETH   ###")
        self.assertEqual(a1, "BTCUSDT")
        self.assertEqual(a2, "BTCETH")
        self.assertEqual(a3, "ETHSPY")
        self.assertEqual(a4, None)
        self.assertEqual(a5, None)
        
        #self.assertFalse('Foo'.isupper())

    def test_add_symbols(self):
        user = Execution()
        user.add_symbol("btc eth")
        user.add_symbol("SolonaUsdt")
        user.add_symbol("###")
        symbols = user.get_symbols()
        s = ["BTCETH", "SOLONAUSDT"]
        self.assertEqual(len(symbols), 2)
        for i in range(len(symbols)):
            self.assertEqual(symbols[i], s[i])
            

if __name__ == '__main__':
    unittest.main()