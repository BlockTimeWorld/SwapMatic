# MiniSwap
MiniSwap implements Uniswap v1 protocol on Matic Mainnet Network. Enjoy fast and affordable swaps again!

## Background
MiniSwap is 100% decentralized service. Anyone
- Can create exchanges
- Add or remove liquidity
- Enjoy 0.25% pool feels, and
- Develop around the core factory contract
- Leverage existing liquidity pools

## Specifications
- Instead of Ether (ETH), the base currency in MiniSwap is MATIC because it replaces 'ETH' in Matic Network
- The core factory contract was implemented in address 0x...
- RPC endpoint: https://rpc.matic.today
- Network ID: 137
- Explorer: https://explorer.matic.today
- Supports injected web3 only; MetaMask is tested, maybe others work, too

## Contracts
The core factory contract is **not** validated in Matic Explorer, because the original contract is written in Vyper, not Solidity and Matic (Blockscout) explorer does not support Vype code validation. However, anyone can compare the bytecode with the orginal Ethereum v1 bytecode and see that there ia 100% match - no foul play!
- Ethereum mainnet contract:
- Matic Network contract:

## Development
Web3 and APIs that work on Uniswap v1 will work on MiniSwap by changing the RPC endpoint (see above)

# Supported Tokens
Like in Uniswap, any user can use any standard ERC20 token in MiniSwap. Create and exchange, pool liquidity, provide custom links, trade!
Read Uniswap v1 docs for details!

## Bridged Tokens
Mainstream tokens for existing Ethereum Mainnet projects with good reputation can be listed. Both Plasma or PoS bridge tokens in Matic Network will be supported. The icon will be picked up in Trust Wallet repository, just like in Uniswap. For that one, you need to provide both mainnet and Matic address of the token to get it configured correctly.

Shall new token bridges emerge (e.g. BlockTime Bridge in DUST Central - to be announced), these can be also supported.

## Native Tokens
Tokens native to Matic Network are supported by default as-is using the frond end or custom links.

Getting a native to Matic token listed - i.e. a adding into the drop-down with an icon - requires manual configuration work, and that can be done after a submission and vetting process - to be announced.

# To be Developed
For anyone interested in contributing MiniSwap and Matic Network ecosystem, ideas for development:
- Instructions, how-to's
- Liquidity Pool Info site
- Market info API endpoint
- Support for other wallets

A standards-compliant market information feed to exchanges and trackers should be developed. However, most of cyrpto market services support Uniswap v1 already, so for them is it a very small step to use MiniSawap as an information source.

## Disclaimer
*MiniSwap, BlockTime Solutions, or DUST Central are **on** but not officially affiliated **with** Matic Network.*
