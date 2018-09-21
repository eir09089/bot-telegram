from test_regex import *
from fixtues import  *

import unittest


class TestMethods(unittest.TestCase):

    def test_stake(self):
        self.assertEqual(1, findStake('FT(OT excl.) Over 1.75 (O/U) (1:0) @ 1.89 1/10 LIVE Marathonbet'))
        self.assertEqual(3, findStake('stake: 3/10'))
        self.assertEqual(None, findStake('hallo you/10'))

    def test_odds(self):
        self.assertEqual('1.85', findOdds('odd: 1.85'))
        self.assertEqual('1,85', findOdds('odd: 1,85'))
        self.assertEqual('1,85', findOdds('cuota: 1,85'))
        self.assertEqual('1,85', findOdds('value: 1,85'))
        self.assertEqual(None, findOdds('value: hello 1,85'))
        self.assertEqual('1,85', findOdds('@ 1,85 hello'))


    def test_sport(self):
        self.assertEqual('football',findSport('Football / Livebet / Kick off: 17 Sep 2018, 18:00'.lower()))
        self.assertEqual('e sports', findSport(' e sports - Kick off: 17 Sep 2018, 18:00'.lower()))


    def test_event(self):
        self.assertEqual('a (a) - b (b)', findEvent('match: a (a) - b (b)'))
        self.assertEqual('a (a) vs b (b)', findEvent('match: a (a) vs b (b)'))
        self.assertEqual('a (a) - b (b)', findEvent('evento: a (a) - b (b)'))
        self.assertEqual('a (a) vs b (b)', findEvent('evento: a (a) vs b (b)'))
        self.assertEqual('a (a) vs b (b)', findEvent('a (a) vs b (b)'))
        self.assertEqual('a (a) - b (b)', findEvent('a (a) - b (b)'))
        self.assertEqual('sc viitorul constanta - afc hermannstadt', findEvent('sc viitorul constanta - afc hermannstadt'))

        self.assertEqual(None, findEvent('a (a) - b (b) - c'), None)
        self.assertEqual(None, findEvent('18.05.1991 - 18:00'), None)

    def test_combo1(self):
        self.assertEqual(('handball', u'1.80', 6, u'ruch chorzow (w) - kpr kobierzyce (w)'), extractInfo(message2.lower()))
    def test_combo2(self):
        self.assertEqual(('football', u'1.89', 1, u'sc viitorul constanta - afc hermannstadt'), extractInfo(message1.lower()))



if __name__ == '__main__':
    unittest.main()