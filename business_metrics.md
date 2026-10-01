# Business metrics and arithmetic

## Observed window
1 Jan 2025–30 Jun 2026: **11,641 tickets**

## SLA exposure
Policy target depends on channel. A first response after target creates a ₹350 credit.

- Breaches: **1,292**
- Breach rate: **1,292 / 11,641 = 11.10%**
- Credit exposure: **1,292 × ₹350 = ₹452,200**

## Billing scenario
- Billing tickets: **2,425**
- Billing breaches: **477**
- Billing breach rate: **477 / 2,425 = 19.67%**
- Overall breach rate: **11.10%**
- Billing credits: **477 × ₹350 = ₹166,950**

If Billing reached the observed overall breach rate:
- Expected breaches at 11.10%: **2,425 × 11.10% ≈ 269**
- Avoided breaches: **477 − 269 ≈ 208**
- Scenario credit reduction: **208 × ₹350 = ₹72,800**

This is a scenario based on an observed benchmark, not a forecast or guaranteed saving.

## Transfer exposure
- Current-system transfers in window: **1,299**
- Cost standard: **₹305 / transfer**
- Transfer cost: **1,299 × ₹305 = ₹396,195**

Billing alone:
- 632 transfers × ₹305 = **₹192,760**

Legacy transfer blanks are not treated as zero.

## Monthly tool cost
- Stated operating volume: 650 tickets/week
- Monthly approximation: **650 × 4.33 = 2,814.5 tickets/month**
- Paid API/model calls: **none**
- Model/API cost per run: **₹0**
- Model/API cost per month at 2,814.5 tickets: **₹0**

Local compute and engineering labor are outside the scope of this cost estimate.
