from ms_demo_project.logger import get_logger
from ms_demo_project.features.feature_math import demo_math_operations
from ms_demo_project.features.feature_string import demo_string_operations
from rich import print

logger = get_logger(__name__)

def main():
    logger.info("Starting ms-demo-project demo...")

    # Capture returned results
    math_results = demo_math_operations()
    string_results = demo_string_operations()

    # Display results when logging is off
    if math_results:
        print(f"[cyan]Math Results:[/cyan] {math_results}")
    if string_results:
        print(f"[cyan]String Results:[/cyan] {string_results}")

    logger.info("Demo completed.")
    print("[bold green]✅ Demo completed successfully![/bold green]")

if __name__ == "__main__":
    main()
