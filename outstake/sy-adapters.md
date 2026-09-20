# SY: Standardized Yield and the adapter matrix

## What is SY?

Yield-bearing tokens come in different shapes: Aave's aToken, Lido's wstETH, Sky's sUSDS, and so on. They come from different protocols, keep their books in different ways, and support different assets for conversion.

**SY (Standardized Yield)** is a uniform wrapper OutStake puts over these yield-bearing tokens. Whichever protocol sits underneath, SY presents the same outward shape: deposit an asset and receive SY, and redeem SY back into the asset. Under normal conditions, you can also check its current value in the underlying asset at any time.

With this wrapper in place, the layers above (minting uAsset, staking, cross-chain transfers) integrate with the SY layer only, instead of adapting to every protocol separately.

## Supported protocols

Each integrated protocol gets a matching SY adapter. Currently supported:

| Protocol | Yield-bearing token | Underlying asset | Accepted for deposit | Redeemable into |
|---|---|---|---|---|
| **Aave V3** | aToken (e.g. aUSDC) | USD | aToken or the underlying asset (e.g. USDC) | aToken or the underlying asset |
| **Lido** | wstETH | ETH | wstETH, stETH, or native ETH | wstETH or stETH |
| **EtherFi** | weETH | ETH | Not yet integrated in the current version | Not yet integrated in the current version |
| **Sky** | sUSDS | USD | sUSDS or USDS | sUSDS or USDS |
| **Ethena** | sUSDe | USD | sUSDe or USDe | sUSDe only |
| **Lista** | slisBNB | BNB | slisBNB or native BNB | slisBNB only |
| **Aster** | asBNB | BNB | asBNB, slisBNB, or native BNB | asBNB only |

Lido and Sky each come in a mainnet deployment and L2 deployments, and the L2 deployments source their prices differently. On L2, Lido's exchange rate comes from the rate feed on Ethereum mainnet. Sky on L2 is priced directly off the Sky savings rate, cross-checked against the swap quote from the PSM3 stability module. For the L2 deployments, the "Accepted for deposit" and "Redeemable into" columns follow the assets each chain actually supports (Sky on L2, for example, also accepts USDC for entry).

Under normal conditions, exchange rates on L2 are readable at any time and quoted at mainnet value. If the rate feed fails briefly, the L2 sequencer goes down, or Sky's two price sources on L2 show a clear divergence, minting that depends on live-rate pricing becomes temporarily unavailable. It returns to normal automatically once conditions recover; no extra action is needed. If the backing an adapter itself holds falls below its outstanding shares, minting freezes automatically in the same way. Both safeguards freeze minting only, never redemption: redemption burns a proportional share of the debt and does not depend on the live rate. Rate feeds and circuit-breaker parameters are maintained by the protocol team and can be replaced when necessary.

## Flexible entry and exit

There are many ways in. You can enter directly with an underlying asset (ETH, USDC, BNB), or with a yield-bearing token you already hold (wstETH, sUSDS). Some adapters also accept a different currency (USDC into Sky on L2, for example). The adapter handles all conversions internally; there is nothing for you to work out yourself.

**What you can deposit is not necessarily what you can redeem back out.** The token you actually receive on redemption follows the "Redeemable into" column in the table above: some protocols redeem only into the yield-bearing token itself (Ethena into sUSDe only, Aster into asBNB only) and never automatically unwrap it into the underlying asset. To get the underlying asset back, unstake on that protocol yourself.

Exchange rates for each protocol are provided by the protocol itself (for example, Aave's lending rate or Lido's staking rate) and move with the market in real time.

## Why this design

- **Unified liquidity**: yield-bearing assets in the same family convert at their respective live values and flow into a single uAsset (UETH), with no separate pool for each.
- **Extensible**: adding a new protocol takes one new adapter and leaves the existing logic untouched.
- **Easy entry**: users can participate with any supported asset they already hold, without swapping into a specific token first.
