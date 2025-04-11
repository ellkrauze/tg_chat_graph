import os
import argparse
import logging
import utils

logger = logging.getLogger(__name__)


def create_diagram(file_path: str, output_dir: str):
    """Main function to load, analyze, and output diagram and Excel data."""
    logger.info("Reading input data...")
    messages = utils.load_chat_data(file_path)
    dates = utils.extract_dates(messages)
    daily_counts = utils.count_messages_per_day(dates)

    os.makedirs(output_dir, exist_ok=True)

    plot_path = os.path.join(output_dir, "plot.png")
    excel_path = os.path.join(output_dir, "output.xlsx")

    utils.save_plot(daily_counts, plot_path)
    utils.save_to_excel(daily_counts, excel_path)

    logger.info(f"Diagram saved to: {plot_path}")
    logger.info(f"Excel file saved to: {excel_path}")


def parse_arguments():
    """Set up CLI argument parsing."""
    parser = argparse.ArgumentParser(
        description="Generate a daily message count diagram and Excel report from Telegram JSON export."
    )
    parser.add_argument(
        "-i", "--input", required=True,
        help="Path to the Telegram chat JSON file"
    )
    parser.add_argument(
        "-o", "--output", default=".",
        help="Directory to save output files (default: current directory)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    create_diagram(args.input, args.output)
