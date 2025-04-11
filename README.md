# Message Intensity Analyzer

This module generates a daily message activity graph from chat data exported from Telegram. The graph visualizes how many messages were sent per day in a specific chat.

> **Tags:** Python, JSON, Matplotlib, Pandas

## 📥 Input Data Format

Expecting a Telegram export in JSON format (no media required), with a structure like this:

```json
{
  "chats": {
    "list": [
      {
        "name": "Person",
        "type": "personal_chat",
        "id": 123456789,
        "messages": [
          {
            "id": 1234,
            "type": "message",
            "date": "2017-08-27T20:15:06",
            "from": "Me",
            "from_id": 5647,
            "text": "Test"
          }
        ]
      }
    ]
  }
}
```

## 📤 Output
A line chart showing message activity over time and a corresponding Excel file.
[![A screenshot from excel](https://raw.githubusercontent.com/ellkrauze/tg_chat_graph/master/graphics.JPG)]()

## 🚀 Usage
1. Make sure Python 3.10+ is installed.

1. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
1. Export your Telegram chat as JSON (without media).
1. Run the script:
     ```bash
     python tg_chat_graph.py -i result.json
     ```
1. Your results will be saved as plot.png and output.xlsx.

> You can also checkout [main.ipynb](main.ipynb) for Python usage examples with additional time series analysis.