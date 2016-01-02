# -*- coding: utf-8 -*-

import konig.lextree


class Chart(list):

    def __init__(self, n):
        super(Chart, self).__init__([[[] for _ in range(n)] for _ in range(n)])
        self._n = n

    def dump(self):
        padding = [0 for _ in range(self.n)]
        for row in self:
            for i, es in enumerate(row):
                padding[i] = max(padding[i], len(str(es)))
        print('=' * (self.n + sum(padding) - 1))
        for row in self:
            def row_mapper(ee):
                return str(ee[1]).ljust(padding[ee[0]])
            row_enum = enumerate(row)
            row_map = map(row_mapper, row_enum)
            print(' '.join(row_map))
        print('=' * (self.n + sum(padding) - 1))

    @property
    def n(self):
        return self._n


class HeadSettings(object):

    left = True
    right = False

    def __init__(self, head=left):
        self._head_left = head

    @property
    def head_left(self):
        return self._head_left

    @property
    def head_right(self):
        return not self.head_left


def decode(tokens, lexicon, settings=None):
    """
    A CYK decoder
    :param tokens: (list[str])
    :param lexicon: map[str -> lexeme.Lexeme]
    :param settings: HeadSettings
    :return: Chart
    """

    if settings is None:
        settings = HeadSettings()

    n = len(tokens)
    chart = Chart(n)

    # base cases
    for i in range(n):
        chart[i][i].extend(lexicon[tokens[i]])

    # dove-tailing
    for i in range(1, n):
        j = 0
        k = i
        while k < n:
            # Explore candidates
            for m in range(k, 0, -1):
                lhc = chart[j][k-m]
                rhc = chart[j+i-m+1][k]
                if len(lhc and rhc) == 0:
                    continue

                for lhs in lhc:
                    for rhs in rhc:
                        print('compare', lhs, '+', rhs)
                        parses = konig.lextree.LexTree.compose(lhs, rhs, settings=settings)
                        chart[j][k].extend(parses)

            # Iterate
            j += 1
            k += 1

    return chart
