#!/usr/bin/env python3
import argparse, re
from pathlib import Path
import pandas as pd

SLA_MINUTES = {"chat":15, "voice":120, "social":240, "email":480}
CONTACT_COST = {"chat":210, "email":260, "voice":520, "social":240}
SLA_CREDIT = 350
TRANSFER_COST = 305

OVERRIDES = [
    ("Delivery & Shipping", [
        r"order not delivered", r"shipment not received", r"dlvry delayed",
        r"delivery delayed", r"shipment not rcvd", r"lost in transit",
        r"rto confirmed", r"incorrect product shipped", r"transit damage"
    ]),
    ("Returns & Refunds", [
        r"refund pending", r"refund not credited", r"rfnd pending",
        r"rfnd delay", r"reverse pickup", r"pkp not done", r"pickup not done"
    ]),
    ("Billing & Payments", [
        r"amount deducted without order", r"payment debited",
        r"failed ord after payment", r"gst invoice", r"invoice query",
        r"coupon not applied", r"payment gateway"
    ]),
    ("Warranty & Repair", [
        r"warranty claim", r"repair status", r"\brma\b",
        r"service centre", r"service center"
    ]),
    ("Charging & Battery", [
        r"battery draining", r"rapid battery drain", r"battery life",
        r"not charging", r"no charge", r"case not charging", r"not powering on"
    ]),
    ("Connectivity", [
        r"pairing failure", r"unable to pair", r"connection dropping",
        r"bt dropouts", r"not discoverable"
    ]),
    ("Account & Login", [
        r"otp", r"unable to log", r"cannot login", r"login code"
    ]),
    ("App & Firmware", [
        r"firmware update", r"update hang", r"app not opening", r"bug logged"
    ]),
    ("Audio Quality", [
        r"no audio one side", r"static noise", r"crackling",
        r"audio quality", r"sound.*one side", r"earbud.*silent"
    ]),
    ("Product Enquiry", [
        r"pre-sales query", r"product enquiry", r"compatibility query",
        r"shared spec sheet"
    ]),
]

def classify(row):
    base = str(row["category"])
    note = str(row["agent_notes"]).lower()
    for category, patterns in OVERRIDES:
        for pattern in patterns:
            if re.search(pattern, note, re.I):
                return category
    return base

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", default="data")
    ap.add_argument("--output-dir", default="outputs")
    args = ap.parse_args()
    data = Path(args.data_dir); out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)

    tickets = pd.read_csv(data/"tickets.csv")
    agents = pd.read_csv(data/"agents.csv")
    customers = pd.read_csv(data/"customers.csv")
    orders = pd.read_csv(data/"orders.csv")
    products = pd.read_csv(data/"products.csv")

    for c in ["created_at","first_response_at","resolved_at"]:
        tickets[c] = pd.to_datetime(tickets[c], errors="coerce")

    # Assignment window is explicitly Jan 2025 through Jun 2026.
    w = tickets[(tickets.created_at >= "2025-01-01") & (tickets.created_at < "2026-07-01")].copy()
    w["category_final"] = w.apply(classify, axis=1)
    w["month"] = w.created_at.dt.to_period("M").astype(str)

    # SLA calculations use policy targets and first response timestamps.
    w["first_response_min"] = (w.first_response_at-w.created_at).dt.total_seconds()/60
    w["sla_target_min"] = w.channel.map(SLA_MINUTES)
    w["sla_breach"] = w.first_response_min > w.sla_target_min
    w["sla_credit_inr"] = w.sla_breach.astype(int) * SLA_CREDIT
    w["transfer_cost_inr"] = w.transfers.fillna(0) * TRANSFER_COST
    w["contact_cost_inr"] = w.channel.map(CONTACT_COST)

    w.to_csv(out/"categorized_tickets.csv", index=False)
    w.pivot_table(index="month", columns="category_final", values="ticket_id", aggfunc="count", fill_value=0).to_csv(out/"monthly_category.csv")
    w.pivot_table(index="month", columns="assigned_team", values="ticket_id", aggfunc="count", fill_value=0).to_csv(out/"monthly_team.csv")

    team = w.groupby("assigned_team").agg(
        tickets=("ticket_id","size"),
        share=("ticket_id",lambda s: len(s)/len(w)),
        sla_breaches=("sla_breach","sum"),
        sla_breach_rate=("sla_breach","mean"),
        sla_credits_inr=("sla_credit_inr","sum"),
        transfers=("transfers","sum"),
        transfer_cost_inr=("transfer_cost_inr","sum")
    ).sort_values("tickets", ascending=False)
    team.to_csv(out/"team_summary.csv")

    category = w.groupby("category_final").agg(
        tickets=("ticket_id","size"),
        share=("ticket_id",lambda s: len(s)/len(w)),
        sla_breaches=("sla_breach","sum"),
        sla_breach_rate=("sla_breach","mean"),
        sla_credits_inr=("sla_credit_inr","sum")
    ).sort_values("tickets", ascending=False)
    category.to_csv(out/"category_summary.csv")

    # Lightweight audit log.
    audit = pd.DataFrame([
        ["tickets_all_rows", len(tickets)],
        ["tickets_in_assignment_window", len(w)],
        ["duplicate_ticket_ids", int(tickets.ticket_id.duplicated().sum())],
        ["created_dates_before_window", int((tickets.created_at < pd.Timestamp("2025-01-01")).sum())],
        ["created_dates_after_window", int((tickets.created_at >= pd.Timestamp("2026-07-01")).sum())],
        ["resolved_before_created", int((tickets.resolved_at < tickets.created_at).sum())],
        ["resolved_before_first_response", int((tickets.resolved_at < tickets.first_response_at).sum())],
        ["tickets_with_missing_order_id", int(tickets.order_id.isna().sum())],
        ["tickets_with_missing_transfers", int(tickets.transfers.isna().sum())],
        ["tickets_with_missing_csat", int(tickets.csat_score.isna().sum())],
    ], columns=["metric","value"])
    audit.to_csv(out/"data_audit.csv", index=False)

    print(f"Processed {len(w):,} tickets in the assignment window.")
    print(f"SLA breaches: {int(w.sla_breach.sum()):,}; SLA credits: Rs {int(w.sla_credit_inr.sum()):,}")
    print(f"Top team by volume: {team.index[0]} ({int(team.iloc[0].tickets):,})")
    print("No paid model/API is used; API run cost = Rs 0.")

if __name__ == "__main__":
    main()
