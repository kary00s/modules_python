from abc import ABC, abstractmethod
from typing import List, Any, Dict, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "type": self.__class__.__name__,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Data batch must be a list")

        self.processed_count += len(data_batch)

        temps = [item.get("temp", 0) for
                 item in data_batch if isinstance(item, dict)]
        if len(data_batch) != 0:
            avg_temp = sum(temps) / len(data_batch)
        else:
            avg_temp = 0
        ret_val = f"Sensor analysis: {len(data_batch)} readings processed,"
        ret_val += f" avg temp: {avg_temp:.1f}°C"
        return ret_val

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria and "high-priority" in criteria.lower():
            return [
                item for item in data_batch
                if (isinstance(item, dict) and (item.get("temp", 0) > 30
                    or item.get("alert") == "critical"))
                or ("critical" in str(item).lower())
            ]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Data batch must be a list")

        self.processed_count += len(data_batch)

        net = 0
        for item in data_batch:
            if isinstance(item, dict):
                if item.get("type") == "buy":
                    net += item.get("amount")
                elif item.get("type") == "sell":
                    net -= item.get("amount", 0)
            else:
                raise ValueError("Data batch must be a list of dict")
        ret_val = f"Transaction analysis: {len(data_batch)} "
        ret_val += f"operations, net flow: {net} units"
        return ret_val

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria and "high-priority" in criteria.lower():
            return [
                item for item in data_batch
                if (isinstance(item, dict) and item.get("amount", 0) > 100)
                or (isinstance(item, (int, float)) and abs(item) > 100)
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.error_count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise ValueError("Data batch must be a list")

        self.processed_count += len(data_batch)

        errors = sum(1 for item in data_batch if isinstance
                     (item, str) and "error" in item.lower())
        self.error_count += errors

        word = "error" if errors == 1 else "errors"
        ret_val = f"Event analysis: {len(data_batch)}"
        ret_val += f"events, {errors} {word} detected"
        return ret_val


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_mixed_batches(self, batches: List[List[Any]]) -> None:
        if len(batches) != len(self.streams):
            raise ValueError("Number of batches must match number of streams")

        print("Batch 1 Results:")

        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = batches[i]

            result = stream.process_batch(batch)

            if isinstance(stream, SensorStream):
                summary = result.replace("Sensor analysis: ", "")
                print(f"- Sensor data: {summary}")

            elif isinstance(stream, TransactionStream):
                summary = result.replace("Transaction analysis: ", "")
                print(f"- Transaction data: {summary}")

            elif isinstance(stream, EventStream):
                summary = result.replace("Event analysis: ", "")
                print(f"- Event data: {summary}")

            else:
                print(f"- {stream.stream_id}: {result}")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type:  Environmental Data")

    sensor_batch = [{"temp": 22.5, "humidity": 65, "pressure": 1013},
                    {"temp": 22.5, "humidity": 65, "pressure": 1013},
                    {"temp": 22.5, "humidity": 65, "pressure": 1013}]
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(sensor_batch))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")
    trans_batch = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ]
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(trans_batch))

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"\nStream ID: {event.stream_id}, Type: System Events")
    event_batch = ["login", "error", "logout"]
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    mixed_sensor_batch = [{"temp": 35}, {"temp": 40}]
    mixed_trans_batch = [
        {"type": "buy", "amount": 50},
        {"type": "buy", "amount": 200},
        {"type": "sell", "amount": 30},
        {"type": "sell", "amount": 40}
    ]
    mixed_event_batch = ["login", "logout", "error"]

    processor.process_mixed_batches([mixed_sensor_batch,
                                     mixed_trans_batch, mixed_event_batch])

    print("Stream filtering active: High-priority data only")

    filtered_sensor = sensor.filter_data(mixed_sensor_batch, "high-priority")
    filtered_trans = trans.filter_data(mixed_trans_batch, "high-priority")

    print(f"Filtered results: {len(filtered_sensor)} "
          f"critical sensor alerts, {len(filtered_trans)} large transaction")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
