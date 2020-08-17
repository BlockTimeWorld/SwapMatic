# MiniSwap
MiniSwap implements Uniswap v1 protocol on Matic Mainnet Network. Enjoy fast and affordable swaps again!

## Background
MiniSwap is 100% decentralized service. Anyone
- Can create exchanges
- Add or remove liquidity
- Enjoy 0.25% pool feels, and
- Leverage existing liquidity pools
- Develop around the core factory contract

## Specifications
- Instead of Ether (ETH), the base currency in MiniSwap is MATIC because it is the 'ETH' in Matic Network
- The core factory contract was implemented in address 0x...
- RPC endpoint: https://rpc.matic.today
- Network ID: 137
- Explorer: https://explorer.matic.today
- Supports injected web3 only; MetaMask is tested, maybe others work, too

## Contracts
The core factory contract is **not** validated in Matic Explorer, because the contract is written in Vyper - not in Solidity - and Matic (Blockscout) explorer does not support Vyper code validation.

However, anyone can compare the bytecode with the code published in Ethereum and see that there ia 100% match - no foul play.
- Ethereum mainnet contract:
- Matic Network contract:

## Development
Web3 libraries and APIs that work on Uniswap v1 will work 100% on MiniSwap by changing the RPC endpoint and network ID (see above).  Read Uniswap v1 docs for details: https://uniswap.org/docs/v1/

# Supported Tokens
Like in Uniswap, anyone can use standard ERC20 tokens in MiniSwap. Create an exchange, add liquidity in pools, provide custom links, trade!

## Bridged Tokens
Mainstream tokens for existing Ethereum Mainnet projects with good reputation can be listed. Both Plasma and PoS bridged tokens in Matic Network will be supported.

Token's icon will be picked up in Trust Wallet repository, just like in Uniswap. For that one, a MiniSwap admin must know both mainnet and Matic address of the token to get it listed and configured correctly.

Shall new token bridges emerge (e.g. BlockTime Bridge in DUST Central - to be announced), these can be also supported.

## Native Tokens
Tokens native to Matic Network are supported by default as-is using the frond end and custom links - read Uniswap v1 docs.

Getting a native to Matic token listed - i.e. a adding in the drop-down with an icon - requires manual configuration, and that can be done after a submission and vetting process (to be announced).

# Development Needs
For anyone interested in contributing MiniSwap and Matic Network ecosystem, ideas for development:
- Liquidity Pool Info site
- Market info API endpoint
- Support for other wallets
- Writing and publishing how-to's
- Replicate the same for Uniswap v2 ("MegaSwap")

A standards-compliant market information feed to exchanges and trackers should be developed. However, most of cyrpto market services support Uniswap v1 already, so for them is it a very small step to use MiniSawap as an information source.

Please note that MiniSwap does not have full-time development resources, so anything and everything that will be done or published is by volunteer basis. BlockTome Solutions is committed to develop and keep the service oprational, but any substantial new development requires more than tan idea and request (wink wink: if you think it is a godo idea, find someone to work on it!).

## Disclaimer
*MiniSwap, BlockTime Solutions, or DUST Central are **on** but not officially affiliated **with** Matic Network.*
