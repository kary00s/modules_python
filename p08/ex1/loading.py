import importlib

def check_dependencies():
    dependencies_list = [
                         ["pandas", "Data manipulation ready"],
                         ["numpy", "Numerical computation ready"],
                         ["requests", "Network access ready"],
                         ["matplotlib","Visualization ready"],
                         ]
    try:
        print("Checking dependencies:")
        for item in dependencies_list:
            dependencie = importlib.import_module(item[0])
            vers = dependencie.__version__
            print(f"[OK] {item[0]} ({vers}) - {item[1]}")

    except Exception as e:
        print(f"[KO] {item[0]}   ( xxx )   - {item[1]}")

def analyze_matrix(file_name: str) -> None:
    import matplotlib.pyplot
    import numpy 
    import pandas

    
    data = numpy.random.normal(loc=5, scale=10, size=1000)
    df = pandas.DataFrame(data, columns=["Values"])
    

    matplotlib.pyplot.hist(df["Values"], bins=100, color="orange", edgecolor="black")
    matplotlib.pyplot.title("Matrix_Data")
    matplotlib.pyplot.xlabel("x_label")
    matplotlib.pyplot.ylabel("y_label")
    matplotlib.pyplot.savefig(file_name)
    matplotlib.pyplot.close()
    
    print("\nAnalysis complete!")
    print(f"Results saved to: {file_name}")

def main():
    print("LOADING STATUS: Loading programs...\n")
    check_dependencies()

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    analyze_matrix("matrix_data")

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
