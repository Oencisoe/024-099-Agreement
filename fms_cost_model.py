#!/usr/bin/env python3
"""
Generates the SDP Co-Employer FMS Start-Up Cost & Revenue Model PDF.
Empowered Futures Independent Facilitation LLC.

All figures are planning-grade estimates compiled from public DDS / WCIRB /
market sources. English-language SDP FMS rates only. Not legal, tax, or
financial advice.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
)

# ---------- palette ----------
NAVY = colors.HexColor("#1f3a5f")
LIGHT = colors.HexColor("#eef2f7")
ACCENT = colors.HexColor("#2c6e8f")
GREY = colors.HexColor("#555555")
LINE = colors.HexColor("#bbbbbb")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("DocTitle", parent=styles["Title"], fontSize=18,
                          textColor=NAVY, spaceAfter=2, leading=21))
styles.add(ParagraphStyle("DocSub", parent=styles["Normal"], fontSize=10.5,
                          textColor=GREY, alignment=TA_CENTER, spaceAfter=2))
styles.add(ParagraphStyle("H2", parent=styles["Heading2"], fontSize=12.5,
                          textColor=NAVY, spaceBefore=12, spaceAfter=4))
styles.add(ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.3,
                          leading=13, spaceAfter=4))
styles.add(ParagraphStyle("Small", parent=styles["Normal"], fontSize=7.8,
                          leading=10, textColor=GREY))
styles.add(ParagraphStyle("Note", parent=styles["Normal"], fontSize=8.6,
                          leading=12, textColor=GREY, spaceAfter=3))
styles.add(ParagraphStyle("Cell", parent=styles["Normal"], fontSize=8.7,
                          leading=11))
styles.add(ParagraphStyle("CellR", parent=styles["Normal"], fontSize=8.7,
                          leading=11, alignment=2))
styles.add(ParagraphStyle("CellH", parent=styles["Normal"], fontSize=8.7,
                          leading=11, textColor=colors.white,
                          fontName="Helvetica-Bold"))
styles.add(ParagraphStyle("CellHR", parent=styles["Normal"], fontSize=8.7,
                          leading=11, textColor=colors.white,
                          fontName="Helvetica-Bold", alignment=2))


def P(t, s="Cell"):
    return Paragraph(t, styles[s])


def header_row(cells, aligns):
    return [Paragraph(c, styles["CellHR"] if a == "r" else styles["CellH"])
            for c, a in zip(cells, aligns)]


def make_table(headers, rows, col_widths, aligns, total_row=None):
    data = [header_row(headers, aligns)]
    for r in rows:
        data.append([P(c, "CellR" if a == "r" else "Cell")
                     for c, a in zip(r, aligns)])
    if total_row:
        data.append([Paragraph(c, ParagraphStyle(
            "tot", parent=styles["CellR" if a == "r" else "Cell"],
            fontName="Helvetica-Bold")) for c, a in zip(total_row, aligns)])
    t = Table(data, colWidths=col_widths, hAlign="LEFT")
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
    ]
    if total_row:
        style.append(("BACKGROUND", (0, -1), (-1, -1), colors.HexColor("#dce6f0")))
        style.append(("LINEABOVE", (0, -1), (-1, -1), 0.8, NAVY))
    t.setStyle(TableStyle(style))
    return t


def rule():
    return HRFlowable(width="100%", thickness=0.6, color=LINE,
                      spaceBefore=6, spaceAfter=6)


def build(path):
    doc = SimpleDocTemplate(path, pagesize=letter,
                            leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                            topMargin=0.55 * inch, bottomMargin=0.5 * inch,
                            title="SDP Co-Employer FMS Start-Up Cost & Revenue Model")
    e = []

    # ---- header ----
    e.append(Paragraph("Empowered Futures Independent Facilitation LLC", styles["DocSub"]))
    e.append(Paragraph("SDP Financial Management Services &mdash; Co-Employer (Code 316)", styles["DocTitle"]))
    e.append(Paragraph("Start-Up Cost &amp; Revenue Model &nbsp;|&nbsp; English-language rates &nbsp;|&nbsp; Prepared June 2026", styles["DocSub"]))
    e.append(rule())

    # ---- assumptions ----
    e.append(Paragraph("Assumptions", styles["H2"]))
    for b in [
        "Lean, remote, founder-led operation built around the <b>Co-Employer model (Service Code 316)</b>; able to add clinical/nursing as participant-directed services.",
        "FMS fees are <b>paid by the Regional Center outside</b> the participant's individual budget &mdash; they do not reduce participant services, and the fee tier is driven by the <b>number of providers</b>, not their wages.",
        "Employer burden (FICA, Medicare, FUTA, SUI, and <b>workers' compensation</b>) is a <b>funded</b> pass-through per the DDS approved employer-burden schedule &mdash; not founder overhead.",
        "Surety bond = <b>20% of the total of all participant individual budgets served</b>; premium estimated at ~1.5% of the bond face (good credit).",
        "Average participant individual budget assumed at <b>$40,000</b> for bond sizing (SDP range ~$15,000&ndash;$50,000+).",
    ]:
        e.append(Paragraph("&bull;&nbsp; " + b, styles["Body"]))

    # ---- Section 1: rates ----
    e.append(Paragraph("1. SDP Co-Employer FMS Rates (English-language, RC-paid outside budget)", styles["H2"]))
    e.append(make_table(
        ["Providers in spending plan", "Maximum monthly rate"],
        [["0&ndash;4 providers", "$420"],
         ["5&ndash;10 providers", "$660"],
         ["11+ providers", "$840"]],
        [3.6 * inch, 3.6 * inch], ["l", "r"]))
    e.append(Paragraph("Effective May 1, 2023 schedule (English maximums). Non-English maximum ($925) excluded. Confirm any one-time start-up fee with your vendoring Regional Center.", styles["Note"]))

    # ---- Section 2: one-time ----
    e.append(Paragraph("2. One-Time Start-Up Costs", styles["H2"]))
    e.append(make_table(
        ["Item", "Low", "Expected", "High"],
        [["Entity formation (LLC, registered agent, operating agreement)", "$500", "$1,500", "$2,500"],
         ["Legal &mdash; FMS agreements, Title 17 compliance review", "$3,000", "$7,500", "$15,000"],
         ["IRS / EDD employer-agent setup (Form 2678, accounts)", "$500", "$1,000", "$2,000"],
         ["FMS / payroll software implementation &amp; onboarding", "$2,000", "$6,000", "$15,000"],
         ["Accounting system setup", "$500", "$1,000", "$2,000"],
         ["Disaster-recovery / business-continuity plan + policies", "$1,000", "$2,500", "$5,000"],
         ["Website / branding / launch marketing", "$1,000", "$3,000", "$6,000"],
         ["Equipment / home office", "$1,000", "$2,000", "$4,000"]],
        [3.7 * inch, 1.1 * inch, 1.2 * inch, 1.1 * inch], ["l", "r", "r", "r"],
        total_row=["Subtotal (core, SOC deferred)", "$9,500", "$24,500", "$51,500"]))
    e.append(Paragraph("Optional SOC 1 audit (often deferred to Year 2): readiness $8,000&ndash;$20,000; Type I $10,000&ndash;$25,000. With SOC, one-time subtotal ~$27,500 / $51,500 / $96,500.", styles["Note"]))

    # ---- Section 3: recurring ----
    e.append(Paragraph("3. Year-1 Recurring Operating Costs", styles["H2"]))
    e.append(make_table(
        ["Item", "Low", "Expected", "High"],
        [["Surety bond premium (see Section 4)", "$1,200", "$3,000", "$6,000"],
         ["Own insurance &mdash; GL + E&amp;O + cyber + fidelity + employer liability", "$2,500", "$4,500", "$8,000"],
         ["FMS / payroll software subscription", "$4,000", "$9,000", "$18,000"],
         ["Outsourced bookkeeping / CPA / payroll-tax filing", "$6,000", "$12,000", "$20,000"],
         ["CA franchise tax", "$800", "$800", "$800"],
         ["Bank fees, phone, misc. software", "$2,000", "$3,500", "$5,000"]],
        [3.7 * inch, 1.1 * inch, 1.2 * inch, 1.1 * inch], ["l", "r", "r", "r"],
        total_row=["Subtotal (before staff labor)", "$16,500", "$32,800", "$57,800"]))
    e.append(Paragraph("Staff labor (payroll-capable, 1&ndash;2 FTE): $0 (founder unpaid) / $80,000 / $135,000. Worker wages and funded employer burden are pass-through, not shown here.", styles["Note"]))

    # ---- Section 4: bond ----
    e.append(Paragraph("4. Surety Bond (scales with participants served)", styles["H2"]))
    e.append(make_table(
        ["Participants", "Total budgets (~$40k ea.)", "Bond face (20%)", "Annual premium (~1.5%)"],
        [["10", "$400,000", "$80,000", "~$1,200"],
         ["25", "$1,000,000", "$200,000", "~$3,000"],
         ["50", "$2,000,000", "$400,000", "~$6,000"],
         ["100", "$4,000,000", "$800,000", "~$12,000"]],
        [1.4 * inch, 2.0 * inch, 1.8 * inch, 2.0 * inch], ["l", "r", "r", "r"]))
    e.append(Paragraph("Annual bond review/renewal applies once served budgets total $500,000 or more in a state fiscal year (~13+ participants).", styles["Note"]))

    # ---- Section 5: revenue ----
    e.append(Paragraph("5. Revenue Projection (Co-Employer, blended ~$525/participant/month)", styles["H2"]))
    e.append(make_table(
        ["Participants", "Annual FMS revenue (RC-paid)"],
        [["10", "~$63,000"],
         ["25", "~$157,500"],
         ["50", "~$315,000"],
         ["100", "~$630,000"]],
        [3.6 * inch, 3.6 * inch], ["l", "r"]))

    # ---- Section 6: break-even ----
    e.append(Paragraph("6. Cash Need &amp; Break-Even Scenarios", styles["H2"]))
    e.append(make_table(
        ["Scenario", "Year-1 cash need", "Break-even"],
        [["Lean solo (founder unpaid, SOC deferred, ~15 participants)", "~$50,000&ndash;$65,000", "~10&ndash;15 participants"],
         ["Staffed (1.5 FTE, SOC readiness + Type I, ~25 participants)", "~$160,000&ndash;$215,000", "~30&ndash;40 participants"]],
        [3.5 * inch, 2.0 * inch, 1.7 * inch], ["l", "r", "r"]))
    e.append(Paragraph("Plan 3&ndash;6 months of runway before first billing (entity setup + 45-day RC vendorization review + onboarding), plus working capital to float payroll between paying workers and RC reimbursement.", styles["Note"]))

    # ---- Section 7: nursing ----
    e.append(Paragraph("7. Adding Nursing / Clinical Services under Co-Employer", styles["H2"]))
    for b in [
        "<b>Permitted &amp; fundable.</b> SDP allows participant-directed nursing; the spending plan must specify a qualified provider (RN, or LVN/LPN under RN supervision, licensed in California).",
        "<b>Generic-resources-first.</b> The participant must exhaust Medi-Cal and other generic nursing resources before SDP-funded nursing &mdash; this limits how much nursing flows through you.",
        "<b>Fee is wage-decoupled.</b> A nurse counts as one provider; your tier ($420/$660/$840) is unchanged by the nurse's higher wage.",
        "<b>Workers' comp is funded.</b> The higher home-health class-8835 premium (CA ~$2&ndash;$4 per $100 of payroll vs. ~$0.30&ndash;$0.50 clerical) is part of the funded employer burden, not your overhead.",
        "<b>Your real exposure.</b> The experience modifier on your master WC policy (a clinical claim raises your renewal across all participants), plus higher employer / professional / abuse-&amp;-molestation liability &mdash; budget toward the high end of own-insurance, and confirm carrier appetite for clinical exposure.",
        "<b>Verify with the RC.</b> Confirm they will authorize/fund nursing in your participants' spending plans and accept the FMS as employer of record for skilled (vs. supportive) nursing.",
    ]:
        e.append(Paragraph("&bull;&nbsp; " + b, styles["Body"]))

    # ---- disclaimer ----
    e.append(rule())
    e.append(Paragraph(
        "<b>Disclaimer.</b> Planning-grade estimates compiled from public DDS, WCIRB, and market sources for internal evaluation only &mdash; not legal, tax, financial, or insurance advice, and not a quote. Verify all FMS rates, bond, insurance, audit, and employer-burden requirements with your vendoring Regional Center, DDS, a licensed broker, and a CPA before relying on these figures.",
        styles["Small"]))
    e.append(Spacer(1, 4))
    e.append(Paragraph(
        "Sources: DDS SDP FMS Revised Rates; DDS Summary of Approved FMS Employer Burden (2025); DDS SDP FAQ (nursing qualifications, generic-resources-first); DDS FMS Models Comparison Chart; Title 17 CCR &sect;&sect;54310, 54327, 58884, 58886, 58887; DDS Directive D-2025-SDP-001 (Additional Requirements for Entities); WCIRB California classification 8835; CA Dept. of Insurance WC rate comparison; surety bond and SOC audit market cost guides.",
        styles["Small"]))

    doc.build(e)
    print("Wrote", path)


if __name__ == "__main__":
    build("FMS-CoEmployer-Cost-Model.pdf")
