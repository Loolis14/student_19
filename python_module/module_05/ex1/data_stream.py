#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str) -> None:
        """Initialize sensors."""
        super().__init__()
        self.stream_id = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        raise NotImplementedError

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    """Stream for sensor data (numbers)."""

    def __init__(self, stream_id: str) -> None:
        """Initialize sensors."""
        print("\nInitializing Sensor Stream...")
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        filtered = self.filter_data(data_batch)
        self.processed_count += len(filtered)
        return (f"Processing sensor batch: [temp:{filtered[0]}, "
                f"humidity:{filtered[1]}, pressure:{filtered[2]}]")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        filtered: List[Any] = []
        for x in data_batch:
            if isinstance(x, (int, float)):
                filtered.append(x)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {'reading processed': 3, 'avg temp': 22.5}


class TransactionStream(DataStream):
    """Stream for transaction data (dicts with amount)."""

    def __init__(self, stream_id: str) -> None:
        """Initialize Transaction transaction."""
        print("\nInitializing Stream...")
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        filtered = self.filter_data(data_batch)
        self.processed_count += len(filtered)
        total: float = sum(item["amount"] for item in filtered)
        return f"Total transaction amount: {total:.2f}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        filtered: List[Any] = []
        for item in data_batch:
            if isinstance(item, dict) and "amount" in item:
                filtered.append(item)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        pass


class EventStream(DataStream):
    """Define a class"""

    def __init__(self, stream_id: str) -> None:
        """Initialize event."""
        print("\nInitializing Event Stream...")
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        filtered = self.filter_data(data_batch)
        self.processed_count += len(filtered)
        return f"{len(filtered)} events processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        filtered: List[Any] = []
        for x in data_batch:
            if isinstance(x, str):
                filtered.append(x)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        stats = super().get_stats()
        stats["type"] = "event"
        return stats


class StreamProcessor():
    """Process any type of DataStream polymorphically."""

    def run(self, stream: DataStream, data: List[Any]) -> None:
        result: str = stream.process_batch(data)
        print(result)
        print("Stats:", stream.get_stats())


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor_data = [22.5, 65, "bad", 1013]
    transaction_data = [{"amount": 100}, {"amount": 50}, "oops"]
    event_data = ["login", "logout", 42, "error"]

    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch(sensor_data))
    sensor_stats = sensor.get_stats()
    print(f"Sensor analysis: {sensor_stats['reading processed']} readings "
          f"processed, avg temp: {sensor_stats['avg temp']}°C")

    transaction = TransactionStream("TRANS_001")
    event = SensorStream("EVENT_001")
"""
    processor = StreamProcessor()

    streams: List[DataStream] = [sensor, transaction, event]
    data_batches: List[List[Any]] = [sensor_data, transaction_data, event_data]

    for stream, data in zip(streams, data_batches):
        processor.run(stream, data)
 """
