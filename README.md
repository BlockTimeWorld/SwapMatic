# MiniSwap on Matic
MiniSwap implements Uniswap v1 protocol on Matic Mainnet Network. Enjoy fast and affordable swaps again!

## Background
MiniSwap is 100% decentralized service. Anyone
- Can create exchanges
- Add or remove liquidity
- Receive 0.3% pool rewards
- Leverage existing liquidity pools
- Develop around the core factory contract

Please note that the full name of service is **MiniSwap on Matic** and not to be confused with other projects with similar sounding name.

## Setup

**Step 1: Configure MetaMask**
- **Expand View** (optional) -> **Settings** -> **Networks** -> **Add Network**
- Network Name: **Matic**
- New RPC URL: **https://rpc-mainnet.matic.network**
- ChainID (optional): **137**
- Symbol (optional): **MATIC**
- Block Explorer URL (optional): **https://explorer.matic.network** -> **Save**

Examples:
- MetaMask: https://github.com/BlockTimeWorld/MiniSwap/blob/master/MetaMask%20for%20Matic.PNG
- See also: https://docs.matic.network/docs/develop/network-details/network#matic-mainnet

**Step 2: The Site**
- The service can be found in https://miniswap.app
- The backup address is https://miniswap.blocktimesolutions.com (same service)

**Note This**
- MiniSwap supports injected web3 only at this moment
- MetaMask, Saturn, and Nifty wallets are tested and working fine
- Instead of Ether (ETH), the base currency in MiniSwap is MATIC because it is the 'ETH' in Matic Network

## Contracts
The core factory contract was implemented in address `0x90D882B2789523403ff263D1F93Ead986c38446C`
> MiniSwap factory contract: https://explorer.matic.network/address/0x90D882B2789523403ff263D1F93Ead986c38446C/contracts

The factory contract is **not** validated in Matic Explorer, because the contract is written in Vyper - not in Solidity - and Matic explorer (Blockscout) does not support Vyper code validation. However, anyone can compare the bytecode with the code published in Ethereum and see that there is a 100% match - no foul play.
> Ethereum mainnet contract: https://etherscan.io/address/0xc0a47dfe034b400b47bdad5fecda2621de6c4d95#code

## APIs
Web3 libraries and APIs that work on Uniswap v1 will work 100% on MiniSwap by changing the RPC endpoint and network ID (see above).  Read Uniswap v1 docs for details: https://uniswap.org/docs/v1/

# Tokens on MiniSwap
Like in Uniswap, anyone can use standard ERC20 tokens in MiniSwap. Create an exchange, add liquidity in pools, provide custom links, trade!

## Bridged Tokens
Mainstream tokens for existing Ethereum Mainnet projects with good reputation can be listed. Both Plasma and PoS bridged tokens in Matic Network will be supported.

For listing a bridged token, the admin must learn about the project and get both mainnet and Matic address of the token to get it listed and configured correctly. We don't want scam tokens in MiniSwap.

## Native Tokens
Tokens native to Matic Network are supported by default using the front end and custom links - read Uniswap v1 docs.

Getting a native Matic Network token listed - i.e. a adding in the drop-down with an icon - requires manual configuration, and that can be done after a submission and vetting process, just like with bridged tokens.

## MiniSwap Token
A MiniSwap token **MISP** is available in MiniSwap for a very low Matic price. It does not try to become the next world domination currency, but is rather an opportunity to try out swapping with very small balances. Buy some MISP, swap it back, but please do not empty the whole MISP pool!

Please remember that MISP will be pooled with MATIC, so it has some value and it is not a pure junk-test token.

Any proceedings from MISP go to development and administration of MiniSwap service.

## Listing Your Token in MiniSwap
For now, use the self-listing feature by pasting your address and creating an exchange and a pool. These are the first steps in any case.
The process to add your token with a logo in the drop-down menu will be defined and announced later.

# Development

## Ideas
For anyone interested in contributing MiniSwap and Matic Network ecosystem, ideas for development:
- Liquidity Pool Info site
- Market info API endpoint
- Support for other wallets
- Writing and publishing how-to's
- Replicate the same for Uniswap v2 ("MegaSwap")

A standards-compliant market information feed to exchanges and trackers should be developed. However, most of cyrpto market services support Uniswap already, so for them is it a very small step to use MiniSawap as an information source.

## Contributions
If you want to contribute MiniSwap financially (server costs, the value of admin's time), feel free to donate anything - your tokens, Matic, ETH - in address `0x207Bb29D5D4BB9C3eDE0747306A1fAD6fD8567E2` in Mainnet or Matic Network. I may send you back some MISP as a thank-you note!

MiniSwap does not have full-time development resources, so anything and everything that will be done or published is by volunteer basis. Any substantial new development requires more than an idea and request - in other words, find a skilled developer or team and get it done yourself.

## Channels
**Discord:** Discussions on development will take place in https://discord.gg/sX4rfTk channel on Discord.

**Telegram:** Someone feel free to launch a Telegram server for reaching out the general audience. (Link will be added here when someone gets that started.)

## Disclaimer
*MiniSwap and BlockTime Solutions are **on** Matic but are not officially affiliated **with** Matic Network.*

___________________________

MiniSwap is provided by https://blocktimesolutions.com/ and it is a fork of https://uniswap.org/docs/v1/
