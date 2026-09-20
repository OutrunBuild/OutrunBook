# OutStake at a glance

> Yield-bearing assets from many protocols, unified and minted into the pegged stablecoin uAsset.

OutStake is Outrun's yield infrastructure. It solves an old problem: the yield-bearing tokens of **Aave, Lido, Sky, Ethena, Lista, and Aster** (aToken, wstETH, sUSDS, sUSDe…) each go their own way, leaving yield and liquidity fragmented across protocols. OutStake unifies them behind a standardized interface, then mints them into uAsset stablecoins that circulate omnichain.

## OutStake in three steps

1. **Take in assets**: the [SY standardized yield layer](sy-adapters.md) wraps yield-bearing tokens from different protocols behind one interface.
2. **Mint the stablecoin**: deposit a yield-bearing asset through [Genesis Staking](staking-modes.md) and mint [uAsset](uasset.md) (UETH / UUSD / UBNB) 1:1 with the asset's current value, each token pegged to 1 unit of the underlying asset. Or swap reserve assets directly at par through the [PSM](psm.md).
3. **Manage it**: redeem the position at any time (no lock-up, no liquidation), park idle uAsset in [USR savings](usr.md) to earn interest, and use the [one-stop entry](router.md) to run the whole flow as a single operation.

## Core concepts

| Concept | In one sentence | Details |
|---|---|---|
| **SY** | The standard layer that wraps all kinds of yield-bearing tokens into a single form | [SY adapter matrix](sy-adapters.md) |
| **uAsset** | Pegged stablecoins (UETH / UUSD / UBNB) | [uAsset](uasset.md) |
| **Genesis Staking** | The stake-to-mint position reserved for Memeverse: minted at face value, no interest, no liquidation, no lock-up | [Genesis Staking](staking-modes.md) |
| **PSM** | Two-way 1:1 par swaps between reserve assets and uAsset, with no position and no debt | [PSM par swaps](psm.md) |
| **USR** | The uAsset savings vault: deposit uAsset, receive interest-earning shares, withdraw anytime | [USR savings](usr.md) |
| **Cross-chain** | uAsset runs on LayerZero and circulates omnichain | [Cross-chain and rate limits](omnichain.md) |

## Where uAsset goes

uAsset does not stay inside OutStake. It is the unified medium of value in the Outrun ecosystem, and it flows to [Memeverse](../memeverse/README.md): as the funding for Memecoin Genesis, the interest on leveraged Genesis, and the payment currency for GenesisCredit. OutStake mints it; Memeverse consumes it. The two sides interlock through the supply and demand of uAsset (each module's yield loop is independent and nothing flows back across, see the [growth flywheel](../ecosystem/flywheel.md)).

## Why not just hold wstETH?

The first question many DeFi users ask is: "Why bother with OutStake when I can just hold wstETH and still collect Lido staking yield?" The answer comes down to three pieces of added value:

- **Unified and omnichain**: wstETH is native to Ethereum alone. Routed through OutStake it becomes UETH, which circulates omnichain over LayerZero and can be used on any supported chain, so liquidity does not have to be built up chain by chain.
- **Collateral keeps earning**: after Genesis Staking, the deposited yield-bearing assets keep generating yield and the exposure stays 100% yours. You take the uAsset and put it to use while the underlying yield keeps accruing in full.
- **A ticket into Memeverse**: UETH / UUSD / UBNB are the currencies that Memeverse's Genesis, leverage, and settlement are denominated in. Holding uAsset lets you join [standard Genesis](../memeverse/genesis.md) and complete your exit within the 24-hour protection window after a successful unlock, capturing Memecoin ecosystem returns on a principal-conserving basis. That is something holding wstETH directly cannot give you.

OutStake is not just "holding your LST in a different wrapper": it upgrades yield-bearing assets into a unified medium that works on every chain, never stops earning, and plugs into community launches.
