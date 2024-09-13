import streamlit as st
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Streamlit App Title
st.title("Interactive Simulation of the Moniac Model")

# User inputs for the simulation parameters
st.sidebar.header("Simulation Parameters")
l_param = st.sidebar.slider(
    "Production Multiplier (l)", min_value=0.1, max_value=2.0, value=0.8, step=0.1
)
m_param = st.sidebar.slider(
    "Consumption Multiplier (m)", min_value=0.1, max_value=2.0, value=0.5, step=0.1
)
delta_v = st.sidebar.number_input(
    "Change in Consumption (Δv)", min_value=-50, max_value=50, value=10, step=1
)


# Define the differential equation representing the system
def economic_model(t, p):
    dp_dt = (l_param - m_param) * p + delta_v
    return dp_dt


# Time span for the simulation
t_span = (0, 50)
# Initial price level (p0)
p0 = [1.0]  # Assuming the price level starts at 1.0

# Solve the differential equation
solution = solve_ivp(economic_model, t_span, p0, t_eval=np.linspace(0, 50, 500))

# Plot the results
fig, ax = plt.subplots()
ax.plot(solution.t, solution.y[0], label="Price Level (p)", color="b")
ax.set_title("Economic Simulation of the Moniac Model")
ax.set_xlabel("Time")
ax.set_ylabel("Price Level")
ax.legend()
ax.grid()

# Display the plot in the Streamlit app
st.pyplot(fig)

# Additional insights
st.write(
    """
## Insights:
- Adjust the **Production Multiplier (l)** and **Consumption Multiplier (m)** to see their impact on the price level dynamics.
- Change the **Consumption Change (Δv)** to simulate sudden shifts in consumer behavior.
"""
)
