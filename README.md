# SwapMatic on Matic Network
SwapMatic implements Uniswap v1 protocol on Matic Mainnet Network. Enjoy fast and affordable swaps in https://swapmatic.io.

## Background
SwapMatic is 100% decentralized service. Anyone
- Can create exchanges
- Add or remove liquidity
- Receive 0.3% pool rewards (= the exchange fee)
- Leverage existing liquidity pools
- Develop around the core factory contract
- See active markets and prices here: https://blocktimeworld.com/swapmatic-markets/
- Website: https://web.swapmatic.io/

## Setup

**Step 1: Configure MetaMask**
- **Expand View** (optional) -> **Settings** -> **Networks** -> **Add Network**
- Network Name: **Matic**
- New RPC URL: **https://rpc-mainnet.maticvigil.com/**
- ChainID (optional): **137**
- Symbol (optional): **MATIC**
- Block Explorer URL (optional): **https://explorer-mainnet.maticvigil.com/** -> **Save**
- More info here: **https://docs.matic.network/docs/develop/network-details/network/**

Examples:
- MetaMask: https://github.com/BlockTimeWorld/MiniSwap/blob/master/MetaMask%20for%20Matic.PNG
- See also: https://docs.matic.network/docs/develop/network-details/network#matic-mainnet

**Step 2: The Site**
- The service can be found in https://swapmatic.io

**Note This**
- SwapMatic supports injected web3 only at this moment
- MetaMask, Saturn, and Nifty wallets are tested and working fine
- Instead of Ether (ETH), the base currency in SwapMatic is MATIC because it is the 'ETH' in Matic Network

## Contracts
The core factory contract was implemented in address `0x90D882B2789523403ff263D1F93Ead986c38446C`
> SwapMatic factory contract: https://explorer.matic.network/address/0x90D882B2789523403ff263D1F93Ead986c38446C/contracts

The factory contract is **not** validated in Matic Explorer, because the contract is written in Vyper - not in Solidity - and Matic explorer (Blockscout) does not support Vyper code validation. However, anyone can compare the bytecode with the code published in Ethereum and see that there is a 100% match - no foul play.
> Ethereum mainnet contract: https://etherscan.io/address/0xc0a47dfe034b400b47bdad5fecda2621de6c4d95#code

## APIs
Web3 libraries and APIs that work on Uniswap v1 will work 100% on SwapMatic by changing the RPC endpoint and network ID (see above).  Read Uniswap v1 docs for details: https://uniswap.org/docs/v1/

Icons for tokens listed in SwapMatic can be found here: https://io.blocktime.solutions/images/icons/

# Tokens on SwapMatic
Like in Uniswap, anyone can use standard ERC20 tokens in SwapMatic. Create an exchange, add liquidity in pools, provide custom links, trade!

## PoS-Mapped Tokens
All PoS-mapped Mainnet tokens with good reputation can and will be listed. Only PoS-mapped tokens will be supported. Plasma-mapped tokens will **not** be supported to avoid confusion between Plasma/PoS WETH and DAI.
> Token mapper: https://mapper.matic.today/

## Native Tokens
Tokens native to Matic Network are supported by default using the front end and custom links - read Uniswap v1 docs.

Getting a native Matic Network token listed - i.e. a adding in the drop-down with an icon - requires manual configuration, and that can be done after a submission and vetting process, just like with bridged tokens.

## SwapMatic Token
A small amount of SwapMatic Token **SWAM** is available in SwapMatic. SWAM will be distributed to liquidity providers and stakers - to be announced. More about SWAM here: https://github.com/BlockTimeWorld/SWAM-Token

## JUNK Token
A "test" token **JUNK** is available in SwapMatic for a very low Matic price.  JUNK is pooled with MATIC, so it has *some* value and it is not a pure junk-testnet token. It does not try to become the next world domination currency! It is an opportunity to try out swapping using very small balances. Buy some JUNK, swap it back or add to the pool, but please do not empty the whole garbage can for yourself.

## Wrapped Matic WMATIC
SwapMatic supports Wrapped Matic (c.f. WETH in Ethereum) deployment in address `0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270`.
- Explorer: https://explorer-mainnet.maticvigil.com/address/0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270/read-contract
- Swap WMATIC: https://swapmatic.io/swap?outputCurrency=0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270

## Listing Your Token in SwapMatic
First, use the self-listing feature by pasting your address and creating an exchange and a pool. These are the first steps in any case.
To list your token with a logo in the drop-down menu item can be requested using this form:
- https://docs.google.com/forms/d/e/1FAIpQLSdP-HxzvmFoSzbAM3VVcZIPNYskcIdAlBNZNy6ZTWdxnF12Xg/viewform

## Custom Linking
- https://swapmatic.io/swap?outputCurrency=0x368306eb52c8313fd398418c8220ddd560940e68
- https://swapmatic.io/swap?inputCurrency=0x368306eb52c8313fd398418c8220ddd560940e68
- https://swapmatic.io/swap?inputCurrency=0x66d575db1BbA30B6364C04A484E14Bc8DfEE2bbb?outputCurrency=0x368306eb52c8313fd398418c8220ddd560940e68
- https://swapmatic.io/send?recipient=0x207Bb29D5D4BB9C3eDE0747306A1fAD6fD8567E2

# Development

## Mumbai Development Build and UI
- Deployed in Mumbai test network and available in https://dev.swapmatic.io
- Use RPC	https://rpc-mumbai.matic.today and network ID 80001
- Mumbai Factory contract address: 0xd02b2F48dc3e8C0706777CE35043670C6e9DC718
- Buy test tokens MERC, RAIN, and TEST from the UI using Mumbai Test MATIC: https://faucet.matic.network/
- More about Mumbai here: https://docs.matic.network/docs/develop/network-details/network/ => Mumbai-Testnet
- Make sure to read the docs https://uniswap.org/docs/v1/

Exchanges deployed for test tokens:
- Exchange ID 1: {'name': 'RAIN Token', 'symbol': 'RAIN', 'decimals': '8', 'totalSupply': '25000000000000000', 'token_address': '0x5aEc90591F32F1098c8eCe7f21C718C3732019b5', 'exchange_address': '0x422aEfbfEF0e3602Dde6a328A6d58360b0803114', 'exchange_id': 1}
- Exchange ID 2: {'name': 'MERC Token', 'symbol': 'MERC', 'decimals': '12', 'totalSupply': '100000000000000000000', 'token_address': '0x3429e89F3bE1e840aE719c9dF59e586E52003eF8', 'exchange_address': '0xdAc5EB1D340AB672bc6078fA8C23514BC973cEfe', 'exchange_id': 2}
- Exchange ID 3: {'name': 'Test Token', 'symbol': 'TEST', 'decimals': '18', 'totalSupply': '100000000000000000000000000', 'token_address': '0x2a4f5817980547331965fc39F5FF531adBDd585D', 'exchange_address': '0xe1ee8Cd63880E42B8140b921cad00fFDBf333F30', 'exchange_id': 3}

## Ideas
For anyone interested in contributing MiniSwap and Matic Network ecosystem, ideas for development:
- Liquidity Pool Info site
- Market info API endpoint
- Support for other wallets
- Writing and publishing how-to's

A standards-compliant market information feed to exchanges and trackers should be developed. However, most of cyrpto market services support Uniswap already, so for them is it a very small step to use SwapMatic as an information source.

## Contributions
If you want to contribute SwapMatic financially (server costs, the value of admin's time), feel free to donate anything - your tokens, Matic, ETH - in address `0x207Bb29D5D4BB9C3eDE0747306A1fAD6fD8567E2` in Mainnet or Matic Network.

SwapMatic does not have full-time development resources, so anything and everything is by volunteer basis. Any substantial new development requires more than an idea and request - in other words, find a skilled developer or team and get it done yourself.

## Channels
- **Discord:** Discussions on development will take place in https://discord.gg/k7NB4wc channel on Discord.
- **Telegram:** Someone feel free to launch a Telegram server for reaching out the general audience. 

## Web Analytics
- **Audience:** https://datastudio.google.com/reporting/36fa453a-de94-4136-8b9e-11925247109c/page/jFwjB
- **Aquisition:** https://datastudio.google.com/reporting/b400beae-1583-4bc5-9e6e-7bd700f719fa/page/6JwjB
- **Behaviors:** https://datastudio.google.com/reporting/72d96dc3-b663-4bd8-88e4-a64aac431e51/page/aOwjB

___________________________

*SwapMatic is provided by [BlockTime Solutions](https://blocktimesolutions.com) and it is a fork of [Uniswap v1](https://uniswap.org/docs/v1/). The service is **not officially affiliated** with [Matic Network](https://matic.network/)*
