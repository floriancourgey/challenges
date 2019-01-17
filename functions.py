# coding: utf-8
import requests
import config
import irc.client

def get(url, returnRequests=False):
    print('functions | get URL ', url)
    r = requests.get(url, cookies={config.COOKIE_KEY:config.COOKIE_VAL})
    if returnRequests:
        return r
    else:
        return r.text

class IrcSolver(irc.client.SimpleIRCClient):
    def __init__(self):
        irc.client.SimpleIRCClient.__init__(self)
        self.server = 'irc.newbiecontest.org'
        self.port = 6667
        self.nickname = 'MisterBob-bot'
        self.channel = '#nc-irc-challs'
        self.target = 'Daneel'
        self.debug_all_events = 0
        self.STEP = 1
        self.reactor.add_global_handler("all_events", self.my_dispatcher, -10)
    def connect_and_start(self):
        self.connect(self.server, self.port, self.nickname)
        self.start()
    def on_welcome(self, connection, event):
        connection.join(self.channel)
    def my_dispatcher(self, connection, event):
        if self.debug_all_events:
            if event.type != 'all_raw_messages':
                print('my_dispatcher:', event)
