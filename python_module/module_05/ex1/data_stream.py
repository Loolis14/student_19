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
        self.avg_temp: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        filtered = self.filter_data(data_batch)
        self.processed_count += len(filtered)
        self.avg_temp = filtered[0]
        return (f"Processing sensor batch: [temp:{filtered[0]}, "
                f"humidity:{filtered[1]}, pressure:{filtered[2]}]")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        filtered: List[Any] = []
        for x in data_batch:
            if isinstance(x, (int, float)):
                if criteria == "critical":
                    if x > 50:
                        filtered.append(x)
                else:
                    filtered.append(x)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        stats = super().get_stats()
        stats['avg temp'] = round(self.avg_temp, 1)
        return stats


class TransactionStream(DataStream):
    """Stream for transaction data (dicts with amount)."""

    def __init__(self, stream_id: str) -> None:
        """Initialize Transaction transaction."""
        print("\nInitializing Transaction Stream...")
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: Financial Data")
        self.money: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        filtered = self.filter_data(data_batch)
        self.processed_count += len(filtered)
        result: List[str] = []
        for action in filtered:
            for key, value in action.items():
                if key == 'buy':
                    self.money -= value
                    result.append(f'buy:{value}')
                elif key == 'sell':
                    self.money += value
                    result.append(f'sell:{value}')
        return f"Processing transaction batch: {", ".join(result)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        filtered: List[Any] = []
        for item in data_batch:
            if isinstance(item, dict):
                if criteria == "critical":
                    if item.get("sell", 0) > 100:
                        filtered.append(item)
                else:
                    filtered.append(item)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "processed": self.processed_count,
            "bank_account": self.money
        }


class EventStream(DataStream):
    """Define a class"""

    def __init__(self, stream_id: str) -> None:
        """Initialize event."""
        print("\nInitializing Event Stream...")
        super().__init__(stream_id)
        self.error: int = 0
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        filtered = self.filter_data(data_batch)
        self.processed_count += len(filtered)
        for event in filtered:
            if event == "error":
                self.error += 1
        return f"Processing transaction batch: {filtered}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on criteria."""
        filtered: List[Any] = []
        for x in data_batch:
            if isinstance(x, str) and x in ["login", "logout", "error"]:
                filtered.append(x)
        return filtered

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        stats = super().get_stats()
        stats["error"] = self.error
        return stats


class StreamProcessor():
    """Process any type of DataStream polymorphically."""

    def run(self, stream: DataStream, data: List[Any]) -> None:
        stream.process_batch(data)
        result = stream.get_stats()
        print(f"- {stream.__class__.__name__}: "
              f"{result['processed']} processed")

    def test_criteria(self, streams: List[DataStream],
                      data_batches: List[List[Any]],
                      criteria: Optional[str]) -> None:
        print("\nStream filtering active: High-priority data only")

        critical_sensors: int = 0
        large_transactions: int = 0

        for stream, data in zip(streams, data_batches):
            filtered = stream.filter_data(data, criteria)

            if isinstance(stream, SensorStream):
                critical_sensors += len(filtered)
            elif isinstance(stream, TransactionStream):
                large_transactions += len(filtered)

        print(f"Filtered results: {critical_sensors} critical sensor alerts, "
              f"{large_transactions} large transaction")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor_data = [22.5, 65, "bad", 1013]
    transaction_data = [{"buy": 100}, {"sell": 50}, {"buy": 75}]
    event_data = ["login", "logout", 42, "error"]

    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch(sensor_data))
    sensor_stats = sensor.get_stats()
    print(f"Sensor analysis: {sensor_stats['processed']} readings "
          f"processed, avg temp: {sensor_stats['avg temp']}°C")

    transaction = TransactionStream("TRANS_001")
    print(transaction.process_batch(transaction_data))
    transaction_stats = transaction.get_stats()
    print(f"Transaction analysis: {transaction_stats['processed']} operations"
          f", net flow: {transaction_stats['bank_account']} units")

    event = EventStream("EVENT_001")
    print(event.process_batch(event_data))
    event_stats = event.get_stats()
    print(f'Event analysis: {event_stats['processed']} events, '
          f'{event_stats['error']} error detected')

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    processor = StreamProcessor()
    data_batches: List[List[Any]] = [
        [22.5, 65, "bad", 1013],
        [{"buy": 100}, {"sell": 50}, {"buy": 75}, {"sell": 900}],
        ["login", "logout", 42, "error", "login", "error"]
    ]

    streams: List[DataStream] = [sensor, transaction, event]
    print("\nBatch 1 Results:")
    for stream, data in zip(streams, data_batches):
        processor.run(stream, data)

    processor.test_criteria(streams, data_batches, "critical")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
