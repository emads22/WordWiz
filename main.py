import logging
from pprint import pprint
from definition import Definition
from config import LOG_FILE, DATA_FILE


# Create the directory for log files if it doesn't exist, and Ensure parent directories are created if they don't exist
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# Configure the logging format and level
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s - %(levelname)s - %(message)s (%(module)s:%(filename)s:%(lineno)d)',
                    level=logging.DEBUG)


def main():
    try:
        word = input("\n- Enter word: ")

        print(f"\n\n>> Definitions of {word}:\n\n")

        pprint(Definition(word).get())

        print("\n\n")

    except Exception as e:
        # Log any exceptions that occur during the execution of the main function
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
