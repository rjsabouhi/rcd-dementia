import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Alzheimer’s Cure Simulator", layout="wide")
st.title("RCD–Pharma Synth: Alzheimer's Cure Engine")

# Glossary
with st.expander("Glossary"):
    st.markdown("""
    - **H (Hope)**: Recursive attractor for future identity projection.
    - **M (Memory)**: Symbolic coherence of personal history.
    - **R (Reinforcement)**: Loop-strength from past + projected continuity.
    - **μ(H, M, R)**: Memory tension — how tightly identity is bound.
    - **Θ**: Clinging/occlusion — symbolic obstruction from trauma, entropy, or plaque.
    - **∇S**: Symbolic entropy gradient — how fast symbolic structure is collapsing.
    - **τ(t)**: Recursive time — identity continuity across subjective time.
    """)

# Drug profiles
DRUGS = {
    "Donepezil": {"memory_boost": 0.2, "entropy_reduction": 0.0, "coherence_restore": 0.0},
    "Memantine": {"memory_boost": 0.0, "entropy_reduction": 0.2, "coherence_restore": 0.0},
    "Lecanemab": {"memory_boost": 0.0, "entropy_reduction": 0.1, "coherence_restore": 0.1},
    "Aletheamine (experimental)": {"memory_boost": 0.3, "entropy_reduction": 0.3, "coherence_restore": 0.4},
}

# Sidebar controls
selected_drug = st.sidebar.selectbox("Choose a drug intervention", list(DRUGS.keys()))
timesteps = st.sidebar.slider("Simulation Duration", 30, 200, 100)
decay_rate = st.sidebar.slider("Baseline Memory Decay Rate", 0.01, 0.1, 0.05)

# Initialize state variables
H = [1.0]
M = [1.0]
R = [1.0]
coherence = [1.0]
entropy = [0.0]

drug = DRUGS[selected_drug]

# Simulation loop
for t in range(1, timesteps):
    dH = -decay_rate * (1 - drug["coherence_restore"])
    dM = -decay_rate * (1 - drug["memory_boost"])
    dR = -decay_rate * 0.5

    H_new = max(0.0, H[-1] + dH)
    M_new = max(0.0, M[-1] + dM)
    R_new = max(0.0, R[-1] + dR)

    coherence_val = (H_new + M_new + R_new) / 3
    entropy_val = 1 - coherence_val + drug["entropy_reduction"]

    H.append(H_new)
    M.append(M_new)
    R.append(R_new)
    coherence.append(coherence_val)
    entropy.append(min(1.0, entropy_val))

# Plotting
fig, ax = plt.subplots()
ax.plot(H, label="Hope")
ax.plot(M, label="Memory")
ax.plot(R, label="Reinforcement")
ax.plot(coherence, label="Total Coherence", linestyle='--')
ax.plot(entropy, label="Entropy ∇S", linestyle=':')
ax.set_title("Symbolic Identity Dynamics under Drug Intervention")
ax.set_xlabel("Time (τ)")
ax.set_ylabel("Attractor Strength")
ax.legend()
st.pyplot(fig)
