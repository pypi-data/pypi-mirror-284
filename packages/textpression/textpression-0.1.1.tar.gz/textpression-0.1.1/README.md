# `textpression`
Textpression is a toolkit for formatting text for silly chats with silly people. 

It is designed as a cli for making expressive text using unicode small, subscript, and small caps. There are many tools online that do this, but I wanted one I could use offline.

## Usage
```sh
textpression --help

textpression small oh no whatever will i do!
# > ᵒʰ ⁿᵒ ʷʰᵃᵗᵉᵛᵉʳ ʷᶦˡˡ ᶦ ᵈᵒᵎ
```

-------

## Development
1. Check python version .tool-versions (asdf)
2. Install pipenv `pip install pipenv`
3. install dependencies and setup env: `pipenv install`

### Install locally for testing
```sh
# install local package (probably do this in your venv)
pip install -e .

textpression --help
textpression small whoopsie
# ʷʰᵒᵒᵖˢᶦᵉ
```