import streamlit as st
from executor import run_python_code

# Page Config for a 'Pro' look
st.set_page_config(page_title="Nexus IDE", layout="wide")

st.title("🚀 Nexus Cloud IDE")
st.subheader("Build and Run Python in the Cloud")

# Sidebar for project info/settings
with st.sidebar:
    st.header("Project Settings")
    st.info("Environment: Python 3.x")
    if st.button("Clear Console"):
        st.rerun()

# Layout: Main Editor and Console
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Editor")
    # Using a high-height text area for the 'Editor' feel
    user_code = st.text_area(
        label="Enter Python Code",
        value="print('Hello from Nexus IDE!')\n\n# Try a loop\nfor i in range(5):\n    print(f'Iteration {i}')",
        height=400,
        label_visibility="collapsed"
    )
    
    if st.button("▶ Run Code", type="primary"):
        with st.spinner("Executing..."):
            output = run_python_code(user_code)
            st.session_state['output'] = output

with col2:
    st.write("### Console")
    if 'output' in st.session_state:
        # Professional dark console look
        st.code(st.session_state['output'], language="bash")
    else:
        st.caption("Output will appear here...")

st.markdown("---")
st.caption("Powered by Streamlit & Subprocess Engine")
