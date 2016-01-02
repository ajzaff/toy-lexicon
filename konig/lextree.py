# -*- coding: utf-8 -*-

import konig.grammar


class Type(object):
    t = 't'
    e = 'e'
    ε = 'ε'
    t_t = t, t
    e_t = e, t
    e_e = e, e
    ε_t = ε, t
    e_et = e, e_t
    e_εt = e, ε_t
    et_t = e_t, t
    et_e = e_t, e
    et_et = e_t, e_t
    et_ett = e_t, et_t
    ett_et = et_t, e_t

    @classmethod
    def domain(cls, typ):
        if isinstance(typ, tuple):
            return typ[0]
        else:
            return None

    @classmethod
    def range(cls, typ):
        if isinstance(typ, tuple):
            return typ[1]
        else:
            return typ

    @classmethod
    def str(cls, typ):
        s = str(typ)
        s = s.replace("'", '')
        s = s.replace('(', '<')
        s = s.replace(')', '>')
        s = s.replace(' ', '')
        return s


class Rule(object):

    fal = 'FAL'  # function application (head left)
    far = 'FAR'  # function application (head right)
    pml = 'PML'  # predicate modification (head left)
    pmr = 'PMR'  # predicate modification (head right)
    eil = 'EIL'  # event indication (head left)
    eir = 'EIR'  # event indication (head right)

    @classmethod
    def test_fal(cls, lhs, rhs, settings):
        if lhs.tag.is_head and settings.head_right:
            return False
        return lhs.domain == rhs.type

    @classmethod
    def test_far(cls, lhs, rhs, settings):
        if rhs.tag.is_head and settings.head_left:
            return False
        return lhs.type == rhs.domain

    @classmethod
    def test_pml(cls, lhs, rhs, settings):
        if lhs.tag.is_head and settings.head_right:
            return False
        return lhs.type == rhs.type == Type.e_t

    @classmethod
    def test_pmr(cls, lhs, rhs, settings):
        if rhs.tag.is_head and settings.head_left:
            return False
        return lhs.type == rhs.type == Type.e_t

    @classmethod
    def test_eil(cls, lhs, rhs, settings):
        if lhs.tag.is_head and settings.head_right:
            return False
        return lhs.type == Type.ε_t and rhs.type == Type.e_εt

    @classmethod
    def test_eir(cls, lhs, rhs, settings):
        if rhs.tag.is_head and settings.head_left:
            return False
        return lhs.type == Type.e_εt and rhs.type == Type.ε_t


class LexTree(object):

    def __init__(self, tokens, typ, tag, left=None, right=None, rule=None):
        self._is_head = tag.is_head
        self._dom = Type.domain(typ)
        self._rng = Type.range(typ)
        self._tokens = tokens
        self._right = right
        self._left = left
        self._rule = rule
        self._type = typ
        self._tag = tag

    @classmethod
    def compose(cls, lhs, rhs, settings):
        combos = []
        new_tokens = lhs.tokens + rhs.tokens
        new_tag = konig.grammar.Grammar.combine(lhs, rhs, settings)
        print('=', new_tag)
        if new_tag:
            if Rule.test_fal(lhs, rhs, settings):
                combos.append(LexTree(new_tokens, lhs.range, new_tag, left=lhs, right=rhs, rule=Rule.fal))
            elif Rule.test_far(lhs, rhs, settings):
                combos.append(LexTree(new_tokens, rhs.range, new_tag, left=lhs, right=rhs, rule=Rule.far))
            elif Rule.test_pml(lhs, rhs, settings):
                combos.append(LexTree(new_tokens, Type.e_t, new_tag, left=lhs, right=rhs, rule=Rule.pml))
            elif Rule.test_pmr(lhs, rhs, settings):
                combos.append(LexTree(new_tokens, Type.e_t, new_tag, left=lhs, right=rhs, rule=Rule.pmr))
            elif Rule.test_eil(lhs, rhs, settings):
                combos.append(LexTree(new_tokens, Type.e_εt, new_tag, left=lhs, right=rhs, rule=Rule.eil))
            elif Rule.test_eir(lhs, rhs, settings):
                combos.append(LexTree(new_tokens, Type.e_εt, new_tag, left=lhs, right=rhs, rule=Rule.eir))
        return combos

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.left and self.right:
            text = '/'.join([' '.join(self.left.tokens), ' '.join(self.right.tokens)])
        else:
            text = ' '.join(self.tokens)
        return '%s(%s):%s' % (text, self.tag, Type.str(self.type))

    def dump(self):
        print('self ', self)
        print('toks ', self.tokens)
        print('type ', Type.str(self.type))
        print('left ', self.left.tokens)
        print('right', self.right.tokens)
        print('rule ', self.rule)
        print('tree ')
        self.pprint()

    def pprint(self, delim='  '):
        def pprint0(i, e):
            if e.left and e.right:
                print('%s(%s: %s' % (delim * i, e.rule, Type.str(e.type)))
                pprint0(i+1, e.left)
                pprint0(i+1, e.right)
                print('%s)' % (delim * i))
            else:
                print('%s%s: %s (head)' % (delim * i, ' '.join(e.tokens), Type.str(e.type)))
        pprint0(0, self)

    @property
    def type(self):
        return self._type

    @property
    def rule(self):
        return self._rule

    @property
    def tokens(self):
        return self._tokens

    @property
    def domain(self):
        return self._dom

    @property
    def range(self):
        return self._rng

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def tag(self):
        return self._tag
