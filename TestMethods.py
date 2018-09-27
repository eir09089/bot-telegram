# -*- coding: utf-8 -*-
from test_regex import *
from fixtues import *

import unittest


class TestMethods(unittest.TestCase):

    def test_stake(self):
        self.assertEqual((1, 'FT(OT excl.) Over 1.75 (O/U) (1:0) @ 1.89  LIVE Marathonbet'), findStake('FT(OT excl.) Over 1.75 (O/U) (1:0) @ 1.89 1/10 LIVE Marathonbet'))
        self.assertEqual((3, '/10'), findStake('stake: 3/10'))
        self.assertEqual((None, 'hallo you/10'), findStake('hallo you/10'))

    def test_odds(self):
        self.assertEqual(('1.85',''), findOdds('odd: 1.85'))
        self.assertEqual(('1,85', ''), findOdds('odd: 1,85'))
        self.assertEqual(('1,85', ''), findOdds('cuota: 1,85'))
        self.assertEqual(('1,85', ''), findOdds('value: 1,85'))
        self.assertEqual((None, 'value: hello 1,85'), findOdds('value: hello 1,85'))
        self.assertEqual(('1,85', 'hello'), findOdds('@ 1,85 hello'))


    def test_sport(self):
        self.assertEqual(('football', 'football / livebet / kick off: 17 sep 2018, 18:00'),findSport('Football / Livebet / Kick off: 17 Sep 2018, 18:00'.lower()))
        self.assertEqual(('e sports', 'e sports - kick off: 17 sep 2018, 18:00'), findSport(' e sports - Kick off: 17 Sep 2018, 18:00'.lower()))


    def test_event(self):
        self.assertEqual(('a (a) - b (b)', ''), findEvent('match: a (a) - b (b)'))
        self.assertEqual(('a (a) vs b (b)', ''), findEvent('match: a (a) vs b (b)'))
        self.assertEqual(('a (a) - b (b)', ''), findEvent('evento: a (a) - b (b)'))
        self.assertEqual(('a (a) vs b (b)', ''), findEvent('evento: a (a) vs b (b)'))
        self.assertEqual(('a (a) vs b (b)', ''), findEvent('a (a) vs b (b)'))
        self.assertEqual(('a (a) - b (b)', ''), findEvent('a (a) - b (b)'))
        self.assertEqual(('sc viitorul constanta - afc hermannstadt', ''), findEvent('sc viitorul constanta - afc hermannstadt'))

        self.assertEqual((None, 'a (a) - b (b) - c'), findEvent('a (a) - b (b) - c'))
        self.assertEqual((None, '18.05.1991 - 18:00'), findEvent('18.05.1991 - 18:00'))

    def test_bet1(self):
        self.assertEqual(('kpr kobierzyce (w) -3.5', ''), findBet('pick: kpr kobierzyce (w) -3.5'))

    def test_bet2(self):
        self.assertEqual(('over 1.75', 'ft(ot excl.)  skfdls (o/u) (1:0) @ 1.89 1/10 live marathonbet'), findBet('FT(OT excl.) Over 1.75 skfdls (O/U) (1:0) @ 1.89 1/10 LIVE Marathonbet'.lower()))
    def test_bet3(self):
        self.assertEqual(('detona win', ''), findBet('detona win'))


    def test_combo1(self):
        self.assertEqual(('handball', u'1.80', 6, u'ruch chorzow - kpr kobierzyce', u'kpr kobierzyce (w) -3.5'), extractInfo(message2.lower()))
    def test_combo2(self):
        self.assertEqual(('football', u'1.89', 1, u'sc viitorul constanta - afc hermannstadt', u'over 1.75'), extractInfo(message1.lower()))

    def test_combo3(self):
        self.assertEqual(('handball', u'1.80', 6, u'ruch chorzow (w) - kpr kobierzyce (w)', u'kpr kobierzyce (w) -3.5'), extractInfo(message3.lower()))
    def test_combo4(self):
        self.assertEqual((None, u'1.73', 1, None, '-1.75'), extractInfo(message4.lower()))
    def test_combo5(self):
        self.assertEqual((None, u'1.90', None, None,  u'win pachuca + chivas o empate'), extractInfo(message5.lower()))
    def test_combo6(self):
        self.assertEqual((None, u'1.8', 3, None, 'casanova'), extractInfo(message6.lower()))
    def test_combo7(self):
        self.assertEqual(('basketball', u'1.83', 6, u'elite roma w vs scafati women', u'over 92,5'), extractInfo(message7.lower()))
    def test_combo8(self):
        self.assertEqual((None, None, 1, u'bulgaria u19 (w) - italy u19 (w)', 'over 121,5'), extractInfo(message8.lower()))
    def test_combo9(self):
        self.assertEqual(('cricket', u'1.66', 2, u'western warriors - new south wales', 'western warriors'), extractInfo(message9.lower()))
    def test_combo10(self):
        self.assertEqual((None, u'2,10', 3, u'windigo (cs) - winstrike (cs)', u'windigo -1.5'), extractInfo(message10.lower()))
    def test_combo11(self):
        self.assertEqual((None, u'2,25', 5, u'detona (cs) - intz-esports (cs)', 'detona win'), extractInfo(message11.lower()))



if __name__ == '__main__':
    unittest.main()