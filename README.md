# quotes
A simple command line utility to save and view quotes.

Made during Calhacks 5.0.

## Installation
Run `install.sh`. This needs permission to add `quotes` to the `/usr/local/bin` folder and to create `/var/lib/quotes` to save data.
Feel free to delete the folder after completion.
Run `uninstall.sh` to uninstall `quotes`.

## Usage
`quotes display --user [name] --random`

`quotes add [user] [quote]`

`quotes search [phrase] --user [name] --delete`

`quotes merge [users]`

## Recent changes
Added error handling.

Changed save format into JSON.

Added install/uninstall script.

## Todo
Better install/uninstall, maybe add a `Makefile`

Add update script

Add import and export options

Turn into webapp?
