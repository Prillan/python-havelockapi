# -*- coding: utf-8 -*-
import base

class CommandError(Exception):
    def __init__(self, msg):
        super(CommandError, self).__init__(msg)

class HavelockCommand():
    def __init__(self, name, required=[], optional=[]):
        self.name = name
        self.required = required
        self.optional = optional

class HavelockApi():
    
    commands = [
        HavelockCommand("ticker", [], ["symbol"]),
        HavelockCommand("tickerfull", [], ["symbol"]),
        HavelockCommand("orderbook", ["symbol"], []),
        HavelockCommand("portfolio", ["key"], []),
        HavelockCommand("balance", ["key"], []),
        HavelockCommand("orders", ["key"], []),
        HavelockCommand("transactions", ["key"],
                        ["limit", "sort", "sinceid", "sincets"]),
        HavelockCommand("withdraw", ["key", "amount", "address"], []),
        HavelockCommand("deposit", ["key"], []),
        HavelockCommand("ordercreate", ["key", "symbol", "action", "price", 
                                        "units"], []),
        HavelockCommand("ordercancel", ["key", "id"], [])
    ]
    _command_dict = dict((cmd.name, cmd) for cmd in commands)

    def __init__(self, key=None):
        self.secret = key

    def __getattr__(self, attr):
        if attr in self._command_dict:
            cmd = self._command_dict[attr]
            def command(**kwargs):
                if "key" in cmd.required and not "key" in kwargs:
                    if self.secret is not None:
                        kwargs["key"] = self.secret
                for key in kwargs.keys():
                    if kwargs[key] is None:
                        del kwargs[key]
                for req in cmd.required:
                    if not req in kwargs:
                        raise CommandError("Missing required argument: {}"\
                                           .format(req))
                for key in kwargs:
                    if not (key in cmd.required or key in cmd.optional):
                        raise CommandError("Invalid argument: {}".format(key))

                return base.command(cmd.name, **kwargs)
                    
            return command

    @classmethod
    def help(cls):
        for cmd in cls.commands:
            print "Command: {}".format(cmd.name)
            print "  Required args: " + ', '.join(cmd.required)
            print "  Optional args: " + ', '.join(cmd.optional)
