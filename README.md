# Vireo Audio — Support Tickets (Set E)

## 1. Project overview
Small, reproducible support-ticket categorization and operating-analysis tool for the Vireo Audio Set E evaluation. It produces a categorized ticket dataset, monthly category/team tables, SLA/business metrics, validation evidence, and charts.

The implementation is deliberately deterministic and uses **no paid LLM/API**. Existing categories are treated as weak labels. The classifier keeps the original category unless the agent closing note contains a high-confidence operational issue phrase that supports a correction.

## 2. Business problem
Priya requested monthly volume by category and team for the Jan 2025–Jun 2026 analysis window, with the headcount question framed around the largest team. The supplied data shows Chat Frontline is the largest first-assigned team by volume, while Billing has materially higher SLA-breach exposure. The analysis therefore reports both volume and service-risk indicators rather than treating raw volume as a sufficient staffing metric.

## 3. Architecture
- ` Source data: supplied separately for analysis; raw ticket-level data is intentionally excluded from this public repository.
- `src/analyze.py`: loading, windowing, deterministic categorization, SLA calculations, summaries, and audit.
- `outputs/`: reproducible CSVs and charts.
- No database, web server, API key, model endpoint, or external service is required.

## 4. Prerequisites
- Python 3.10+
- pip

## 5. Installation
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## 6. Environment variables
None.

## 7. How to run
```bash
python src/analyze.py --data-dir data --output-dir outputs
```

## 8. Input files
`tickets.csv`, `agents.csv`, `customers.csv`, `orders.csv`, `products.csv`, `support-policy.pdf`, and `email-thread.txt`.

## 9. Output files
- `categorized_tickets.csv` (ticket-level working output; not published in this public repository)
- `monthly_category.csv`
- `monthly_team.csv`
- `team_summary.csv`
- `category_summary.csv`
- `validation_summary.csv` (public aggregate validation output)
- `data_audit.csv`
- PNG charts

## 10. Categorization approach
The taxonomy is the 11 categories already present in the export because they are operationally recognizable and stable enough for reporting. Existing tags are **not** treated as ground truth.

The classifier starts with the bot category and applies only high-confidence corrections from the closing note, e.g. `order not delivered` → Delivery & Shipping, `refund pending` → Returns & Refunds, `amount deducted without order` → Billing & Payments, `warranty claim` → Warranty & Repair, `battery draining` → Charging & Battery, `pairing failure` → Connectivity, `OTP` → Account & Login, `update hang` → App & Firmware, and `static noise` → Audio Quality.

This is intentionally narrower than a general-purpose LLM classifier: it is deterministic, inspectable, and has zero API cost.

## 11. Validation methodology
A stratified 110-ticket review sample was used: 10 tickets from each of the 11 categories. Each sampled ticket was reviewed using the opening customer message and closing agent note, without assuming the original tag was correct.

- Original tag agreement with reviewed labels: **90.0%**
- Final hybrid classifier agreement: **100.0%**
- Review design: equal allocation by category, so this is not a volume-weighted production accuracy estimate.
- The reviewed sample is evidence of the implemented corrections, not proof of future production accuracy.

## 12. Business metrics
Assignment window: **1 Jan 2025 through 30 Jun 2026**.

- 11,641 tickets.
- 1,292 first-response SLA breaches = 11.10%.
- SLA credit exposure: 1,292 × ₹350 = **₹452,200**.
- Chat Frontline: 3,030 tickets = **26.03%**, largest team by volume.
- Billing: 2,425 tickets = **20.83%**, 477 SLA breaches = **19.67%**, and ₹166,950 in SLA credits.
- Billing had 632 recorded transfers. At ₹305/transfer, that is **₹192,760** of transfer cost.
- Total current-system transfers in-window: 1,299, costing **₹396,195** under the policy rate. Legacy transfer fields are blank and are not treated as zero.

A useful data-derived process goal is to close Billing's SLA-breach-rate gap to the overall observed rate of 11.10%. At the same 2,425-ticket Billing volume, that would mean roughly 269 breaches instead of 477, or about 208 fewer breaches, equivalent to approximately **₹72,800** of SLA credits over the observed window. This is a scenario, not a forecast.

## 13. Cost calculation
The tool uses no paid API or model calls.

- Cost per run in API/model usage: **₹0**
- At approximately 650 tickets/week: 650 × 4.33 = **2,814.5 tickets/month**
- API/model cost at that volume: **₹0/month**
- Local compute, electricity, and engineering labor are not modeled.

## 14. Known limitations
- The export contains 139 tickets created before the stated Jan 2025 window. They are excluded from the requested monthly analysis but retained in the audit.
- 2,379 rows have `resolved_at < created_at`; 2,575 have `resolved_at < first_response_at`. These chronology anomalies are concentrated in `legacy_fd`. Resolution timestamps for migrated tickets were reconstructed from a legacy UTC event log, so handle-time metrics are not used as a business-case driver here.
- `transfers` is blank on legacy rows and is not imputed as zero.
- Existing categories are weak reference labels, not ground truth.
- Validation is a small, stratified analyst-reviewed sample; it should be expanded before production deployment.
- The classifier is deterministic rather than a learned model. This is intentional for the five-hour scope and reproducibility.
- The staffing analysis cannot establish true capacity, occupancy, handle-time distribution, shrinkage, or required FTEs.

## 15. Scope decisions
Deliberately excluded:
- Real-time production deployment — not required to answer the evaluation questions.
- Full workforce-management model — data lacks the capacity inputs needed for defensible FTE sizing.
- Automated hiring recommendation — would overstate what ticket volume alone can prove.
- CRM/helpdesk integration — unnecessary for the local evaluation.
- Sentiment analysis and SLA prediction — not needed for the requested decision.
- Multilingual model — not required to demonstrate the core categorization workflow.

## 16. Example output
Running the command produces the CSVs and charts under `outputs/`. The included `validation_summary.csv` (public aggregate validation output) records the reviewed sample and classifier agreement.

