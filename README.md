- What is written below applies to https://swapdog.io - a re-branded SwapMatic v1
- SwapMatic v2 is a 0x-protocol based aggregator found in https://swapmatic.io and https://v2.swapmatic.io

# SwapMatic v1 a.k.a. Swapdog.io on Matic Network
Swapdog implements Uniswap v1 protocol on Matic Mainnet Network. Enjoy fast and affordable swaps in https://swapdog.io.

## Background
Swapdog is 100% decentralized service. Anyone
- Can create exchanges
- Add or remove liquidity
- Receive 0.3% pool rewards (= the exchange fee)
- Leverage existing liquidity pools
- Develop around the core factory contract
- See active markets and prices here: https://info.swapdog.io

## Setup

**Step 1: Configure MetaMask**
- MetaMask: https://github.com/BlockTimeWorld/MiniSwap/blob/master/MetaMask%20for%20Matic.PNG
- See also: https://docs.matic.network/docs/develop/network-details/network#matic-mainnet

**Step 2: The Site**
- The service can be found in https://swapdog.io

**Note This**
- Swapdog supports injected web3 only at this moment
- MetaMask, Saturn, and Nifty wallets are tested and working fine
- Instead of Ether (ETH), the base currency in Swapdog is MATIC because it is the 'ETH' in Polygon Network

## Contracts
The core factory contract was implemented in address `0x90D882B2789523403ff263D1F93Ead986c38446C`
> Swapdog factory contract: https://polygonscan.com/address/0x90D882B2789523403ff263D1F93Ead986c38446C

The factory contract is **not** validated in Polygon Explorer, because the contract is written in Vyper - not in Solidity - and Polygon explorer does not support Vyper code validation. However, anyone can compare the bytecode with the code published in Ethereum and see that there is a 100% match - no foul play.
> Ethereum mainnet contract: https://etherscan.io/address/0xc0a47dfe034b400b47bdad5fecda2621de6c4d95#code

## APIs
Web3 libraries and APIs that work on Uniswap v1 will work 100% on Swapdog by changing the RPC endpoint and network ID (see above).  Read Uniswap v1 docs for details: https://uniswap.org/docs/v1/

Icons for tokens listed in Swapdog can be found here: https://io.blocktime.solutions/images/icons/

# Tokens on SwapMatic
Like in Uniswap, anyone can use standard ERC20 tokens in Swapdog. Create an exchange, add liquidity in pools, provide custom links, trade!

## PoS-Mapped Tokens
All PoS-mapped Mainnet tokens with good reputation can and will be listed. Only PoS-mapped tokens will be supported. Plasma-mapped tokens will **not** be supported to avoid confusion between Plasma/PoS WETH and DAI.
> Token mapper: https://mapper.matic.today/

## Native Tokens
Tokens native to Polygon Network are supported by default using the front end and custom links - read Uniswap v1 docs.

Getting a native Polygon Network token listed - i.e. a adding in the drop-down with an icon - requires manual configuration, and that can be done after a submission and vetting process, just like with bridged tokens.

## SwapMatic Token
A small amount of SwapMatic Token **SWAM** is available in Swapdog. SWAM will be distributed to liquidity providers and stakers - to be announced. More about SWAM here: https://github.com/BlockTimeWorld/SWAM-Token

## JUNK Token
A "test" token **JUNK** is available in Swapdog for a very low Matic price.  JUNK is pooled with MATIC, so it has *some* value and it is not a pure junk-testnet token. It does not try to become the next world domination currency! It is an opportunity to try out swapping using very small balances. Buy some JUNK, swap it back or add to the pool, but please do not empty the whole garbage can for yourself.

## Wrapped Matic WMATIC
Swapdog supports Wrapped Matic (c.f. WETH in Ethereum) deployment in address `0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270`.
- Explorer: https://polygonscan.com/address/0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270
- Swap WMATIC: https://swapdog.io/swap?outputCurrency=0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270

## Listing Your Token in SwapMatic
First, use the self-listing feature by pasting your address and creating an exchange and a pool. These are the first steps in any case.
To list your token with a logo in the drop-down menu item can be requested using this form:
- https://docs.google.com/forms/d/e/1FAIpQLSdP-HxzvmFoSzbAM3VVcZIPNYskcIdAlBNZNy6ZTWdxnF12Xg/viewform

## Custom Linking
- https://swapdog.io/swap?outputCurrency=0x368306eb52c8313fd398418c8220ddd560940e68
- https://swapdog.io/swap?inputCurrency=0x368306eb52c8313fd398418c8220ddd560940e68
- https://swapdog.io/swap?inputCurrency=0x66d575db1BbA30B6364C04A484E14Bc8DfEE2bbb?outputCurrency=0x368306eb52c8313fd398418c8220ddd560940e68
- https://swapdog.io/send?recipient=0x207Bb29D5D4BB9C3eDE0747306A1fAD6fD8567E2

## Contributions
If you want to contribute Swapdog financially (server costs, the value of admin's time), feel free to donate anything - your tokens, Matic, ETH - in address `0x207Bb29D5D4BB9C3eDE0747306A1fAD6fD8567E2` in Mainnet or Polygon Network.

Swapdog does not have full-time development resources, so anything and everything is by volunteer basis. Any substantial new development requires more than an idea and request - in other words, find a skilled developer or team and get it done yourself.

## Channels
- **Discord:** Discussions on development will take place in https://discord.gg/k7NB4wc channel on Discord.
- **Telegram:** Someone feel free to launch a Telegram server for reaching out the general audience. 

## Web Analytics
- **Audience:** https://datastudio.google.com/reporting/36fa453a-de94-4136-8b9e-11925247109c/page/jFwjB
- **Aquisition:** https://datastudio.google.com/reporting/b400beae-1583-4bc5-9e6e-7bd700f719fa/page/6JwjB
- **Behaviors:** https://datastudio.google.com/reporting/72d96dc3-b663-4bd8-88e4-a64aac431e51/page/aOwjB

___________________________

*Swapdog is provided by [BlockTime Solutions](https://blocktimesolutions.com) and it is a fork of [Uniswap v1](https://uniswap.org/docs/v1/). The service is **not officially affiliated** with [Matic Network](https://matic.network/)*
