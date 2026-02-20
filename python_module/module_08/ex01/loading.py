#!/usr/bin/env python3

"""Second exercise."""

import sys
import os
import importlib.util


def check_dependencies() -> bool:
    """Check if the dependencies are installed."""
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    missing = []

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
        print("\nFirst install and activate a virtual environnement:")
        print("python3 -m venv venv")
        print("source venv/bin/activate")
        print("\nThen choose the way the dependencies will be installed:")
        print("with Pip:    pip install -r requirements.txt")
        print("with Poetry: pip install -U pip setuptools")
        print("             pip install poetry")
        print("             poetry install")

        return False
    return True


def run_matrix_analysis() -> None:
    """Create a diagram."""
    import pandas
    import numpy
    import matplotlib.pyplot as plt

    demonstrate_management()

    print("\nAnalyzing Matrix data...")
    data = numpy.random.randn(1000).cumsum()
    df = pandas.DataFrame(data, columns=['Matrix Stream'])

    print(f"Processing {len(df)} data points...")

    plt.figure(figsize=(10, 5))
    plt.plot(df, color='green')
    plt.title("Matrix Data Stream Analysis", color='green')
    plt.savefig("matrix_analysis.png")

    print("Generating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def demonstrate_management():
    print("=== Dependency Manager analyse ===\n")
    lock_file = os.path.join(os.getcwd(), "poetry.lock")

    if os.path.exists(lock_file):
        manager = "POETRY"
        description = ("Dependencies versions locked on a file and a "
                       "virtual environnement automatically created.")
    else:
        manager = "PIP"
        description = "Manually managed versions (Risk of dependency drift)"

    print(f"Dependecy Manager detected: {manager}")
    print(description)


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    if check_dependencies():
        run_matrix_analysis()
    else:
        sys.exit(1)
