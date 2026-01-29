from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        # default implementation
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: List[int]) -> str:
        total = sum(data)
        avg = total / len(data) if data else 0
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(isinstance(n, (int, float)) for n in data)

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        words = len(data.split())
        chars = len(data)
        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        # check level
        if data.startswith("ERROR"):
            level = "ALERT"
        elif data.startswith("INFO"):
            level = "INFO"
        else:
            level = "LOG"
        message = data.split(":", 1)[1].strip() if ":" in data else data
        return f"[{level}] {message}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


# Polymorphic demo
def main():
    processors = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), "ERROR: Connection timeout")
    ]

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    for processor, data in processors:
        print(f"Initializing {processor.__class__.__name__}...")
        if processor.validate(data):
            processed = processor.process(data)
            output = processor.format_output(processed)
            print(f"Processing data: {data}")
            print(f"Validation: {processor.__class__.__name__} data verified")
            print(output)
        else:
            print("Validation failed")
        print()


if __name__ == "__main__":
    main()
