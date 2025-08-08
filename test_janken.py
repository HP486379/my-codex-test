import unittest

from janken import judge


class TestJanken(unittest.TestCase):
    def test_draw(self):
        for choice in ["グー", "チョキ", "パー"]:
            with self.subTest(choice=choice):
                self.assertEqual(judge(choice, choice), "あいこ")

    def test_player_wins(self):
        wins = [
            ("グー", "チョキ"),
            ("チョキ", "パー"),
            ("パー", "グー"),
        ]
        for player, computer in wins:
            with self.subTest(player=player, computer=computer):
                self.assertEqual(judge(player, computer), "勝ち")

    def test_player_loses(self):
        loses = [
            ("グー", "パー"),
            ("チョキ", "グー"),
            ("パー", "チョキ"),
        ]
        for player, computer in loses:
            with self.subTest(player=player, computer=computer):
                self.assertEqual(judge(player, computer), "負け")


if __name__ == "__main__":
    unittest.main()
