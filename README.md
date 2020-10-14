#
# OANDA Trading
#
## References
- https://github.com/oanda/v20-python-samples
- oanda-candles
- oanda-chart
- v20

## Setup

The following procedure describes how to create a virtualenv appropriate for
running the v20 sample code:

<<<<<<< HEAD
## Set up the virtualenv and install required packages. 
```
C:\user\oanda: pip install virtualenv
C:\user\oanda: virtualenv -p python3 env
C:\user\oanda: cd env/Scripts
C:\user\oanda: activate.bat
(env)C:\user\oanda: pip install -r requirements.txt
(env)C:\user\oanda: python setup.py develop
(env)C:\user\oanda: pip install oanda-candles
(env)C:\user\oanda: pip install pyautogui
=======
#
# Set up the virtualenv and install required packages. 
#
```
pip install virtualenv
virtualenv -p python3 env
cd env/Scripts
activate.bat

(env)C:\user\oanda: pip install -r requirements.txt
```
#
# Create the v20-* launch entry points in the virtualenv. These entry points
# are aliases for the scripts which use the v20 REST API to interact with an
# account (e.g. v20-market-order, v20-trades-list, etc.)
#
```
(env)C:\user\oanda: python setup.py develop
>>>>>>> cf61f1c683b58e0ba04eb90b0eafffc28183a83e
```

## Configuration-free Example

Most of the examples provided use a v20.conf discussed below. For a full
example of how to create and use a v20 API context without the configuration
wrapper, please examine `src/market_order_full_example.py`. This program
enables the creation of a limited Market Order solely based on command line
arguments.
```
(env)C:\user\oanda: python src/market_order_full_example.py accID token instrument units
```

## Configuration

Using OANDA's v20 REST API requires configuration to set up connections and 
interact with the endpoints. This configuration includes:

* API hostname
* API port
* API token
* username of client
* Account ID of account being manipulated

To simplify the management of this configuration, the v20 Python sample code
requires that a configuration file be created. All of the sample code loads
this configuration file prior to connecting to the v20 system.

### v20 Configuration File Format

The v20 configuration is stored in a YAML file that resembles the following:

```yaml
hostname: api-fxpractice.oanda.com
streaming_hostname: stream-fxpractice.oanda.com
port: 443
ssl: true
token: e6ab562b039325f12a026c6fdb7b71bb-b3d8721445817159410f01514acd19hbc
username: user
accounts:
- 101-001-100000-001
- 101-001-100000-002
active_account: 101-001-100000-001
```

### Generating v20 Configuration files

v20 configuration files may be generated manually, however a script is provided that
will generate one interactively located at `src/configure.py`.

To run it and generate a v20 configuration file, simply run:

```
(env)C:\user\oanda: v20-configure
```

and follow the instructions.

### Using v20 Configuration files

There are several ways to load a v20 configuration file in each of v20 sample scripts:

#### 1. Run the script with the `--config` option 

The `--config` options allows you to specify the location of a valid v20 configuration file v20. Example: 

```
(env)C:\user\oanda: ~/v20-python-samples$ v20-account-details --config /home/user/v20.conf
```

#### 2. Use the default v20 configuration file location

The default location for the v20 configuration file is `~/.v20.conf`. If a v20
configuration file exists in the default location, no `--config` option needs
to be used. Example:

```
# Looks for config file at ~/.v20.conf
(env)C:\user\oanda: ~/v20-python-samples$ v20-account-details
```

#### 3. Set the location of the `V20_CONF` environment variable 

This `V20_CONF` environment variable changes what the default location of the
v20 configuration file is. If a configuration file exists in this location, no
`--config` option needs to be used. Example:

```
(env)C:\user\oanda: ~/v20-python-samples$ export V20_CONF=/home/user/v20.conf
(env)C:\user\oanda: ~/v20-python-samples$ v20-account-details
```


## Sample Code

Following is a listing of the sample code provided. More details can be found
in the READMEs provided in each src directory.

| Source File | Entry Point | Description |
| ----------- | ----------- | ----------- |
| `src/configure.py` | v20-configure | Create/update a v20.conf file |
| `src/market_order_full_example.py` | v20-market-order-full-example | Limited Market Order example that does not use the v20.conf file |
| `src/account/details.py` | v20-account-details | Get the details of the current active Account |
| `src/account/summary.py` | v20-account-summary | Get the summary of the current active Account |
| `src/account/instruments.py` | v20-account-instruments | Get the list of tradeable instruments for the current active Account |
| `src/account/changes.py` | v20-account-changes | Follow changes to the current active Account |
| `src/account/configure.py` | v20-account-configure | Set configuration in the current active Account |
| `src/instrument/candles.py` | v20-instrument-candles | Fetch candles for an instrument |
| `src/instrument/candles_poll.py` | v20-instrument-candles-poll | Fetch and poll for candle updates for an instrument |
| `src/order/get.py` | v20-order-get | Get the details of an order in the current active Account |
| `src/order/list_pending.py` | v20-order-list-pending | List all pending Orders for the current active Account |
| `src/order/cancel.py` | v20-order-cancel | Cancel a pending Order in the current active Account |
| `src/order/set_client_extensions.py` | v20-order-set-client-extensions | Set the client extensions for a pending Order in the current active Account |
| `src/order/market.py` | v20-order-market | Create a Market Order in the current active Account |
| `src/order/entry.py` | v20-order-entry | Create or replace an Entry Order in the current active Account |
| `src/order/limit.py` | v20-order-limit | Create or replace a Limit Order in the current active Account |
| `src/order/stop.py` | v20-order-stop | Create or replace a Stop Order in the current active Account |
| `src/order/take-profit.py` | v20-order-take-profit | Create or replace a Take Profit Order in the current active Account |
| `src/order/stop-loss.py` | v20-order-stop-loss | Create or replace a Stop Loss Order in the current active Account |
| `src/order/trailing-stop-loss.py` | v20-order-trailing-stop-loss | Create or replace a Trailing Stop Loss Order in the current active Account |
| `src/pricing/get.py` | v20-pricing-get | Fetch/poll the current Prices for a list of Instruments |
| `src/pricing/stream.py` | v20-pricing-stream | Stream Prices for a list of Instruments |
| `src/transaction/stream.py` | v20-transaction-stream | Stream Transactions for the current active Account |
| `src/transaction/poll.py` | v20-transaction-poll | Poll Transactions for the current active Account |
| `src/transaction/get.py` | v20-transaction-get | Get details for a Transaction in the current active Account |
| `src/transaction/range.py` | v20-transaction-range | Get a range of Transactions in the current active Account |
| `src/trade/get.py` | v20-trade-get | Get all open Trades or a specific Trade in the current active Account |
| `src/trade/close.py` | v20-trade-close | Close (partially or fully) a Trade in the current active Account |
| `src/trade/set_client_extensions.py` | v20-trade-set-client-extensions | Set the client extensions for an open Trade in the current active Account |
| `src/position/close.py` | v20-position-close | Close a position for an instrument in the current active Account |


# Commonly-used-commands Examples:
## Account
#### returns table of active orders
```
(env)C:\user\oanda: python src/account/details.py
```
#### returns account details
```
(env)C:\user\oanda: python src/account/summary.py
```
#### returns list of tradable instruments (e.g. EUR_USD)
```
(env)C:\user\oanda: python src/account/instruments.py
```
## Order
#### place market order
```
(env)C:\user\oanda: python src/order/market.py INSTRUMENTS UNITS --stop-loss-price STOPLOSSPRICE --take-profit-price TAKEPROFITPRICE
e.g. 
(env)C:\user\oanda: python src/order/market.py EUR_USD 2 --stop-loss-price 1.72 --take-profit-price 1.91
```
#### place limit order
```
(env)C:\user\oanda: python src/order/market.py INSTRUMENTS UNITS PRICE
e.g. 
(env)C:\user\oanda: python src/order/market.py EUR_USD 2 1.75
```
#### returns list of pending orders
(env)C:\user\oanda: python src/order/list_pending.py

## Instrument 
#### Displays candlestick chart
```
(env)C:\user\oanda: python src/instrument/candles_chart.py
```
#### Returns list of candles for an instrument
```
(env)C:\user\oanda: python src/instrument/candles.py INSTRUMENT
```

## Capture screenshots
## Commonly-used-commands Examples:

----Account----

# returns table of active orders
(env)C:\user\oanda: python src/account/details.py

# returns account details
(env)C:\user\oanda: python src/account/summary.py

# returns list of tradable instruments (e.g. EUR_USD)
(env)C:\user\oanda: python src/account/instruments.py

----Order----

# place market order
(env)C:\user\oanda: python src/order/market.py INSTRUMENTS UNITS --stop-loss-price STOPLOSSPRICE --take-profit-price TAKEPROFITPRICE
e.g. 
(env)C:\user\oanda: python src/order/market.py EUR_USD 2 --stop-loss-price 1.72 --take-profit-price 1.91

# place limit order
(env)C:\user\oanda: python src/order/market.py INSTRUMENTS UNITS PRICE
e.g. 
(env)C:\user\oanda: python src/order/market.py EUR_USD 2 1.75

# returns list of pending orders
(env)C:\user\oanda: python src/order/list_pending.py

----Instrument----
pip install oanda-candles

# Displays candlestick chart
(env)C:\user\oanda: python src/instrument/candles_chart.py

# Returns list of candles for an instrument
(env)C:\user\oanda: python src/instrument/candles.py INSTRUMENT


## Capture screenshots ##
```
(env)C:\user\oanda: python src/instrument/candles_chart.py
```
- Open another terminal
- change image destination path in capture.py
- set time interval for captures in capture.py
- adjust the capture region using x and y values as needed in capture.py
```
(env)C:\user\oanda: pip install pyautogui
>>>>>>> cf61f1c683b58e0ba04eb90b0eafffc28183a83e
(env)C:\user\oanda: python capture.py
```
