#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def process(self, data: List) -> str:
        return "".join(str(data))

    def validate(self, data: Any) -> bool:
        for n in data:
            try:
                int(n)
            except Exception:
                print(f'{n} is not a number')
                return False
        return True

    def format_output(self, result: str) -> str:
        return f"Ouput: {result}"


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        return data

    def validate(self, data: Any) -> bool:
        try:
            str(data)
        except Exception:
            print(f'{data} is not a string')
            return False
        return True

    def format_output(self, result: str) -> str:
        return result + "Processed text: 17 characters, 3 words"


class LogProcessor(DataProcessor):
    def process(self, data: Dict) -> str:
        return data

    def validate(self, data: Any) -> bool:
        try:
            data.keys()
        except Exception:
            print(f'{data} is not a dictionnary')
            return False
        return True

    def format_output(self, result: str) -> str:
        return result + "2 players on server"


def test():
    print("\nInitializing Numeric Processor...")
    a = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    result = "Output: "
    print(f'Processing data: {a.process(data)}')
    if a.validate(data):
        print("Validation: Numeric data verified")
    else:
        print("Wrong: Numeric data not verified")
    print(a.format_output(result))

    print("\nInitializing Text Processor...")
    b = TextProcessor()
    sentence = "Hello Nexus World"
    print(f'Processing data: {b.process(sentence)}')
    if b.validate(sentence):
        print("Text data verified")
    else:
        print("Text data not verified")
    print(b.format_output(result))

    print("\nInitializing Log Processor...")
    c = LogProcessor()
    dictionnary = {'Charlie': "active", 'Alice': "log out"}
    print(f'Processing data: {c.process(dictionnary)}')
    if c.validate(dictionnary):
        print("Log data verified")
    else:
        print("Log data not verified")
    print(c.format_output(result))


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    test()
