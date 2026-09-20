# Glossary

A quick reference to terms used throughout the Outrun docs. Product terms stay in English; definitions are written in English.

## Core concepts

| Term | Definition |
|---|---|
| **uAsset** | Outrun's pegged stablecoins: UETH (pegged to ETH), UUSD (pegged to USD), and UBNB (pegged to BNB). Minted by OutStake; circulates omnichain. |
| **SY** | Standardized Yield: the standard layer that wraps yield-bearing tokens into one unified format. |
| **OFT** | Omnichain Fungible Token: the LayerZero-based omnichain token standard; uAsset, Memecoin, and GenesisCredit are all built on it. |
| **LayerZero** | An omnichain messaging and asset transfer protocol; the foundation of Outrun's omnichain capability. |

## OutStake

| Term | Definition |
|---|---|
| **Genesis Staking** | The staking mint reserved for Memeverse: deposit a yield-bearing asset, mint an equal value of uAsset at face value, and commit it to Genesis. No interest, no liquidation, no lock-up; redeem anytime. |
| **CDP position** | The position created by Genesis Staking: it records the yield-bearing collateral and the outstanding uAsset debt, and redemption repays the equal uAsset amount. |
| **Liquidity lock-up** | The liquidity locked once a Memeverse Genesis reaches its target: fixed at 365 days, during which the launcher cannot withdraw it. |
| **PSM** | The par swap pool: reserve assets and uAsset swap both directions at par 1:1 (USDC/USDT↔UUSD, ETH↔UETH, BNB↔UBNB), with no position and no debt. |
| **USR** | The uAsset savings vault: deposit uAsset and receive shares, deposit and withdraw anytime; the share price grows at the per-family rate. |
| **suToken** | USR savings shares (suETH / suUSD / suBNB). |
| **Mint cap** | The minting limit on each position manager and PSM swap pool, preventing over-issuance. |

## Memeverse

| Term | Definition |
|---|---|
| **Genesis** | The opening phase of a Memecoin launch, where participants commit uAsset. |
| **Four pools** | The four liquidity pools set up when a Genesis reaches its target: the primary pool (Memecoin/uAsset), POL/uAsset, PT/uAsset, and PT/POL. |
| **POL** | An ownership claim on locked liquidity. |
| **PT** | Principal Token, split from POL; represents the claim on principal and is pegged to uAsset. |
| **YT** | Yield Token, split from POL; represents the claim on yield, works as a leveraged asset, and redeems its share of residual value after settlement. |
| **YT Flash Swap** | The trading route for buying and selling YT with POL during the lock-up; it reuses PT/POL pool liquidity instead of running a separate YT pool. |
| **POL split** | Splitting 1 POL into 1 PT + 1 YT. |
| **POLend (leveraged Genesis)** | The mechanism that scales up a Genesis allocation by paying interest (in uAsset or GenesisCredit). |
| **Preorder** | Locks in Memecoin before Genesis; settles at a fixed low fee rate and unlocks linearly. |
| **Dynamic fee hook** | The Uniswap V4 hook that lets each pool's fee adjust dynamically with volatility and market impact. |
| **GenesisCredit** | A cross-chain participation credit used to offset leveraged Genesis interest. |
| **Memecoin Staking** | Staking Memecoin into the YieldVault to earn trading fee returns. |
| **YieldVault** | The staking yield vault for Memecoin Staking, with async redemption (deposits are instant; redemption arrives about one day after the request). |
| **DAO Governor** | The on-chain governance contract for each Memecoin community, managing proposals, voting, and the treasury. |
| **Settlement** | The process after the lock-up ends in which the protocol recalls the funds, repays debts, and distributes what remains. |
| **Genesis refund** | When a Genesis misses its target, participant funds are returned to the beneficiary recorded at participation. |
