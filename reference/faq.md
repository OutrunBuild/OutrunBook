# FAQ

## About uAsset stablecoins

**Is uAsset a stablecoin?**
Yes. uAsset is a pegged stablecoin: UETH is pegged to ETH, UUSD to USD, and UBNB to BNB. Each uAsset corresponds to one unit of the underlying asset's value and is backed by staked yield-bearing assets.

> Technical note: at the code level, uAsset is accounted for in a debt ledger. Each position records its outstanding minted amount, fully covered by the SY assets locked as collateral, and each PSM swap pool is backed one-for-one by protocol reserves. At the product level, uAsset works as a pegged stablecoin: minting converts at the full real-time value of the deposit, and redemption extinguishes debt in proportion to your share of the position. If an underlying protocol runs into trouble, that risk carries through to the corresponding uAsset. This is the risk inherent in holding any yield-bearing asset (see [Genesis Staking](../outstake/staking-modes.md) and [PSM par swaps](../outstake/psm.md)).

**Can uAsset be over-minted?**
No. Every position manager and every PSM swap pool has a mint cap that minting cannot exceed, and uAsset is burned when you redeem or swap it back. Minted amounts are calculated strictly from the current value of the staked assets or the face value of the reserves.

**Is it safe to transfer uAsset across chains?**
Cross-chain transfers are rate-limited, so unusually large outflows get buffered. Transfers already in flight are not affected by a temporary uAsset pause and will still arrive on the destination chain. Under extreme configurations or if a channel fails, funds can still be stranded and need recovery.

## About participating in Genesis

**Can I lose money joining a Memecoin Genesis?**
If the Genesis fails to reach its target, the uAsset you deposited (and the leverage interest you paid) is refunded in full, so you lose no principal. If the Genesis succeeds, you receive Memecoin or related claims under the rules.

**Can a Genesis be front-run or rugged?**
Genesis liquidity is locked for 365 days, and the team cannot withdraw it during the lock-up. The high fee at pool opening and the dynamic fees are **mitigations** against front-running and sandwich attacks: they significantly raise the cost of jumping the queue and of sandwiching. That greatly reduces the rug and front-running risks common to traditional Memecoins, but these mitigations do not promise to eliminate the risk entirely.

**What is leveraged Genesis? Is there liquidation risk?**
Leveraged Genesis lets you pay an interest charge to amplify your Genesis allocation. It has **no liquidation risk and does not depend on oracles**: what it amplifies is your Genesis share, the protocol carries out the unified settlement, and no position can become insolvent and be force-liquidated.

## About staking

**Can the system pause temporarily? Are my funds safe during a pause?**
It can. During maintenance or an emergency, the protocol may temporarily suspend some operations, or an L2 rate feed may be briefly disrupted. While a pause or disruption lasts, minting, swaps, savings, redemption, and transfers are temporarily unavailable; your funds stay safe where they are, and operations become available again automatically once service resumes. Cross-chain transfers already sent are unaffected and will still arrive normally.

**Do I have to redeem my position myself? Is there an auto-redeem?**
There is no auto-redeem. Positions have no maturity date and no automatic redemption; redeeming is entirely up to you (have an equivalent amount of uAsset ready and approve it for deduction; see [Genesis Staking](../outstake/staking-modes.md)). You do not need to worry about forgetting to redeem: a position never expires, and the collateral keeps earning inside it.

**How do I choose between Genesis Staking, PSM swaps, and USR savings?**
Hold yield-bearing assets and want uAsset while they keep earning → Genesis Staking. Hold only reserve assets like USDC, ETH, or BNB and want uAsset directly → PSM swaps. Hold idle uAsset and want interest on it → USR savings (when the per-family rate is active).

**How does a Memecoin earn yield?**
Stake the Memecoin in the YieldVault to earn a share of its trading fees. The more active the trading, the more stakers earn.

**What if I sent tokens to a protocol contract address by mistake?**
Some protocol contracts support a recovery operation executed by the protocol, and you can try requesting help through official channels. Not every asset can be recovered, so double-check the address before sending.

## About governance

**Who can take part in a Memecoin's DAO governance?**
Stake the Memecoin in the YieldVault to receive shares, then delegate the voting power to yourself (or to a delegate of your choice) to propose and vote. Shares that are not delegated produce no votes, but they still count toward the voting base.

**Who controls the DAO treasury's funds?**
Governance proposals decide. Treasury spending initiated through governance must be approved by a proposal vote, and a per-disbursement percentage cap prevents too much from being taken in a single action. Epoch rewards are distributed automatically at the preset ratio and need no proposal for each payment.

## About launching a Memecoin

**Can anyone launch a Memecoin?**
Yes, there is no barrier to entry. The launcher sets the rules and picks the chain, then starts the Genesis.

**Can I launch on multiple chains at the same time?**
Yes. A Memecoin is an omnichain token and supports simultaneous launches on multiple chains. Each chain raises funds and builds its pools independently and advances through the phases on its own, so one chain can reach a successful launch while another falls short of its raise and refunds.

## About the ecosystem

**What is the relationship between OutStake and Memeverse?**
OutStake mints uAsset; Memeverse consumes it (Genesis funding, leverage interest, GenesisCredit settlement). The two interlock through the supply and demand for uAsset: Memeverse makes uAsset useful, which drives more people to mint it on OutStake. Each side runs its own yield loop, and no yield flows back and forth between them. See the [growth flywheel](../ecosystem/flywheel.md) for details.

**How is Outrun different from other Memecoin platforms like Pump.fun?**
Memeverse is not a pure PvP launchpad: it pairs each Memecoin with four-pool depth, dynamic fees, leveraged Genesis, staking yield, and DAO governance, turning it into a community asset with lasting value. See [vs Pump.fun](../memeverse/vs-pump-fun.md) for details.
