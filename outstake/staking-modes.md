# Genesis Staking: minted for Memeverse

OutStake staking has exactly one use: **minting uAsset to take part in Memeverse Genesis**. You deposit a yield-bearing asset, mint an equal value of uAsset at face value, and the minted uAsset goes straight into Genesis. The collateral keeps earning, and the exposure stays 100% with you.

## Minting at face value

Minting settles at **face value**, with no discount and no multiplier: a yield-bearing asset worth 1 ETH mints 1 UETH, and one worth 1,000 USD mints 1,000 UUSD.

Each mint opens a **position** for you. The position records two things: the yield-bearing asset you deposited as collateral, and the uAsset you minted (the debt). The two are matched one to one at their value at mint time.

## Three "no"s

- **No interest**: the debt does not grow over time. The current version charges no interest on minting.
- **No liquidation**: there is no forced liquidation on-chain. Price swings in the underlying asset never trigger any disposal of your position.
- **No lock-up**: the position has no maturity date and can be redeemed at any time. There is no such thing as "forgetting to redeem": redemption only happens when you initiate it, and the protocol never redeems on your behalf.

## Who keeps the yield: you do

The collateralized yield-bearing asset **keeps earning** inside the position, and the appreciation exposure is entirely yours. On redemption you get back the collateral together with all the yield it has accumulated.

The trade-off is that redemption requires you to **return an equal value of uAsset** (see below). If you have already spent the uAsset you minted (sent it into Genesis, for example), you need to acquire that amount again before you can redeem.

## Redeeming a position

- **When available**: any time after the position is opened; no waiting is required. Briefly unavailable during temporary system pauses (see the [FAQ](../reference/faq.md) for details).
- **Inputs and outputs**: you put in uAsset equal to the position's debt and get back the collateralized yield-bearing asset, accumulated yield included.
- **Prerequisites and approvals**: before you start, your wallet must hold enough uAsset, and the spending approval must be in place. The tokens you receive on redemption depend on the adapter of the protocol you deposited into; see the [adapter matrix](sy-adapters.md) for the assets each protocol can be redeemed into. uAsset that has been bridged to another chain must first be bridged back to its original chain before it can be used for redemption. Bridging is subject to cross-chain limits and channel configuration (see [Cross-chain and rate limits](omnichain.md) for details).
- **Fees and failure handling**: redemption itself carries no protocol fee; you only pay gas. If your wallet holds insufficient uAsset or the approval is too low, the whole transaction reverts, with no loss of funds.
- **Steps**: prepare an equal value of uAsset → confirm the spending approval → submit the redemption and choose the asset to receive → the yield-bearing asset arrives and the position settles at the same time (with a partial redemption, the remaining position stays open).

## Mint cap

Every position manager has a **mint cap**: its outstanding minted amount cannot exceed the configured limit, and this cap is the brake on uAsset supply. A mint that hits the cap reverts in full. Before submitting, you can preview the mint amount and set a minimum acceptable output as your slippage tolerance; below it the transaction reverts.

## Risk notes

- The underlying yield-bearing assets carry the risks of their own protocols (if Lido, Aave, or a similar protocol runs into trouble), and those risks pass through to the corresponding uAsset. This is inherent to holding any yield-bearing asset, not a risk created by Outrun's mechanism.
- If an adapter's on-chain rate feed is briefly off or lacks sufficient backing, minting that depends on live pricing becomes temporarily unavailable and resumes automatically once the feed recovers. The redemption path is unaffected.

Only have reserve assets like USDC, ETH, or BNB? Use the [PSM par swaps](psm.md) to swap directly into uAsset, no position needed. Holding idle uAsset and want it to earn? See [USR savings](usr.md).
