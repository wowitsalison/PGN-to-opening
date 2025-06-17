import unittest
from app import app, classify_opening

class OpeningClassifierTests(unittest.TestCase):
    def test_classify_valid_pgn(self):
        pgn = """
        [Event "Live Chess"]
        [Site "Chess.com"]
        [Date "2021.05.01"]
        [Round "?"]
        [White "player1"]
        [Black "player2"]
        [Result "1-0"]
        [ECO "C60"]
        [Opening "Ruy Lopez"]

        1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 1-0
        """
        eco, opening = classify_opening(pgn)
        self.assertEqual(eco, "C60")
        self.assertEqual(opening, "Ruy Lopez")

    def test_classify_invalid_pgn(self):
        eco, opening = classify_opening("not a pgn")
        self.assertIsNone(eco)
        self.assertTrue("Error" in opening)

if __name__ == "__main__":
    unittest.main()
