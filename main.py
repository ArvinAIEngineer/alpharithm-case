import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- KNOWLEDGE BASE ---
# This is the information the AI will use to answer questions.
# CORRECTED: Now includes all case studies provided.
KNOWLEDGE_BASE = """
Alpharithm Technologies – Case Studies

# Banking - Enterprise Data Warehouse and Analytics

&lt;img&gt;alpharithm logo&lt;/img&gt;

**About the client:** Central Bank of India is a leading bank which was established in 1911, Central Bank of India was the first Indian commercial bank which was wholly owned and managed by Indians.

**Business Challenges:** The client wanted to gain better insights from their customer data. setup a comprehensive data warehousing platform to enable publishing standard KPI’s on Dashboards and perform Analytics. Existing reports were built on top of an ODS and did not cover all the data requirements. Daily KPI’s monitoring and preparation of statutory reports were time consuming and many times inaccurate. Bank then decided to implement a comprehensive Datawarehouse for their reporting and analytical needs

**Solution:** The proposed solution consisted of IBM IIAS appliance into which data was extracted from 17+ applications using IBM InfoSphere Information Server. IBM CDC was implemented between the Core Banking Application and Staging areas. Jobs were designed to meet business defined SLAs. Cognos was used for Reporting and Predictive analytics. Approximately 12 Data Marts and 76 Dashboards were created. The Data Dictionary and Data lineage options were recommended to enable the business user to track the journey of data from reports all the way to the source systems, thereby increasing the trust in Analytics.

**Benefits:**
*   Improved Monitoring of Business: KPI based dashboards allowing day to day monitoring of critical KPI’s
*   Improved Governance and Trust: Significantly increased the process and trust that the users had in the IT systems and Data.
*   Regulatory Reports generation: Improved ease of generation of reports based on regulatory demands (Standard and Ad-hoc)
*   Improved Customer 360 View – Comprehensive data of customer and transactions has increased the quality of Analytics, allowing for better targeting of customers

**Technology:** IBM Information Server ( Datastage and QualityStage), IBM Db2 Warehouse, IBM IIAS, IBM Change Data Capture, Information Governance Catalog / Glossary (IGC), IBM Cognos, Oracle, SQL Server

&lt;img&gt;Central Bank of India logo with text "सेन्ट्रल बैंक ऑफ इंडिया" and "Central Bank of India"&lt;/img&gt;
<footer>2023 Alpharithm Technologies</footer>

---


## Page 3

&lt;img&gt;Blue square logo&lt;/img&gt; Insurance - Data Lake ,Analytics & Integration &lt;img&gt;Alpharithm logo&lt;/img&gt;

**About the client:** Top mid market General Insurance company in India providing Health, Motor, and Commercial Insurance.

**Business Challenges:** Siloed applications, no central data repository, hence business users were finding it difficult to generate their day-to-day reports. They had to perform considerable manual work for generating key insurance specific KPI's. Customer data contained duplicate records and had various types of data issues. Additionally, Salesforce was being implemented across all the major functions to provide Customer 360 to Customer Service and for tracking Lead to Customer conversion. This needed not only Unique Identification of Customers but also accurate transactional data. In the absence of a single repository of data none of the organizational requirements could be met.

**Solution:** Data Lake was designed to capture data from across 30+ applications and bring them to the central repository. A combination of IBM CDC for Core Application and IBM Datastage for other applications was implemented. Alpharithm accelerator SiNGL was used to create Unique Customer Repository with adequate data cleansing and normalization. Data from Data Lake was integrated with Salesforce using REST API's and is maintained on T-1 basis. Tableau will be used for Analytical and Dashboard reporting.

**Benefits:**
1) **Real-time Visibility:** Near real-time availability of data from various source systems in Data lake
2) **Improved Customer Service :** Customer Support equipped with up-to-date information to handle customer queries
3) **Ease of Operational Reporting generation :** Single Repository helping generation of day-to-day Operational reports
4) **Performance Driven KPI's :** Customer is in the process of implementing business specific KPI based reporting to help measure business health

**Technology:** IBM CDC, IBM DataStage and IBM QualityStage, SiNGL(MDM), IBM Db2 Warehouse, IBM Reference Data Management, Oracle, SQL Server, MySQL

&lt;img&gt;Universal Sompo General Insurance Co. Ltd. logo&lt;/img&gt;
Suraksha, Hamesha Aapke Saath

<footer>2023 Alpharithm Technologies</footer>

---


## Page 4

&lt;img&gt;Blue square logo&lt;/img&gt; Microfinance - ODS &lt;img&gt;Alpharithm logo&lt;/img&gt;

**About the client:** Ujjivan is a leading Microfinance company in India and have recently been awarded the Small bank license by the Reserve Bank of India.

**Business Challenges:** The client wanted to gain better insights from their customer data. Multiple legacy systems and complex IT infrastructure meant that they were not able to glean timely insights. In addition, the new banking license necessitated appropriate Data Governance frameworks to meet future compliance requirements and to increase the business trust in the underlying data and information systems.

**Solution:** The proposed solution using IBM InfoSphere will connect to various databases, capture changes at source (CDD) and perform complex ETL and populate the Data mart. The Change Data Delivery option reduces the number of records moved/processed on the ETL server and help meet the business defined SLAs. Cognos and SPSS were used for Reporting and Predictive analytics. The Data Dictionary and Data lineage options were recommended to enable the business user to track the journey of data from reports all the way to the source systems, thereby increasing the trust in Analytics.

**Benefits:**
*   **Achieved business SLAs:** With CDD enabled, parallel data transformation, the ETL processing time was reduced from 16 hours to 4 hours.
*   **Improved Governance and Trust:** Significantly increased the process and trust that the users had in the IT systems and Data.
*   **Improved Productivity:** With less data issues to deal with, the business spends more time in analyzing data and gleaning insights
*   **Future Proof Investment:** Common Meta data layer enables seamless integration with future tools and capabilities such as Data Quality, MDM and Smart Archiving
*   **Increased up-sell/cross-sell opportunities** – The timely delivery of data into the mart for reporting and the predictive models enables substantial increase in revenue and paves way for future growth

**Technology:** IBM Information Server (IBM Datastage and IBM QualityStage), Information Governance Catalog / Glossary (IGC), IBM Change Data Delivery.

&lt;img&gt;Ujjivan logo&lt;/img&gt;

<footer>2023 Alpharithm Technologies</footer>

---


## Page 5

&lt;img&gt;Financial Services – Data Lake&lt;/img&gt;
&lt;img&gt;alpharithm logo&lt;/img&gt;

**About the client:** One of the Leading payment solutions provider in India

**Business Challenges:** Client had undertaken an initiative to implement Cloudera based Data Lake and were facing huge challenges in the acquisition of data from their mainframe applications based on Z/OS as well as from dozens of satellite applications based on Oracle. Z/OS being proprietary in nature did not allow for easy access of data. Client needed a sophisticated solution to extract data in real-time from not only mainframes from also various applications and store them in Cloudera. Client wanted to leverage native Hadoop capabilities for business intelligence reporting as well as for Predictive Analytics

**Solution:** IBM CDC was used to extract changed data from mainframes as well as from Oracle RDBMS, these data were then fed to a Kafka cluster and then posted to Cloudera. IBM BigIntegrate jobs were used to process data on Cloudera to generate relevant output data for Business Intelligence and Analytics. As part of the engagement governance catalog was also configured to track technical assets and provide end-to-end lineage.

**Benefits:**
1) **Real Time Visibility:** Real-time replication of data from various source systems to Cloudera (Data Lake)
2) **End-to-End Automation:** Leveraged native Hadoop capabilities through IBM products to process data to perform transformation and speed up processing of terabytes of data
3) **Streamlined MIS :** Enabled day to day operational reporting
4) **Enabled Analytics:** Supported downstream Analytics Users for model building with near real-time data

**Technology:** IBM CDC (zOS and Oracle based applications), IBM BigIntegrate for Hadoop (DataStage, QualityStage, Governance Catalog) , Cloudera, Kafka, Oracle

&lt;img&gt;SBI card logo&lt;/img&gt;

<footer>2023 Alpharithm Technologies</footer>

---


## Page 6

&lt;img&gt;Blue square logo&lt;/img&gt; Banking - Master Data Management & Data Governance &lt;img&gt;Alpharithm logo&lt;/img&gt;

**About the client:** ICICI Bank one of largest private Bank in India.

**Business Challenges:** ICICI Bank has the vision to persist and deepen its customer knowledge with the goal to improve customer engagement and experience by having accurate customer data across all the channels. Current customer information was distributed across two applications one for Retail and other for Corporate, hence any customer interlinkages could not be inferred. There were considerable number of duplicate records leading to improper offers across channels. ICICI wanted to implement a comprehensive MDM that will serve as a Single Repository of Customer data and provide consistent data across all the channels.

**Solution:** Data from 70+ applications was integrated with IBM MDM . Data was standardized, cleansed and loaded into the MDM hub using IBM Datastage jobs. Complex validation rules were implemented in the ETL Jobs for cleansing of data. Probabilistic Matching algorithms were configured to identify unique, duplicate and suspect records. Data Stewardship processes were implemented to arrive at proper customer Golden record which as made available to all the consuming applications vis REST API through APIGEE middleware. Watson Knowledge Catalog provides Data Lineage from Source through ETL to Target.

**Benefits:**
1) **One-Bank One-Id:** Unique Identification of Customer across various line of business, leading to Single Source of Truth across On-boarding and Channels applications
2) **Improved Customer Experience:** Golden Profile view enabling effective Up-sell/Cross-Sell opportunities
3) **Centralized Consent Management:** Unambiguous consent capture for a Golden Profile across various LOB's
4) **Faster identification of new opportunities & risks:** Advanced ‘Householding’ for accurate customer scoring, based on significant customer events.

**Technology:** MDM AE (Advanced Edition) on OpenShift environment. IBM Cloud Pack Cartridge Information Server on OpenShift , IBM Watson Knowledge Catalog, IBM Consent Management, IBM Reference Data Management, APIGEE Middleware, Vertica, Oracle EXADATA, Oracle, SQL Server

&lt;img&gt;ICICI Bank logo&lt;/img&gt;

<footer>2023 Alpharithm Technologies</footer>

---


## Page 7

&lt;img&gt;Blue square logo&lt;/img&gt; Banking - Master Data Management &lt;img&gt;Alpharithm logo&lt;/img&gt;

**About the client:** DHFL is the 3rd largest Mortgage lender in India.

**Business Challenges:** The client had embarked on a Data Migration journey moving from old Legacy systems to modern applications such as ERP and CRM for their Lending and Deposits business. The master and reference data is of very poor data quality. Migration of the data as is into the new applications would result in majority of the records being rejected. A pre-requisite to this migration is cleansing the master data and creating a single view of customer across the enterprise.

&lt;img&gt;DHFL logo with "Changing Rules Changing Lives" tagline&lt;/img&gt;

**Solution:** Data from on-prem was migrated to the MDM Cloud on SoftLayer environment, standardized, cleansed and loaded into the MDM hub. Dedup matching algorithms were written to identify unique, duplicate and suspect records. Finally Unique Enterprise IDs were created for customers and then mapped to the transaction data based on which the data migration to ERP and CRM was completed.

**Benefits:**
1) **Faster time to value:** The proposed solution on cloud enabled them to create single view of customer within 2 months.
2) **Reduced overall cost:** Reduced Upfront payment as they could buy initially for 6 months and then extend on a monthly basis as per the project demand
3) **Improved marketing effectiveness** – With single customer view, the campaign effectiveness and response rates will be improved.
4) **Increased up-sell/cross-sell opportunities** – With single view across Loans and Deposits, the client could target specific, personalized products to existing customer base

**Technology:** MDM AE (Advanced Edition) on IBM SoftLayer Cloud, IBM Datastage and IBM QualityStage

<footer>2023 Alpharithm Technologies</footer>

---


## Page 8

&lt;img&gt;Blue square logo&lt;/img&gt; Other Non-Financial Clients in India &lt;img&gt;Alpharithm logo&lt;/img&gt;

<table>
  <tr>
    <td>&lt;img&gt;SANOFI logo&lt;/img&gt;</td>
    <td>&lt;img&gt;SONY PICTURES NETWORKS logo&lt;/img&gt;</td>
    <td>&lt;img&gt;TITAN logo&lt;/img&gt;</td>
  </tr>
  <tr>
    <td>IBM MDM, IBM Datastage and Qualitystage, IBM BPM, SQL Server</td>
    <td>IBM MDM, IBM Datastage and Qualitystage, IBM IIB</td>
    <td>IBM Datastage and Qualitystage, IBM Netezza, Hortonworks, AWS Redshift, AWS Dynamodb, AWS API Gateway, IBM Db2, SQL Server</td>
  </tr>
  <tr>
    <td>&lt;img&gt;Government of Tamil Nadu logo&lt;/img&gt;</td>
    <td>&lt;img&gt;Government of Odisha logo&lt;/img&gt;</td>
    <td>&lt;img&gt;Government of Rajasthan logo&lt;/img&gt;</td>
  </tr>
  <tr>
    <td>IBM MDM, IBM Datastage and Qualitystage, SQL Server, IBM Db2, Oracle,</td>
    <td>IBM MDM, IBM Datastage and Qualitystage, SQL Server, IBM Db2</td>
    <td>IBM MDM, IBM Datastage and Qualitystage, SQL Server, IBM Db2, Oracle</td>
  </tr>
</table>

<footer>2023 Alpharithm Technologies</footer>

---


## Page 9

&lt;img&gt;Blue square logo&lt;/img&gt; International Clients &lt;img&gt;Alpharithm logo&lt;/img&gt;

&lt;img&gt;Barclays logo&lt;/img&gt; &lt;img&gt;M&S logo with EST. 1884&lt;/img&gt; &lt;img&gt;Brakes logo with a green leaf icon and "a Sysco company" text&lt;/img&gt;
&lt;img&gt;NHS logo&lt;/img&gt; &lt;img&gt;Etisalat logo&lt;/img&gt; &lt;img&gt;Parkway Hospitals Singapore logo&lt;/img&gt;

&lt;img&gt;Blue square logo&lt;/img&gt; **Case Study – Pharma** &lt;img&gt;Alpharithm logo&lt;/img&gt;

**About the client:** One of the Largest European head quartered Pharma companies

**Business Challenges:** The client lacked visibility of consolidated payments made to Doctors. This is because the Doctor data is duplicated across different CRM and Data originating systems. To add to this a Doctor can be associated with multiple hospitals and clinics. In addition the same Doctor is seen by different Sales Reps, each in turn creating new Doctor Id for every thereby duplicating the data. This led to several operational staff engaged in manually validating and de-duplicating the data which increased the cost of operations, increased risk and reduced the efficiency. In addition, they had to comply with the Transparency Act.

**Solution:** Data was extracted from Sanofi’s source systems including CRM and then validated, cleansed, deduplicated, matched and loaded into a Master data hub called the Doctors Hub. This hub would contain the Golden record for each Doctor and their association with Hospitals. Master Data Governance process was established using a Workflow model to prevent data deterioration and ensure that the systems remained duplicate free. The Doctor Hub delivered Single version of truth and enabled accurate information sharing across the enterprise.

**Benefits:** *Circa 3 Million USD over 3 years*

*   **Deduplication of data:** 35% duplication was identified and removed from the existing database
*   **Spend Analysis:** Visibility into Doctors and associated spend
*   **Doctor Hub:** Golden record for each Doctor and link between disparate systems
*   **Compliance:** Met the regulatory requirements
*   **Information Governance:** Laid foundation to create Products and Distributor hubs in the future

**Technology:** MDM SE (Standard Edition) on Prem, Information Server, DB2

&lt;img&gt;SANOFI logo&lt;/img&gt;

<footer>© 2017 Alpharithm Technologies Pvt Ltd</footer>

---


## Page 3

&lt;img&gt;Blue square graphic&lt;/img&gt; **Case Study – Media** &lt;img&gt;alpharithm logo&lt;/img&gt;

**About the client:** Sony Pictures Networks is one of the largest Entertainment company in India with over 10 Satellite TV channels in multiple languages. Sony has grown rapidly both organically and inorganically.

**Business Challenges:** Sony has multiple media specific applications to manage the Customers, Titles, Episodes, Rights management and Broadcasting/Scheduling including SAP for Financial management. As a result master data is created and duplicated in multiple systems. This lead to Process issues, data, integration and reporting issues. Sony is also growing by acquisitions which further added to their data management challenges.

**Solution:** The solution involves creating a Platform that would deliver a Scalable and Distributable Integration Platform using Service Oriented Architecture whereby all applications can seamlessly exchange data/ information using homogeneous master data elements and reusable API’s. Within MDM, multiple master data domains such as Customer, Title, Episodes, Deals, General Ledger etc will be mastered.

**Benefits:** *Circa 20 Million USD over 3 years (projected)*

1) Revenue uplift: The Syndication team and Ad sales team would benefit from the new Integrated platform
2) Better Governance: Increased TAT Via automated workflows and better process management
3) Improved marketing effectiveness – With single customer view, the client will improved the campaign effectiveness and response rate

**Technology:** MDM CE (Collaborative Edition) on prem, Information Server, BPM and Integration Bus

&lt;img&gt;Sony Pictures Networks logo&lt;/img&gt;

<footer>© 2017 Alpharithm Technologies Pvt Ltd</footer>

---


## Page 4

&lt;img&gt;Blue square logo&lt;/img&gt; **Case Study – NBFC** &lt;img&gt;alpharithm logo&lt;/img&gt;

**About the client:** DHFL is the 3rd largest Mortgage lender in India.

**Business Challenges:** The client had embarked on a Data Migration journey moving from old Legacy systems to modern applications such as ERP and CRM for their Lending and Deposits business. The master and reference data is of very poor data quality. Migration of the data as is into the new applications would result in majority of the records being rejected. A pre-requisite to this migration is cleansing the master data and creating a single view of customer across the enterprise.

&lt;img&gt;DHFL logo with "Changing Rules Changing Lives" tagline&lt;/img&gt;

**Solution:** Data from on-prem was migrated to the MDM Cloud on SoftLayer environment, standardized, cleansed and loaded into the MDM hub. Dudupe matching algorithms were written to identify unique, duplicate and suspect records. Finally Unique Enterprise IDs were created for customers and then mapped to the transaction data based on which the data migration to ERP and CRM was completed.

**Benefits:** *Circa 8 Million USD over 3 years (projected)*

1) **Faster time to value:** The proposed solution on cloud enabled them to create single view of customer within 2 months.
2) **Reduced overall cost:** Without the Cloud option the client would have purchased the Perpetual licenses for at least 1 year. The cloud option meant that they could buy initially for 6 months and then extend on a monthly basis as per the project demand
3) **Improved marketing effectiveness** – With single customer view, the client will improved the campaign effectiveness and response rate
4) **Increased up-sell/cross-sell opportunities** – With single view across Loans and Deposits, the client could target specific, personalized products to existing customer base

**Technology:** MDM AE (Advanced Edition) on IBM SoftLayer Cloud

<footer>© 2017 Alpharithm Technologies Pvt Ltd</footer>

---


## Page 5

<header>Case Studies – Government</header>

&lt;img&gt;Alpharithm logo&lt;/img&gt;

**About the client:** These 3 clients represent three different states within India. Each State has several benefit schemes and service appx. 50 to 70 Million residents.

**Business Challenges:** Citizen demographic data and Benefits data was scattered across multiple departmental databases. Each database contained duplicate Citizen information leading to the same Citizen claiming benefits multiple times in a month resulting in Revenue leakage and poor Governance. The State department decided to embark on a Centralized Data Hub called SRDH to overcome these challenges and improve the benefits distribution process.

**Solution:** The solution for SRDH (State Resident Data Hub) involved extracting data from 13 departmental databases and deduping, matching and linking with the National Population Registry data and National ID (Aadhar) database. A unique record for each Citizen was created and relationships between family members were identified. The suspect records were sent back to governance team for field verification and further action.

**Benefits:** Circa 580 Million USD over 3 years (projected - for each State Department)

- State and National government bodies can now identify fraudulent benefits applications and claims, to minimize wasteful spending  
- Established a Clean, Authenticated and deduplication data repository for all the Residents of the State  
- Support State Government Departments in effective planning of welfare and development Schemes  
- Established the frameworks for effective monitoring of schemes  
- Enabled the transformation of service delivery through integrated service delivery Creation of a 360 degree profile of a resident  

**Technology:** MDM Standard Edition (SE) on prem, Information Server (DataStage and QualitySatge), Oracle Exadata, IBM Information Governance Catalog, IBM Information Analyzer

&lt;img&gt;Government of Rajasthan logo&lt;/img&gt;
Government of Rajasthan

&lt;img&gt;Government of Odisha logo&lt;/img&gt;
Government of Odisha

&lt;img&gt;Government of Tamil Nadu logo&lt;/img&gt;
Government of Tamil Nadu

# Case Studies – Leading Multi-brand Retailer and Manufacturer

**About the client:** Leading Retailer and Manufacturer in India known for leading brands in the area of Eyecare, Jewellery, Fashion Clothing, and Perfumes. Client has Pan India presence and leverage Analytics for their critical decision making.

**Business Challenges:** Client wanted a Single Vendor to manage all of their Analytical needs. They have complete IBM Analytics stack for core of their Data Management and Data Integration needs. They needed agility in delivering as per business needs as their business was growing exponentially. They also wanted to migrate to AWS stack for scalability.

**Solution:** We provided them a team of qualified resources who acted as an extended arm of the IT department and took over from the existing Vendor and helped stabilize the existing deployment. We managed the Administration of the following components:

1.  **IBM Information Server (On-prem and AWS Cloud):**
    *   a) Patching
    *   b) Monitoring
    *   c) Performance Improvement
    *   d) Housekeeping
    *   e) Helping in Backup and Recovery Process
2.  **HortonWorks:**
    *   a) Day to Day administration
    *   b) User Management
    *   3) Hbase Maintenance
    *   4) Hadoop Services maintenance
3.  **IBM Netezza :**
    *   a) Managing User Creation and access
    *   b) Creation of New Tables / Modification of Tables
    *   c) View Creation
    *   d) Performance Tuning of Queries and ensuring proper table design as per NZ best practices
    *   e) Regular Housekeeping
    *   f) Migrating data to AWS

**L2 and L3 Support**

*   Execution of BAU Jobs
*   Establish and Implement comprehensive framework for Exception handling and dealing with AWS Redshift Data Upload)
*   Fine Tuning of jobs to run within their stipulated times
*   Catering to new needs for ETL development across various lines of businesses for reporting purposes (designing new tables, Writing ETL routines to populate data)
*   Troubleshooting and fixing issues, coordinating with IBM for PMR’s raised

**Benefits:**

1)  **Timely Reporting:** Improved reporting across Lines of Businesses helping meet Reporting SLA’s
2)  **Operational Efficiency:** Improved automation of jobs, reduced manual intervention, optimum utilization of IT resources

**Technology:** IBM Information Server, IBM Netezza, HortonWorks, Tableau, AWS Redshift, AWS S3, AWS Dynamodb

Project: Enterprise Data Transformation – Centralized MDM and X360 Data Lake for Universal Sompo General Insurance (USGI)
About the Client:
Universal Sompo General Insurance (USGI) is a significant and unique player in the Indian insurance landscape, established as the nation's first public-private partnership in the general insurance industry. Its foundation is a strategic consortium of major financial institutions, including two nationalized banks (Allahabad Bank, Indian Overseas Bank), a private sector bank (Karnataka Bank Ltd), a major FMCG entity (Dabur Investment Corp), and a global insurance leader from Japan (Sompo Japan Nipponkoa Insurance Inc). This diverse parentage gives USGI a vast distribution network and a complex operational footprint, necessitating a highly robust and unified approach to data management to serve its diverse customer base effectively.

Business Challenges & Strategic Imperatives:
USGI is at a pivotal point in its growth, aiming to execute a fundamental shift from a product-focused to a customer-centric business model. However, this strategic vision is severely hampered by a deeply fragmented and complex data ecosystem.

Profound Data Fragmentation: Critical business data is siloed across an extensive and heterogeneous landscape of approximately 30 distinct applications. These include core insurance platforms like Genisys, specialized portals for agents and customers (Agency Portal, CSC Portal), various integration points (Banca Portal, Maruti Integration), and numerous other legacy and modern systems. This fragmentation makes it impossible to form a coherent, enterprise-wide view of any business entity.
Absence of a "Golden Record": The primary consequence of data fragmentation is the inability to create a single, authoritative, and trustworthy record—a "Golden Record"—for each customer, agent, or broker. The same customer may exist with different identifiers and inconsistent details across multiple systems, leading to operational inefficiencies, poor customer experience, and inaccurate reporting.
Inability to Execute a 360-Degree Customer Strategy: The core objective of integrating a complete customer view into their primary engagement platform, Salesforce, is currently unachievable. Without a 360-degree view encompassing every policy, claim, interaction, and relationship, the sales and service teams are operating with incomplete information, limiting their ability to personalize service, anticipate needs, and identify cross-sell or up-sell opportunities.
Impediments to Data-Driven Decision-Making: The leadership's goal to implement and monitor Key Performance Indicators (KPIs) for vital functions—such as Claims Processing, Corporate Planning, Finance, and Underwriting—is stymied by the lack of reliable, consolidated data. The effort required to manually aggregate and reconcile data for reporting is immense, and the resulting analytics lack the trust required to drive strategic decisions.
Lack of Formalized Data Governance: There is an absence of a formal, centralized data governance framework. This results in inconsistent data definitions, a lack of clear data ownership, and uncontrolled data quality issues (e.g., invalid characters, inconsistent reference codes like 'M' vs. '01' for gender, missing critical fields), which perpetuates the cycle of poor data.
The Envisioned Solution: A Three-Track Enterprise Data Foundation Initiative
Alpharithm proposes a multi-faceted, phased solution to systematically dismantle these data silos and construct a robust, centralized data foundation. The project is meticulously structured into three interconnected tracks, each building upon the last to deliver a comprehensive transformation.

Track A: Forging the Single Source of Truth – The Centralised Master Data Repository (MDM)
This foundational track is focused on creating the definitive "Golden Record" for USGI's core business entities: Customers, Agents, and Brokers.

Comprehensive Data Ingestion and Profiling: The process begins by connecting to all ~30 source applications via ETL (using IBM DataStage) to extract all instances of master data. This raw data is then subjected to rigorous profiling using IBM InfoSphere Information Analyzer to discover its structure, quality, and inherent inconsistencies.
Advanced Data Cleansing and Standardization: Using IBM InfoSphere QualityStage, the extracted data undergoes a multi-step cleansing process. This includes standardizing addresses, parsing names, correcting data types, and resolving formatting issues to prepare the data for matching.
Sophisticated Matching and Survivorship: The core of the MDM process involves applying a combination of deterministic (rule-based) and probabilistic (fuzzy logic) matching algorithms. These algorithms are fine-tuned to accurately identify duplicate and related records across the entire application landscape. Survivorship rules are then configured to intelligently merge the "best" attributes from multiple source records into a single, consolidated Golden Record.
Creation of the Universal Identifier (UCIC): Each resulting Golden Record is assigned a new, persistent Unique Customer Identification Code (UCIC). This UCIC will become the master key for that entity across the entire USGI enterprise, providing a definitive way to link all related data.
Centralizing Reference Data (RDM): In parallel, IBM Reference Data Management (RDM) will be implemented to consolidate and govern reference data sets (e.g., product codes, state lists, vehicle models). This ensures that all applications use a standardized set of codes, eliminating a major source of data inconsistency.
Empowering Data Stewards: The solution includes the deployment of Alpharithm's SINGL accelerator, a user-friendly interface designed to streamline data stewardship activities. This will empower USGI's newly established team of Data Stewards to review match results, resolve suspect records, and manage the ongoing governance of the master data.
Track B: Building the Contextual Hub – The Enterprise Data Lake (X360)
With the master data foundation established, this track focuses on consolidating all related transactional data to build rich, contextual, 360-degree views.

Transactional Data Aggregation: ETL processes will extract a wide array of transactional data—including Policies, Claims, Beneficiaries, Transactions, and Commission details—from all relevant source systems. This includes a one-time load of 8 years of historical data to provide deep historical context.
Linking and Co-relation: The ingested transactional data is persisted in the X360 Data Lake, built on a scalable IBM Db2 database. The crucial step here is linking every transactional record to its corresponding master record from the MDM Hub using the UCIC. This co-relation is what transforms raw data into a meaningful, interconnected web of information.
Constructing 360-Degree Views: The linked data is then structured into pre-defined, business-centric analytical views. These views, such as Customer360, Agent360, Broker360, and Policies360, aggregate all relevant information for a given entity, providing an at-a-glance, comprehensive profile.
Track C: Operationalizing Intelligence – X360 and Salesforce Integration
This final track focuses on delivering the value created in the first two tracks directly into the hands of the end-users by deeply integrating the X360 Data Lake with Salesforce.

Seamless Data Publication to Salesforce: A dedicated, continuous ETL process is engineered to read the curated 360-degree views from the X360 database.
Data Model Mapping and Transformation: This data is then transformed and meticulously mapped to the specific objects and data models within USGI's Salesforce instance, ensuring that information like "Contact360" and "Policies360" is presented natively within the CRM interface.
Empowering the Front Line: By continuously feeding this rich, reliable, and holistic data into Salesforce, the solution empowers sales and service teams with unprecedented insight. They will be able to view a customer's entire policy history, claim status, and relationships directly within the CRM, enabling a new level of proactive and personalized engagement.
Anticipated Business Transformation & Benefits:

Achieving True Customer-Centricity: The project will directly enable USGI's core strategic goal by embedding a complete, trusted 360-degree view of the customer into the primary system of engagement, Salesforce. This will transform customer interactions from transactional to relational.
Radical Improvement in Operational Efficiency: Automating the consolidation and cleansing of data from 30 systems will eliminate countless hours of manual reconciliation, reduce data-related errors in downstream processes, and provide a single, reliable source for all business operations.
Unlocking High-Value Analytics and Insights: The centralized and cleansed data in the X360 lake will become the trusted source for all business intelligence and analytics. This will enable the accurate tracking of KPIs, the development of predictive models, and the uncovering of new business insights.
Significant Enhancement of Cross-Sell/Up-Sell Revenue: With a complete view of each customer's portfolio and history, sales teams can intelligently identify gaps and propose relevant new products, driving significant revenue growth.
Establishment of a Lasting Data Governance Culture: Beyond the technology, the project establishes the processes and roles (i.e., Data Stewards) necessary for a sustainable data governance framework, ensuring that data remains a trusted, high-quality asset for years to come.
Technology Stack:

Data Integration & ETL: IBM InfoSphere DataStage
Data Quality, Cleansing & Matching: IBM InfoSphere QualityStage & IBM InfoSphere Information Analyzer
Master Data & Stewardship: IBM MDM framework complemented by Alpharithm's SINGL Accelerator
Reference Data Governance: IBM Reference Data Management (RDM)
Database & Data Lake Platform: IBM Db2
Primary Consuming Application (CRM): Salesforce

Annexure 1: Case Studies
31.1 Case Study #1: NBFC (MDM)

About the client: DHFL is the 3rd largest Mortgage lender in India.
Business Challenges: The client had embarked on a Data Migration journey moving from old Legacy systems to modern applications such as ERP and CRM for their Lending and Deposits business. The master and reference data is of very poor data quality. Migration of the data as is into the new applications would result in a majority of the records being rejected. A pre-requisite to this migration is cleansing the master data and creating a single view of the customer across the enterprise.
Solution: Data from on-prem was migrated to the MDM Cloud on the SoftLayer environment, standardized, cleansed, and loaded into the MDM hub. Dedupe matching algorithms were written to identify unique, duplicate, and suspect records. Finally, Unique Enterprise IDs were created for customers and then mapped to the transaction data based on which the data migration to ERP and CRM was completed.
Benefits: Circa 8 Million USD over 3 years (projected).
Faster time to value: The proposed solution on the cloud enabled them to create a single view of the customer within 2 months.
Reduced overall cost: Without the Cloud option, the client would have purchased Perpetual licenses for at least 1 year. The cloud option meant that they could buy initially for 6 months and then extend on a monthly basis as per the project demand.
Improved marketing effectiveness: With a single customer view, the client will improve campaign effectiveness and response rate.
Increased up-sell/cross-sell opportunities: With a single view across Loans and Deposits, the client could target specific, personalized products to the existing customer base.
Technology: MDM AE (Advanced Edition) on IBM SoftLayer Cloud.
31.2 Case Study #2: State Government (MDM)

About the client: These 3 clients represent three different states within India (Rajasthan, Odisha, Tamil Nadu). Each State has several benefit schemes and serves approx. 50 to 70 Million residents.
Business Challenges: Citizen demographic data and Benefits data were scattered across multiple departmental databases. Each database contained duplicate Citizen information, leading to the same Citizen claiming benefits multiple times in a month, resulting in Revenue leakage and poor Governance. The State department decided to embark on a Centralized Data Hub called SRDH to overcome these challenges and improve the benefits distribution process.
Solution: The solution for SRDH (State Resident Data Hub) involved extracting data from 13 departmental databases and deduping, matching, and linking with the National Population Registry data and National ID (Aadhar) database. A unique record for each Citizen was created, and relationships between family members were identified. The suspect records were sent back to the governance team for field verification and further action.
Benefits: Circa 580 Million USD over 3 years (projected - for each State Department).
State and National government bodies can now identify fraudulent benefits applications and claims, to minimize wasteful spending.
Established a Clean, Authenticated, and deduplication data repository for all the Residents of the State.
Support State Government Departments in the effective planning of welfare and development Schemes.
Established the frameworks for the effective monitoring of schemes.
Enabled the transformation of service delivery through integrated service delivery and the Creation of a 360-degree profile of a resident.
Technology: MDM Standard Edition (SE) on-prem, Information Server, Oracle Exadata.
31.3 Case Study #3: Data Lake for Cards Company

About the client: One of the Leading payment solutions providers in India (SBI Card).
Business Challenges: The client had undertaken an initiative to implement a Cloudera-based Data Lake and were facing huge challenges in the acquisition of data from their mainframe applications based on Z/OS as well as from dozens of satellite applications based on Oracle. Z/OS being proprietary in nature did not allow for easy access to data. The client needed a sophisticated solution to extract data in real-time from not only mainframes but also from various applications and store them in Cloudera. The client wanted to leverage native Hadoop capabilities for business intelligence reporting as well as for Predictive Analytics.
Solution: IBM CDC was used to extract changed data from mainframes as well as from Oracle RDBMS; these data were then fed to a Kafka cluster and then posted to Cloudera. IBM BigIntegrate jobs were used to process data on Cloudera to generate relevant output data for Business Intelligence and Analytics. As part of the engagement, a governance catalog was also configured to track technical assets and provide end-to-end lineage.
Benefits:
Real Time Visibility: Real-time replication of data from various source systems to Cloudera (Data Lake).
End-to-End Automation: Leveraged native Hadoop capabilities through IBM products to process data to perform transformation and speed up the processing of terabytes of data.
Streamlined MIS: Enabled day-to-day operational reporting.
Enabled Analytics: Supported downstream Analytics Users for model building with near real-time data.
Technology: IBM CDC, IBM BigIntegrate (DataStage, QualityStage, Governance Catalog).
31.4 Case Study #4: Microfinance Company (ODS)

About the client: Ujjivan is a leading Microfinance company in India and has recently been awarded the Small bank license by the Reserve Bank of India.
Business Challenges: The client wanted to gain better insights from their customer data. Multiple legacy systems and complex IT infrastructure meant that they were not able to glean timely insights. In addition, the new banking license necessitated appropriate Data Governance frameworks to meet future compliance requirements and to increase the business trust in the underlying data and information systems.
Solution: The proposed solution using IBM InfoSphere will connect to various databases, capture changes at the source (CDD), perform complex ETL, and populate the Data mart. The Change Data Delivery option reduces the number of records moved/processed on the ETL server and helps meet the business-defined SLAs. Cognos and SPSS were used for Reporting and Predictive analytics. The Data Dictionary and Data lineage options were recommended to enable the business user to track the journey of data from reports all the way to the source systems, thereby increasing the trust in Analytics.
Benefits:
Achieved business SLAs: With CDD enabled and parallel data transformation, the ETL processing time was reduced from 16 hours to 4 hours.
Improved Governance and Trust: Significantly increased the process and trust that the users had in the IT systems and Data.
Improved Productivity: With less data issues to deal with, the business spends more time in analyzing data and gleaning insights.
Future Proof Investment: A common Meta data layer enables seamless integration with future tools and capabilities such as Data Quality, MDM, and Smart Archiving.
Increased up-sell/cross-sell opportunities: The timely delivery of data into the mart for reporting and the predictive models enables a substantial increase in revenue and paves the way for future growth.
Technology: IBM Information Server, Change Data Delivery, Information Governance Catalog / Glossary (IGC), Cognos.


"""

# --- PROMPT ENGINEERING ---
# This is the instruction given to the AI to control its behavior.
SYSTEM_PROMPT = f"""
You are an expert AI assistant for Alpharithm Technologies. Your name is 'AlphaBot'.
Your knowledge is strictly limited to the case studies provided in the text below.
You must answer user questions based ONLY on this information.
If the answer is not available in the text, you must clearly state: "Based on the provided case studies, I don't have information on that topic."
Do not, under any circumstances, use external knowledge or make up information.
Be friendly, professional, and concise in your answers.

Here is your knowledge base:
---
{KNOWLEDGE_BASE}
---
"""

# --- STREAMLIT APP ---

# Load environment variables from the .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Alpharithm AI Assistant", page_icon="🤖")
st.title("🤖 Alpharithm Case Study AI Assistant")
st.write("I have been trained on Alpharithm's case studies. Ask me anything!")

# --- API KEY and MODEL SETUP ---
if not GOOGLE_API_KEY:
    st.error("Google API Key not found. Please create a .env file with GOOGLE_API_KEY='your_key'")
    st.stop()

# Configure the Generative AI client
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash-lite')
except Exception as e:
    st.error(f"Error configuring Google API: {e}")
    st.stop()

# --- SESSION STATE MANAGEMENT ---
# Initialize the chat history if it doesn't exist
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(
        history=[
            # Prime the model with the system prompt and an initial response
            {'role': 'user', 'parts': [SYSTEM_PROMPT]},
            {'role': 'model', 'parts': ["Hello! I'm AlphaBot, your expert on Alpharithm's case studies. How can I help you today?"]}
        ]
    )

# --- CHAT INTERFACE ---
# Display previous messages from the chat history
# We skip the first two messages which are the system prompt and the initial greeting
for message in st.session_state.chat.history[2:]:
    with st.chat_message(name=message.role):
        st.markdown(message.parts[0].text)

# Get new user input
if prompt := st.chat_input("What was the solution for the Central Bank of India?"):
    # Display the user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user's message to the model and get the response
    try:
        with st.spinner("Thinking..."):
            response = st.session_state.chat.send_message(prompt)
        
        # Display the model's response
        with st.chat_message("model"):
            st.markdown(response.text)
    
    except Exception as e:
        st.error(f"An error occurred while generating the response: {e}")
