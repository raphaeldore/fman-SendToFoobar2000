# SendToFoobar2000

[fman](https://fman.io) plugin to send files or folders to [Foobar2000](http://foobar2000.org/) from fman.

## Usage

The plugin allows to send a single file or folder, or a selection of files and/or folders to Foobar2000. To call the plugin, you use the shortcut `CTRL+M` (or you can call the `Send to foobar2000` command from the Command Palette) to send the file(s) or folder(s) to Foobar2000. Note that the files will be appended to the end of the default Foobar2000 playlist, so this will not overwrite your playlist.

So, for example:

* If your cursor is over the file `foo.mp3`, and you execute the plugin, then that file will be appended to the default Foobar2000 playlist.
* The same thing occurs if you select (with the spacebar) the files `foo.mp3` and `bar.mp3`.
* The same behavior applies to folders.

## First run

The first time you execute the plugin, you will be asked to locate your foobar2000 executable. By default, the file selection dialog should open at the default install location of foobar2000, which is `C:\Program Files (x86)\foobar2000`. Once this is done, there will be no further interruptions of the sort.

## Installation

Use fman's [built-in command for installing plugins](https://fman.io/docs/installing-plugins).