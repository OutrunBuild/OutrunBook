# USR savings: earn interest on your uAsset

**USR** is the savings layer for uAsset. Deposit idle uAsset into the matching vault and receive **shares** in return; the share price grows over time at the per-family savings rate. Withdraw whenever you like; interest accrues automatically.

## The three vaults

| Deposit | You receive | Notes |
|---|---|---|
| UETH | suETH | ETH-family savings |
| UUSD | suUSD | USD-family savings |
| UBNB | suBNB | BNB-family savings |

Shares are your deposit receipt: at a glance you can see how many you hold and how much uAsset they convert back into at the current share price.

## Depositing and withdrawing

- **When available**: normally you can deposit and withdraw at any time. During a temporary uAsset pause, deposits and withdrawals are briefly unavailable (see the [FAQ](../reference/faq.md)). If the per-family rate is 0 (inactive), deposits and withdrawals work as usual; the shares simply do not grow in value. For whether the rate is currently active for each asset, go by what the interface shows.
- **Inputs and outputs**: you deposit uAsset and receive shares; on withdrawal you hand back shares and receive your uAsset principal plus interest.
- **Prerequisites and approvals**: your wallet must hold enough uAsset, and you confirm the spending approval before your first deposit; withdrawals require no approval.
- **Fees and failure handling**: deposits and withdrawals charge no protocol fee; you only pay network gas. Interest is paid out of a budget the protocol funds. When the budget runs short, interest growth pauses and resumes automatically once the budget is refilled. During a pause, your principal and the ability to deposit or withdraw are unaffected, and interest already accumulated stays as it is. Always go through the deposit entry: **do not transfer uAsset directly to the vault address**. A direct transfer creates no shares and the funds cannot be recovered.
- **Steps**: choose a vault → confirm the approval (first time only) → deposit and receive shares → withdraw at any time (principal plus interest arrives together).

## Is your money safe?

- **Not even the protocol can withdraw it**: the vault reserves no withdrawal path for the protocol; it can only fund the vault, never withdraw from it. Every uAsset in the vault belongs to the shareholders alone and can leave only by redeeming shares.
- **Interest is paid only from the funded budget**: interest does not come from minting; it comes from the budget the protocol actually deposits. When that budget falls short, growth pauses automatically and no new interest accrues during the pause; it resumes as soon as the budget is topped up.
- **A pause halts operations, not ownership**: during a uAsset pause the deposit and withdraw buttons are temporarily unavailable, but your shares and accumulated interest are unaffected; once the pause lifts, deposits and withdrawals work as normal.

Just swapped into uAsset and not sure where to put it yet? Let it earn in USR for now; you can always join a [standard Genesis](../memeverse/genesis.md) later.
