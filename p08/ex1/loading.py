import importlib

def check_dependencies():
    dependencies_list = [
                         ["pandas", "Data manipulation ready"],
                         ["numpy", "Numerical computation ready"],
                         ["requests", "Network access ready"],
                         ["matplotlib","Visualization ready"],
                         ]
    try:
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

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    
    data = numpy.random.normal(loc=0.5, scale=0.15, size=1000)
    df = pandas.DataFrame(data, columns=["Values"])
    
    print("Generating visualization...")
    matplotlib.pyplot.hist(df["Values"], bins=30, color="green", edgecolor="black")
    matplotlib.pyplot.title("Matrix Data Distribution")
    matplotlib.pyplot.xlabel("Value")
    matplotlib.pyplot.ylabel("Frequency")
    matplotlib.pyplot.savefig(file_name)
    matplotlib.pyplot.close()
    
    print("\nAnalysis complete!")
    print(f"Results saved to: {file_name}")

def main():
    


