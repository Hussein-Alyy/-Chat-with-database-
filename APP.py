import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from langchain_google_genai import GoogleGenerativeAI
import re

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Data Intelligence Hub", page_icon="🤖", layout="wide")

# --- CREDENTIALS ---

GOOGLE_API_KEY = 
DB_URL = 

# --- DATABASE ENGINE ---
@st.cache_resource
def get_db_engine():
    return create_engine(DB_URL)

def run_query(query_string):
    """Function to execute SQL and return a DataFrame"""
    engine = get_db_engine()
    with engine.connect() as conn:
        return pd.read_sql(text(query_string), conn)

# --- SCHEMA EXTRACTION ---
@st.cache_data(ttl=3600)
def fetch_database_schema():
    query = """
    SELECT table_name, column_name 
    FROM information_schema.columns 
    WHERE table_schema = 'public';
    """
    df = run_query(query)
    schema_details = "Database Schema:\n"
    for table in df['table_name'].unique():
        columns = df[df['table_name'] == table]['column_name'].tolist()
        schema_details += f"- Table '{table}' with columns: {', '.join(columns)}\n"
    return schema_details

# --- AI INITIALIZATION ---
llm = GoogleGenerativeAI(model="gemini-2.5-flash", api_key=GOOGLE_API_KEY)

# --- UI ELEMENTS ---
st.title("🚀 Smart SQL Analyst Pro")
st.markdown("---")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "data" in msg:
            st.dataframe(msg["data"])

# --- MAIN LOGIC ---
if user_input := st.chat_input("What would you like to know from your data?"):
    
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        db_schema = fetch_database_schema()
        
        sql_generation_prompt = f"""
        You are an expert PostgreSQL developer. 
        Database Schema:
        {db_schema}

        Task: Write a SQL query to answer: {user_input}

        STRICT RULES:
        1. ALWAYS use double quotes around table and column names (e.g., "Customer", "TotalSpent").
        2. Ensure the case of the table/column names matches the schema EXACTLY.
        3. Only return the SQL code. No markdown, no backticks, no explanations.
        4. Use JOINs where necessary based on common keys (like "CustomerId").
        """
        
        raw_sql = llm.invoke(sql_generation_prompt)
        clean_sql_query = re.sub(r"sql|", "", raw_sql).strip()
        
        st.code(clean_sql_query, language="sql")
        
        try:
            query_results = run_query(clean_sql_query)
            st.dataframe(query_results)
            
            analysis_prompt = f"""
            Context: The user asked "{user_input}"
            Data Results:
            {query_results.to_string()}
            
            Summarize the findings in a concise and professional manner.
            """
            final_answer = llm.invoke(analysis_prompt)
            st.markdown(final_answer)
            
            st.session_state.chat_history.append({
                "role": "assistant", 
                "content": final_answer, 
                "data": query_results
            })
            
        except Exception as error:
            st.error(f"⚠️ SQL Execution Error: {str(error)}")
            st.info("Tip: Make sure the table names in the schema are correct.")




###  streamlit run "c:/Users/hussein aly/Downloads/Chinhook/Chinhook/APP.py"   ###
