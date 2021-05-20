# DellyBoard

A Soundboard for a 1991 Mitsubishi Delica

## Installation

Only available as source. Clone the repo and use your favorite method to install dependencies, mine is
```
pip install -r requirements.txt
```

## Configuration

See [config/sounds.json](config/sounds.json) for an example configuration.

A set of profiles are configured, each with a hotkey to swap to it.
Each profile contains a set of sounds, each with a hotkey to ply it.

Sound files can be in any format that's compatible with [playsound](https://pypi.org/project/playsound/) on Windows/Mac or `aplay` on Linux.
By default, sound files are read from the [sounds](sounds) directory.

## Usage

Run with
```
python main.py -c <path to your sounds.json file> -s <path to directory with your sound files>
```

Or just
```
python main.py
```
if you're basic.