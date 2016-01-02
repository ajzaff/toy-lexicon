# -*- coding: utf-8 -*-

from copy import copy


class Tag(object):

    def __init__(self, name, is_head, is_root=False):
        self._is_head = is_head
        self._is_root = is_root
        self._name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    @property
    def is_head(self):
        return self._is_head

    @property
    def is_root(self):
        return self._is_root


class Grammar(object):

    @classmethod
    def combine(cls, lht, rht, settings):
        tag = grammar.get((lht.tag.name, rht.tag.name))
        if tag:
            return tags[tag]

grammar = {

    # Non-terminal
    ('NP', 'VP'): 'S',
    ('DP', 'VP'): 'S',
    ('AP', 'NP'): 'NP',
    ('VP', 'PP'): 'VP',
    ('AP', 'PP'): 'NP',
    ('NP', 'PP'): 'NP',

    # Terminal
    ('D', 'NP'): 'DP',
    ('D', 'AP'): 'DP',
    ('N', 'NP'): 'NP',
    ('N', 'PP'): 'NP',
    ('P', 'DP'): 'PP',
    ('P', 'NP'): 'PP',
    ('P', 'AP'): 'PP',
    ('Adj', 'NP'): 'AP',
    ('Adj', 'PP'): 'AP',
    ('Adv', 'DP'): 'AdvP',
    ('Adv', 'PP'): 'AdvP',
}

# Heads
heads = {
    'D': Tag('D', is_head=True),
    'N': Tag('N', is_head=True),
    'V': Tag('V', is_head=True),
    'P': Tag('P', is_head=True),
    'Adj': Tag('Adj', is_head=True),
    'Adv': Tag('Adv', is_head=True)
}

# Phrases
phrases = {
    'DP': Tag('DP', is_head=False),
    'NP': Tag('NP', is_head=False),
    'VP': Tag('VP', is_head=False),
    'PP': Tag('PP', is_head=False),
    'AP': Tag('AP', is_head=False),
    'AdvP': Tag('AdvP', is_head=False),
    'S': Tag('S', is_head=False, is_root=True)
}

tags = copy(heads)
tags.update(phrases)

phrase_map = {
    'D': phrases['DP'],
    'N': phrases['NP'],
    'V': phrases['VP'],
    'P': phrases['PP'],
    'Adj': phrases['AP'],
    'Adv': phrases['AdvP']
}