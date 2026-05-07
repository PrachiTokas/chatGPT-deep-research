from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak


OUTPUT_FILE = "gas_supply_chain_management_industry_report.pdf"


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23, leading=29, textColor=colors.HexColor("#12355B"), spaceAfter=14))
styles.add(ParagraphStyle(name="PageTitle", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=colors.HexColor("#12355B"), spaceAfter=8))
styles.add(ParagraphStyle(name="SectionTitle", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11, leading=13, textColor=colors.HexColor("#1F4E79"), spaceBefore=5, spaceAfter=3))
styles.add(ParagraphStyle(name="BodySmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.55, leading=11.05, spaceAfter=4))
styles.add(ParagraphStyle(name="BulletSmall", parent=styles["BodySmall"], leftIndent=12, firstLineIndent=-7, bulletIndent=0))
styles.add(ParagraphStyle(name="TableText", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.15, leading=8.75))
styles.add(ParagraphStyle(name="TableHead", parent=styles["TableText"], fontName="Helvetica-Bold", textColor=colors.white))


def p(text, style="BodySmall"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(f"- {text}", styles["BulletSmall"])


def tbl(data, col_widths, repeat_rows=1, font_size=7.15):
    formatted = []
    for r, row in enumerate(data):
        formatted.append([p(str(cell), "TableHead" if r == 0 else "TableText") for cell in row])
    table = Table(formatted, colWidths=col_widths, repeatRows=repeat_rows, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1F4E79")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#B7C9D6")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F8FA")]),
    ]))
    return table


def page(title, elements):
    return [p(title, "PageTitle"), *elements, PageBreak()]


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.4)
    canvas.setFillColor(colors.HexColor("#5B6770"))
    canvas.drawString(0.55 * inch, 0.35 * inch, "Asset-Light Specialty Gas SCM Platform Report")
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


story = [
    p("Technology-Driven, Asset-Light Gas Supply Chain Management Platform", "CoverTitle"),
    p("Industry report focused on multi-gas supply orchestration across CO2, helium, propane, nitrous oxide, nitrogen, oxygen, and related specialty gases serving healthcare, QSR / beverage, and industrial end markets.", "BodySmall"),
    Spacer(1, 6),
    p("Executive Summary", "PageTitle"),
    tbl([
        ["Section", "What We Like", "What We Want to Investigate Further"],
        ["Company Overview / Platform Model", "Asset-light intermediary model can solve fragmented local gas procurement for multi-location customers without owning production or delivery fleets.<br/><br/>Single contact, consolidated billing, account management, telemetry, and automated replenishment address operational pain points that enterprise customers often cannot solve internally.", "Assess quality, exclusivity, and density of supplier relationships by ZIP code, gas type, and service-level performance.<br/><br/>Determine whether proprietary technology is workflow-critical or primarily a customer-facing layer over third-party telemetry and distributor execution."],
        ["Market Overview and Trends", "End markets have recurring, non-discretionary gas needs: CO2 for beverage, nitrous oxide and oxygen for care, helium for MRI/labs, propane for industrial operations.<br/><br/>Supply volatility in CO2 and helium increases the value of distributor optionality, inventory visibility, and proactive replenishment.", "Quantify customer willingness to pay for resilience, single-invoice administration, and runout avoidance versus direct local distributor relationships.<br/><br/>Evaluate how much addressable demand sits with national chains requiring multi-state service versus local accounts served effectively by incumbents."],
        ["Competitive Landscape", "Large gas majors have scale and supply control, while regional distributors have local density; the platform model can intermediate between both and enterprise buyers.<br/><br/>Technology-enabled distributors increasingly use telemetry, portals, and automated delivery, validating customer demand for digital gas management.", "Map competitive overlap between national suppliers, beverage-gas specialists, propane telemetry providers, and distributor roll-up platforms.<br/><br/>Assess whether majors could replicate account consolidation and telemetry, or whether channel conflict and local service complexity protect specialists."],
        ["Value Creation and Risks", "Telemetry and usage analytics can reduce emergency deliveries, optimize storage sizing, detect leaks, and convert reactive ordering into managed replenishment.<br/><br/>Distributor-network model supports rapid geographic breadth with lower capital intensity than owning branches, trucks, tanks, and production assets.", "Investigate supplier concentration, data ownership, device interoperability, billing accuracy, and SLA enforceability as the platform scales.<br/><br/>Evaluate exposure to CO2 shortages, helium allocation, FDA medical gas compliance, hazardous-material safety, and customer-site incident risk."],
    ], [1.35 * inch, 3.05 * inch, 3.05 * inch]),
    PageBreak(),
]


pages = []

pages.append(page("1. Scope and Reframed Industry Definition", [
    p("This report focuses on technology-driven, asset-light supply chain management platforms for specialty and packaged gases. The model serves as an intermediary between networks of local/regional distributors and multi-location enterprise customers, providing one contact, consolidated billing, centralized account management, technology-enabled visibility, telemetry, and automated replenishment."),
    p("Included gases", "SectionTitle"),
    bullet("Carbon dioxide: beverage carbonation, beer gas blends, dry ice, food processing, healthcare, water treatment, and industrial use."),
    bullet("Helium: MRI, laboratories, analytical instruments, leak detection, specialty manufacturing, aerospace, and controlled atmospheres."),
    bullet("Propane: commercial heating, forklifts, temporary heat, hospitality, unmanned industrial sites, and distributed energy applications."),
    bullet("Nitrous oxide, oxygen, nitrogen, medical CO2, and specialty mixes: healthcare, dental, veterinary, beverage, welding, and industrial processes."),
    p("What is excluded", "SectionTitle"),
    bullet("Traditional natural gas pipeline/LNG supply chain management is not the focus, except where technology and replenishment analogies apply."),
    bullet("This is an industry perspective, not a company diligence memo; company examples are used only to illustrate archetypes and peers."),
]))

pages.append(page("2. Platform Model Overview", [
    p("The target model is neither a gas producer nor a conventional local distributor. It is a managed supply orchestration layer that coordinates many local suppliers and presents a unified operating interface to enterprise customers. Its value proposition is administrative simplification, service reliability, data visibility, and multi-location standardization."),
    tbl([
        ["Layer", "What the platform does", "Value to enterprise customer"],
        ["Supplier network", "Qualifies and routes orders to local/regional distributors by market, gas type, availability, and service capability.", "Retains local fulfillment density while avoiding vendor-by-vendor management."],
        ["Commercial wrapper", "Provides single contract, account manager, pricing structure, consolidated billing, and issue escalation.", "Reduces AP burden, store-level inconsistency, and procurement leakage."],
        ["Technology layer", "Offers portal ordering, EDI/API integrations, telemetry dashboard, threshold alerts, and usage analytics.", "Improves visibility, controls usage, reduces runouts, and supports corporate reporting."],
        ["Operational execution", "Schedules refills, monitors inventory, coordinates exceptions, and follows up on service levels.", "Converts reactive store ordering into proactive managed replenishment."],
        ["Optimization layer", "Analyzes usage, tank sizing, delivery frequency, abnormal consumption, and market-level supplier performance.", "Reduces emergency delivery, waste, leakage, and over-inventory."],
    ], [1.4 * inch, 3.25 * inch, 2.8 * inch]),
]))

pages.append(page("3. Industry Classification and Core Offerings", [
    tbl([
        ["Classification lens", "Relevant classification"],
        ["GICS", "Industrials - Trading Companies & Distributors; Materials - Industrial Gases; Health Care - Health Care Supplies for medical gas applications; IT - Application Software for telemetry/platform elements."],
        ["PICS-style mapping", "Industrial distribution, asset-light B2B services, vertical SaaS-enabled supply chain orchestration, specialty gas services."],
        ["Sub-sector", "Managed gas supply, packaged/bulk gas procurement, beverage gas logistics, medical gas distribution coordination, propane telemetry and replenishment."],
    ], [2.0 * inch, 5.45 * inch]),
    p("Core offerings", "SectionTitle"),
    bullet("Multi-site account setup, supplier assignment, consolidated billing, standardized pricing, and centralized account management."),
    bullet("Gas ordering and replenishment across cylinders, microbulk, bulk tanks, and commercial propane tanks."),
    bullet("Remote tank monitoring, threshold alerts, abnormal-usage detection, and predictive delivery scheduling."),
    bullet("Compliance-support workflows for medical gases, hazardous-material handling, CO2 monitoring, delivery documentation, and audit trails."),
]))

pages.append(page("4. Source Identification and Prioritization", [
    p("The report prioritizes public-sector and regulator sources for gas-specific market risk, safety, and compliance, supplemented by company websites for platform capabilities and competitive positioning. Paid market-research estimates are avoided."),
    tbl([
        ["Tier", "Source type", "Sources used", "Role in report"],
        ["Tier 1", "Government, regulators, public agencies.", "EPA, FDA, OSHA, USGS.", "CO2 supply-chain risk, medical gas rules, CO2 safety, helium data."],
        ["Tier 2", "Company websites and consulting/industry operations sources.", "EspriGas, Linde, Airgas, Tank Utility, Superior Propane, Gray Gray & Gray / BPN.", "Platform model, telemetry, automatic delivery, distributor operations."],
        ["Tier 3", "Industry associations / trade media / specialist publications.", "CGA references, gas industry publications, beverage gas sources.", "Operational norms and competitive context."],
        ["Tier 4", "Blogs, unverified forums, paid market sizing.", "Avoided.", "Not used for conclusions or sizing."],
    ], [0.75 * inch, 2.0 * inch, 2.5 * inch, 2.2 * inch]),
]))

pages.append(page("5. Demand Drivers by End Market", [
    tbl([
        ["End market", "Core gas needs", "Why supply chain management matters"],
        ["QSR / beverage", "CO2, nitrogen, beer gas blends, dry ice.", "Runouts stop fountain drinks and draft programs; inconsistent site ordering creates emergency deliveries and invoice complexity."],
        ["Healthcare / dental / veterinary", "Oxygen, nitrous oxide, nitrogen, medical CO2, helium, specialty mixes.", "Gas availability affects care delivery; FDA CGMP, labeling, supplier qualification, and traceability elevate compliance requirements."],
        ["Industrial / commercial", "Propane, acetylene, oxygen, nitrogen, CO2, helium.", "Distributed sites and unmanned assets need reliable replenishment, safety, and cost control."],
        ["Laboratory / specialty", "Helium, nitrogen, calibration gases, high-purity mixes.", "Shortages can idle instruments; quality and continuity matter more than lowest delivered price."],
        ["Food processing / cold chain", "CO2, nitrogen, dry ice.", "Gas supports preservation, freezing, modified-atmosphere packaging, and temperature-controlled logistics."],
    ], [1.35 * inch, 2.3 * inch, 3.8 * inch]),
    p("Investor interpretation", "SectionTitle"),
    bullet("Demand is recurring and operationally embedded, but gas type mix matters: CO2 and propane are logistics-heavy, helium is allocation-sensitive, and medical gases are compliance-heavy."),
]))

pages.append(page("6. Gas-Specific Supply Chain Characteristics", [
    tbl([
        ["Gas", "Supply chain traits", "Platform implications"],
        ["CO2", "Commercial CO2 is largely recovered as a co-product of ethanol, ammonia, and hydrogen production; it is transported as liquefied gas, cylinders, or dry ice.", "Supply is regionally vulnerable; platforms can arbitrage distributor optionality and monitor consumption to reduce waste."],
        ["Helium", "Produced from natural gas streams, with U.S. sales valued near $1.1B for 81 million cubic meters in 2024 per USGS.", "Allocation risk and high value make supplier redundancy and customer prioritization important."],
        ["Propane", "Retail distribution is route-density driven; margins depend on delivery size, routing, and tank ownership economics.", "Tank monitors and predictive routing can improve gallons per stop and reduce runouts."],
        ["Nitrous oxide", "Medical and dental use requires designated medical gas compliance and supplier qualification.", "Compliance workflows and documentation become part of the value proposition."],
        ["Nitrogen / oxygen", "Used in medical, beverage, welding, food, and industrial applications with cylinder, bulk, and specialty-grade variants.", "Multi-gas support increases wallet share but requires grade, container, and supplier complexity management."],
    ], [0.95 * inch, 3.45 * inch, 3.05 * inch]),
]))

pages.append(page("7. Historical Market Trends: Supply Volatility", [
    p("The last several years have highlighted that specialty gas supply chains can be fragile despite mature distribution networks. CO2 disruptions during 2020-2023 were tied to ethanol and ammonia production changes, plant closures, force majeure notices, regional outages, and contamination of natural CO2 sources. EPA characterizes CO2 as high criticality with a moderate-low supply disruption risk rating, while noting high likelihood of regional disruption history."),
    p("For helium, USGS data show continued importance to MRI, laboratories, analytical gases, leak detection, aerospace, and specialty applications. The U.S. Federal Helium System privatization and import reliance reinforce the need for allocation planning and supplier diversification."),
    p("For propane, distributor economics are increasingly efficiency-driven. The 2024 propane survey highlighted technology adoption, delivery planning, and tank monitor usage as key operational themes, with 69% focusing on fleet optimization and 68% on fewer but larger deliveries."),
    p("Platform implication", "SectionTitle"),
    bullet("Supply volatility increases willingness to outsource coordination to a platform if it can prove better visibility, supplier redundancy, and service-level discipline than local procurement alone."),
]))

pages.append(page("8. Future Outlook: Why the Model Should Matter More", [
    p("The asset-light gas SCM platform model should benefit from four structural shifts: enterprise customers consolidating fragmented site-level procurement, distributors seeking national-account access without building national sales infrastructure, growing telemetry adoption, and increasing compliance/safety expectations around medical gases and CO2 storage."),
    tbl([
        ["Forward trend", "Why it is relevant", "Likely beneficiary"],
        ["Telemetry penetration", "Tank monitoring enables automatic replenishment and reduces emergency service.", "Platforms, telemetry vendors, efficient distributors."],
        ["Supplier fragmentation", "Local gas distribution remains branch- and route-density dependent.", "Asset-light network managers that aggregate demand."],
        ["Compliance complexity", "FDA medical gas rules and CO2 safety requirements increase documentation needs.", "Platforms with audit trails and qualified supplier workflows."],
        ["Enterprise procurement centralization", "National chains want one invoice, one contact, and consistent service standards.", "Managed gas supply platforms and national gas suppliers."],
        ["Gas shortages and allocation", "CO2 and helium disruptions make supplier optionality valuable.", "Platforms with diverse supply networks and predictive demand data."],
    ], [1.55 * inch, 3.0 * inch, 2.9 * inch]),
]))

pages.append(page("9. Most Insightful Industry Trend Bullets", [
    bullet("Enterprise buyers increasingly value gas-supply administration as much as delivered gas price, because fragmented local invoices and runouts create hidden costs."),
    bullet("Telemetry is moving gas supply from reactive ordering to managed replenishment, enabling fewer emergencies, better tank sizing, and clearer usage accountability."),
    bullet("CO2 and helium volatility create resilience premiums for platforms that can route demand across qualified local suppliers and monitor usage patterns."),
    bullet("Healthcare and dental gas supply rewards documentation, supplier qualification, and service reliability, not just geographic coverage or unit price."),
    bullet("Regional distributors may partner with asset-light platforms because national-account access offsets the risk of being displaced by gas majors."),
]))

pages.append(page("10. Value Chain: Asset-Light Specialty Gas SCM", [
    tbl([
        ["Stage", "Key activities", "Value addition", "Example participants"],
        ["Gas production / sourcing", "CO2 recovery, air separation, helium extraction, propane wholesale, nitrous oxide production.", "Creates qualified gas supply by grade and application.", "Linde, Air Liquide/Airgas, Messer, Matheson, producers."],
        ["Local distribution", "Cylinder fills, bulk/microbulk deliveries, route execution, service calls.", "Provides physical fulfillment and local service density.", "Regional gas distributors, propane marketers."],
        ["Platform orchestration", "Supplier selection, order routing, account management, billing, usage analytics.", "Simplifies fragmented supply for enterprise customers.", "Asset-light gas SCM platforms."],
        ["Telemetry / monitoring", "Tank sensors, dashboards, alerts, estimated fill dates, anomaly detection.", "Reduces runouts and supports automated replenishment.", "EspriVision, Tank Utility, Otodata, supplier systems."],
        ["Customer operations", "Store, clinic, plant, or site consumes gases and manages exceptions.", "End-use reliability, safety, and productivity.", "QSR chains, dental groups, hospitals, industrial operators."],
        ["Compliance / safety", "FDA CGMP, OSHA CO2 safety, hazmat transport, supplier qualification.", "Reduces operational, regulatory, and incident risk.", "Regulators, QA teams, CGA practices."],
    ], [1.15 * inch, 2.1 * inch, 2.15 * inch, 2.05 * inch]),
]))

pages.append(page("11. Direct Competitor Set and Relevancy Ranking", [
    p("The competitive set includes national gas majors, beverage gas specialists, regional distributor networks, propane telemetry providers, and asset-light gas-supply managers. Relevancy is based on overlap with multi-location, technology-enabled gas supply orchestration."),
    tbl([
        ["Rank", "Peer / archetype", "One-line business description", "Relevancy", "Reason"],
        ["1", "EspriGas-style platform", "Asset-light network manager providing one contact, one invoice, supplier routing, telemetry, and multi-gas service.", "High", "Closest match to the specified model."],
        ["2", "Airgas / Air Liquide", "National gas supplier with branch network, medical, industrial, beverage, and specialty gases.", "High", "Direct alternative for enterprise customers needing broad gases and national support."],
        ["3", "Linde", "Global industrial gas major with beverage CO2, telemetry, and broad supply modes.", "High", "Scale, production, and telemetry create strong competitive overlap."],
        ["4", "NuCO2 / beverage CO2 specialists", "Focused beverage carbonation and CO2 delivery providers for restaurants and convenience channels.", "High", "Strong QSR/beverage overlap, narrower multi-gas breadth."],
        ["5", "Regional distributor groups", "Local/regional gas distributors with route density and customer relationships.", "High", "Fulfillment partners and competitors for local accounts."],
        ["6", "Meritus Gas Partners", "Network of independent gas distributors serving medical, industrial, and specialty gas markets.", "Medium", "Roll-up model creates regional density but less pure asset-light orchestration."],
        ["7", "Messer / Matheson", "Industrial gas suppliers with packaged, bulk, medical, and specialty gases.", "Medium", "Broad gases, less focused on outsourced multi-distributor orchestration."],
        ["8", "Tank Utility / Otodata", "Telemetry platforms for propane and tank monitoring.", "Medium", "Important technology substitutes/partners, not full gas supply managers."],
    ], [0.35 * inch, 1.25 * inch, 2.45 * inch, 0.7 * inch, 2.75 * inch], font_size=6.75),
]))

pages.append(page("12. Competitive Landscape: Where Each Archetype Wins", [
    tbl([
        ["Archetype", "Where it wins", "Where it is weaker"],
        ["Gas majors", "Production scale, supply security, technical expertise, national accounts, broad gas catalog.", "May be less flexible with local suppliers; can have channel conflict and complex account bureaucracy."],
        ["Regional distributors", "Local delivery density, service relationships, emergency response, flexible execution.", "Limited national coverage, fragmented billing, inconsistent technology."],
        ["Asset-light platforms", "Multi-location simplicity, supplier optionality, consolidated billing, centralized management, technology layer.", "Depends on partner execution; must prove SLA control without owning assets."],
        ["Beverage specialists", "QSR and restaurant expertise, CO2 systems, safety familiarity, route density.", "Often narrower outside CO2/nitrogen beverage use cases."],
        ["Propane telemetry vendors", "Sensor hardware, estimated fill dates, routing analytics, customer apps.", "Technology layer only; not a complete multi-gas supply chain manager."],
        ["Distributor roll-ups", "Regional density, branch ownership, cross-selling opportunities.", "Capital-intensive; integration and standardization challenges."],
    ], [1.55 * inch, 3.0 * inch, 2.9 * inch]),
]))

pages.append(page("13. Competitive Heat Map", [
    tbl([
        ["Player / archetype", "Gas breadth", "Geographic presence", "Technology depth", "Model fit"],
        ["Asset-light gas SCM platform", "Broad", "National through partners", "Medium-High", "Highest fit for network orchestration and enterprise simplification."],
        ["Airgas / Air Liquide", "Broad", "National / global", "Medium", "Strong direct supplier alternative with owned network."],
        ["Linde", "Broad", "National / global", "Medium", "Strong supply and telemetry, especially beverage and bulk applications."],
        ["Messer / Matheson", "Broad", "National / regional", "Medium", "Broad gas and technical capability; less platform-led positioning."],
        ["NuCO2 / BevCarb specialists", "Narrow-Medium", "National / regional", "Medium", "High beverage fit, narrower healthcare/industrial breadth."],
        ["Regional distributors", "Medium-Broad", "Local / regional", "Low-Medium", "Critical fulfillment layer; inconsistent enterprise support."],
        ["Meritus-style distributor networks", "Broad", "Multi-regional", "Low-Medium", "Combines local distributors; more asset-heavy than platform model."],
        ["Tank Utility / Otodata", "Narrow", "National / global tech", "High", "Telemetry layer; partner or substitute for platform's monitoring module."],
    ], [1.45 * inch, 1.15 * inch, 1.45 * inch, 1.15 * inch, 2.25 * inch], font_size=6.8),
]))

pages.append(page("14. Platform Positioning: Why Customers Buy", [
    bullet("Multi-location customers buy administrative simplicity: one contact, one invoice, one escalation path, and standard operating procedures across markets."),
    bullet("QSR and beverage buyers value avoiding fountain drink outages, CO2 emergencies, and store-manager time spent managing local vendors."),
    bullet("Healthcare and dental buyers value continuity, documentation, medical gas supplier qualification, and centralized oversight across clinics or facilities."),
    bullet("Industrial buyers value uptime at distributed sites, especially where propane or cylinder runouts stop operations or require costly emergency service."),
    bullet("Procurement and finance teams value consolidated invoices, usage analytics, vendor reduction, and the ability to benchmark site-level consumption."),
    p("Differentiation test", "SectionTitle"),
    p("The platform must prove that it reduces total cost to serve, not only unit gas price. Hard-dollar value comes from fewer runouts, fewer emergency deliveries, right-sized inventory, lower AP workload, reduced leakage, and better supplier performance management."),
]))

pages.append(page("15. Technology Stack and Data Moat", [
    tbl([
        ["Technology component", "Role", "Potential moat / risk"],
        ["Customer portal", "Ordering, ticketing, account view, location hierarchy, invoice access.", "Sticky if embedded in customer workflows; weak if only a web order form."],
        ["Telemetry dashboard", "Tank levels, alerts, usage rates, leak/anomaly detection, reorder thresholds.", "Strong if integrated into replenishment and billing; weaker if hardware-agnostic data is easy to replicate."],
        ["Supplier routing engine", "Assigns orders by ZIP, gas, grade, SLA, price, availability, and performance.", "Potential data moat if performance history improves routing."],
        ["Billing engine", "Consolidates distributor charges into customer invoices and site-level reporting.", "High switching friction if accurate and integrated with customer AP/ERP."],
        ["EDI / API integrations", "Connects customer procurement systems and supplier order systems.", "Creates operational lock-in and lowers manual exceptions."],
        ["Analytics layer", "Usage benchmarking, tank sizing, demand forecasts, cost leakage, supplier scorecards.", "Differentiates if insights trigger measurable savings."],
    ], [1.45 * inch, 3.0 * inch, 3.0 * inch]),
]))

pages.append(page("16. End-Market Deep Dive: QSR / Beverage", [
    p("QSR, restaurant, convenience, brewery, and beverage customers use CO2 for carbonation and nitrogen/beer gas blends for draft systems and nitro products. The operational pain is highly visible: a gas runout can stop beverage sales, damage customer experience, and create urgent service needs."),
    p("EPA notes food and beverage accounts for approximately 70% of domestic demand for CO2 supplied as a byproduct of ethanol production. OSHA highlights that CO2 beverage systems also create safety risk because CO2 is colorless, odorless, denser than air, and can accumulate in below-grade areas."),
    p("Platform opportunity", "SectionTitle"),
    bullet("Use telemetry to monitor tank levels, detect abnormal usage, and trigger proactive refill scheduling."),
    bullet("Standardize store-level ordering and reduce manager dependency through automated replenishment."),
    bullet("Consolidate billing and reporting across franchisee, corporate, and multi-brand structures."),
    bullet("Provide safety and storage guidance, especially for bulk CO2 installations where local monitoring rules may apply."),
]))

pages.append(page("17. End-Market Deep Dive: Healthcare, Dental, and Veterinary", [
    p("Healthcare, dental, and veterinary facilities consume medical oxygen, nitrous oxide, nitrogen, medical CO2, helium, and specialty mixtures. Reliability and documentation are critical because these gases can support procedures, sedation, respiratory therapy, laboratory workflows, and patient care."),
    p("FDA's 2024 final rule establishes medical-gas-specific CGMP regulations under 21 CFR Part 213, reflecting how medical gases are manufactured, packaged, labeled, stored, and distributed. This increases the importance of supplier qualification, documentation, labeling, and traceability."),
    p("Platform opportunity", "SectionTitle"),
    bullet("Centralize supplier qualification and documentation across multi-site healthcare organizations."),
    bullet("Provide one billing and account-management process for clinics operating in multiple local distributor markets."),
    bullet("Monitor usage and inventory where telemetry is feasible, while preserving compliance-specific records for medical-grade gases."),
    bullet("Support procurement teams that lack gas-specific expertise but need reliable service and documentation discipline."),
]))

pages.append(page("18. End-Market Deep Dive: Industrial and Propane", [
    p("Industrial and commercial customers use propane for heat, forklifts, generators, temporary sites, hospitality, and unmanned operations, while also using oxygen, acetylene, nitrogen, CO2, helium, and specialty gases for welding, fabrication, processing, labs, and maintenance."),
    p("Propane distribution economics are operationally sensitive. The 2024 propane survey shows distributors prioritizing efficiency, with 69% seeking better delivery planning and 68% seeking fewer but larger deliveries. Tank monitoring is still underpenetrated, with many dealers monitoring only a small share of tanks."),
    p("Platform opportunity", "SectionTitle"),
    bullet("Deploy or ingest tank monitor data to improve fill timing, reduce emergency calls, and manage remote sites."),
    bullet("Help regional distributors serve national enterprise accounts without building national sales and billing infrastructure."),
    bullet("Benchmark consumption across locations and identify abnormal usage, leaks, or poor tank sizing."),
]))

pages.append(page("19. Value Creation Levers", [
    tbl([
        ["VCL or Risk", "Title", "Description"],
        ["VCL", "Supplier network density", "A dense qualified distributor network allows the platform to route orders by service quality, gas type, and availability, improving enterprise coverage without owning branches."],
        ["VCL", "Telemetry-led replenishment", "Remote tank data converts gas ordering from reactive store requests into automated replenishment, reducing runouts, emergency deliveries, and customer disruption."],
        ["VCL", "Consolidated billing", "One invoice and location-level reporting reduce AP workload, improve spend visibility, and make multi-site gas procurement easier to control."],
        ["VCL", "Usage analytics", "Site-level consumption benchmarking can identify leaks, over-storage, abnormal usage, and right-sizing opportunities that improve gross retention and savings credibility."],
        ["VCL", "Healthcare compliance workflow", "Supplier qualification, documentation, and medical gas records can create differentiated value for dental, veterinary, and clinic networks."],
        ["VCL", "Distributor partnership flywheel", "Suppliers gain national-account volume while the platform gains better market coverage, producing scale benefits without direct fleet ownership."],
        ["VCL", "Cross-sell gas breadth", "Starting with CO2 or propane can expand into nitrogen, oxygen, helium, and nitrous oxide, raising wallet share per location."],
    ], [0.85 * inch, 1.55 * inch, 5.05 * inch]),
]))

pages.append(page("20. Key Risks", [
    tbl([
        ["VCL or Risk", "Title", "Description"],
        ["Risk", "Supplier execution leakage", "The platform owns the customer promise but not every truck, driver, or branch, so poor local execution can damage enterprise relationships."],
        ["Risk", "Major supplier bypass", "Large gas majors may sell directly to enterprise accounts, limiting the platform's margin if customers prioritize owned supply over network orchestration."],
        ["Risk", "Telemetry interoperability", "Multiple sensor brands, tanks, gases, and supplier systems can fragment data unless the platform maintains strong integration and device governance."],
        ["Risk", "CO2 supply disruption", "CO2 supply depends heavily on ethanol, ammonia, and hydrogen co-product streams, so regional outages can cause allocation, price spikes, and service failures."],
        ["Risk", "Helium allocation exposure", "Helium scarcity can force supplier rationing, making customer prioritization and alternative sourcing critical for MRI, lab, and specialty users."],
        ["Risk", "Medical gas compliance", "FDA CGMP, labeling, and supplier qualification requirements create risk if documentation, roles, and quality ownership are unclear."],
        ["Risk", "Safety and incident liability", "CO2 asphyxiation, cylinder handling, propane, and hazmat delivery risks can create reputational and legal exposure despite asset-light positioning."],
    ], [0.85 * inch, 1.55 * inch, 5.05 * inch]),
]))

pages.append(page("21. Operating KPIs and Diligence Questions", [
    tbl([
        ["KPI / diligence area", "What to examine", "Why it matters"],
        ["Supplier density", "Qualified suppliers per ZIP, gas, delivery mode, and SLA band.", "Measures resilience and routing optionality."],
        ["Runout rate", "Runouts per 1,000 locations before and after telemetry / managed replenishment.", "Direct proof of operational value."],
        ["Emergency delivery share", "Percent of orders delivered outside normal route cadence.", "Indicates planning quality and cost leakage."],
        ["Billing accuracy", "Invoice disputes, credit memos, and AP cycle time.", "Tests back-office reliability and switching friction."],
        ["Telemetry coverage", "Share of monitored tanks by gas, customer, and location type.", "Determines data depth and automation potential."],
        ["Gross retention", "Logo retention and location retention by end market.", "Shows stickiness of service model."],
        ["Supplier SLA performance", "On-time delivery, fill accuracy, incident rates, and escalation resolution.", "Validates control of asset-light execution."],
        ["Compliance readiness", "FDA medical gas documentation, supplier qualifications, OSHA/CO2 safety processes.", "Reduces downside in regulated end markets."],
    ], [1.55 * inch, 2.9 * inch, 3.0 * inch], font_size=6.9),
]))

pages.append(page("22. Investment Perspective", [
    p("The asset-light gas SCM platform is attractive when it becomes the operating system between fragmented local distributors and enterprise buyers. The best version of the model combines distributor density, customer-facing simplicity, automated replenishment, billing accuracy, and analytics that lower total cost rather than merely reselling gas."),
    p("What we like", "SectionTitle"),
    bullet("Recurring, mission-critical demand across beverage, healthcare, industrial, and propane use cases."),
    bullet("Low capital intensity versus gas majors and distributor roll-ups, if supplier partnerships remain durable."),
    bullet("Clear operational ROI from fewer runouts, fewer emergency deliveries, right-sized tanks, lower AP burden, and better site visibility."),
    bullet("Potential to expand wallet share by adding gases, telemetry, compliance workflows, and analytics across an existing location base."),
    p("What to underwrite carefully", "SectionTitle"),
    bullet("Whether technology is truly proprietary and operationally embedded, or mostly a branded dashboard over commodity supplier processes."),
    bullet("Supplier power, margin durability, service-level enforceability, and customer propensity to bypass the platform at scale."),
]))

pages.append([
    p("23. Bottom-Line Conclusions and Source Tiers", "PageTitle"),
    p("This sector should be viewed as vertical supply-chain orchestration, not traditional industrial gas production. The platform's strategic role is to simplify fragmented gas procurement for enterprise customers while using local distributors for fulfillment. The strongest opportunity is where customers have recurring multi-location gas needs, meaningful runout costs, complex billing, and limited in-house gas expertise."),
    p("The most compelling wedge is beverage CO2 or propane telemetry because the operational ROI is tangible and measurable. Healthcare and dental add compliance-driven stickiness, while helium and specialty gases add resilience value during allocation periods. The key diligence question is whether the platform can control supplier execution tightly enough to own the customer relationship without owning the physical network."),
    p("Tier 1 - Highest Confidence", "SectionTitle"),
    bullet("EPA Carbon Dioxide Supply Chain Profile: CO2 sources, risk rating, food/beverage demand share, transport, production, and supply vulnerabilities. https://www.epa.gov/system/files/documents/2023-03/Carbon%20Dioxide%20Supply%20Chain%20Profile.pdf"),
    bullet("FDA Final Rule on medical gas CGMP, certification, postmarketing reporting, and labeling under 21 CFR Part 213. https://www.fda.gov/about-fda/economic-impact-analyses-fda-regulations/current-good-manufacturing-practice-certification-postmarketing-safety-reporting-and-labeling-0"),
    bullet("OSHA Hazard Information Bulletin on CO2 asphyxiation risks in stationary low-pressure CO2 supply systems. https://www.osha.gov/publications/hib19960605"),
    bullet("USGS Mineral Commodity Summaries 2025 for helium market data, applications, production, and pricing. https://www.usgs.gov/publications/mineral-commodity-summaries-2025"),
    p("Tier 2 - High Confidence", "SectionTitle"),
    bullet("EspriGas website pages on supplier network, 4,000+ supply locations, one contact/one invoice model, EspriVision telemetry, beverage, medical, and industrial offerings. https://esprigas.com"),
    bullet("Linde beverage gas page on beverage-approved CO2, supply facilities, remote telemetry, inventory, pressure, flow-rate, and historical demand visibility. https://www.lindeus.com/industries/food-and-beverage/beverages"),
    bullet("Tank Utility and Superior Propane pages on tank monitoring, estimated fill dates, automatic delivery, portal access, and customer alerts. https://tankutility.com and https://www.superiorpropane.com"),
    bullet("BPN / Gray Gray & Gray 2024 Propane Industry Survey for propane distributor technology, efficiency, fleet planning, and tank monitor adoption. https://bpnews.com/news/2024-national-propane-industry-survey-results-released-gray-gray-gray"),
    p("Tier 3 - Medium Confidence", "SectionTitle"),
    bullet("CGA medical gas standards and trade sources used as supporting context for supplier qualification and operational norms."),
    p("Tier 4 - Avoided", "SectionTitle"),
    bullet("No Wikipedia, unverified forums, or paid market-research sizing estimates were used for conclusions or sizing."),
])

for pg in pages:
    story.extend(pg)

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(f"Wrote {OUTPUT_FILE}")
