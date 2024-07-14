# What is Textchat?
Textchat is a TUI made with Textual and the [irc](https://github.com/jaraco/irc) library. It is designed to work with a single server.


## How to Use
Textchat is available on pypi and can be installed with `pip install textchat`. The only platform confirmed to be working right now is Linux. Alternatively, you can clone the repo and install with `pip install -e .`


## Screenshots
![libera](/assets/libera.png)

--------



### 
Known Bugs:
* Upon first launch, after saving the server info, it does not connect to irc or update the channel list, causing the user to have to restart the application and launch it again.