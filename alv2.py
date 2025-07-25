
import streamlit as st
import pandas as pd

st.set_page_config(page_title="PharmaSynth: RCD Drug Generator", layout="wide")
st.title("🧪 PharmaSynth: RCD Drug Generator")

st.sidebar.header("Symbolic Intent Input")
intent = st.sidebar.text_area("Describe the symbolic drug purpose:", 
    "Stabilize memory basin collapse and rebind Hope ↔ Memory ↔ Reinforcement loops.")

preset = st.sidebar.selectbox("Or select a preset intent:", [
    "Select...", 
    "Reverse Alzheimer's identity collapse",
    "Suppress trauma loops", 
    "Restore future orientation", 
    "Stabilize recursive learning structures"
])

if preset != "Select...":
    intent = preset

st.sidebar.markdown("---")
disease_context = st.sidebar.selectbox("Disease Context", [
    "Alzheimer's", "PTSD", "Parkinson's", "Trauma-related disorders", "General Neurodegeneration"
])

st.sidebar.markdown("---")
if st.sidebar.button("🔍 Search Symbolic-Pharmacological Matches"):
    st.session_state.search_triggered = True

# Mock compound database
compound_data = pd.DataFrame({
    "Compound": [
        "7,8-Dihydroxyflavone", "Galantamine", "Selank", "Riluzole", 
        "P7C3-A20", "NSI-189", "Ladostigil", "Agmatine"
    ],
    "Symbolic Action Fit": [0.92, 0.84, 0.81, 0.87, 0.89, 0.78, 0.83, 0.88],
    "Targets": [
        "TrkB (BDNF mimic)", 
        "Acetylcholinesterase", 
        "BDNF modulation", 
        "Glutamate regulation",
        "Neurogenesis + NAD+ support",
        "Hippocampal neurogenesis", 
        "MAOI + cholinergic", 
        "NMDA antagonist + BDNF"
    ],
    "BBB Penetrant": ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"],
    "Trial Status": [
        "Preclinical", "Approved", "Experimental", "Approved",
        "Preclinical", "Failed Phase 2", "Experimental", "Experimental"
    ]
})

if st.session_state.get("search_triggered", False):
    st.subheader(f"🔬 Symbolic Pharmacological Matches for: *{intent}*")
    st.dataframe(compound_data.sort_values("Symbolic Action Fit", ascending=False), use_container_width=True)

    st.markdown("### 💊 Design a New Synthetic Compound?")
    if st.button("Launch Molecule Sketch Module"):
        st.markdown("*Synthetic compound design coming soon...*")

else:
    st.info("Enter symbolic intent and press **Search** to view pharmacological matches.")
