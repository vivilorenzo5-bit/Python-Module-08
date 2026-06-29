import importlib.metadata
import sys


def print_pip_vs_poetry_comparison() -> None:
    print("\n==================================")
    print("      PIP VS POETRY COMPARISON      ")
    print("====================================")
    print("1. DEPENDENCY RESOLUTION:")
    print("   - PIP: Resolve pacotes de forma linear (requirements.txt).")
    print("          Pode causar 'Dependency Hell' se houver conflitos.")
    print("   - POETRY: Usa um resolvedor avançado baseado em grafos.")
    print("             Garante que todas as sub-dependências coexistem.")
    print("")
    print("2. DETERMINISM & LOCKING:")
    print("   - PIP: Instala o que estiver disponível no momento.")
    print("          Versões podem oscilar se não forem travadas rigidamente.")
    print("   - POETRY: Cria o ficheiro 'poetry.lock'.")
    print(r"            Garante instalações 100% idênticas em qualquer PC.")
    print("")
    print("3. ENVIRONMENT ISOLATION:")
    print("   - PIP: Requer que cries e atives o venv manualmente.")
    print("   - POETRY: Abstrai o processo, gerindo o venv silenciosamente.")
    print("=======================================================\n")


def check_dependencies() -> bool:
    required = ["pandas", "numpy", "matplotlib"]
    missing = []

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package in required:
        try:
            version = importlib.metadata.version(package)
            print(f"[OK] {package.ljust(11)} ({version})")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {package.ljust(11)} (Not installed)")
            missing.append(package)

    if missing:
        print("ERROR: Missing core dependencies")
        print(f"Following software is absent: {', '.join(missing)}")
        print("\n>>> HOW TO FIX (Choose one pathway):")
        print("A) PIP:")
        print("   $ pip install -r requirements.txt")
        print("   $ python3 ex1/loading.py")
        print("B) POETRY:")
        print("   $ poetry install")
        print("   $ poetry run python ex1/loading.py")

        print_pip_vs_poetry_comparison()
        return False
    return True


def run_matrix_pipeline() -> None:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Data manipulation ready")
    print("Numerical computation ready")
    print("Network access ready")
    print("Visualization ready\n")
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    np.random.seed(42)
    timestamps = np.arange(1000)
    signal_strength = np.random.normal(loc=50, scale=15, size=1000)
    anomaly_noise = np.random.choice([0, 30, -30], size=1000,
                                     p=[0.95, 0.025, 0.025])
    final_signal = signal_strength + anomaly_noise
    df = pd.DataFrame({"Sequence": timestamps, "Signal": final_signal})
    plt.figure(figsize=(10, 5))
    plt.plot(df["Sequence"], df["Signal"], color="green", alpha=0.7,
             label="Matrix Stream")
    plt.axhline(y=50, color="red", linestyle="--", label="Baseline Reality")
    plt.title("Vicente Mainframe - Matrix Signal Analysis")
    plt.xlabel("Time Sequence")
    plt.ylabel("Signal Magnitude")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)

    output_filename = "matrix_analysis.png"
    plt.savefig(output_filename, dpi=150)
    plt.close

    print("Analysis complete!")
    print(f"Results saved to: {output_filename}")


def main() -> None:
    if not check_dependencies():
        sys.exit(1)
    run_matrix_pipeline()


if __name__ == "__main__":
    main()
