# Cross-chain and rate limits

## uAsset is natively omnichain

uAsset (UETH / UUSD / UBNB) is built on the **LayerZero OFT** standard and moves 1:1 between chains: tokens are burned when they leave the source chain and minted in equal amount on the destination chain. Total supply never changes; the tokens have simply crossed a chain boundary.

Every cross-chain send pays a messaging fee, quoted by the system and paid in the source chain's native token; the fee varies with the state of the pathway. Cross-chain amounts are carried at 6-decimal precision: any balance beyond six decimals stays on the source chain and does not travel. For example, if you hold 100.000000123 UUSD and send the full balance cross-chain, the amount transferred and delivered is 100.000000; the trailing 0.000000123 stays in your wallet on the source chain.

This means you can mint UUSD on one chain and use it on another, or send UETH from Ethereum to Base: uAsset is not tied to any single chain.

## Rate limits: preventing abnormal outflows

Cross-chain bridges carry risks (the security of the bridge itself, and sudden large outflows). Every cross-chain pathway therefore has a **rate limit**:

- It defines a volume cap and a recovery time window.
- Capacity consumed by transfers already in flight **recovers gradually** over time.
- Normal usage is unaffected. If an **abnormally large cross-chain outflow** occurs within a short period, the portion above the cap is temporarily blocked.

The effect: everyday cross-chain traffic flows freely, and if something abnormal happens the system has buffer time to respond instead of being drained in a short burst.

## Transfers already in flight are unaffected by pauses

One detail acts as a safeguard: even when uAsset is temporarily paused, **a cross-chain transfer that has already been sent still completes its delivery on the destination chain**. When the cross-chain message arrives, the destination chain mints the corresponding uAsset; the pause does not apply to this delivery path. This is so user funds aren't stranded by a pause. Symmetrically, **newly initiated cross-chain sends are temporarily blocked** during a pause and become available again automatically once it lifts. Note that cross-chain delivery is not absolutely guaranteed. Under extreme configuration or pathway problems, a stranded state can still occur: the tokens are already burned on the source chain but have not yet arrived on the destination chain.

## Adjustable per chain

The rate limit for each destination chain and each uAsset can be set independently, and the protocol adjusts them according to actual security needs.

## What cross-chain enables

Cross-chain capability makes uAsset a true **omnichain medium**: it can flow from OutStake to any chain where Memeverse is deployed, take part in Genesis and leverage on any chain, and never gets trapped on a single chain.
