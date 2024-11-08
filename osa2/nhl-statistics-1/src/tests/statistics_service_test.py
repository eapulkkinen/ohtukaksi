import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_name_found(self):
        vastaus = self.stats.search("Kurri")
        taulukko = PlayerReaderStub().get_players()
        self.assertAlmostEqual(str(vastaus), str(taulukko[2]))

    def test_search_name_not_found(self):
        name = "NotAName"
        vastaus = self.stats.search(name)
        self.assertEqual(vastaus, None)
    
    def test_team(self):
        vastaus = self.stats.team("PIT")
        taulukko = PlayerReaderStub().get_players()
        self.assertAlmostEqual(str(vastaus[0]), str(taulukko[1]))

    def test_top(self):
        vastaus = self.stats.top(4)
        taulukko = PlayerReaderStub().get_players()
        self.assertAlmostEqual(str(vastaus[0]), str(taulukko[4]))


