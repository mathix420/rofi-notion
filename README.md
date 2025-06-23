# Rofi-Notion

[![wakatime](https://wakatime.com/badge/github/mathix420/rofi-notion.svg)](https://wakatime.com/badge/github/mathix420/rofi-notion) [![Maintainability](https://api.codeclimate.com/v1/badges/5c9f6aa7ba7bf5d8d8bc/maintainability)](https://codeclimate.com/github/mathix420/rofi-notion/maintainability) [![PyPi version](https://badgen.net/pypi/v/rofi-notion/)](https://pypi.org/project/rofi-notion)

> This script allows you to quickly create new Notion pages for your databases.

*Example:* I use a Notion database as a task tracker for my business. With Rofi-Notion and some key bindings, I can quickly create a new entry in my Notion database without the hassle of waiting and navigating the slow Notion interface.


https://user-images.githubusercontent.com/37625778/172062053-0332ab05-2782-482b-97ee-98d33854e58d.mp4

## Requirements

- Python >= 3.7
- A Notion integration with read and write access to the desired databases.

## Installation

### For archlinux users (AUR package)

```bash
yay -S rofi-notion
```
[AUR package details](https://aur.archlinux.org/packages/rofi-notion)

### For everyone else

```bash
pip install rofi-notion
```
[Pypi package details](https://pypi.org/project/rofi-notion/)

## Setup

Check if the installation was successful
```bash
rofi-notion -h
```

### 1. Add your Bot Notion secret

Get your `API_SECRET` by [creating a new Notion integration](https://www.notion.so/my-integrations).

```bash
rofi-notion set-creds
# Then paste your creds
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

**Note:** When filling in fields, press `Escape` to skip optional fields. Required fields (like title) cannot be skipped.

## Add i3 bindings

Simply add a similar line to your i3 config file.
```config
bindsym $mod+Insert exec rofi-notion run $YOUR_DB_NAME
```

## Config

Default config destination is `$XDG_CONFIG_HOME/rofi-notion` or `$HOME/.config/rofi-notion` if `$XDG_CONFIG_HOME` is not set.

## Development

Use this command to run the CLI locally.
```bash
python3 stub.py
```

## Publish

Do not forget to bump versions in `pyproject.toml` and `PKGBUILD`.

### PyPi

~~Run `make` to publish a new version.~~

Git tag the new version and push it.
Then publish the automatically created Draft release.

```
git tag vX.X.X
git push --tags
```

### AUR

First publish new release on GitHub, then run `make aur`.
