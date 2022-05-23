# Rofi-Notion

> This script allows you to quickly create new Notion pages for your databases.

*Example:* I use a Notion database as a task tracker for my business. With Rofi-Notion and some key bindings, I can quickly create a new entry in my Notion database without the hassle of waiting and navigating the slow Notion interface.

## Requirements

- Python >= 3.7
- A Notion integration with read and write access to the desired databases.

## Installation

1. Put the script in a permanent location (ex: /opt/rofi-notion)
2. Add a `.env` file at the same location with your Notion integration secret named `API_SECRET`
3. Add a key binding to your favorite key binding manager to run the following command
    ```
    /usr/bin/env python3 /opt/rofi-notion/main.py DESIRED_DATABASE_ID
    ```

**You're done!**
