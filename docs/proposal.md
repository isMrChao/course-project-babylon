# Introduction:
The Crypto market is a fast-paced and constantly changing environment, making it challenging for individual investors to make informed trading decisions. This project proposes the creation of an Automated Crypto Trading Bot that will use a trading algorithm designed in Python to make trades based on market data. The bot will connect to the Alpaca API to gather the necessary data and make trades on behalf of the user. The results of the trades will be displayed on a web interface designed using JavaScript for users to monitor the performance of the bots.

# Pitch:
There are two part for this project.  One is the trading bot part, which we will design bot will provide investors with a convenient, automated solution for trading cryptos, backed by data and analysis from the Alpaca platform. Another part will be the bot monitoring interface. To help algorithmic traders clearly control the working process of trading robots, the control panel allows traders to stop the operation of robots at any time to avoid economic losses caused by system problems. Users can also observe the performance of the model through the panel, so that the algorithm can be further optimized

# Functionality:
1. Connecting to the Alpaca API to gather real-time level-2 order book data of crypto products
2. Developing a trading algorithm in Python that will make trades based on market conditions.
3. Designing a web interface using JavaScript to display full order books records executed by different bots.
4. Monitor the transaction records of all robots and control the status of the robots at any time
5. Observe and visualize model performance
6. Providing a convenient and efficient solution for individual investors looking to enter the crypto market.

# Components:
**[Backend]**
Trading Algorithm: designed in Python with Numpy, PyTorch, and/or Pandas libraries to make trades based on market conditions. We will use paper trading system in Alpaca to do integration testing and python scripts for unit tests. The unit tests will be generating a few data sets with predicted results and see if the results coming out from the algorithm match the expectations, or how accurate it is.

Bots Management: due to the fact that different types of crypto products need different trading strategies to control, we will build a bot management class to manage different trading strategies to ensure that they are executed on the right product.



**[API]**
Self-built API : we will built our own api structure that has two classes: Execution and Events. The Execution class will function as a connection between frontend command and backend bot’s executions. It will have functions such as add/delete desired crypto products, run/pause/reset robots, and log in to Alpaca API keys and secrets.
The Events class will send trading records based on time stamps back to the frontend when the robots put orders in the (paper trading) market. It will also deliver related model performance statistics to the interface for display.

Alpaca API : We will gather real-time market data from Alpaca and parsed selected information for the algorithm. The testing method will be checking if the data grabbed and parsed as expected from the Alpaca.

**[Frontend]**
Web Interface: designed using JavaScript to display the results of the trades. This component will hold any result or conclusion produced by the algorithm.

Server: used to host the bot and ensure a stable connection to the Alpaca API, and checked if there is any data lost during the process. This part will hold the first two component and connect with the web interface.

# Schedule:
Research and Study: 2 weeks
Self-built API and a naive trading bot model: 2 weeks
Further Implementation of Trading Strategies and backend development: 4 weeks
Frontend Design and server connection testings: 3 weeks
Backtests and Paper Trading Experiments: 2 weeks

# Risks:
Market volatility: 
The crypto market is subject to sudden and unpredictable changes, which can have a significant impact on the success of the trades made by the bot. When designing the algorithm, the bot will grab the newest data whenever the user requesting for information, and any delay will be noted in advanced so that the users can keep refreshing to finally get what they want.
Technical issues: 
The bot relies on a stable connection to the Alpaca API and a functioning trading algorithm. Any technical issues could result in incorrect trades or missed opportunities. Reconnect whenever people notice a technical issue occurred.
Regulation: 
The crypto market is subject to government regulations that can impact the success of the trades made by the bot. If applicable, the government regulations will be considered when designing the algorithm. Otherwise, user will get notice for any government regulations that will possibly affect the trade and make further decision based on the decision and regulations given by the bot.

# Teamwork:
Project Manager (Chaoxiong Liang): responsible for overall project management and coordination.
Backend Developer (Tass Hu): responsible for trading bot and API implementations.
Frontend Developer (Xinyi Ye and Jinyan Hu): responsible for designing and developing the web interface.
Quality Assurance Tester (Xinyi Ye and Chaoxiong Liang): responsible for testing the bot and ensuring it meets the requirements.

# Conclusion: 
This project aims to provide individual investors with a convenient and efficient solution for entering the crypto market. By using the Alpaca API to gather real-time market data and a trading algorithm designed in Python, the Automated Crypto Trading Bot will make trades based on market conditions and display the results on a web interface designed using JavaScript. This project is estimated to take 13 weeks, but the results will be a valuable tool for individual investors looking to maximize their returns in the crypto market.

# Continuous Integration:
Testing Library: 
We will try to use the pytest testing framework as our testing library due to its flexibility, simplicity, and compatibility with various types of testing. Pytest provides a rich set of features, such as fixtures, parametrization, and plugins, that enable us to write clear, concise, and maintainable tests. Under the situation which there is plenty of time allowing such testing, we will use it to implement unit, integration, and functional tests for our project.
Style Guide:
If  we finish any weekly objective in advance by 2 days, then we will adopt the PEP 8 style guide as our standard for code formatting and style. PEP 8 is widely accepted in the Python community and provides a comprehensive set of guidelines for writing readable and consistent code. We will use automated tools, such as flake8 and pylint, to enforce the PEP 8 rules and catch style violations early in the development process. 
Test Coverage Computation: 
If our proficiency in python allows, we will use the coverage.py tool to measure the test coverage of our codebase. Coverage.py is a reliable and efficient tool that can determine which lines of code have been executed during the tests. As mentioned earlier, if the timeframe and the team’s fluence in the toolkit allows, we will aim to achieve a minimum of 80% test coverage for all code files. 
Pull Request Workflow:
 We will aiming to learn and use the Git and relevant branching model as our pull request workflow. We will have two primary branches: the main branch for production-ready code, and the develop branch for ongoing development. Developers will create feature branches off the develop branch and submit pull requests to merge their changes into the develop branch. We will also use code reviews to ensure that the code changes meet our quality standards, including the testing and style guidelines. 
In conclusion, for the Continuous Integration part strategy will use pytest as our testing library, adopt the PEP 8 style guide, measure the test coverage using coverage.py, and follow the Git branching model for pull requests. By implementing these best practices, we aim to build a high-quality, robust, and scalable software project that meets the needs of our stakeholders.
