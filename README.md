# Havelock Investments API

This is a simple python wrapper for the Havelock Investments API
([documentation](https://www.havelockinvestments.com/apidoc.php)).

## Installation

Using `setuptools`

	$ cd python-havelockapi
	$ python setup.py install

## Usage

The API can be used in two different ways. By importing `havelockapi`
or by running `python -m havelockapi CMD`.

### Simple ticker example

	>>> import json
    >>> from havelockapi import HavelockApi
	>>> api = HavelockApi()
	>>> data = api.ticker()
	>>> print json.dumps(data, indent=2)
	{
	  "ASICM": {
	    "units": "243837", 
	    "last": "0.02910000"
      }, 
      "VTX": {
        "units": "10000", 
        "last": "0.48011000"
      }, 
      "SDICE": {
        "units": "14460", 
        "last": "0.20401999"
      }, 
      "KCIM": {
        "units": "907", 
        "last": "1.01211000"
      }, 
      "HIM": {
        "units": "40000", 
        "last": "0.29000000"
      }
    }
	
Commands with arguments are called using keyword arguments.

	>>> data = api.ticker(symbol="SDICE")
	>>> print json.dumps(data, indent=2)
    {
      "SDICE": {
        "units": "14460", 
        "last": "0.20401999"
      }
    }

### Using a secret key

This can either be done using `HavelockApi(key=<SECRET_KEY>)` or
using `api.<COMMAND>(key=<SECRET_KEY>)` on those supporting it.

	>>> import json
    >>> from havelockapi import HavelockApi
	>>> api = HavelockApi(key=<SECRET_KEY>)
	>>> api.balance()
	{
      "status": "ok", 
      "balance": {
        "balanceescrow": "0.00000000", 
        "balance": "0.01757922", 
        "balanceavailable": "0.01757922"
      }
    }

or

	>>> import json
    >>> from havelockapi import HavelockApi
	>>> api = HavelockApi()
	>>> api.balance(key=<SECRET_KEY>)
	{
      "status": "ok", 
      "balance": {
        "balanceescrow": "0.00000000", 
        "balance": "0.01757922", 
        "balanceavailable": "0.01757922"
      }
    }

### From the command line

All commands can also be run directly from the command line by running

    $ python -m havelockapi CMD
	
For help, run
	
	$ python -m havelockapi --help
	
or

	$ python -m havelockapi CMD --help

#### Example

	$ python -m havelockapi ticker --symbol ASICM
	{
      "ASICM": {
        "units": "244268", 
        "last": "0.02853002"
      }
    }
