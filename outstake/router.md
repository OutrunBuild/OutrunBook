# One-stop entry

## One operation, start to finish

Normally, turning the tokens in your wallet into uAsset committed to a Memeverse Genesis takes several steps: swap into a yield-bearing token or a reserve asset, convert that into uAsset, then send it into Genesis.

The Router folds these steps into **one operation**: you specify which token to spend and which channel to take, and the system completes the entire process. All tokens are debited from your account automatically, with no manual moving of funds (on first use, you need to grant the spending approval).

## Channels into Genesis

Three channels lead from any token to Genesis:

- **PSM channel**: you hold a reserve asset such as USDC, USDT, ETH, or BNB → swap it at par for uAsset → send it straight into Genesis. **No position, no debt**; the lightest of the three.
- **CDP channel**: you hold any supported token, or already hold a yield-bearing asset → (the token is first swapped into a yield-bearing asset) → [Genesis Staking](staking-modes.md) mints uAsset → into Genesis. An OutStake position is created for you at the same time (the collateral keeps earning, no lock-up, redeem anytime).
- **Leveraged Genesis channel**: you hold a reserve asset → swap it at par for uAsset → commit the full amount as interest into Leveraged Genesis. You pay only the interest to receive the shares, and no position is created (see [Leveraged Genesis](../memeverse/polend.md)).

## Redeeming the position

Genesis through the CDP channel leaves a position behind. To redeem it, you need to hold uAsset equal to the position's debt and confirm the spending approval. Which protocol's assets you redeem into, and what you end up holding, follows the [adapter matrix](sy-adapters.md). uAsset that has been bridged to another chain must be bridged back first. Redemption itself charges no protocol fee; you only pay on-chain gas (see [Genesis Staking](staking-modes.md)).

## Preview before you transact

Genesis Staking and redemption both let you **preview before you execute**: before submitting, you see the estimated mint or redemption amount based on the on-chain state at that moment, so you can judge whether it is worth it.

Note: the preview is an **estimate of the current state, not a guaranteed value**. The rate and the room left under the mint cap at the moment of execution may both differ from preview time, and the amount you actually receive may be lower. If minting has already hit its cap, the entire transaction reverts. When submitting, set a minimum acceptable received amount as your slippage tolerance; if execution would land below it, the transaction reverts as well. Preview once more before the transaction goes through, and go by the latest state.

## Straight through to Memeverse

This is the shortest bridge between OutStake and Memeverse: have your uAsset ready in OutStake, and you can head straight to Memeverse to launch or join a community.

Note: the uAsset committed at Genesis goes into the Memecoin's four-pool portfolio and is managed by the protocol. To redeem the position left behind by the CDP channel, you must **hold an equivalent amount of uAsset separately** (the portion committed at Genesis is still in the four pools). You'll need to get that much uAsset before the redemption can go through.

The one paying and the one on record can be two different people: you put up the tokens, and the Genesis shares or the position are recorded under a designated user. Handy when you are operating for a friend.
