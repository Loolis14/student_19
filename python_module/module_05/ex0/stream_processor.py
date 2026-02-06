#!/usr/bin/env python3

"""First exercise."""

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Define common interface for all subclasses."""

    def __init__(self) -> None:
        """Initialize an abstract class."""
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Initiliaze an abstract method."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Initiliaze an abstract method."""
        pass

    def format_output(self, result: Any) -> str:
        """Format output for child class"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Process numeric data."""

    def process(self, data: List[int]) -> str:
        if not data:
            return "No numeric values to process"
        lenght: int = len(data)
        sum_: int = sum(data)
        average: int = sum_ / lenght
        return f"Processed {lenght} numeric values, sum={sum_}, avg={average}"

    def validate(self, data: Any) -> bool:
        try:
            for n in data:
                _ = n + 0
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    """Process text data."""

    def process(self, data: str) -> str:
        if not data:
            return "No text values to process"
        char_ = len(data)
        word = len(data.split())
        return f"Processed text: {char_} characters, {word} words"

    def validate(self, data: str) -> bool:
        try:
            data.split()
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    """Process log data."""

    def process(self, data: str) -> str:
        log: List = data.split()
        return f'[{log[0]}] {log[0]} level detected: {" ".join(log[1:])}'

    def validate(self, data: str) -> bool:
        try:
            first_word = data.split()[0]
        except Exception:
            return False
        if first_word in ["ERROR", "INFO", "WARN", "DEBUG"]:
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
