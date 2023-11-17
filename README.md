# AnimeBase

AnimeBase is a web application that allows users to store and manage a list of their watched animes. The project utilizes MongoDB Cloud for storage, Flask as the backend framework, and incorporates web scraping to fetch the latest anime news. Additionally, AnimeBase recommends popular anime titles for users to explore and provides links to well-known anime websites.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following dependencies installed:

- Python 3.x
- Flask
- MongoDB
- Beautifulsoup
- (Optional) Virtual environment for Python

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Abhay-1552/AnimeBase.git
   cd AnimeBase
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up MongoDB Cloud:

   - Create a MongoDB Cloud account: [MongoDB Cloud](https://cloud.mongodb.com/)
   - Create a cluster and obtain the connection string.

4. Configure the application:

   - Create a `.env` file in the project root and add the following:

     ```dotenv
     MONGO_URI=<your-mongodb-connection-string>
     ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access AnimeBase.

## Features

- **Anime Watchlist:** Keep track of animes you've watched.
- **Anime News:** Stay updated with the latest anime news using web scraping.
- **Anime Recommendations:** Discover popular anime titles to watch.
- **External Links:** Find links to popular anime websites for more content.

## Contributing

If you'd like to contribute to AnimeBase, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.
