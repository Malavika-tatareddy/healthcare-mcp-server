# US Healthcare Domain Notes
(Techcanvass course + extra terms that came up in practice tests)

---

## 1. Healthcare System Overview

No single government healthcare like UK/India's public hospitals — US healthcare runs mainly on **insurance**. Three key players:

- **Payer** — insurance company (UnitedHealthcare, Cigna, Aetna). Collects premium, pays for care.
- **Provider** — hospital, doctor, clinic, lab. Delivers the care.
- **Member/Patient** — receives the care.

Most Americans get insurance via their **employer**; a smaller group buys it individually or gets it from the government (Medicare/Medicaid).

**Real-life example:** Like a wedding function — the caterer (Provider) serves food, the person paying the bill (Payer) isn't the guest eating (Member).

**Interview tip:** Every healthcare software project is really just connecting these 3 parties.

---

## 2. Key Terms (Insurance Vocabulary)

| Term | Simple Meaning |
|---|---|
| **Premium** | Monthly fee to keep insurance active (like a subscription) |
| **Deductible** | Amount YOU pay first, before insurance starts paying |
| **Copay** | Small fixed fee per doctor visit |
| **Coinsurance** | After deductible, you pay a %, insurance pays the rest |
| **Out-of-Pocket Max** | Max you'll pay in a year — after that, insurance covers 100% |
| **Claim** | Bill the provider sends to the payer requesting payment |
| **EOB** (Explanation of Benefits) | Statement showing what was billed/paid — NOT a bill itself |
| **In-Network / Out-of-Network** | Providers with a contract with your insurer (cheaper) vs without (costly) |
| **Prior Authorization** | Insurance approval needed BEFORE certain treatments |
| **PCP** (Primary Care Physician) | Your family doctor — first point of contact |
| **Beneficiary/Subscriber** | The main person who owns the policy |
| **Dependent** | Family members covered under the subscriber's policy |

**Interview tip:** Deductible vs Copay is one of the most commonly asked distinctions.

---

## 3. Healthcare Quality and Patient Safety

- **Quality measures** — standardized scorecards (e.g., **HEDIS** = Healthcare Effectiveness Data and Information Set, maintained by **NCQA**) rating how well a health plan delivers preventive/quality care
- **Never Events** — serious preventable mistakes (wrong-site surgery, tool left inside patient) — heavily penalized
- **Accreditation** — bodies like **The Joint Commission** certify hospitals meet safety/quality standards (like ISO certification for hospitals)

**Real-life example:** HEDIS is like a school report card — but for a health insurance plan, grading whether members actually got preventive care.

---

## 4. Value Based Care (VBC)

Two payment models:
- **Fee-for-Service** (old) — paid per service done, regardless of outcome → can cause overtreatment
- **Value-Based Care** (new) — paid based on patient outcomes/quality, focused on **patient-centered care**

**Related terms:**
- **ACO** (Accountable Care Organization) — group of providers jointly responsible for patient health/cost; get bonus (shared savings) if they keep patients healthy and reduce costs
- **Bundled Payment** — one fixed payment for an entire treatment episode instead of billing each step separately

**Interview tip:** US healthcare is actively shifting from Fee-for-Service to Value-Based Care to control costs.

---

## 5. Health Insurances in USA

### 5a. Overview, Providers, Benefits
- **Private** insurance (employer/individual) vs **Public** insurance (government — Medicare/Medicaid)
- **Providers** — hospitals, doctors, labs, pharmacies who deliver care; insurers build a **network** of contracted providers
- **Benefits** — the specific services a plan covers (doctor visits, hospitalization, drugs, maternity, mental health, etc.)

### 5b. Type of Insurance Plans

| Plan | Full Form | Meaning |
|---|---|---|
| **HMO** | Health Maintenance Organization | Cheapest; needs PCP + referral for specialists; only in-network covered |
| **PPO** | Preferred Provider Organization | Costlier; no referral needed; can go out-of-network at higher cost |
| **EPO** | Exclusive Provider Organization | Like PPO but zero out-of-network coverage |
| **POS** | Point of Service | Mix of HMO+PPO — needs referral, but out-of-network allowed at higher cost |
| **HDHP** | High Deductible Health Plan | Low premium, high deductible |

**Interview tip:** HMO = cheap but restrictive (referral needed); PPO = costly but flexible (no referral).

### 5c. Claims (Claims Lifecycle) — most-asked topic

1. Patient gets treatment
2. Provider submits a **claim** (using EDI 837 — see section 8) to the payer
3. Payer does **Adjudication** — checks coverage, eligibility, prior authorization
4. This includes **Benefit Determination** — deciding coverage and payment for that specific treatment
5. Claim is **Approved / Denied / Partially Paid**
6. Patient receives an **EOB**
7. Payment released to provider (via EDI 835 — see section 8)

---

## 6. Health Policy and Legislation

- **HIPAA** (Health Insurance Portability and Accountability Act, 1996) — protects patient data privacy/security. **PHI** (Protected Health Information) must be encrypted, access-controlled, audit-logged. Any healthcare software MUST be "HIPAA compliant."
- Health policy plays a role in: balancing cost containment with access to care, ensuring equitable distribution of resources, and addressing health disparities — **all of these together**, not just one.

**Interview tip:** "HIPAA compliant" is one of the most commonly used phrases in this domain.

---

## 7. Health IT and Digital Health

- **EHR/EMR** — digital patient records (full detail in section 11)
- **Telehealth** — doctor consultations via video/phone
- **HIE** (Health Information Exchange) — system letting hospitals securely share patient records with each other
- **Interoperability** — different hospital software systems being able to correctly exchange/understand data (a major ongoing challenge)
- **HL7 / FHIR** — the actual technical standards that make interoperability possible (see section 9)
- **HITECH Act** (2009) — law that pushed hospitals to adopt and meaningfully use EHRs, via financial incentives. (Different from HIPAA — HIPAA = protects data privacy; HITECH = pushed EHR adoption)

**Chain to remember:** HL7/FHIR (format rules) → HIE (sharing network) → Interoperability (the goal)

---

## 8. EDI Transactions (Electronic Data Interchange)

Standardized electronic formats for payer-provider communication — no manual phone calls needed.

| Code | Purpose |
|---|---|
| **837** | Claim submission (provider → payer) |
| **835** | Payment/remittance advice (payer → provider) |
| **834** | Enrollment (adding/removing members) |
| **270/271** | Eligibility inquiry/response |
| **276/277** | Claim status inquiry/response |

**Interview tip:** Remember at minimum — **837 = claim going out, 835 = payment response coming back.**

---

## 9. HL7 and the OSI Model (background for "why Layer 7")

**HL7** (Health Level 7) = standard format for exchanging healthcare data between systems, so different hospital software can understand each other's patient data.

The "7" refers to **Layer 7 (Application Layer)** of the **OSI Model** — a 7-layer model describing how computer networking works, from raw signals up to actual usable content:

| Layer | Name | What it does |
|---|---|---|
| 1 | Physical | Raw signals over cables/WiFi |
| 2 | Data Link | Local device-to-device delivery (MAC address) |
| 3 | Network | Routing across networks (IP address) |
| 4 | Transport | Reliable, complete delivery (TCP/UDP) |
| 5 | Session | Keeps a connection open during a conversation |
| 6 | Presentation | Formats/encrypts data so both sides understand it |
| **7** | **Application** | Actual usable content — what the user/software sees |

HL7 only operates at Layer 7 — it defines the **structure of healthcare data itself** (like a lab report format), not how it physically travels over the network.

**FHIR** = the newer, modern version of HL7, built for web/app APIs.

---

## 10. Healthcare Reforms

Reforms fix 3 core issues: **Cost, Access, Quality**. The biggest reform = **ACA** (next section). Reforms create major BA/IT work since systems must be rebuilt to comply with new laws.

---

## 11. Medicare and Medicaid

| Program | Who it's for | Funded by |
|---|---|---|
| **Medicare** | Age 65+, or disability | Federal government (federal taxes) |
| **Medicaid** | Low-income (any age) | Federal + State combined |

**Medicare Parts:**
- **Part A** — Hospital (inpatient)
- **Part B** — Doctor visits (outpatient)
- **Part C** — Medicare Advantage (private plan alternative)
- **Part D** — **D**rugs (prescription coverage) — easy hook: "D for Drugs"

**Interview tip:** Medicare = age/disability-based, federal only. Medicaid = income-based, federal+state.

---

## 12. Affordable Care Act (ACA / "Obamacare")

2010 law. **Biggest provision: insurers cannot deny coverage or charge more for pre-existing conditions.**

Other changes:
- Created the **Health Insurance Marketplace** — online portal to compare/buy plans
- Expanded **Medicaid** eligibility
- Defined **Essential Health Benefits** every plan must cover
- Young adults can stay on parents' insurance till age 26

**Interview tip:** Lead with pre-existing conditions coverage first — it's the headline fact.

---

## 13. EHRs (Electronic Health Records)

- **EMR** (Electronic Medical Record) = digital record used within **one clinic/hospital only**
- **EHR** (Electronic Health Record) = digital record **shareable across multiple providers**

**Benefits:** Reduces medical errors, faster access to history, better coordination between doctors.

**Real-life example:** EMR = a single bank branch's paper ledger. EHR = Net Banking, accessible from anywhere.

**Future direction:** AI analyzing EHR data to predict health risks and suggest treatments.

**CPT & ICD codes** (used to document what's in a patient's record for billing/reporting):
- **CPT** (Current Procedural Terminology) — 5-digit codes for **procedures/services performed**, maintained by **AMA**
- **ICD** (International Classification of Diseases) — codes for **diagnoses**, maintained by WHO (US uses ICD-10-CM)
- Hook: CPT = what was *done*, ICD = what's *wrong*

---

## 14. Other Important Terms

- **COB** (Coordination of Benefits) — decides which insurance pays first ("primary") vs second ("secondary") when a patient has two insurance plans
- **NPI** (National Provider Identifier) — unique 10-digit ID for every healthcare provider, like an Aadhaar number for providers

---

# FINAL SUMMARY — All Abbreviations at a Glance

Use this table to drill yourself until these are automatic:

| Abbreviation | Full Form | One-line meaning |
|---|---|---|
| **HMO** | Health Maintenance Organization | Cheap plan, needs referral |
| **PPO** | Preferred Provider Organization | Costly, flexible, no referral |
| **EPO** | Exclusive Provider Organization | Like PPO, no out-of-network at all |
| **POS** | Point of Service | Mix of HMO+PPO |
| **HDHP** | High Deductible Health Plan | Low premium, high deductible |
| **PCP** | Primary Care Physician | Your main/family doctor |
| **EOB** | Explanation of Benefits | Statement of what was billed/paid (not a bill) |
| **HEDIS** | Healthcare Effectiveness Data and Information Set | Scorecard measuring health plan quality |
| **NCQA** | National Committee for Quality Assurance | Body that maintains HEDIS |
| **ACO** | Accountable Care Organization | Providers jointly responsible for patient outcomes/cost |
| **HIPAA** | Health Insurance Portability and Accountability Act | Protects patient data privacy/security |
| **PHI** | Protected Health Information | Patient's personal medical data |
| **HITECH** | Health Information Technology for Economic and Clinical Health (Act) | Pushed EHR adoption (incentives) |
| **EHR** | Electronic Health Record | Digital record, shareable across providers |
| **EMR** | Electronic Medical Record | Digital record, single clinic only |
| **HIE** | Health Information Exchange | Network/system for sharing patient records |
| **HL7** | Health Level 7 | Data format standard for healthcare (Application/Layer 7) |
| **FHIR** | Fast Healthcare Interoperability Resources | Modern/API version of HL7 |
| **CPT** | Current Procedural Terminology | Codes for procedures done (by AMA) |
| **ICD** | International Classification of Diseases | Codes for diagnoses (by WHO) |
| **EDI** | Electronic Data Interchange | Standard electronic format for payer-provider data exchange |
| **837** | (EDI transaction) | Claim submission (provider → payer) |
| **835** | (EDI transaction) | Payment/remittance advice (payer → provider) |
| **834** | (EDI transaction) | Enrollment (add/remove members) |
| **270/271** | (EDI transaction) | Eligibility inquiry / response |
| **276/277** | (EDI transaction) | Claim status inquiry / response |
| **COB** | Coordination of Benefits | Decides primary vs secondary insurer |
| **NPI** | National Provider Identifier | Unique ID for a healthcare provider |
| **ACA** | Affordable Care Act | "Obamacare" — no denial for pre-existing conditions |
| **Medicare Part A** | — | Hospital (inpatient) |
| **Medicare Part B** | — | Doctor visits (outpatient) |
| **Medicare Part C** | — | Medicare Advantage (private plans) |
| **Medicare Part D** | — | Drugs (prescription coverage) |

**Quick memory hooks:**
- HMO/PPO → "H = Held back (needs referral), P = free to Pick any doctor"
- HIPAA vs HITECH → "HIPAA = the lock (privacy), HITECH = the push (EHR adoption)"
- CPT vs ICD → "CPT = what was done, ICD = what's wrong"
- 837 vs 835 → "837 = claim going OUT, 835 = payment coming BACK"
- Medicare Parts → "A = Admitted (hospital), B = Basic doctor visits, C = Choice (private plan), D = Drugs"
