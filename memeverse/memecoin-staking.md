# Memecoin Staking

## Stake to earn trading fees

Once a Memecoin goes live for trading (entering the Locked phase), its holders can **stake** the Memecoin into the YieldVault and earn continuous rewards.

## Where the rewards come from

The rewards come from **the Memecoin-denominated portion of this Memecoin's trading fees**: the more active the market and the higher the turnover, the more fees flow into the YieldVault, and the higher the stakers' rewards.

> Keep the fee split straight: of every trading fee, the Memecoin-denominated portion goes to the staking YieldVault, the uAsset-denominated portion goes to the DAO treasury, and the POL-denominated portion is burned. Stakers receive the Memecoin portion.

> Don't confuse the two vaults: the **YieldVault** belongs to Memecoin stakers, and its shares appreciate over time; the **DAO treasury** belongs to community governance and is spent through proposal votes. They are separate pools with separate beneficiaries.

This is what turns a "speculative asset" into a "yield-bearing asset".

## How it works

- Deposit Memecoin and receive the YieldVault's **share token**.
- Trading fees flow into the YieldVault continuously, and the value of the shares rises with them.
- On redemption, shares are converted back into Memecoin at a value that grows with accumulated rewards. The YieldVault carries a buffer mechanism: while the vault is still small, most incoming rewards are credited to the buffer first, so they are not all immediately reflected in share value.

The YieldVault is an **async-redemption** vault: deposits take effect immediately, while a redemption requires submitting a request first, with the payout arriving about 1 day later.

## Manipulation-resistant design

The YieldVault has two built-in protections against gaming:

- **Virtual buffer**: a fixed buffer amount is added to the share-to-asset conversion. To manipulate the share price with a large donation, an attacker would have to pay a cost comparable to the buffer, which makes the manipulation uneconomical. The buffer has a cost of its own: it also absorbs a portion of the rewards (the smaller the vault, the larger the portion), and that portion is not reflected in share value. That is the price paid for a stable exchange rate.
- **Delayed redemption**: payouts are not instant. Redemption happens in two steps: first submit a redemption request, and after a waiting period of about 1 day, **execute the second step yourself**. Only then is the Memecoin actually transferred back to your wallet. The waiting period prevents flash-loan arbitrage that deposits and withdraws within an instant. Each account can have at most 5 pending redemption requests at a time, and payouts only go to your own account. From the moment the request is submitted, that portion is fixed at its then-current value, stops accruing, and loses its voting power, effectively an early exit from governance. Once you have submitted a request, remember to come back and execute the payout when the waiting period ends.

## Stake and delegate to gain governance rights

The YieldVault share token **does not confer voting power directly**. Voting power takes effect only after the shares' voting power is **delegated** to yourself (or a designated representative). After staking, remember to complete this step: only then do the shares carry **voting power** in this Memecoin's community and let you participate in DAO governance (see [DAO governance](dao-governance.md); for where delegation sits in the epoch reward loop, see the [epoch reward diagram](dao-governance.md) on that page).

Voting power follows the shares, not the depositor: even if someone else made the deposit, the votes belong solely to whoever holds the shares, and that holder must complete the delegation personally. Undelegated shares generate no votes, but they still count toward the governance voting base, raising the number of votes a proposal needs to reach quorum.

This creates a virtuous cycle: **people who hold and stake long term and complete delegation earn the rewards and gain a voice in governance**, steering the community from short-term speculation toward long-term building.

## Cross-chain yield aggregation

A Memecoin may trade on multiple chains. The fee yield generated on each chain is **aggregated cross-chain** into the YieldVault on the governance chain and distributed to stakers from there. Wherever the trading happens, stakers receive their share.

> Note: cross-chain staking depends on the YieldVault being in place on the governance chain (the YieldVault is deployed only after the Memecoin completes Genesis on the governance chain and enters the Locked phase). If the YieldVault is not yet in place when you initiate, or the Memecoin ultimately fails its Genesis, the Memecoin arriving cross-chain goes directly to the recipient and does not enter the YieldVault. In that case there are no staking shares and no voting power. After it arrives, verify your YieldVault shares rather than just your token balance (see [Omnichain interoperability](omnichain.md)).

## Example

> A Memecoin goes live and trades actively, generating large fees every day, with the Memecoin-denominated portion flowing into the YieldVault. Holders stake their Memecoin into the YieldVault; the shares appreciate as fees accumulate, and on redemption they typically get back more Memecoin than they deposited. Once delegation is complete, the shares' voting power takes effect and can be used to vote on proposals in that Memecoin's DAO. The hotter the trading, the higher the staking rewards; and staking in turn locks circulating supply and confers governance rights. This is the key to its shift from "pure speculation" to "an asset with ongoing value".
