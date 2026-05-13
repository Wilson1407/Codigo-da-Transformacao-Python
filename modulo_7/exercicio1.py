# Módulo utilidades.py com fuções matemáticas e importar no programa principal.

def soma(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b): return a / b if b else None

if __name__ == "__main__":
    x, y = 10, 5
    print(f"{x}+{y}={soma(x,y)}")
    print(f"{x}+{y}={sub(x,y)}")
    print(f"{x}+{y}={mult(x,y)}")
    print(f"{x}+{y}={div(x,y)}")