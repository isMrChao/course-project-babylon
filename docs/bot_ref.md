# BOT Reference

> **Last Update in Feb 15 2023 BY Tass**

# Setup API

The trading API we're going to be using is called [Alpaca](https://alpaca.markets/).
We will run the script on local computer, or on the cloud [Codesphere](https://codesphere.com/)

**install pipenv**

```js
pip install --user pipenv
pipenv shell
```

**install the Alpaca API**

```js
pipenv install alpaca_trade_api`
```

**Library**

```
import alpaca_trade_api as tradeapi
import numpy as np
import time
```
