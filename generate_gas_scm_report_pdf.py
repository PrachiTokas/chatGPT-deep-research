from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)


OUTPUT_FILE = "gas_supply_chain_management_industry_report.pdf"


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        textColor=colors.HexColor("#12355B"),
        spaceAfter=18,
    )
)
styles.add(
    ParagraphStyle(
        name="PageTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#12355B"),
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#1F4E79"),
        spaceBefore=6,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySmall",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.6,
        leading=11.2,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        name="BulletSmall",
        parent=styles["BodySmall"],
        leftIndent=12,
        firstLineIndent=-7,
        bulletIndent=0,
    )
)
styles.add(
    ParagraphStyle(
        name="TableText",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.2,
        leading=8.7,
    )
)
styles.add(
    ParagraphStyle(
        name="TableHead",
        parent=styles["TableText"],
        fontName="Helvetica-Bold",
        textColor=colors.white,
    )
)


def p(text, style="BodySmall"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(f"- {text}", styles["BulletSmall"])


def table(data, col_widths, repeat_rows=1, font_size=7.2):
    formatted = []
    for r, row in enumerate(data):
        formatted.append([p(str(cell), "TableHead" if r == 0 else "TableText") for cell in row])
    t = Table(formatted, colWidths=col_widths, repeatRows=repeat_rows, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E79")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#B7C9D6")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), font_size),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F8FA")]),
            ]
        )
    )
    return t


def page(title, elements):
    return [p(title, "PageTitle"), *elements, PageBreak()]


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#5B6770"))
    canvas.drawString(0.55 * inch, 0.35 * inch, "Gas Supply Chain Management Industry Report")
    canvas.drawRightString(7.95 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.setStrokeColor(colors.HexColor("#D9E2EA"))
    canvas.line(0.55 * inch, 0.5 * inch, 7.95 * inch, 0.5 * inch)
    canvas.restoreState()


doc = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=letter,
    rightMargin=0.45 * inch,
    leftMargin=0.45 * inch,
    topMargin=0.45 * inch,
    bottomMargin=0.6 * inch,
)

story = []

story.extend(
    [
        p("Gas Supply Chain Management Industry Report", "CoverTitle"),
        p(
            "Deep research report prepared from an industry perspective. Company-specific sections are intentionally reframed into market structure, participant archetypes, and competitive positioning across the gas supply chain management space.",
            "BodySmall",
        ),
        Spacer(1, 8),
        p("Executive Summary", "PageTitle"),
        table(
            [
                ["Section", "What We Like", "What We Want to Investigate Further"],
                [
                    "Industry / Company Overview Proxy",
                    "Gas SCM manages mission-critical flows from upstream supply through pipelines, storage, LNG, distribution, trading, and compliance workflows.<br/><br/>The space benefits from operational complexity, volatility, and regulation, creating demand for specialized infrastructure, optimization, and workflow platforms.",
                    "Assess which profit pools accrue to infrastructure owners versus software-led orchestration platforms as gas flows become more LNG-linked.<br/><br/>Determine whether customers prefer integrated enterprise suites or best-of-breed modules for scheduling, nominations, risk, and emissions reporting.",
                ],
                [
                    "Market Overview and Trends",
                    "Global gas demand reached a new high in 2024, while LNG supply remained tight, increasing the value of flexibility and storage.<br/><br/>A large LNG capacity wave by 2030 should deepen liquidity and increase portfolio-optimization complexity.",
                    "Test how quickly Asia and emerging import markets can build regasification, pipeline, and downstream infrastructure to absorb cheaper LNG.<br/><br/>Analyze whether lower LNG prices after 2026 expand demand enough to offset European decline and decarbonization.",
                ],
                [
                    "Competitive Landscape",
                    "Competitive advantage is shifting toward portfolio flexibility, storage access, LNG shipping optionality, digital visibility, and risk management.<br/><br/>Vendors with integrated physical/financial workflows address pain points in nominations, scheduling, imbalance management, settlements, and compliance.",
                    "Map vendor win rates by customer segment: producers, pipelines, LNG traders, utilities, power generators, and local distribution companies.<br/><br/>Quantify fragmentation between global CTRM suites, North American gas scheduling specialists, and LNG optimization platforms.",
                ],
                [
                    "Value Creation and Risks",
                    "Volatility, methane regulation, storage needs, and LNG contract flexibility create clear levers for differentiated SCM capabilities.<br/><br/>Operators that convert emissions, logistics, and trading data into decisions can improve margins while reducing compliance risk.",
                    "Evaluate whether methane traceability, carbon-intensity certification, and AI optimization become budgeted must-haves or remain project-based enhancements.<br/><br/>Assess cyber, integration, and data-quality risks as gas SCM systems connect more deeply to physical operations.",
                ],
            ],
            [1.35 * inch, 3.05 * inch, 3.05 * inch],
        ),
        PageBreak(),
    ]
)

pages = []

pages.append(
    page(
        "1. Scope, Definitions, and Classification",
        [
            p("Industry definition", "SectionTitle"),
            p(
                "Gas supply chain management (Gas SCM) refers to the systems, assets, commercial processes, and operating capabilities that coordinate natural gas flows from source to end-use. It covers production, gathering, processing, pipeline transmission, storage, liquefaction, LNG shipping, regasification, distribution, trading, nominations, balancing, settlements, risk management, and compliance.",
            ),
            p("Scope exclusions", "SectionTitle"),
            bullet("All company-specific diligence sections are ignored; the report uses an industry-only lens."),
            bullet("Company overview requirements are translated into market participant archetypes and core industry offerings."),
            bullet("Market sizing avoids paid market-research estimates and relies primarily on Tier 1 public sources."),
            p("Classification", "SectionTitle"),
            table(
                [
                    ["Classification lens", "Relevant classification"],
                    ["GICS", "Energy - Oil, Gas & Consumable Fuels; Utilities - Gas Utilities; Information Technology - Application Software for digital SCM platforms."],
                    ["PICS-style mapping", "Energy - Midstream / LNG / Gas Utilities; Software - Vertical SaaS / ETRM / CTRM / Asset Optimization."],
                    ["Sub-sector", "Natural gas logistics, LNG portfolio management, pipeline scheduling, storage optimization, commodity trading and risk management."],
                ],
                [2.0 * inch, 5.45 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "2. Industry Overview and Core Offerings",
        [
            p(
                "Gas SCM sits at the intersection of energy security, commodity logistics, and industrial software. Unlike many supply chains, gas requires continuous balancing because networks must match supply and demand in near real time. Pipeline pressure, storage inventory, LNG cargo timing, weather-driven demand, and power-market dispatch all affect operational decisions.",
            ),
            p(
                "The industry became more strategically important after the 2022-23 gas shock. IEA notes that markets remain fragile, with tight LNG supply and geopolitical risks keeping markets sensitive to supply or demand shocks. Global gas demand rose 2.8%, or 115 bcm, in 2024, reaching a new high.",
            ),
            table(
                [
                    ["Offering area", "Description", "Buyer / user"],
                    ["Supply procurement", "Securing pipeline gas, LNG cargoes, storage capacity, and flexible supply.", "Utilities, marketers, industrials."],
                    ["Nominations and scheduling", "Submitting and coordinating daily and intraday pipeline flows.", "Shippers, pipelines, schedulers."],
                    ["Storage management", "Managing injections, withdrawals, inventory, and imbalances.", "Utilities, traders, storage operators."],
                    ["LNG cargo optimization", "Coordinating lifting schedules, shipping, routes, and regas slots.", "LNG portfolio players."],
                    ["Trading and risk", "Capturing physical and financial trades, hedging, credit, VaR, and P&L.", "Traders, risk teams, treasury."],
                    ["Settlements and accounting", "Reconciling volumes, tariffs, invoices, and imbalance cashouts.", "Back office, accounting."],
                    ["Compliance and reporting", "FERC / NAESB, methane MRV, emissions tracking, and audit trails.", "Compliance, ESG, regulators."],
                ],
                [1.65 * inch, 3.2 * inch, 2.6 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "3. Key Geographies",
        [
            table(
                [
                    ["Geography", "Industry relevance", "Gas SCM implications"],
                    ["North America", "Deep shale, pipeline, storage, power-gas integration, and LNG export base.", "Scheduling, nominations, gas-electric coordination, and export feedgas optimization."],
                    ["Europe", "High import dependency, storage mandates, LNG substitution for Russian pipeline gas.", "Storage planning, LNG procurement, cross-border balancing, and emissions compliance."],
                    ["Asia Pacific", "Largest incremental demand region and largest LNG-importing region.", "Demand forecasting, LNG portfolio optimization, regas scheduling, and price-sensitive procurement."],
                    ["Middle East", "Major low-cost gas and LNG supply growth, especially Qatar.", "Long-term LNG contracting, liquefaction expansion, and emissions-intensity management."],
                    ["South / Southeast Asia", "Emerging LNG demand with infrastructure and affordability constraints.", "Regas, downstream pipeline, credit, FX, and contract-flexibility management."],
                    ["Latin America", "Hydro variability drives seasonal LNG and gas demand.", "Short-term procurement, floating regas, and weather-linked optimization."],
                    ["Africa", "Gas production, LNG export growth, and domestic energy-access potential.", "Flaring reduction, gas monetization, LNG, and domestic pipeline development."],
                ],
                [1.35 * inch, 3.05 * inch, 3.05 * inch],
            ),
            p("Investor read-through", "SectionTitle"),
            bullet("Regional value creation is highly specific: North America rewards pipeline connectivity and gas-power integration; Europe rewards storage and compliance; Asia rewards LNG portfolio flexibility."),
            bullet("Emerging markets may offer demand growth, but realized value depends on regasification, pipeline, credit, and downstream infrastructure readiness."),
        ],
    )
)

pages.append(
    page(
        "4. Source Identification and Prioritization",
        [
            p(
                "The research prioritizes public-sector and intergovernmental data over commercial market research. This is important because gas market estimates vary materially by scenario, commodity-price assumptions, regional infrastructure constraints, and policy trajectories.",
            ),
            table(
                [
                    ["Tier", "Source type", "Sources used", "Role in report"],
                    ["Tier 1", "Government, intergovernmental, regulators, statistical agencies.", "IEA, EIA, Eurostat, European Commission, World Bank, PHMSA, ACER.", "Market size, demand outlook, storage, LNG exports, methane, regulation."],
                    ["Tier 2", "Consulting firms and company websites.", "Deloitte, Quorum, ION, PCI, Trellis, selected company materials.", "Technology trends, vendor positioning, product capabilities."],
                    ["Tier 3", "Industry associations and publications.", "IGU, GIIGNL.", "LNG trade, exporter/importer structure, liquefaction context."],
                    ["Tier 4", "Blogs, unverified forums, paid market-research estimates.", "Avoided.", "Not used for sizing or conclusions."],
                ],
                [0.8 * inch, 2.0 * inch, 2.5 * inch, 2.15 * inch],
            ),
            p("Research stance", "SectionTitle"),
            bullet("Tier 1 sources are used for quantitative market claims wherever available."),
            bullet("Tier 2 company sources are used for product and positioning claims, not for independent market sizing."),
            bullet("Tier 3 sources are used selectively for LNG trade and infrastructure context where industry associations publish consolidated data."),
        ],
    )
)

pages.append(
    page(
        "5. Historical Market Trends: Demand, Supply, and Trade",
        [
            p("Market size and growth", "SectionTitle"),
            p(
                "The clearest Tier 1 proxy for Gas SCM demand is the size and complexity of the physical gas system. IEA estimates global gas demand rose 2.8%, or 115 bcm, in 2024, above the 2010-20 average growth rate of roughly 2%.",
            ),
            p("United States", "SectionTitle"),
            p(
                "EIA reported 2024 U.S. natural gas consumption averaged 90.3 Bcf/d, a record, supported by power-sector demand and competitive gas prices. U.S. LNG exports averaged 11.9 Bcf/d, keeping the country the world's largest LNG exporter.",
            ),
            p("LNG globalization", "SectionTitle"),
            p(
                "IGU reported global LNG trade grew 2.4% in 2024 to 411.24 million tonnes, connecting 22 exporting markets with 48 importing markets. This makes LNG a central driver of cross-regional gas SCM complexity.",
            ),
            p("Storage and flexibility", "SectionTitle"),
            p(
                "IEA states that underground storage and reserve mechanisms played a key role in the 2024/25 winter. EU net storage withdrawals rose more than 50% year over year and represented over 30% of gas demand during November-March.",
            ),
        ],
    )
)

pages.append(
    page(
        "6. Historical Regional Trends",
        [
            table(
                [
                    ["Region", "Recent trend", "SCM implication"],
                    ["Europe", "EU natural gas import dependency reached 85.6% in 2024, while domestic production fell 12.4%.", "More dependence on storage, LNG procurement, cross-border balancing, and supplier traceability."],
                    ["United States", "Record gas consumption and world-leading LNG exports in 2024.", "Higher value for feedgas coordination, pipeline scheduling, and LNG terminal utilization."],
                    ["Asia Pacific", "Demand growth returned in 2024, but high LNG prices slowed growth during winter 2024/25.", "Price sensitivity makes contract flexibility and cargo optimization critical."],
                    ["Middle East", "Qatar and other regional players continue major LNG development.", "Low-cost supply can reset global cost curves and contracting benchmarks."],
                    ["Latin America", "Hydro variability drives episodic LNG demand in countries such as Brazil and Colombia.", "Weather-linked optionality and floating regas capacity matter."],
                ],
                [1.35 * inch, 3.2 * inch, 2.9 * inch],
            ),
            p("Key interpretation", "SectionTitle"),
            bullet("The market is not simply growing; it is becoming more operationally complex because gas flows are more global, seasonal, and policy-sensitive."),
            bullet("The strategic importance of storage, LNG import capacity, and real-time commercial systems increased after the 2022-23 supply shock."),
        ],
    )
)

pages.append(
    page(
        "7. Historical Product and Segment Trends",
        [
            table(
                [
                    ["Segment", "Historical trend", "SCM implication"],
                    ["Pipeline gas", "Still core in North America, Europe, Russia-linked Eurasia, and domestic markets.", "Scheduling, nominations, and imbalance management remain foundational."],
                    ["LNG", "Trade expanded to 411.24 MT in 2024; Europe and Asia compete for flexible cargoes.", "Cargo optimization, regas capacity, shipping routes, and contract optionality matter more."],
                    ["Storage", "Became a strategic security asset after 2022.", "Inventory analytics, withdrawal planning, and reserve mechanisms create value."],
                    ["ETRM / CTRM", "Shift from transactional systems to integrated trading ecosystems.", "Users need real-time physical and financial visibility."],
                    ["Emissions / methane", "Measurement, reporting, and verification requirements are increasing.", "Carbon-intensity and methane data become supply-chain attributes."],
                    ["Gas-to-power", "Renewables intermittency increases gas balancing role.", "Gas-electric coordination and dispatch-linked procurement become more valuable."],
                ],
                [1.45 * inch, 3.0 * inch, 3.0 * inch],
            ),
            p("Management implication", "SectionTitle"),
            p(
                "A modern Gas SCM capability must connect operational data, commercial positions, regulatory records, emissions attributes, and financial exposures. Platforms that solve only one workflow may remain useful, but platforms that connect workflows can become systems of record.",
            ),
        ],
    )
)

pages.append(
    page(
        "8. Future Market Outlook: Next Five Years",
        [
            p(
                "IEA's medium-term gas outlook is the most important forward-looking source. It expects approximately 300 bcm/year of new LNG export capacity by 2030, mainly from the United States and Qatar. This could translate into 250 bcm of net incremental LNG supply by 2030 after accounting for declines and ramp-up factors.",
            ),
            p("Demand outlook", "SectionTitle"),
            p(
                "IEA's base case expects global gas demand to increase at nearly 1.5% annually between 2024 and 2030, adding approximately 380 bcm. Asia Pacific accounts for roughly half of the growth, with the Middle East also contributing materially. European gas demand is expected to decline about 8%.",
            ),
            p("LNG supply outlook", "SectionTitle"),
            p(
                "The LNG supply wave should improve affordability and liquidity, but it may pressure margins for higher-cost assets. IEA notes that not all incremental LNG supply may be absorbed under base-case demand assumptions, creating possible surplus supply later in the decade.",
            ),
            p("Low-emissions gases", "SectionTitle"),
            p(
                "IEA expects low-emissions gases to expand rapidly but remain small, accounting for less than 1% of global gaseous fuels supply by 2030. Biomethane contributes more than half of the increase.",
            ),
        ],
    )
)

pages.append(
    page(
        "9. Emerging Themes and Investment Implications",
        [
            table(
                [
                    ["Theme", "Why it matters", "Investor relevance"],
                    ["LNG liquidity and flexibility", "More destination-free contracts and portfolio players increase cargo optionality.", "Supports optimization software and trading capability investment."],
                    ["Storage and reserve mechanisms", "Systems need resilience against weather, geopolitical, and renewable-output shocks.", "Drives value for storage owners and inventory analytics."],
                    ["Methane MRV and traceability", "EU regulation pushes measurement and reporting into import supply chains.", "Creates compliance software, certification, and data-integration demand."],
                    ["Gas-electric coordination", "Renewables variability increases gas-fired balancing needs.", "Benefits platforms connecting gas procurement, power dispatch, and risk."],
                    ["Emerging-market infrastructure", "Price-sensitive Asia may absorb LNG only if regas and pipeline capacity expands.", "Infrastructure bottlenecks determine realized demand growth."],
                    ["AI-enabled optimization", "Complex contracts, routes, constraints, and volatility exceed spreadsheet workflows.", "Creates premium for integrated data and optimization tools."],
                ],
                [1.6 * inch, 3.0 * inch, 2.85 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "10. Most Insightful Industry Trend Bullets",
        [
            bullet("LNG supply growth should ease market tightness after 2026, but infrastructure bottlenecks may limit demand response in price-sensitive Asian markets."),
            bullet("Storage has shifted from seasonal buffer to strategic supply-security infrastructure, increasing the value of inventory analytics and withdrawal optimization."),
            bullet("Methane regulation is turning emissions data into a commercial attribute, especially for gas sold into Europe and climate-sensitive buyers."),
            bullet("Gas-electric coordination is becoming more important as renewable variability increases demand for flexible gas-fired generation and faster procurement decisions."),
            bullet("Portfolio players with destination flexibility, shipping optionality, and integrated risk systems are better placed to monetize volatility than single-asset operators."),
            p("Why these trends matter", "SectionTitle"),
            p(
                "These themes are not generic energy-sector observations. They are specific to Gas SCM because they affect daily operational decisions: nominations, lifting schedules, storage dispatch, cargo routing, supplier selection, and commercial exposure management.",
            ),
        ],
    )
)

pages.append(
    page(
        "11. Value Chain Analysis",
        [
            table(
                [
                    ["Stage", "Key activities", "Value addition", "Example players"],
                    ["Upstream production", "Exploration, drilling, production, gathering.", "Converts reserves into saleable gas supply.", "ExxonMobil, Chevron, Equinor, ADNOC, QatarEnergy."],
                    ["Processing", "Dehydration, NGL removal, quality control.", "Makes gas pipeline- or LNG-ready.", "Enterprise Products, Williams, Kinder Morgan."],
                    ["Transmission", "Long-haul pipelines, compression, interconnects.", "Moves gas to demand centers and LNG terminals.", "TC Energy, Kinder Morgan, Enbridge, Snam, GRTgaz."],
                    ["Storage", "Injection, withdrawal, balancing, reserve capacity.", "Provides seasonal and shock-response flexibility.", "Uniper, Centrica, Enbridge, Kinder Morgan."],
                    ["Liquefaction", "Converts gas to LNG for marine export.", "Enables global arbitrage and long-distance trade.", "Cheniere, QatarEnergy, Venture Global, Shell."],
                    ["Shipping", "LNG carriers, charters, routing, boil-off management.", "Converts cargo optionality into delivered flexibility.", "Nakilat, NYK, MOL, Flex LNG."],
                    ["Regasification", "LNG receipt, storage, vaporization, send-out.", "Connects global LNG to domestic gas systems.", "Snam, Enagas, Excelerate Energy."],
                    ["Distribution", "Local networks, metering, customer delivery.", "Delivers gas to end users safely and reliably.", "National Grid, Atmos, Tokyo Gas."],
                    ["Trading / SCM systems", "Trade capture, scheduling, nominations, risk, settlement.", "Optimizes physical and financial flows.", "ION, Quorum, SAP, PCI, Trellis, Fendahl."],
                ],
                [1.1 * inch, 2.0 * inch, 2.15 * inch, 2.2 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "12. Competitive Landscape: Physical Market Participants",
        [
            p(
                "The physical gas SCM landscape is not a single market with clean public market shares. Competitive positions vary by role: resource ownership, pipeline access, LNG capacity, portfolio flexibility, storage, trading capability, and software enablement.",
            ),
            table(
                [
                    ["Archetype", "Competitive advantage", "Examples"],
                    ["Integrated majors", "Global portfolios across upstream, LNG, trading, shipping, and downstream customers.", "Shell, TotalEnergies, BP, ExxonMobil, Chevron."],
                    ["National resource owners", "Low-cost reserves and large sanctioned LNG expansions.", "QatarEnergy, ADNOC, Petronas."],
                    ["LNG pure-play exporters", "Contracted liquefaction capacity and execution focus.", "Cheniere, Venture Global."],
                    ["Midstream operators", "Pipeline, gathering, processing, and storage network control.", "Kinder Morgan, Williams, Enbridge, TC Energy."],
                    ["Utilities / importers", "Captive demand, regas access, and long-term procurement.", "JERA, Tokyo Gas, Korea Gas, Uniper."],
                    ["Commodity traders", "Optionality, risk appetite, logistics, and short-term arbitrage.", "Vitol, Trafigura, Gunvor."],
                    ["SCM software vendors", "Workflow digitization, ETRM/CTRM, nominations, analytics.", "ION, Quorum, SAP, PCI, Trellis."],
                ],
                [1.7 * inch, 3.3 * inch, 2.45 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "13. Peer Universe and Relevancy Ranking",
        [
            p("Ranking basis: relevance to Gas SCM breadth, overlap with physical gas workflows, LNG/pipeline applicability, and geographic reach."),
            table(
                [
                    ["Rank", "Peer / participant", "One-line business description", "Relevancy", "Reason"],
                    ["1", "ION Commodities", "CTRM / ETRM platform spanning natural gas, LNG, trading, scheduling, logistics, and risk.", "High", "Covers wellhead-to-consumer workflows and integrates physical and financial positions."],
                    ["2", "Quorum Software", "Midstream and gas pipeline software for nominations, scheduling, allocations, invoicing, and compliance.", "High", "Deep fit for gas pipeline and storage transaction management."],
                    ["3", "SAP Oil & Gas / TSW", "Enterprise software supporting nominations, logistics, scheduling, and ERP integration.", "High", "Strong enterprise integration, though less gas-specialist than vertical platforms."],
                    ["4", "Trellis Energy", "Cloud platform for natural gas lifecycle management across trading, scheduling, capacity, settlement, and compliance.", "High", "Purpose-built for natural gas transaction workflows and pipeline connectivity."],
                    ["5", "PCI Energy Solutions", "Gas and fuels management platform for utilities and power companies.", "High", "Strong gas-electric coordination and U.S. pipeline nomination relevance."],
                    ["6", "Fendahl Fusion", "CTRM platform for LNG, LPG, and commodity trading lifecycle management.", "Medium", "Strong LNG trading fit, narrower pipeline scheduling footprint."],
                    ["7", "Lacima Analytics", "LNG shipping and portfolio optimization tools for cargo and vessel planning.", "Medium", "High-value LNG niche, narrower workflow breadth."],
                    ["8", "NatGasHub", "Multi-pipeline nominations and scheduling platform connected to U.S. pipelines.", "Medium", "Highly relevant to nominations, less broad across ETRM and LNG."],
                ],
                [0.35 * inch, 1.25 * inch, 2.55 * inch, 0.7 * inch, 2.6 * inch],
                font_size=6.8,
            ),
        ],
    )
)

pages.append(
    page(
        "14. Peer Universe and Relevancy Ranking, Continued",
        [
            table(
                [
                    ["Rank", "Peer / participant", "One-line business description", "Relevancy", "Reason"],
                    ["9", "Pandell Latitude", "Pipeline and storage management software for nominations, notices, capacity, and invoicing.", "Medium", "Relevant midstream workflow focus with regional concentration."],
                    ["10", "Shell", "Integrated global LNG, trading, upstream, and downstream gas portfolio player.", "High", "Benchmark physical portfolio optimizer with global LNG optionality."],
                    ["11", "TotalEnergies", "Integrated energy major with LNG production, trading, and long-term sales portfolio.", "High", "Strong LNG and portfolio-management relevance."],
                    ["12", "Cheniere", "Leading U.S. LNG exporter with contracted liquefaction and cargo delivery model.", "Medium", "Highly relevant to LNG supply, narrower across downstream SCM."],
                    ["13", "QatarEnergy", "National energy company leading major LNG capacity expansion from Qatar's North Field.", "Medium", "Dominant LNG supply relevance, less a third-party SCM platform."],
                    ["14", "Kinder Morgan", "North American midstream operator with major gas pipelines and storage assets.", "Medium", "Strong physical network relevance, mainly regional."],
                    ["15", "JERA", "Large Asian LNG buyer, power generator, and portfolio manager.", "Medium", "Important LNG procurement and demand-side optimization participant."],
                    ["16", "Vitol / Trafigura / Gunvor", "Global commodity traders active in gas, LNG, logistics, and risk-taking.", "Medium", "Strong optionality and market-making relevance; limited public operating detail."],
                ],
                [0.35 * inch, 1.35 * inch, 2.45 * inch, 0.7 * inch, 2.6 * inch],
                font_size=6.8,
            ),
            p("Interpretation", "SectionTitle"),
            p(
                "Software peers score highly where they control operational workflows and data. Physical peers score highly where they demonstrate portfolio flexibility, supply scale, or infrastructure optionality directly relevant to gas flows.",
            ),
        ],
    )
)

pages.append(
    page(
        "15. Competitive Factors",
        [
            table(
                [
                    ["Competitive factor", "Why it matters"],
                    ["Physical optionality", "Storage, pipeline paths, LNG cargo flexibility, and regas slots allow players to respond to shocks."],
                    ["Contract flexibility", "Destination-free LNG and hub-indexed contracts increase portfolio value and trading agility."],
                    ["Real-time data visibility", "Nominations, metering, pricing, weather, shipping, and risk data must be integrated quickly."],
                    ["Regulatory compliance", "FERC, NAESB, EU methane rules, and safety reporting create non-discretionary workflows."],
                    ["Trading and risk integration", "Physical gas decisions affect P&L, credit, collateral, and hedge effectiveness."],
                    ["Emissions traceability", "Methane and carbon intensity are becoming commercial differentiators and compliance requirements."],
                    ["Cyber resilience", "Connected pipeline, trading, and settlement systems expand the attack surface."],
                ],
                [2.0 * inch, 5.45 * inch],
            ),
            p("Management takeaway", "SectionTitle"),
            bullet("Market leaders will combine optional physical assets with digital decision support and disciplined risk governance."),
            bullet("Specialized vendors can compete against enterprise suites when workflow depth, pipeline connectivity, and compliance specificity are decisive."),
        ],
    )
)

pages.append(
    page(
        "16. Market Positioning: Peer Archetypes",
        [
            bullet("Integrated majors position around portfolio flexibility, combining upstream supply, liquefaction, shipping, trading, and customer channels to monetize regional price spreads."),
            bullet("LNG exporters position around reliability, long-term contracts, and capacity expansion, with U.S. exporters emphasizing Henry Hub-linked affordability and Qatar emphasizing scale."),
            bullet("Midstream operators position around network reliability, interconnectivity, storage access, and regulatory credibility, creating defensible regional infrastructure positions."),
            bullet("Software vendors position around single-source-of-truth workflows, reducing spreadsheet dependency across nominations, scheduling, settlement, risk, and compliance."),
            bullet("LNG optimization specialists position around cargo, vessel, route, and contract optionality, solving high-value but narrower planning problems."),
            p("Customer lens", "SectionTitle"),
            p(
                "Customers evaluate Gas SCM offerings through operational reliability, compliance burden, integration cost, reduction in manual work, ability to manage volatility, and fit with existing ETRM, ERP, metering, and pipeline-data environments.",
            ),
        ],
    )
)

pages.append(
    page(
        "17. Target Positioning Implications for a Potential Gas SCM Asset",
        [
            p(
                "Because company-specific sections are excluded, this section describes how an attractive potential target in Gas SCM would ideally position itself.",
            ),
            bullet("A differentiated Gas SCM target should own mission-critical workflows where errors create imbalance penalties, missed nominations, settlement disputes, or supply-security exposure."),
            bullet("Strong positioning would combine physical gas specificity with enterprise-grade integration across ETRM, ERP, metering, weather, pipeline bulletin boards, and market data."),
            bullet("The most attractive targets should serve multiple participant types, including utilities, pipelines, storage operators, LNG traders, and power generators."),
            bullet("Emissions and methane traceability can strengthen positioning if embedded into existing operational workflows rather than sold as a standalone ESG module."),
            bullet("AI optimization is most credible when applied to constrained operational decisions such as storage dispatch, cargo routing, pipeline paths, and gas-to-power coordination."),
        ],
    )
)

pages.append(
    page(
        "18. Competitive Heat Map",
        [
            table(
                [
                    ["Player / archetype", "Product / service breadth", "Geographic presence", "Heat-map interpretation"],
                    ["Shell", "Broad", "Global", "Full portfolio benchmark across LNG, trading, upstream, and customer channels."],
                    ["TotalEnergies", "Broad", "Global", "Integrated LNG portfolio with strong commercial optimization relevance."],
                    ["BP", "Broad", "Global", "Broad gas and trading participation, though less LNG-dominant than Shell."],
                    ["QatarEnergy", "Medium", "Global export", "Extremely strong supply scale, narrower third-party SCM breadth."],
                    ["Cheniere", "Medium", "Global export", "LNG export specialist with contracted capacity and U.S. supply linkage."],
                    ["Kinder Morgan", "Medium", "National / regional", "North American pipeline and storage network strength."],
                    ["JERA", "Medium", "Global import / Asia-led", "Large demand-side LNG portfolio and power-generation integration."],
                    ["ION Commodities", "Broad", "Global", "Broad CTRM/ETRM and gas/LNG value-chain software coverage."],
                    ["Quorum", "Medium", "North America-led", "Deep midstream and gas pipeline management specialization."],
                    ["SAP", "Broad", "Global", "Enterprise breadth, strong integration, less vertically specialized."],
                    ["PCI Energy Solutions", "Medium", "North America-led", "Strong gas-power and utility fuels management specialization."],
                    ["Trellis Energy", "Medium", "North America-led", "Modern gas transaction platform with pipeline connectivity."],
                ],
                [1.55 * inch, 1.2 * inch, 1.25 * inch, 3.45 * inch],
                font_size=6.9,
            ),
        ],
    )
)

pages.append(
    page(
        "19. Value Creation Levers",
        [
            table(
                [
                    ["VCL or Risk", "Title", "Description"],
                    ["VCL", "LNG optionality optimization", "Players can monetize destination flexibility, shipping routes, regas slots, and storage by using integrated optimization tools that convert volatility into portfolio margin."],
                    ["VCL", "Storage intelligence", "Better injection, withdrawal, and reserve planning improves reliability and captures seasonal spreads, especially as weather and renewables volatility increase."],
                    ["VCL", "Gas-electric coordination", "Linking gas procurement with power dispatch reduces fuel-cost leakage and imbalance exposure for utilities and generators with gas-fired fleets."],
                    ["VCL", "Methane data monetization", "Operators can use measurement-based methane data to protect market access, differentiate lower-intensity gas, and reduce avoidable product losses."],
                    ["VCL", "Workflow automation", "Automating nominations, confirmations, tariffs, and settlements reduces manual errors, shortens close cycles, and lowers compliance and imbalance costs."],
                    ["VCL", "Contract flexibility analytics", "Better modeling of take-or-pay, destination, indexation, and volume tolerance terms helps players value optionality and negotiate superior contracts."],
                    ["VCL", "AI-constrained optimization", "AI can create value when trained on operational constraints, enabling faster decisions across pipeline paths, cargo schedules, storage, and hedge actions."],
                ],
                [0.85 * inch, 1.65 * inch, 4.95 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "20. Key Risks",
        [
            table(
                [
                    ["VCL or Risk", "Title", "Description"],
                    ["Risk", "LNG surplus pressure", "The 2030 LNG capacity wave may pressure margins if demand response lags, requiring players to optimize contracts, utilization, and customer diversification."],
                    ["Risk", "Infrastructure bottlenecks", "Emerging-market demand may not materialize if regas, pipelines, credit, and downstream infrastructure lag, limiting growth for LNG-linked SCM players."],
                    ["Risk", "Methane compliance burden", "EU-style methane MRV requirements can raise data, audit, and supplier-management costs, especially for complex or opaque upstream supply chains."],
                    ["Risk", "Geopolitical route disruption", "Panama, Red Sea, Ukraine transit, sanctions, and chokepoint risks can disrupt physical flows, increasing the need for scenario planning and optionality."],
                    ["Risk", "Cyber-physical exposure", "More connected scheduling, pipeline, trading, and settlement platforms increase cyber risk, requiring resilient architecture and operational continuity planning."],
                    ["Risk", "Data-quality fragmentation", "Fragmented meters, EBBs, contracts, tariffs, and ERP systems can undermine automation benefits unless governance and integration are addressed early."],
                    ["Risk", "Policy-driven demand erosion", "European demand decline and decarbonization policy can reduce volumes, making growth dependent on Asia, power-sector flexibility, and low-emissions positioning."],
                ],
                [0.85 * inch, 1.65 * inch, 4.95 * inch],
            ),
        ],
    )
)

pages.append(
    page(
        "21. Regulatory and Emissions Outlook",
        [
            p(
                "Methane is the most important emerging compliance theme for Gas SCM. The European Commission adopted the EU Methane Regulation in 2024, requiring fossil gas, oil, and coal operators in Europe to measure, monitor, report, and verify methane emissions. The regulation also progressively introduces requirements affecting imported fossil fuels.",
            ),
            p(
                "IEA's Global Methane Tracker 2025 estimates fossil fuels are responsible for nearly one-third of human-caused methane emissions, with energy-related methane emissions still above 120 Mt annually. IEA also estimates global energy-related methane emissions are about 80% higher than what countries report to the UNFCCC.",
            ),
            p(
                "World Bank reported global flaring reached 151 bcm in 2024, the highest since 2007, releasing 389 MtCO2e. This highlights the supply-chain opportunity to convert wasted associated gas into marketable supply.",
            ),
            p("Implications for Gas SCM", "SectionTitle"),
            bullet("Emissions data will need to connect with physical supply, contract, and cargo records."),
            bullet("Methane MRV may influence supplier qualification and LNG procurement decisions."),
            bullet("Captured methane and reduced flaring can add supply while lowering emissions intensity."),
            bullet("Compliance modules become more valuable if embedded into existing scheduling and trade workflows."),
        ],
    )
)

pages.append(
    page(
        "22. Technology and Digital SCM Trends",
        [
            p(
                "Deloitte argues that advanced CTRM ecosystems require a transactional core, integrated UI/UX, advanced analytics, optimization tools, and AI/ML. This aligns closely with gas SCM needs because physical and financial decisions are tightly linked.",
            ),
            bullet("Quorum positions My Quorum Pipeline around nominations, scheduling, allocations, imbalances, invoicing, and NAESB-certified compliance, with 350 gathering systems and pipelines in North America under management."),
            bullet("ION states that its natural gas and LNG solutions cover gathering, processing, transportation, storage, utility distribution, physical and financial gas, LNG logistics, risk, and P&L visibility."),
            bullet("PCI emphasizes gas-power coordination, nominations across major U.S. pipelines, transportation contracts, tariffs, storage, risk, and gas cost savings for physical power companies."),
            bullet("Trellis positions itself as a cloud platform for the natural gas lifecycle, serving traders, schedulers, capacity traders, accountants, and technology managers across 100+ connected pipelines."),
            p("Implication", "SectionTitle"),
            p(
                "The software market is shifting from isolated modules to connected ecosystems. The winning architecture may be common platform, best-of-breed, or hybrid, but integration quality and data governance will determine realized value.",
            ),
        ],
    )
)

pages.append(
    page(
        "23. Investment Perspective and Diligence Questions",
        [
            p("What makes the space attractive", "SectionTitle"),
            bullet("Mission-critical workflows: gas scheduling and balancing failures can create direct financial and reliability consequences."),
            bullet("High switching complexity: integrations with pipelines, meters, ERP, ETRM, market data, and compliance workflows create embeddedness."),
            bullet("Regulatory durability: safety, methane, FERC, NAESB, and audit requirements create recurring needs."),
            bullet("Volatility upside: more volatility increases the value of optimization, storage, and flexible contracting."),
            bullet("Energy transition relevance: gas remains a balancing fuel while methane and carbon-intensity requirements create new data workflows."),
            p("Key diligence questions", "SectionTitle"),
            bullet("How much revenue is recurring versus implementation or professional services?"),
            bullet("What share of customer workflows are system-of-record versus analytics overlay?"),
            bullet("How deep are pipeline, exchange, meter, EBB, ERP, and ETRM integrations?"),
            bullet("Does the platform solve daily operational pain or only periodic reporting needs?"),
            bullet("Are methane and carbon workflows tied to physical supply records?"),
        ],
    )
)

pages.append(
    [
        p("24. Bottom-Line Conclusions and Source Tiers", "PageTitle"),
        p(
            "Gas supply chain management is becoming more valuable because the gas market is more global, more volatile, more regulated, and more data-intensive. LNG connects regional markets, storage is increasingly strategic, and methane regulation is turning emissions into a supply-chain attribute.",
        ),
        p(
            "The most attractive opportunities are likely to sit where physical complexity meets recurring digital workflow: nominations, scheduling, storage, LNG cargo optimization, ETRM/CTRM integration, settlement, and emissions traceability.",
        ),
        p(
            "The main risk is not that gas disappears quickly; Tier 1 outlooks still show demand growth through 2030. The sharper risk is that value migrates unevenly toward lower-cost LNG suppliers, flexible portfolio players, storage-rich operators, and digital platforms that can manage volatility, compliance, and real-time physical constraints.",
        ),
        p("Tier 1 - Highest Confidence", "SectionTitle"),
        bullet("IEA: Global Gas Security Review 2024; Gas Market Report Q2 2025; Gas 2025; Global Methane Tracker 2025. https://www.iea.org"),
        bullet("EIA: Short-Term Energy Outlook and U.S. LNG export analysis. https://www.eia.gov"),
        bullet("Eurostat: Natural gas supply statistics. https://ec.europa.eu/eurostat"),
        bullet("European Commission: EU Methane Regulation. https://energy.ec.europa.eu"),
        bullet("World Bank: Global Gas Flaring Tracker 2025. https://www.worldbank.org"),
        bullet("PHMSA: Pipeline incident reporting data framework. https://www.phmsa.dot.gov"),
        p("Tier 2 - High Confidence", "SectionTitle"),
        bullet("Deloitte: Advanced CTRM ecosystems. https://www.deloitte.com"),
        bullet("Quorum, ION, PCI Energy Solutions, and Trellis Energy company websites for vendor positioning and product capabilities."),
        p("Tier 3 - Medium Confidence", "SectionTitle"),
        bullet("International Gas Union 2025 World LNG Report and GIIGNL annual report pages for LNG trade and infrastructure context."),
        p("Tier 4 - Avoided", "SectionTitle"),
        bullet("No Wikipedia, blogs, unverified forums, or paid market-research estimates were used for conclusions or sizing."),
    ]
)

for pg in pages:
    story.extend(pg)

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(f"Wrote {OUTPUT_FILE}")
