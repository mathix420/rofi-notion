# Rofi-Notion

[![wakatime](https://wakatime.com/badge/user/32448728-a0db-4c3d-a9a6-a4f778c67d05/project/0134b71d-7b21-44b2-8c75-3bde6a5859e9.svg)](https://wakatime.com/badge/user/32448728-a0db-4c3d-a9a6-a4f778c67d05/project/0134b71d-7b21-44b2-8c75-3bde6a5859e9)

> This script allows you to quickly create new Notion pages for your databases.

*Example:* I use a Notion database as a task tracker for my business. With Rofi-Notion and some key bindings, I can quickly create a new entry in my Notion database without the hassle of waiting and navigating the slow Notion interface.

## Requirements

- Python >= 3.7
- A Notion integration with read and write access to the desired databases.

## Installation

1. Clone the repo in a permanent location (ex: /opt/rofi-notion) (you want to use symlinks)
2. Add a `.env` file at the same location with your Notion integration secret named `API_SECRET`
3. Add a key binding to your favorite key binding manager to run the following command
    ```
    /usr/bin/env python3 /opt/rofi-notion DESIRED_DATABASE_ID
    ```

<!-- ### Alternative option

You can also use this script with **rofi modi**
1. Create a script like this one `/opt/rofi-notion/run.sh`
    ```sh
    #! /usr/bin/env bash
    /usr/bin/env python3 /opt/rofi-notion DESIRED_DATABASE_ID
    ```
2. `chmod +x /opt/rofi-notion/run.sh`
3. Use this line to run `rofi` with a `modi` config
    ```
    rofi --no-startup-id -modi "Quick Notion:/opt/rofi-notion/run.sh" -show "Quick Notion"
    ``` -->


## Exemple `.env`

Get your `API_SECRET` by [creating a new integration](https://www.notion.so/my-integrations).

```
API_SECRET=secret_AaAAaaAaAaaaaAaaAAAAAaAaAaaaaAAaaAaAAAAAAAa
```
