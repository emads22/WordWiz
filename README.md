# WordWiz: Instant Dictionary

## Overview (Update)
**Update**: WordWiz now utilizes the WordWiz-API for fetching word definitions in real-time. Ensure that the WordWiz-API server is running and accessible at [http://localhost:8080](http://localhost:8080) for the application to function correctly.

WordWiz is a web application built on Object-Oriented Programming principles that provides instant word definitions as you type, offering an effortless way to explore language in real-time. With a user-friendly interface and multiple pages, WordWiz simplifies the process of discovering and expanding your vocabulary.

## Features
- **Real-time Definitions**: Get instant definitions for any English word as you type.
- **User-Friendly Interface**: Enjoy a simple and intuitive interface for seamless user experience.
- **Multiple Pages**: Includes home, about, and dictionary pages for comprehensive functionality.
- **Custom Logger**: Easily add a custom logger to track and manage application logs efficiently. Users are free to adjust custom logging settings by modifying the `AppLogger` class according to their requirements.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Place your additional data in the `resources/data.csv` file to expand the dictionary.
5. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).
3. Navigate between the home, about, and dictionary pages to explore the functionality.
4. Use the dictionary page to instantly discover word definitions.

## WordWiz-API
WordWiz now utilizes the WordWiz-API for fetching word definitions in real-time. Ensure that the WordWiz-API server is running and accessible at [http://localhost:8080](http://localhost:8080) for the application to function correctly. For more details about the WordWiz-API, visit its repository on [WordWiz-API](https://github.com/emads22/WordWiz-API.git).

## API Documentation
Explore the WordWiz-API documentation to understand its endpoints and usage. Access the API documentation at [http://localhost:8000/api-docs](http://localhost:8000/api-docs).

Feel free to explore and enjoy the WordWiz web application!

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.