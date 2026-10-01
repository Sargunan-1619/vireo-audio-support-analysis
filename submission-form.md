# Submission form — verified draft

**What did you build, and what business outcome does it move?**  
A reproducible support-ticket categorization and operating-analysis tool for Jan 2025–Jun 2026. It produces categorized tickets, monthly category/team volume, SLA metrics, validation evidence, and charts. The clearest measured business opportunity is reducing first-response SLA breaches and associated ₹350 credits.

**State the number and the money.**  
11,641 tickets; 1,292 SLA breaches; 11.10% breach rate; ₹452,200 observed SLA-credit exposure.

**What does one run cost?**  
₹0 in model/API usage. The implementation uses no paid model/API.

**What would a month cost at approximately 650 tickets/week?**  
650 × 4.33 = 2,814.5 tickets/month; model/API cost remains ₹0.

**Show arithmetic.**  
1,292 breaches × ₹350 = ₹452,200.  
1,299 transfers × ₹305 = ₹396,195.  
Billing: 477 breaches × ₹350 = ₹166,950.  
Scenario: approximately 208 fewer Billing breaches × ₹350 = approximately ₹72,800.

**How do you know it works?**  
110-ticket stratified analyst review, 10 per category. Original tags agreed with reviewed labels on 90.0%; final hybrid categorizer agreed on 100.0%.

**Sample size.**  
110 tickets.

**How checked.**  
Reviewed opening customer message and closing agent note for each sampled ticket, without treating the original category as ground truth.

**Error rate.**  
Original tags: 10.0% error on the reviewed sample. Final hybrid: 0.0% error on the reviewed sample.

**Kind of case it gets wrong.**  
The deterministic rules can miss novel wording when the closing note lacks a high-confidence issue phrase; in those cases it intentionally preserves the existing tag rather than making a low-confidence guess.

**Did you change/narrow/push back on the client's ask? What, when, and why?**  
Yes. I did not treat “largest team gets two hires” as sufficient staffing evidence. The requested volume chart is provided, but the analysis also shows SLA breaches and transfers because raw ticket volume cannot establish capacity or FTE need. I also treated existing tags as weak labels rather than truth.

**What is wrong with what you are handing us? Bugs / shortcuts / known inaccuracies.**  
The supplied export contains pre-window legacy tickets and legacy chronology anomalies. Validation is limited to 110 tickets. The classifier is deterministic rather than an LLM model. No production capacity model is claimed.

**What did you deliberately leave out and why?**  
Real-time deployment, CRM integration, full workforce management, automated hiring recommendation, sentiment analysis, SLA prediction, and multilingual classification. These were not required to answer the core questions within the five-hour constraint and some require data not present in the pack.

**Anything built/found that nobody asked for?**  
A focused SLA-credit and transfer-cost analysis was added because Finance asked for the volume case and process-vs-hiring evidence.

**What did you use AI for? Tools/models.**  
AI assistance was used for analytical planning, implementation review, QA reasoning, and drafting deliverables. The final categorization tool itself uses no external AI model/API.

**Where AI helped.**  
Data-audit reasoning, rule design, edge-case review, and concise business reporting.

**Where AI wasted time.**  
Broad keyword classification was tested and discarded because generic support language created cross-category false matches.

**What was discarded?**  
The broad keyword-scoring classifier; the final implementation uses high-confidence closing-note overrides only.

**Screen recording link.**  
[MANUAL ACTION REQUIRED: paste final recording link]

**Public Google Drive link.**  
[MANUAL ACTION REQUIRED: paste public Drive link]

**Three things a person needs to know on Monday.**  
1. Chat Frontline is the largest team by volume in the requested window (26.03%).  
2. Billing has the highest SLA-breach rate (19.67%) and ₹166,950 observed breach-credit exposure.  
3. Do not use raw ticket volume alone to size the two hires; capacity/handling-time evidence is still missing.

**Honest hours spent.**  
[MANUAL ACTION REQUIRED: enter actual elapsed working time]

**GitHub repository URL.**  
[MANUAL ACTION REQUIRED: paste final repository URL]
