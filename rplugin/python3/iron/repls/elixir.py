# encoding:utf-8
"""Elixir repl definition for iron.nvim. """
from iron.repls.utils.cmd import detect_fn

iex = {
    'command': 'iex',
    'language': 'elixir',
}

iexmix = {
    'command': 'iex -S mix',
    'language': 'elixir',
    'detect': detect_fn('iex', ['mix.exs']),
}
