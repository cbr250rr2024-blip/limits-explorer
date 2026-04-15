import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Derivatives Explorer", layout="centered")

# Title
st.title("📘 Derivatives & Differentiation Explorer")
st.write("Learn derivatives step-by-step, visualize graphs, and understand function behavior.")

# Input section
st.header("1️⃣ Enter a Function")
user_input = st.text_input("Enter a function in terms of x (e.g., x^2, sin(x), exp(x)):", "x^2")

# Symbol
x = sp.symbols('x')

try:
    # Convert input to sympy expression
    expr = sp.sympify(user_input)

    st.success(f"Parsed function: {sp.latex(expr)}")

    # Derivative
    st.header("2️⃣ Derivative")
    derivative = sp.diff(expr, x)
    st.latex(f"f'(x) = {sp.latex(derivative)}")

    # Step-by-step (basic)
    st.header("3️⃣ Step-by-Step Solution")
    st.write("Here is a simplified breakdown:")

    steps = sp.srepr(derivative)
    st.code(steps, language='python')

    st.info("Tip: For full symbolic steps, more advanced tools are needed, but this shows the structure.")

    # Graph
    st.header("4️⃣ Graph")

    f_lambdified = sp.lambdify(x, expr, 'numpy')
    df_lambdified = sp.lambdify(x, derivative, 'numpy')

    x_vals = np.linspace(-10, 10, 400)

    y_vals = f_lambdified(x_vals)
    dy_vals = df_lambdified(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='f(x)')
    ax.plot(x_vals, dy_vals, linestyle='--', label="f'(x)")

    ax.axhline(0)
    ax.axvline(0)

    ax.legend()
    ax.set_title("Function vs Derivative")

    st.pyplot(fig)

    # Increasing / decreasing
    st.header("5️⃣ Increasing or Decreasing?")
    point = st.number_input("Enter a value for x:", value=1.0)

    slope = df_lambdified(point)

    st.write(f"Derivative at x = {point} is {slope}")

    if slope > 0:
        st.success("The function is increasing at this point 📈")
    elif slope < 0:
        st.error("The function is decreasing at this point 📉")
    else:
        st.warning("The function is stationary at this point ⚖️")

except Exception as e:
    st.error("Invalid function. Please try again.")
    st.text(str(e))

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & SymPy")
