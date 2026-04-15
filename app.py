import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Limits Explorer", layout="centered")

# Title
st.title("📘 Limits & Continuity Explorer")
st.write("Learn limits step-by-step, visualize graphs, and understand function behavior.")

# Input section
st.header("1️⃣ Enter a Function")
user_input = st.text_input("Enter a function in terms of x (e.g., (x^2-1)/(x-1), sin(x)/x):", "(x**2-1)/(x-1)")

x = sp.symbols('x')

try:
    expr = sp.sympify(user_input)
    st.success(f"Parsed function: ${sp.latex(expr)}$")

    # Limit calculation
    st.header("2️⃣ Calculate the Limit")
    point = st.number_input("Find the limit as x approaches:", value=1.0)
    a = sp.sympify(point)

    left_limit = sp.limit(expr, x, a, '-')
    right_limit = sp.limit(expr, x, a, '+')
    general_limit = sp.limit(expr, x, a)

    st.latex(f"\\lim_{{x \\to {a}^-}} f(x) = {sp.latex(left_limit)}")
    st.latex(f"\\lim_{{x \\to {a}^+}} f(x) = {sp.latex(right_limit)}")

    if left_limit == right_limit:
        st.success(f"✅ The limit EXISTS! lim f(x) = {general_limit}")
    else:
        st.error("❌ The limit DOES NOT EXIST (left ≠ right)")

    # Step-by-step
    st.header("3️⃣ Step-by-Step Solution")
    st.write(f"**Step 1:** Identify the function: f(x) = {sp.latex(expr)}")
    st.write(f"**Step 2:** Find the left-hand limit as x → {a}⁻ = {left_limit}")
    st.write(f"**Step 3:** Find the right-hand limit as x → {a}⁺ = {right_limit}")
    if left_limit == right_limit:
        st.write(f"**Step 4:** Since both sides are equal, the limit = **{general_limit}**")
    else:
        st.write("**Step 4:** Since both sides are NOT equal, the limit does not exist.")

    # Continuity check
    st.header("4️⃣ Continuity Check")
    func_value = expr.subs(x, a)
    st.write(f"f({a}) = {func_value}")
    if func_value == general_limit and left_limit == right_limit:
        st.success("✅ The function is CONTINUOUS at this point!")
    else:
        st.warning("⚠️ The function is DISCONTINUOUS at this point.")

    # Graph
    st.header("5️⃣ Graph")
    f_lambdified = sp.lambdify(x, expr, 'numpy')
    x_vals = np.linspace(float(a) - 5, float(a) + 5, 400)
    with np.errstate(divide='ignore', invalid='ignore'):
        y_vals = f_lambdified(x_vals)
        y_vals = np.where(np.abs(y_vals) > 100, np.nan, y_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='f(x)', color='cyan')
    ax.axvline(float(a), color='red', linestyle='--', label=f'x = {a}')
    ax.axhline(0, color='white', linewidth=0.5)
    ax.axvline(0, color='white', linewidth=0.5)
    ax.legend()
    ax.set_title(f"Graph of f(x) near x = {a}")
    ax.set_facecolor('#0e1117')
    fig.patch.set_facecolor('#0e1117')
    ax.tick_params(colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    st.pyplot(fig)

except Exception as e:
    st.error("Invalid function. Please try again.")
    st.text(str(e))

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & SymPy")
