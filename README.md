# Rofi-Notion

[![wakatime](https://wakatime.com/badge/github/mathix420/rofi-notion.svg)](https://wakatime.com/badge/github/mathix420/rofi-notion)


https://user-images.githubusercontent.com/37625778/172062053-0332ab05-2782-482b-97ee-98d33854e58d.mp4


> This script allows you to quickly create new Notion pages for your databases.

*Example:* I use a Notion database as a task tracker for my business. With Rofi-Notion and some key bindings, I can quickly create a new entry in my Notion database without the hassle of waiting and navigating the slow Notion interface.

## Requirements

- Python >= 3.7
- A Notion integration with read and write access to the desired databases.

## Installation

```bash
pip install rofi-notion
```

## Usage

```bash
rofi-notion -h
```

### 1. Add your Bot Notion secret

Get your `API_SECRET` by [creating a new Notion integration](https://www.notion.so/my-integrations).

```bash
rofi-notion set-creds $YOUR_API_SECRET
```

### 2. Link your first database

```bash
rofi-notion link
# Follow instructions
```

### 3. Run `rofi-notion`

```bash
rofi-notion run $YOUR_DB_NAME
```

## Add i3 bindings

Simply add a similar line to your i3 config file.
```config
bindsym $mod+Insert exec rofi-notion run $YOUR_DB_NAME
```
