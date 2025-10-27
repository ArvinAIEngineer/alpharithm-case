import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- KNOWLEDGE BASE ---
# This is the information the AI will use to answer questions.
# CORRECTED: Now includes all case studies provided.
KNOWLEDGE_BASE = """
Alpharithm Technologies – Case Studies

Financial Services & Banking

Central Bank of India – Enterprise Data Warehouse and Analytics
About the client: Central Bank of India, established in 1911, was the first Indian commercial bank wholly owned and managed by Indians.
Business Challenges: The client needed better insights from customer data. Existing reports built on an ODS did not cover all requirements. Daily KPI monitoring and statutory report preparation were time-consuming and often inaccurate.
Solution: Implemented an IBM IIAS appliance with data from 17+ applications using IBM InfoSphere Information Server. IBM CDC connected Core Banking Applications to Staging areas. Cognos was used for Reporting and Predictive Analytics. 12 Data Marts and 76 Dashboards were created. Data Dictionary and lineage ensured trust in analytics.
Benefits:
- KPI dashboards for day-to-day monitoring
- Improved governance and trust in IT systems
- Easier generation of regulatory reports
- Enhanced Customer 360 View for targeted analytics
Technology: IBM Information Server, IBM Db2 Warehouse, IBM IIAS, IBM CDC, IBM Cognos, Oracle, SQL Server

ICICI Bank – Master Data Management & Data Governance
About the client: ICICI Bank, one of the largest private banks in India.
Business Challenges: Customer information was fragmented across retail and corporate applications, leading to duplicate records and inconsistent offers.
Solution: Integrated data from 70+ applications into IBM MDM. Data standardized, cleansed, and probabilistic matching applied to identify duplicates. Golden records made available via REST API through APIGEE middleware.
Benefits:
- Unique customer identification across business lines
- Improved customer experience with Golden Profile
- Centralized consent management
- Advanced householding for accurate customer scoring
Technology: MDM AE on OpenShift, IBM Cloud Pack Cartridge Information Server, IBM Watson Knowledge Catalog, IBM Consent Management, IBM Reference Data Management, APIGEE Middleware, Vertica, Oracle EXADATA, Oracle, SQL Server

DHFL – Master Data Management
About the client: DHFL is the 3rd largest mortgage lender in India.
Business Challenges: Data migration from legacy systems to modern ERP/CRM applications had poor master data quality.
Solution: Data migrated to MDM Cloud on SoftLayer, standardized, cleansed, and loaded into MDM hub. Deduplication algorithms created unique enterprise IDs mapped to transaction data for ERP/CRM migration.
Benefits:
- Single view of customer created within 2 months
- Reduced overall cost with cloud-based subscription
- Improved marketing effectiveness
- Increased up-sell/cross-sell opportunities
Technology: MDM AE on IBM SoftLayer Cloud, IBM Datastage, IBM QualityStage

Ujjivan – Microfinance ODS
About the client: Leading microfinance company, recently awarded Small Bank license by RBI.
Business Challenges: Multiple legacy systems and complex IT infrastructure made timely insights difficult.
Solution: IBM InfoSphere connected to various databases, captured changes at source, performed ETL, and populated Data Mart. Cognos and SPSS enabled reporting and predictive analytics.
Benefits:
- ETL processing reduced from 16 to 4 hours
- Improved governance and trust
- Increased productivity and insights
- Future-proof integration with new tools and capabilities
Technology: IBM Information Server, IBM Datastage, IBM QualityStage, IGC

SBI Card – Financial Services Data Lake
About the client: Leading payment solutions provider in India.
Business Challenges: Data acquisition from mainframes (Z/OS) and multiple satellite applications was challenging.
Solution: IBM CDC extracted changed data from mainframes and Oracle, posted to Kafka and Cloudera. IBM BigIntegrate processed data for BI and analytics. Governance catalog tracked technical assets.
Benefits:
- Real-time visibility into source systems
- End-to-end automation of data processing
- Streamlined operational reporting
- Supported downstream analytics and model building
Technology: IBM CDC, IBM BigIntegrate, Cloudera, Kafka, Oracle

Insurance

Universal Sompo – Data Lake, Analytics & Integration
About the client: Mid-market general insurance company providing Health, Motor, and Commercial Insurance.
Business Challenges: Siloed applications, manual reporting, duplicate customer records, Salesforce implementation across functions.
Solution: Centralized data from 30+ applications into Data Lake. IBM CDC and Datastage implemented. Alpharithm SiNGL created unique customer repository. Data integrated with Salesforce and visualized with Tableau.
Benefits:
- Near real-time visibility of customer data
- Improved customer support
- Easier operational reporting
- KPI-based performance monitoring
Technology: IBM CDC, IBM Datastage, IBM QualityStage, SiNGL (MDM), IBM Db2 Warehouse, Oracle, SQL Server, MySQL

Pharma

Sanofi – Master Data Hub
About the client: Largest European-headquartered Pharma company.
Business Challenges: Duplicate Doctor data across CRM and other systems. Manual deduplication increased operational costs and risk. Regulatory compliance required accurate records.
Solution: Data extracted, validated, cleansed, deduplicated, and loaded into Doctor Hub. Governance workflows ensured single version of truth.
Benefits: Circa 3 Million USD over 3 years, 35% duplication removed, Visibility into spend per Doctor, Golden record for each Doctor, Regulatory compliance met, Foundation for Products and Distributor hubs.
Technology: MDM SE (Standard Edition), Information Server, DB2

Media

Sony Pictures Networks – Integration Platform
About the client: One of the largest entertainment companies in India with 10+ TV channels.
Business Challenges: Multiple media-specific applications with duplicated master data; integration and reporting issues.
Solution: Scalable Integration Platform using SOA. Master data domains included Customer, Title, Episodes, Deals, General Ledger.
Benefits: Circa 20 Million USD over 3 years (projected), Revenue uplift for syndication and ad sales teams, Improved governance via automated workflows, Improved marketing effectiveness with single customer view.
Technology: MDM CE (Collaborative Edition), Information Server, BPM, Integration Bus

Government

State Resident Data Hub (SRDH) – Rajasthan, Odisha, Tamil Nadu
About the client: Three Indian states, 50–70 million residents each, with multiple benefit schemes.
Business Challenges: Citizen and benefits data scattered across departments, duplicate claims, revenue leakage, and poor governance.
Solution: Data extracted from 13 departmental databases, deduped, matched with National Population Registry and Aadhar. Unique citizen records created with family relationships. Suspect records sent for verification.
Benefits: Circa 580 Million USD over 3 years per state, Identify fraudulent claims, Clean, authenticated data repository, Effective planning of welfare schemes, Frameworks for monitoring schemes, 360-degree resident profiles.
Technology: MDM SE, Information Server (DataStage and QualityStage), Oracle Exadata, IBM Information Governance Catalog, IBM Information Analyzer

Retail & Manufacturing

Leading Multi-brand Retailer – Analytics & AWS Migration
About the client: Pan-India retailer and manufacturer in Eyecare, Jewellery, Fashion, and Perfumes.
Business Challenges: Needed a single vendor for analytics. Existing IBM stack required stabilization and migration to AWS for scalability.
Solution: Administered IBM Information Server, HortonWorks, IBM Netezza, and managed L2/L3 support. Developed ETL routines, maintained jobs, performed tuning and troubleshooting.
Benefits:
- Timely reporting across business lines
- Improved operational efficiency and automation
Technology: IBM Information Server, IBM Netezza, HortonWorks, Tableau, AWS Redshift, AWS S3, AWS DynamoDB

Netezza Migration – Retail Client
Benefits:
- Timely reporting across business lines
- Improved automation and operational efficiency
Technology: IBM Netezza
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
