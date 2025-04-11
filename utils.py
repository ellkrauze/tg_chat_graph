import logging
from collections import Counter
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)


def load_chat_data(file_path: str) -> list:
    """Load Telegram chat JSON data and return messages list."""
    df = pd.read_json(file_path)

    try:
        messages = df["messages"].values
    except (KeyError, IndexError) as e:
        raise ValueError("Invalid or unexpected Telegram export format.") from e

    return messages


def extract_dates(messages: list) -> list:
    """Extract and normalize date strings to date objects."""
    date_arr = []
    for message in messages:
        if "date" in message:
            try:
                date_obj = datetime.fromisoformat(message["date"]).date()
                date_arr.append(date_obj)
            except ValueError:
                continue  # skip malformed dates
    return date_arr


def count_messages_per_day(dates: list) -> Counter:
    """Count the number of messages per day."""
    return Counter(dates)


def save_plot(counter: Counter, output_path: str):
    """Generate and save a bar chart of messages per day."""
    plt.figure(figsize=(16, 6))
    plt.bar(counter.keys(), counter.values())
    plt.xlabel("Date")
    plt.ylabel("Number of Messages")
    plt.title("Daily Message Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_to_excel(counter: Counter, output_path: str):
    """Save message counts to Excel."""
    df = pd.DataFrame.from_dict(counter, orient="index", columns=["Messages"])
    df.index.name = "Date"
    df.reset_index(inplace=True)
    df.to_excel(output_path, index=False)
