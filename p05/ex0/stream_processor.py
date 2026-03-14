from abc import ABC, abstractmethod
from typing import Any, List, Union

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            raise ValueError("NumericProcessor expects a list of numbers")

        for item in data:
            try:
                int(item)
            except (TypeError, ValueError):
                raise ValueError(f"Non-numeric value found: {item}")
        print("Validation: Numeric data verified")
        return True

    def process(self, data: List) -> str:
        print(f"Processing data: {data}")
        self.validate(data)
  
        total = sum(data)
        count = len(data)
        if count > 0:
            avg = total / count 
        else:
            avg = 0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            raise ValueError("TextProcessor expects a string")
        print("Validation: Text data verified")
        return True

    def process(self, data: str) -> str:
        print(f'Processing data: "{data}"')
        self.validate(data)

        char_count = len(data)
        word_count = len(data.split(" "))
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            raise ValueError("LogProcessor expects a string")
        print("Validation: Log entry verified")
        return True

    def process(self, data: str) -> str:
        print(f"Processing data: {data}")
        self.validate(data)
        hint = data.split(":")[0]
        msg = data.split(":")[1]

        level = "UNKNOWN"
        if hint == "ERROR":
            level = "ALERT"
        elif hint ==  "SUCCESS":
            level = "SUCCESS"

        return f"[{level}] {hint} level detected: {msg}"


###################################################################################
def data_processing(processor: DataProcessor, data: Any) -> None:
    print(f"\nInitializing {processor.__class__.__name__}...")
    result = processor.process(data)
    print("Output:", result)

def data_distribution(data_lst: list) -> None:
    for item in data_lst:
        result = item[0].process(item[1])
        print(f"\nResult {item[1]}: {result}")

if __name__ == "__main__":
    try:
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

        data_processing(NumericProcessor(), [1, 2, 3, 4, 5])
        data_processing(TextProcessor(), "Hello Nexus World")
        data_processing(LogProcessor(), 123)

        print("\n=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")

        processors = [
            (NumericProcessor(), [1, 2, 3]),
            (TextProcessor(), "Hello Nexus"),
            (LogProcessor(), "SUCCESS: System is done")
            ]
        data_distribution(processors)
        print("Foundation systems online. Nexus ready for advanced streams.")
    except Exception as error:
        print(error)
