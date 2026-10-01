# 3-minute screen recording script

## 0:00–0:20 — Context
“This is the Vireo Audio Set E support-ticket analysis. The request was monthly category and team volume, plus evidence for the two-hire question. I kept the implementation deliberately small and reproducible.”

## 0:20–0:45 — Prompts / approaches used
“The initial approach was to inspect the whole pack first, treat the existing tags as weak labels, and use the opening message plus closing note as the classification evidence. I tested broader keyword classification, but it over-triggered on generic support language.”

## 0:45–1:05 — What changed / what was discarded
“I discarded the broad keyword scorer because it produced too many false cross-category matches. The final approach keeps the existing category and only overrides it when the closing note contains a high-confidence issue phrase, such as ‘order not delivered’, ‘refund pending’, ‘amount deducted without order’, ‘warranty claim’, or ‘battery draining’.”

## 1:05–1:35 — Final tool
“Here is the local CLI. It loads the CSVs, applies the categorization rules, calculates SLA breaches using the policy targets, and writes the monthly category/team outputs. There is no API key and no external model dependency.”

## 1:35–2:05 — Validation
“I reviewed a stratified sample of 110 tickets, ten per existing category. The original tags agreed with the reviewed labels on 90 percent. The final hybrid categorizer agreed on 100 percent of that reviewed sample. This is deliberately presented as limited validation, not as a production accuracy guarantee.”

## 2:05–2:35 — Business result
“The requested window contains 11,641 tickets. Chat Frontline is the largest team at 3,030 tickets, or 26.03 percent. Billing has 477 SLA breaches, a 19.67 percent breach rate, and ₹166,950 of breach-credit exposure. Across all teams, the observed SLA-credit exposure is ₹452,200.”

## 2:35–3:00 — Staffing conclusion
“The data does not support using raw volume as the only staffing metric. The literal volume rule points to Chat Frontline, while Billing has the highest SLA-breach rate and transfer exposure. The policy also says Tier 2 should not be compared with Tier 1 on volume. The next decision should combine volume with actual capacity and handling-time data before assigning the two hires.”
