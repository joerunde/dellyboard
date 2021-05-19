# TibiAlerter

Hotkey alerts for Tibia. Uses cross-platform python libraries to support both Mac and Windows.

Have you ever had teammates pissed off that you forgot to cast Enchant Party?
Have you ever died because you forgot to renew you magic shield or invisibility spell?
Do you just want a reminder every 10 minutes to make a new stack of diamond arrows?

This stupid app listens for hotkey presses, and will play sounds at a configurable delay after the last time each hotkey is pressed.

## Installation

Only available as source. Clone the repo and use your favorite method to install dependencies, mine is
```
pip install -r requirements.txt
```

## Configuration

See [config/alerts.json](config/alerts.json) for an example configuration.

Each alert is configured with the hotkey to listen for, a delay to wait in seconds, and a sound to play when that much time has passed since the last time the hotkey was pressed.
Multiple alerts can be configured for a single hotkey, e.g. you can set a 10 minute alert for your diamond arrow hotkey, and an 11 minute alert for when you're dumb and miss the first one.

Sound files can be in any format that's compatible with [playsound](https://pypi.org/project/playsound/). By default files are read from the [sounds](sounds) directory.

## Usage

Run with
```
python main.py -c <path to your alerts.json file> -s <path to directory with your sound files>
```

Or just
```
python main.py
```
if you're basic.