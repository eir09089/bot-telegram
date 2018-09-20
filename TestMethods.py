from test_regex import *
from fixtues import  *

import unittest


class TestMethods(unittest.TestCase):

    def test_stake(self):
        self.assertEqual(findStake('FT(OT excl.) Over 1.75 (O/U) (1:0) @ 1.89 1/10 LIVE Marathonbet'), 1)
        self.assertEqual(findStake('stake: 3/10'), 3)
        self.assertEqual(findStake('hallo you/10'), None)

    def test_odds(self):
        self.assertEqual(findOdds('odd: 1.85'), '1.85')
        self.assertEqual(findOdds('odd: 1,85'), '1,85')
        self.assertEqual(findOdds('cuota: 1,85'), '1,85')
        self.assertEqual(findOdds('value: 1,85'), '1,85')
        self.assertEqual(findOdds('value: hello 1,85'), None)
        self.assertEqual(findOdds('@ 1,85 hello'), '1,85')


    def test_sport(self):
        self.assertEqual(findSport('Football / Livebet / Kick off: 17 Sep 2018, 18:00'.lower()), 'football')
        self.assertEqual(findSport(' e sports - Kick off: 17 Sep 2018, 18:00'.lower()), 'e sports')


    def test_event(self):
        self.assertEqual(findEvent('match: a (a) - b (b)'), 'a (a) - b (b)')
        self.assertEqual(findEvent('match: a (a) vs b (b)'), 'a (a) vs b (b)')
        self.assertEqual(findEvent('evento: a (a) - b (b)'), 'a (a) - b (b)')
        self.assertEqual(findEvent('evento: a (a) vs b (b)'), 'a (a) vs b (b)')
        self.assertEqual(findEvent('a (a) vs b (b)'), 'a (a) vs b (b)')
        self.assertEqual(findEvent('a (a) - b (b)'), 'a (a) - b (b)')
        self.assertEqual(findEvent('sc viitorul constanta - afc hermannstadt'), 'sc viitorul constanta - afc hermannstadt')

        self.assertEqual(findEvent('a (a) - b (b) - c'), None)
        self.assertEqual(findEvent('18.05.1991 - 18:00'), None)

    def test_combo(self):
        self.assertEqual(extractInfo(message1), ('football', '1.89', 1, 'sc viitorul constanta - afc hermannstadt'))
        self.assertEqual(extractInfo(message2), ('handball', '1.80', 6, 'ruch chorzow (w) - kpr kobierzyce (w)'))



if __name__ == '__main__':
    unittest.main()