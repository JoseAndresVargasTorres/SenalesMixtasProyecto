import sympy as sp

def complex_integration():
    # Definir el símbolo complejo z
    z = sp.symbols('z', complex=True)

    # Definir la expresión que se integrará
    expression = z ** 2 + sp.exp(z)

    # Realizar la integración simbólica
    integral_result = sp.integrate(expression, z)

    return integral_result

    # Llamada a la función


result = complex_integration()
print("Resultado de la integración compleja:", result)