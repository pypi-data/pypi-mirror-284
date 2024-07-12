This repository contains a stash plugin package for [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme). 

See [yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#plugins) for more details.


## Installation

Requires yt-dlp as well as stashapp-tools.

You can install this package with pip:
```shell
python3 -m pip install -U https://github.com/schmoaaaaah/yt-dlp-stash/archive/master.zip
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.


## Usage

To use this plugin, you must have a stash server running and add following to your yt-dlp command:
```shell
--use-postprocessor Stash:scheme="http"\;host="stash"\;port="9999"\;apikey="example_key"\;when=after_video
```
The apikey is optional and can be left out if you dont have authentication enabled.
```shell
--use-postprocessor Stash:scheme="http"\;host="stash"\;port="9999"\;when=after_video
```
### Variables

|name|default|required|description|
|---|---|---|---|
|scheme|http|x|scheme at which stash is available. either http or https|
|host|localhost|x|fqdn of the stash instance|
|port|9999|x| port on which stash is accessable|
|apikey||| api key which should be used
|sessioncookie|||sessioncookie which should be used|

if api key and sessioncookie are provided api key is preferred.

You might need to change `after_video` to `playlist` if you are downloading a playlist.
I haven't tested this yet.

The Processor expects the same path for the media in stash as it is downloaded.

## Development

See the [Plugin Development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development) section of the yt-dlp wiki.
