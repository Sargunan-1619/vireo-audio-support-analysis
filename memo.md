# To: Priya Raman, Head of Customer Experience, Vireo Audio
## Subject: Support ticket categorization and staffing analysis — Set E

### Executive summary
We built a reproducible ticket-categorization and support-operations analysis for the Jan 2025–Jun 2026 window. It uses the existing ticket taxonomy as a starting point but does not assume the bot tags are correct. The final categorizer makes only high-confidence corrections from agent closing notes, keeping the implementation deterministic and auditable.

### What we found
The analysis contains **11,641 tickets** in the requested window. **Chat Frontline is the largest first-assigned team with 3,030 tickets (26.03%)**. Billing has 2,425 tickets (20.83%).

The important operational difference is service risk: Billing has **477 first-response SLA breaches (19.67%)**, versus **11.10% across the full window**. Under the policy's ₹350 breach credit, the observed Billing exposure is **₹166,950**; total observed SLA-credit exposure is **₹452,200**.

The data also records **632 Billing transfers**, which represent **₹192,760** at the policy's ₹305 transfer-cost standard. Legacy rows have blank transfer fields and are not treated as zero.

### The number and the money
The cleanest directly observed business number is **₹452,200 of SLA credits across 1,292 breaches** in the analysis window:

**1,292 breaches × ₹350 = ₹452,200**

A data-derived process goal is to bring Billing's breach rate toward the overall observed rate of 11.10%. At the same Billing volume, that would imply about 269 breaches rather than 477 — approximately **208 fewer breaches, or ₹72,800 of SLA credits** over the observed window. This is a scenario, not a forecast.

### Categorization validation
We reviewed **110 tickets**, stratified at 10 per existing category. The original tags agreed with the reviewed labels on **90.0%** of the sample. The final hybrid categorizer agreed on **100%** of the reviewed sample.

This should be read as validation of the correction rules on a small stratified sample, not as a production-scale accuracy guarantee.

### Staffing question
The supplied data does **not** justify a staffing decision from raw volume alone. If Priya's literal rule is applied to the requested window, Chat Frontline — not Billing — is the largest team. At the same time, Billing shows the highest SLA-breach rate and the highest transfer count among the teams.

The policy also explicitly says Tier 2 agents should not be compared with Tier 1 on ticket volume. A defensible staffing decision therefore needs capacity/occupancy and handling-time evidence that this export does not contain.

### Limitations
The export contains pre-window legacy tickets and legacy chronology anomalies; these are documented in the audit. The categorizer is deterministic and uses no paid model/API. The validation sample is limited. Transfer metrics cannot be compared historically before the current helpdesk because the field did not exist in Freshdesk.

### Next step
Use the categorization output as the reporting layer, then validate the correction rules on a larger independent sample before production use. For staffing, combine ticket volume with actual handle time, staffed hours/occupancy, backlog, and repeat-contact measures before assigning the two hires.
