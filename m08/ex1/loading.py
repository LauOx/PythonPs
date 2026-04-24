#!/usr/bin/env python3

import sys


PACK_DESCRIPTION = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computation",
            "matplotlib": "Visualization",
            }


def check_dependencies() -> None:
    """Check if required packages are installed and print their version
     if a dependency is missing, print installation instrucion and exit """
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:\n")
    lib_required = ["pandas", "numpy", "matplotlib"]
    all_ok = True
    for lib in lib_required:
        try:
            # dinamic import
            module = __import__(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - {PACK_DESCRIPTION[lib]}")
        except ImportError:
            print(f"[ERROR] {lib} is missing")
            all_ok = False

    if not all_ok:
        print("\nTo fix this, run:")
        print("*** Using pip ***")
        print("pip install -r requirements.txt")
        print("python3 loading.py")
        print("OR")
        print("*** Using poetry ***")
        print("pip install poetry (if not installed yet)")
        print("poetry config keyring.enabled false (To avoid Kering problems)")
        print("poetry install")
        print("poetry run python3 loading.py\n")
        sys.exit(1)


def data_analysis() -> None:
    """create data with numpy, manipulate de data with pandas and
    generate a graphic with matplotlib"""
    import numpy
    import pandas
    import matplotlib.pyplot as plt
    print("Analyzing Matrix data...")
    # generate data with numpy
    data = {
        'Matrix_X': numpy.random.randint(1, 200, 50),
        'Matrix_Y': numpy.random.randint(1, 200, 50)
    }
    df_object = pandas.DataFrame(data)
    print(f"Processing {len(data)} data points...")
    # manipulate data with pandas
    df_object = pandas.DataFrame(data, columns=["Matrix_X", "Matrix_Y"])
    print("Generating visualization...")
    # create graphic
    plt.scatter(
        df_object['Matrix_X'],
        df_object['Matrix_Y'],
        color='green',
        alpha=0.6)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Data on axis X")
    plt.ylabel("Data on axis Y")
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete! \nResults saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_dependencies()
    data_analysis()
