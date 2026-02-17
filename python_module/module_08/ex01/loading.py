#!/usr/bin/env python3

"""Second exercise."""

import sys
import importlib.util


def check_dependencies() -> None:
    """Check if the dependencies are installed."""
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    missing = []

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package in packages:
        spec = importlib.util.find_spec(package)
        if spec is None:
            print(f"[ERROR] {package} is missing!")
            missing.append(package)
        else:
            from importlib.metadata import version
            print(f"[OK] {package} ({version(package)}) - Ready")

    if missing:
        print("\n=== INSTALLATION INSTRUCTIONS ===")
        print("For Pip:    pip install -r requirements.txt")
        print("For Poetry: poetry install")
        sys.exit(1)


def run_matrix_analysis() -> None:
    """Create a diagram."""
    import pandas
    import numpy
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    # Simulation de données : 1000 points de "code" de la Matrix
    data = numpy.random.randn(1000).cumsum()
    df = pandas.DataFrame(data, columns=['Matrix Stream'])

    print(f"Processing {len(df)} data points...")

    # Génération du graphique
    plt.figure(figsize=(10, 5))
    plt.plot(df, color='green')
    plt.title("Matrix Data Stream Analysis", color='green')
    plt.savefig("matrix_analysis.png")

    print("Generating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_dependencies()
    run_matrix_analysis()
