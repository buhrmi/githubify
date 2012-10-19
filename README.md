# Githubify

This plugin allows you to view a file in Sublime Text 2, and instantly open a browser window showing or blaming the file at the current line (on the current branch) on Github.

## Installation

If you use [Package Control](http://wbond.net/sublime_packages/package_control), just install it from there. If not:

Clone this repo to your Sublime Text 2 Packages folder:

    cd ~/"Library/Application Support/Sublime Text 2/Packages/"
    git clone https://github.com/buhrmi/githubify.git

The plugin should be picked up automatically. If not, restart Sublime Text.

## Usage

Select some text (or not).
Hit Shift+Command+P and choose 'View file on Github' or by keypress (&#8984;+\\ by default, configurable in .sublime-keymap file). Shift+&#8984;+\\ blames the current line.