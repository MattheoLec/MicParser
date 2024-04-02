# MicParser

A Python script to extracts method names from a microservices Java application.
Take the application root directory as an argument, and saves the extracted methods to a CSV file.

### Prerequisites

- Python 3.x
- Pandas library `pip install pandas`

### Installation & Usage

1. Clone this repository:
   ```shell
   git clone https://github.com/MattheoLec/MicParser.git
   ```

2. Navigate to the project directory:
   ```shell
   cd MicParser
   ```

3. Run the script:
   ```
   python main.py /path/to/java/project
   ```

- Ensure your Java project is structured according to Maven's standard directory layout (src/main/java).

### License

This project is licensed under the MIT License.