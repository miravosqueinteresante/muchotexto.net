# Structural Readiness for Agricultural Tokenization in Paraguay

## Research Findings & Concrete Solution Proposals

---

## 1. Financial Literacy in Paraguay and Latin America

### Current State

Paraguay does not participate directly in the OECD/INFE international financial literacy surveys, but regional CAF (Development Bank of Latin America) studies using OECD/INFE methodology provide comparable data. The OECD/INFE 2023 International Survey of Adult Financial Literacy covered 39 countries (20 OECD members) measuring knowledge, behavior, and attitudes on a 0-100 scale. Average financial literacy across participating countries was approximately 60/100.

For Latin America specifically:
- CAF has conducted financial capabilities surveys across the region using OECD/INFE methodology, building indexes on financial inclusion, capabilities, digital financial literacy, and financial well-being
- Brazil (regional benchmark) scores ~60/100 on financial literacy (Central Bank of Brazil data)
- The Mastercard/PCMI 2024 LatAm survey found 81% of online respondents owned a financial account, but this skews urban and digitally connected
- The IMF's 2025 Financial Access Survey shows a "dual gap in digital and financial literacy" hindering financial access, with low financial literacy correlating strongly with lower usage of digital financial services

**Key finding: Paraguay's financial literacy level is likely below the OECD average, probably in the 50-60/100 range, consistent with regional peers. Rural financial literacy—where tokenization would first need adoption—is certainly lower.**

### Sources
- https://www.oecd.org/en/publications/oecd-infe-2023-international-survey-of-adult-financial-literacy_56003a32-en.html
- https://initiatives.weforum.org/global-future-council-on-financial-education/case-study-details/caf---financial-capabilities-surveys/aJYTG0000000wAT4AY
- https://www.mastercard.com/news/media/g5qcvpam/mastercard_financial_inclusion_2024_en_1-21-25-fv.pdf
- https://data.imf.org/-/media/iData/External-Storage/Documents/7FC05452C6C743D2BFB6188D2E248A38/en/2025-FAS-Annual-Report.pdf
- https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/12/oecd-infe-2023-international-survey-of-adult-financial-literacy_8ce94e2c/56003a32-en.pdf

### Concrete Solutions

**A) National Financial Literacy Strategy for Digital Assets**
Design a multi-channel financial education program specifically targeting agricultural producers, delivered through:
- Cooperative networks (existing trust structures)
- Radio-based education (reaching rural areas with low internet penetration)
- Mobile-first micro-learning modules via SMS/WhatsApp (ubiquitous in Paraguay)
- Partnership with CAF and OECD/INFE to adapt their digital financial literacy measurement toolkit to the Paraguayan context

**B) "Learn-to-Earn" Pilot for Tokenization**
Mandate that any regulated tokenization platform operating in Paraguay must include an educational onboarding module that teaches basic concepts (wallet, token, smart contract, risk) before allowing transactions. Draw from global "learn and earn" models used by Coinbase, Binance, and Bitget.

**C) Curriculum Integration in Agricultural Education**
Partner with the Ministry of Agriculture (MAG) and the SNPP (National Professional Promotion Service) to incorporate digital financial literacy modules into existing extension programs for smallholder farmers.

---

## 2. Digital Literacy and Rural Internet Access in Paraguay

### Current State

**Paraguay's digital landscape (2025-2026 data):**
- Internet penetration: 82-83% of population (5.84 million users) — DataReportal Digital 2026
- Rural internet penetration: 74% (vs 86% urban) — Internet Society Pulse 2024
- Mobile connections: 9.46 million (134% of population)
- 4G coverage: 98% of population
- 5G coverage: 16% of population
- Median internet speed: 28.46 Mbps mobile, 118.28 Mbps broadband
- Internet cost: 1.73% of GNI per capita for low-consumption basket
- 40% IPv6 adoption
- 9 active data centers, 3 Internet Exchange Points

**Key structural issues:**
- **Rural-urban gap persists**: 12 percentage point difference in internet access
- **Digital literacy gap**: only ~61% of Paraguay's top 1000 websites are locally cached, indicating limited local digital ecosystem
- The U.S. Mission to Paraguay has a $6M grant program specifically for "Advancing Secure Digital Connectivity in Paraguay" targeting rural connectivity and digital literacy
- Paraguay received a cybersecurity score of 74.93 on the 2024 Global Cybersecurity Index and e-government readiness of 72.51
- Internet Society rates ISP choice as "poor"

### Sources
- https://datareportal.com/reports/digital-2026-paraguay
- https://pulse.internetsociety.org/en/reports/PY
- https://simpler.grants.gov/opportunity/9e27f4f3-702c-4be1-8cbf-d6ba549152bb
- https://www.conatel.gov.py/resoluciones-2025/
- https://publications.iadb.org/publications/spanish/document/Desconectados-Servicios-publicos-digitales-y-el-reto-de-la-equidad-Hallazgos-para-Paraguay.pdf

### Concrete Solutions

**A) Offline-First Digital Architecture for Tokenization**
Design tokenization platforms with offline-capable components:
- SMS-based transaction confirmation for rural producers without smartphones
- USSD codes for balance checks and basic operations
- Biometric-embedded SIM cards linking digital identity to mobile subscriptions
- Batch-sync architecture: transactions recorded offline, synchronized when connectivity available

**B) Community Digital Access Points (Telecentros Rurales)**
Scale CONATEL's existing framework to establish "Agro-Digital Hubs" in rural cooperative centers with:
- Solar-powered satellite internet terminals
- Trained community digital facilitators (young agronomy graduates)
- Shared smart devices for producers to interact with tokenization platforms
- Integration with the US-funded "Advancing Secure Digital Connectivity in Paraguay" program

**C) Public-Private Rural Connectivity Fund**
Create a fund (modeled on the UK's Shared Rural Network) where tokenization platforms contribute a percentage of transaction fees to finance rural internet infrastructure expansion, coordinated with CONATEL's spectrum licensing.

---

## 3. Paraguay's Public Registry System (Registro Público)

### Current State

**Significant progress in 2025-2026:**
- The **Unified National Registry (RUN)** launched in early 2026, replacing 150 years of paper-based records with a digital system (Asunción Times, Jan 2026)
- RUN consolidates multiple dispersed registries into a single digital platform
- Notaries can now file documents for verification while simultaneously entering them into RUN for "blocking status" to prevent competing claims
- The Supreme Court of Justice has established direct communication channels with the Notary Guild to resolve implementation issues

**IDB-Backed Modernization:**
- IDB approved a $25 million loan for the **Cadastre and Property Registry Program II** (PR-L1061)
- Objectives: increase agricultural productivity by 9%, improve property values by 9%, consolidate information on 543,000 farms in the **SICAR system** (Cadastre and Registry Information System)
- Increase from 0% to 60% the percentage of national land with rural cadastral mapping
- Formalize titling and registration in 79 colonies of INDERT (National Rural and Land Development Institute)
- Phase I results: 3 regional cadastre/registry offices opened, 100% digital scanning of urban and rural cadastral data, 1M+ registry entries scanned, SICAR designed and implemented

**Remaining challenges:**
- Full interoperability between cadastre and registry not yet achieved
- 150+ years of paper records present digitization quality challenges
- Rural cadastral mapping coverage still incomplete (Program II aims for 60%)
- Conflict resolution mechanisms still in development

### Sources
- https://asunciontimes.com/paraguay-news/national-news/unified-national-registry-of-paraguay-replaces-150-years-of-paper-records/
- https://www.iadb.org/en/news/paraguay-will-improve-security-land-ownership-idb-support
- https://www.iadb.org/en/projects/project,1303.html?id=PR-L1061
- https://www.oas.org/ext/en/democracy/cadastre
- https://www.vouga.com.py/en/res-cg-cnv-35-2023-cambios-importantes-en-la-regulacion-de-mercado-de-valores-en-paraguay

### Concrete Solutions

**A) Blockchain-Based Registry Layer on Top of RUN**
Rather than replacing RUN, build a **blockchain-based proof-of-existence layer** that hashes registry entries to create immutable timestamped records. This provides cryptographic evidence of registration order without requiring the entire registry to migrate to blockchain. The hashed references can feed directly into tokenized asset issuance.

**B) Tokenization-Ready Metadata Standard**
Work with the CNV (Comisión Nacional de Valores) and the Directorate of Registries to define a **tokenization metadata standard** that every digitally registered property must include: GPS coordinates, area, land use type, existing encumbrances, ownership chain hash, and environmental compliance status. This standard becomes the data layer for any future tokenization.

**C) Smart Contract Templates for Land Parcels**
Develop Paraguay-specific smart contract templates that integrate with SICAR data for:
- Fractional ownership registration
- Usufruct rights tokenization
- Crop lien registration
- Carbon credit rights attached to land tokens

---

## 4. Property Rights and Land Titling in Paraguay

### Current State

**Structural challenges:**
- Significant inequality in land tenancy and extensive titling irregularities (World Bank, 2021)
- Smallholder farmers constrained by limited access to land, technology, and human/social capital
- Nearly one-third of rural population (33.86%) lives in poverty (2020 data)
- 36% of the population lives in rural areas (DataReportal 2026)
- The **PRODERS project** (World Bank, 2009-2020) supported 105 communities in regularizing land titles, with 249,662 direct beneficiaries (53% women)
- PRODERS improved cassava and maize productivity by at least 25%

**Land insecurity impacts:**
- Slash-and-burn agriculture and monoculture due to lack of tenure security
- Environmental degradation from unsustainable practices
- Limited access to formal credit (land cannot serve as collateral without clear title)
- World Bank's Land 2030 Global Partnership estimates 1.1 billion people globally feel uncertain about their land rights

**Important caveat from research:**
Studies in Peru (a comparable Andean context) show land titling programs are "necessary but not sufficient" to promote rural development. Titling effects on investment are positive but small, particularly where customary institutions function well. This means tokenization cannot simply assume that digital titles will solve investment constraints.

### Sources
- https://www.worldbank.org/en/results/2021/11/10/transforming-rural-areas-of-paraguay
- https://www.iadb.org/en/news/paraguay-will-improve-security-land-ownership-idb-support
- https://research.wur.nl/en/publications/property-rights-after-market-liberalization-reforms-land-titling-
- https://www.sciencedirect.com/science/article/pii/S0264837721003744
- https://www.worldbank.org/en/programs/land-2030/overview

### Concrete Solutions

**A) Prior Titling Regularization as a Prerequisite**
No tokenization program should proceed in a jurisdiction where >90% of land lacks clear title. The first phase must be: (1) complete the IDB's Cadastre Program II mapping, (2) digitize all titles in INDERT colonies, (3) then tokenize. **Tokenization without clear title is securitization of dispute.**

**B) GRN (Gradual Rights Notation) System for Untitled Land**
For the estimated 40%+ of rural land without formal title, create a **progressive rights notation system** on blockchain:
1. Level 1: Possession claim (timestamped on blockchain via mobile phone)
2. Level 2: Community-validated possession (smart contract with neighbor validators)
3. Level 3: Municipal-recognized usufruct
4. Level 4: Full registered title (integrated with RUN)

This allows producers to begin participating in tokenized value chains while their formal title is being processed.

**C) Tokenized Land Bond for Regularization**
Issue a government-guaranteed "Tierra Titulada" bond on BVPASA whose proceeds fund mass titling campaigns. The bond is tokenized and sold to international ESG investors. Each bond unit corresponds to a specific number of hectares to be titled, with published KPIs on regularization progress.

---

## 5. Investor Protection Frameworks in Paraguay

### Current State

**Doing Business (archived, last data 2019):**
Paraguay's "Protecting Minority Investors" score placed it in the middle range globally. Key indicators:
- **Extent of disclosure index**: Measures transparency of related-party transactions
- **Extent of director liability index**: Measures shareholders' ability to sue directors for self-dealing
- **Ease of shareholder suits index**: Measures access to evidence and legal cost allocation
- **Extent of shareholder governance index**: Measures shareholder rights, ownership/control, corporate transparency

**Securities Market Regulation (2023 Update):**
The CNV introduced a **new General Securities Market Regulation** in February 2023 (Resolución CG CNV 35/2023) with important modernizations:
- **Market makers** authorized to maintain liquidity
- **Direct Market Access (DMA)** for investors to send orders directly to trading systems
- Modernized framework for brokerage houses
- New rules for public offerings

**Crypto/Asset Regulation:**
- Paraguay does NOT currently have specific legislation for asset tokenization
- Tokenization projects can be structured under general private law
- If tokens represent transferable securities, they could fall under CNV supervision
- No legal provisions recognize blockchain/DLT as an official registration system
- No regulatory sandbox or pilot regime for tokenization exists
- DNIT (tax authority) issued Resolution 47/26 requiring crypto platforms to report all digital asset transactions over $5,000 (January 2025) — this is AML/KYC, not innovation framework

### Sources
- https://archive.doingbusiness.org/en/data/exploreeconomies/paraguay
- https://archive.doingbusiness.org/en/methodology/protecting-minority-investors
- https://www.vouga.com.py/en/res-cg-cnv-35-2023-cambios-importantes-en-la-regulacion-de-mercado-de-valores-en-paraguay
- https://metlabs.io/en/blockchain-regulation-paraguay
- https://bitcoinmagazine.com/news/paraguay-adopts-stricter-crypto-oversight

### Concrete Solutions

**A) Multi-Layered Investor Protection for Tokenized Assets**
Design a protection framework with graduated requirements:

| Investor Type | Max Investment per Token | Disclosure Required | Cooling-Off Period |
|---|---|---|---|
| Non-accredited (retail) | $1,000 equivalent | Simplified prospectus + risk quiz | 7 days |
| Semi-accredited (>$50k income) | $10,000 equivalent | Full prospectus | 3 days |
| Accredited (>$200k income) | No limit | Full prospectus | None |
| Institutional | No limit | Issuer briefing | None |

**B) Mandatory Token Insurance Pool**
Require all tokenization platforms operating in Paraguay to contribute to a **Fondo de Garantía de Tokens Agrícolas** (Agri-Token Guarantee Fund), similar to the Fondo de Garantía de Depósitos in banking. Covers smart contract failures, not market risk.

**C) Smart Contract Audit Mandate and Registry**
Create a CNV-supervised registry of approved smart contract auditors (local and international firms). All tokenization smart contracts must be audited by a CNV-registered auditor and the audit hash stored on-chain before any public offering.

**D) Transparent Oracle System for Agricultural Data**
For tokenized agricultural assets (crop yields, land values, commodity prices), mandate the use of a **redundant oracle system** with at least three independent data sources, reducing manipulation risk. Publish oracle failure rates transparently.

---

## 6. Regulatory Sandboxes: Global Lessons for Paraguay

### Current State

**Global benchmarks:**

| Country | Sandbox Launch | Regulator | Key Results |
|---|---|---|---|
| **UK** (FCA) | 2016 | Financial Conduct Authority | 75% of first-cohort firms completed testing successfully; ~90% of firms that completed testing went on to full authorization. Pioneered the model globally. |
| **Brazil** (BCB) | 2020 | Banco Central do Brasil | Focused on payments, credit, and digital currencies. Integrated with Pix instant payment system. Created regulatory pathways for fintech innovation. |
| **Mexico** | 2018 (Fintech Law) | CNBV | First comprehensive fintech law in LatAm. Regulated crowdfunding, digital payments, and API standards. Created "Modelos Novedosos" sandbox for unregulated innovations. |
| **UAE** | 2017 | CBUAE + ADGM/DIFC | Co-sandbox program between central bank and financial free zones. Focused on digital banking, blockchain trade finance, and Islamic fintech. |

**Paraguay's current status:**
- Paraguay has implemented EMPE (e-wallet) regulation since 2014 (BCP Resolutions 6/14 and 6/20)
- ~2.7 million active e-wallet accounts, $160M monthly transactions
- Limited crowdfunding regulation exists
- **No regulatory sandbox exists** for fintech, crypto, or tokenization
- No specific VASP registration regime (unlike Argentina's CNV Resolution 1058/2025)

**IDB Regional Perspective:**
The IDB published "Regulatory Sandboxes, Innovation Hubs, and Other Regulatory Innovation Tools in Latin America and the Caribbean" studying progress in Brazil, Colombia, Mexico, and others, with specific lessons for the region.

### Sources
- https://publications.iadb.org/publications/english/document/Regulatory-Sandboxes-Innovation-Hubs-and-Other-Regulatory-Innovation-Tools-in-Latin-America-and-the-Caribbean.pdf
- http://fca.org.uk/publication/research-and-data/regulatory-sandbox-lessons-learned-report.pdf
- https://www.bcb.gov.br/en/financialstability/regulatorysandbox
- https://openknowledge.worldbank.org/entities/publication/b688bc5a-af76-5a96-ab04-37c9ad657baf
- https://www.vouga.com.py/wp-content/uploads/2023/12/VOUGA_Fintech__4_Ingles-minimo.pdf

### Concrete Solutions

**A) "Paraguay-First" Agri-Tokenization Sandbox Design**

A sandbox with the following specific parameters:

| Parameter | Proposed Design |
|---|---|
| **Scope** | Agricultural asset tokenization only (Phase 1) |
| **Regulator** | Joint BCP-CNV working group |
| **Duration** | 24 months, renewable once |
| **Max participants** | 10 projects per cohort |
| **Max total issuance** | $5M per project during sandbox |
| **Max per investor** | $10,000 per project (retail) |
| **Reporting** | Monthly operational data, quarterly investor reports |
| **Consumer protection** | Mandatory risk disclosure, 7-day withdrawal right |
| **KYC/AML** | Full SEPRELAD compliance required |
| **Exit criteria** | Successful testing → full authorization; failure → orderly wind-down |

**B) "Test-and-Learn" Approach**
Adopt the FCA's model of **graduated authorization**: sandbox participants start with restricted licenses that automatically widen as they demonstrate compliance capacity. Key metrics for graduation: transaction volume thresholds, months without security incidents, investor complaint rates.

**C) Cross-Border Sandbox Recognition**
Establish MOUs with Brazil's BCB sandbox and Argentina's CNV for cross-recognition of sandbox-tested tokenization products, creating a regional market for Paraguayan agricultural tokens.

**D) Mandatory Data-Sharing Requirement**
Sandbox participants must publish anonymized operational data (default rates, secondary market liquidity, investor demographics) to build a public evidence base for future regulation. This is essential because the IDB study notes that "data from sandboxes remains limited and fragmented."

---

## 7. Blockchain/Crypto Education at Paraguayan Universities

### Current State

**Limited formal blockchain education in Paraguay:**
- No evidence of dedicated blockchain or crypto degree programs at UNA (Universidad Nacional de Asunción), UC (Universidad Católica), or other major Paraguayan universities
- No Paraguayan university appears in the **Blockchain Education Network** (BEN) global map of 200+ universities
- Ripple's UBRI (University Blockchain Research Initiative) has funded programs in 30+ countries but Paraguay is not included
- The fintech ecosystem is growing (25 brokerages, active Fintech Day Paraguay events) but educational infrastructure lags

**Regional context:**
- Argentina and Brazil have more developed blockchain education ecosystems
- Global platforms (101 Blockchains, Blockchain Education Network) provide remote certification
- Most blockchain skills in Paraguay are likely self-taught or acquired through international online courses

**Bright spots:**
- **BVPASA** offers investor education through CEBVPASA (Centro de Estudios Bursátiles)
- Index Casa de Bolsa (2025) specifically emphasizes "education and artificial intelligence" as differentiators
- Fintech Day Paraguay 2025 (organized by Ceibo Digital) indicates growing industry interest

### Sources
- https://www.blockchainedu.org/
- https://infonegocios.com.py/y-ademas/paraguay-ya-tiene-25-casas-de-bolsa-index-se-suma-al-mercado-de-valores-con-enfoque-tecnologico
- https://www.bitget.com/academy/crypto-learn-earn-6
- https://www.ceibo.digital/en/newsroom/fintech-day-py-2025
- https://metlabs.io/en/blockchain-regulation-paraguay

### Concrete Solutions

**A) Curriculum Development Program**
Partner with one international blockchain education platform (e.g., 101 Blockchains, Alchemy University, or the Blockchain Education Network) to co-develop a **"Tokenización Agroindustrial" specialization** at UNA's Faculty of Agricultural Sciences and UC's School of Business Administration. Modules:
- Blockchain fundamentals for agricultural supply chains
- Smart contract development (Solidity/Rust)
- Agricultural tokenomics and incentive design
- Regulatory compliance for digital assets in Paraguay

**B) BVPASA-CNV Blockchain Certification**
Create a **"Certified Tokenization Professional"** credential jointly offered by BVPASA and CNV, covering:
- Legal framework for tokenized assets in Paraguay
- Investor protection obligations
- Smart contract audit basics
- SEPRELAD compliance for VASPs

**C) University Sandbox Program**
Establish a **university-linked sandbox** where computer science and agronomy students can deploy experimental tokenization projects on test networks, mentored by BCP/CNV professionals. Successful projects can fast-track into the main regulatory sandbox.

**D) Scholarship Fund via Tokenization Royalties**
Mandate that 0.1% of every tokenized agricultural issuance on BVPASA funds a scholarship for Paraguayan students to study blockchain/Fintech at international programs (MIT, Oxford, or UBRI-partner universities).

---

## 8. Capital Market Development in Paraguay

### Current State

**Market size and growth:**
- BVPASA recorded a record trading volume of G. 51.58 trillion (>$6.6 billion) in 2024
- 25 brokerage houses (casas de bolsa) operating as of January 2025
- Index Casa de Bolsa (Jan 2025) focuses on democratizing investment access via technology
- Paraguay achieved **investment grade** credit rating (a significant milestone)
- February 2025: Paraguay issued first-ever **guarani-denominated global bonds** ($ equivalent, 10-year, 8.50%) and USD bonds (30-year, 6.65%)
- Sixth Latin American sovereign to access international markets in favorable conditions in early 2025

**Regulatory modernization (World Bank, 2025):**
- Key inter-agency coordination between BCP and Ministry of Economy and Finance
- Trading systems of central public debt depository and stock exchange linked
- Implementation of **CDA-e** (Electronic Deposit Savings Certificates) for digital transactions
- Modernization of financial and foreign exchange regulations
- World Bank notes: "Paraguay's capital markets open up to the world with key reforms"

**Foreign Direct Investment context (IDB, 2018):**
- FDI flows average 1.3% of GDP, below regional values
- Institutional variables have a strong effect on FDI decisions
- Despite sound macroeconomic fundamentals, institutional weaknesses deter investment

**Securities market participants (BVPASA):**
- Emisores (issuers) include AFD (Agencia Financiera de Desarrollo), agricultural companies (Agro Nathura, AgroAlianza, Alamo), and various corporate issuers
- Risk rating agencies, fund administrators, and brokerage houses are active participants
- The market remains bond-heavy with limited equity listings

### Sources
- https://blogs.worldbank.org/en/latinamerica/paraguay-capital-markets-reform
- https://infonegocios.com.py/y-ademas/paraguay-ya-tiene-25-casas-de-bolsa-index-se-suma-al-mercado-de-valores-con-enfoque-tecnologico
- https://www.bcp.gov.py/bolsas-de-valores-y-productos
- https://www.bolsadevalores.com.py/listado-de-emisores
- https://publications.iadb.org/en/fdi-flows-paraguay-what-do-investors-prioritize
- https://data.worldbank.org/country/paraguay

### Concrete Solutions

**A) Agricultural Tokenization as a New Asset Class on BVPASA**
Create a **dedicated "Agri-Token" segment** within BVPASA's listing structure with:
- Simplified listing requirements for tokenized agricultural assets
- Lower listing fees to encourage first-time issuers (subsidized in first 2 years)
- Transparent secondary market pricing via the SEN (Electronic Trading System)
- Integration with BCP's real-time gross settlement system for instant settlement

**B) Tokenized Agricultural Bonds (Fintech-Friendly Structure)**
Structure tokenized agricultural investments as **negotiable obligations (ON)** under existing securities law, but:
- Issued in fractional units (as low as G. 100,000 / ~$13)
- Smart-contract based automatic coupon payments
- Collateralized by specific agricultural assets or receivables (with SICAR registration)
- Listed and traded on BVPASA

**C) Institutional Investor Participation Framework**
Design tokenized agricultural products specifically for:
- AFD (Agencia Financiera de Desarrollo) — as anchor investor in early issuances
- Pension funds (AFP) — once tokenized products achieve investment-grade rating
- International ESG investors — Paraguayan agricultural tokens as "impact investments"
- IDB Invest — as partial guarantor for first-loss tranche

**D) Capital Market Infrastructure Upgrades Needed Before Tokenization**
1. **BVPASA-BCP direct settlement integration** (already underway)
2. **Digital custody framework** for tokenized assets (currently absent)
3. **CSD (Central Securities Depository) functional upgrade** to support DLT-based securities
4. **Real-time price discovery** for tokenized agricultural products
5. **Market maker obligations** for token liquidity (framework exists since 2023 CNV regulation)

---

## Cross-Cutting Readiness Assessment

| Readiness Dimension | Score (1-10) | Key Constraint |
|---|---|---|
| Financial literacy (rural) | 3 | No national strategy for digital asset education |
| Digital infrastructure (rural) | 5 | 74% penetration; offline architecture needed |
| Public registry digitalization | 7 | RUN launched Jan 2026; cadastre gap remains |
| Land titling completeness | 4 | <60% rural land with clear title |
| Investor protection framework | 5 | Good base law; no token-specific regulation |
| Regulatory sandbox | 1 | Does not exist |
| Blockchain education | 2 | No university programs |
| Capital market depth | 6 | Growing rapidly; investment grade achieved |

**Overall Readiness: ~4/10**

### Most Critical Preconditions

1. **First: Complete the IDB Cadastre Program II** (reach 60% rural cadastral mapping) before any large-scale land tokenization
2. **Second: Establish a regulatory sandbox** (learn from UK, Brazil, Mexico) with specific agri-token focus
3. **Third: Build digital identity infrastructure** for rural producers (leveraging RUN digital registry and MOSIP open-source platform)
4. **Fourth: Launch financial literacy programs** through cooperative networks (can run in parallel)
5. **Fifth: Pilot selective tokenization** on BVPASA with 1-2 well-titled, large-scale agricultural cooperatives before expanding to smallholders

---

## Summary of Key Source URLs

### Financial Literacy
- https://www.oecd.org/en/publications/oecd-infe-2023-international-survey-of-adult-financial-literacy_56003a32-en.html
- https://initiatives.weforum.org/global-future-council-on-financial-education/case-study-details/caf---financial-capabilities-surveys/aJYTG0000000wAT4AY
- https://www.mastercard.com/news/media/g5qcvpam/mastercard_financial_inclusion_2024_en_1-21-25-fv.pdf

### Digital & Internet (Paraguay)
- https://datareportal.com/reports/digital-2026-paraguay
- https://pulse.internetsociety.org/en/reports/PY
- https://simpler.grants.gov/opportunity/9e27f4f3-702c-4be1-8cbf-d6ba549152bb
- https://www.conatel.gov.py/

### Public Registry & Land Titling
- https://asunciontimes.com/paraguay-news/national-news/unified-national-registry-of-paraguay-replaces-150-years-of-paper-records/
- https://www.iadb.org/en/news/paraguay-will-improve-security-land-ownership-idb-support
- https://www.worldbank.org/en/results/2021/11/10/transforming-rural-areas-of-paraguay

### Investor Protection
- https://archive.doingbusiness.org/en/data/exploreeconomies/paraguay
- https://www.vouga.com.py/en/res-cg-cnv-35-2023-cambios-importantes-en-la-regulacion-de-mercado-de-valores-en-paraguay

### Regulatory Sandboxes
- https://publications.iadb.org/publications/english/document/Regulatory-Sandboxes-Innovation-Hubs-and-Other-Regulatory-Innovation-Tools-in-Latin-America-and-the-Caribbean.pdf
- http://fca.org.uk/publication/research-and-data/regulatory-sandbox-lessons-learned-report.pdf
- https://www.bcb.gov.br/en/financialstability/regulatorysandbox

### Blockchain Regulation & Education
- https://metlabs.io/en/blockchain-regulation-paraguay
- https://www.blockchainedu.org/

### Capital Markets
- https://blogs.worldbank.org/en/latinamerica/paraguay-capital-markets-reform
- https://infonegocios.com.py/y-ademas/paraguay-ya-tiene-25-casas-de-bolsa-index-se-suma-al-mercado-de-valores-con-enfoque-tecnologico
- https://www.bolsadevalores.com.py/listado-de-emisores
- https://www.bcp.gov.py/bolsas-de-valores-y-productos
