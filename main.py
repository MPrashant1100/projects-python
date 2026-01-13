from io_utils import read_json, write_json
from processor import process_scores
from validators import validate_input
from logger import get_logger

logger = get_logger()

def main():
    try:
        logger.info("Starting DataForge pipeline")

        data = read_json("data/input.json")
        validate_input(data)

        result = process_scores(data)

        write_json("output/result.json", result)
        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
