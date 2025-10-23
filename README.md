# Python Github Follower Scraper

This project is a sophisticated Python application that utilizes the **Selenium framework** for automated web scraping of GitHub follower lists. The script is designed to navigate dynamic web pages, manage user authentication (login), and collect data efficiently, including handling pagination (navigating 'Next' pages).

This repository showcases strong skills in **Web Automation**, **Object-Oriented Programming (OOP)**, and handling modern web elements.

## Key Features

* **Browser Automation (Selenium):** Fully automates the process of opening the browser, navigating to the login page, and submitting credentials.
* **Authentication:** Includes a dedicated method for user sign-in to access profile-specific data.
* **Dynamic Content Handling:** Effectively uses Selenium locators to find and extract usernames from the follower list.
* **Pagination Management:** Implements a loop to automatically click the 'Next' button and iterate through all available follower pages to ensure complete data retrieval.
* **Data Retrieval:** Collects all follower usernames into a dedicated list and prints the total count and the list itself.

## Technologies Used

* **Language:** Python 3
* **Libraries/Frameworks:**
    * **Selenium WebDriver:** For browser automation and interaction.
    * **time:** For managing necessary delays during page loading and interactions.
* **Design Pattern:** Object-Oriented Programming (OOP) with a dedicated `Github` class.

## Setup and Execution

Follow these steps to set up and run the application locally.

### 1. Prerequisites

* **Python:** Ensure Python 3 is installed.
* **Web Driver:** You must have the appropriate browser driver (e.g., **ChromeDriver**) installed and accessible in your system's PATH, or specify its location in the code.

### 2. Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/muratkazma0/github-follower-scraper
    cd github-follower-scraper
    ```
2.  **Install Dependencies:**
    This project requires the `selenium` library. Install it using pip:
    ```bash
    pip install selenium
    ```

### 3. Configuration

Open the main file (`github_follower_scraper.py`) and replace the placeholder credentials with the user's actual GitHub username and password to enable the login process.

### 4. Execution

Run the main Python file from your terminal:
```bash
python github_follower_scraper.py
