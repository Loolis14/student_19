#!/usr/bin/env python3

"""First exercise."""

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Define common interface for all subclasses."""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: Any) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Process numeric data."""

    def process(self, data: List) -> str:
        lenght: int = len(data)
        sum_: int = sum(data)
        average: int = sum_ / lenght
        return f"Processed {lenght} numeric values, sum={sum_}, avg={average}"

    def validate(self, data: Any) -> bool:
        for n in data:
            if not isinstance(n, int):
                return False
        return True

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Process text data."""

    def process(self, data: str) -> str:
        char_ = len(data)
        word = len(data.split())
        return f"Processed text: {char_} characters, {word} words"

    def validate(self, data: str) -> bool:
        if isinstance(data, str):
            return True
        return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """Process log data."""

    def process(self, data: str) -> str:
        log: List = data.split()
        return f'[{log[0]}] {log[0]} level detected: {" ".join(log[1:])}'

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            return False
        if data.split()[0] in ["ERROR", "INFO", "WARN", "DEBUG"]:
            return True
        return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    processor: List = [NumericProcessor(), LogProcessor(), TextProcessor()]
    datas: List = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR Connection timeout"
    ]
    for data in datas:
        for process in processor:
            if process.validate(data):
                name: str = process.__class__.__name__.replace("Processor", "")
                print(f'\nInitializing {name} Processor...')
                print(f"Processing data: {data}")
                print(f'Validation: {name} data verified')
                result = process.process(data)
                print(process.format_output(result))
                break
    print("\n=== Polymorphic Processing Demo ===")
