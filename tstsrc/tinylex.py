from konig.lextree import Type
from konig.grammar import heads, phrases
import konig.lextree
import konig.decoder


if __name__ == '__main__':
    lexicon = {
        'the': [konig.lextree.LexTree(['the'], Type.et_e, heads['D'])],
        'student': [konig.lextree.LexTree(['student'], Type.e_t, heads['N'])],
        'female': [konig.lextree.LexTree(['female'], Type.e_t, heads['Adj'])],
        'difficult': [konig.lextree.LexTree(['difficult'], Type.e_t, heads['Adj'])],
        'some': [konig.lextree.LexTree(['some'], Type.et_ett, heads['D'])],
        'aced': [konig.lextree.LexTree(['aced'], Type.e_et, heads['V'])],
        'final': [konig.lextree.LexTree(['final'], Type.e_t, heads['Adj']),
                  konig.lextree.LexTree(['final'], Type.e_t, heads['N']),
                  konig.lextree.LexTree(['final'], Type.e_t, phrases['NP'])],
        'for': [konig.lextree.LexTree(['for'], Type.e_et, heads['P'])],
        'to': [konig.lextree.LexTree(['to'], Type.e_et, heads['P'])],
        'it': [konig.lextree.LexTree(['it'], Type.e, heads['D'])],
        'in': [konig.lextree.LexTree(['in'], Type.e_et, heads['P'])],
        'Linguistics_510': [konig.lextree.LexTree(['Linguistics', '510'], Type.e, phrases['NP'])],
        'car': [konig.lextree.LexTree(['car'], Type.e_t, heads['N'])],
        'flew': [konig.lextree.LexTree(['flew'], Type.e_t, heads['V'])],
        'horse': [konig.lextree.LexTree(['horse'], Type.e_t, heads['N']),
                  konig.lextree.LexTree(['horse'], Type.e_t, phrases['NP'])],
        'ran': [konig.lextree.LexTree(['ran'], Type.e_t, phrases['VP'])],
        'raced': [konig.lextree.LexTree(['raced'], Type.e_t, phrases['VP']),
                  konig.lextree.LexTree(['raced'], Type.e_et, heads['V']),
                  konig.lextree.LexTree(['raced'], Type.ett_et, heads['V']),
                  konig.lextree.LexTree(['raced'], Type.e_εt, heads['V'])],
        'barn': [konig.lextree.LexTree(['barn'], Type.e_t, heads['N']),
                 konig.lextree.LexTree(['barn'], Type.e_t, phrases['NP'])],
        'fell': [konig.lextree.LexTree(['fell'], Type.e_t, phrases['VP'])],
        'past': [konig.lextree.LexTree(['past'], Type.e_et, phrases['VP']),
                 konig.lextree.LexTree(['past'], Type.e_εt, heads['Adv'])],
        'Barack': [konig.lextree.LexTree(['Barack', 'Obama'], Type.e, phrases['NP'])],
        'smokes': [konig.lextree.LexTree(['smokes'], Type.e_t, phrases['VP']),
                   konig.lextree.LexTree(['smokes'], Type.e_et, heads['V'])],
        'he': [konig.lextree.LexTree(['he'], Type.e, phrases['DP'])],
        'ate': [konig.lextree.LexTree(['ate'], Type.e_et, heads['V']),
                konig.lextree.LexTree(['ate'], Type.e_t, phrases['VP']),
                konig.lextree.LexTree(['ate'], Type.ett_et, heads['V'])]
    }
    s = 'the horse ran past the barn'.split()
    n = len(s)
    chart = konig.decoder.decode(s, lexicon)

    chart.dump()

    ans = chart[0][n-1]
    # for r in ans:
    #     print(' '.join(map(str, r)))

    for i in ans:
        i.dump()
        print('---')
