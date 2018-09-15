import unittest
from lab2_helper import rock_message, paper_message, scissors_message, lizard_message, spock_message

class Lab2HelperTestCase(unittest.TestCase):
    
    def test_rock_message(self):
        """This method tests when a player is Rock what should happen when the computer is each of the options"""
        self.assertEqual(rock_message("Rock"),     "You Tie! Rock equals Rock")
        self.assertEqual(rock_message("Paper"),    "You Lose! Paper covers Rock")
        self.assertEqual(rock_message("Scissors"), "You Win! Rock smashes Scissors")
        self.assertEqual(rock_message("Lizard"),   "You Win! Rock smashes Lizard")
        self.assertEqual(rock_message("Spock"),    "You Lose! Spock vaporizes Rock")

    def test_paper_message(self):
        """This method tests when a player is Paper what should happen when the computer is each of the options"""
        self.assertEqual(paper_message("Rock"),     "You Win! Paper covers Rock")
        self.assertEqual(paper_message("Paper"),    "You Tie! Paper equals Paper")
        self.assertEqual(paper_message("Scissors"), "You Lose! Scissors cuts Paper")
        self.assertEqual(paper_message("Lizard"),   "You Lose! Lizard eats Paper")
        self.assertEqual(paper_message("Spock"),    "You Win! Paper covers Spock")
        
    def test_scissors_message(self):
        """This method tests when a player is Scissors what should happen when the computer is each of the options"""
        self.assertEqual(scissors_message("Rock"),     "You Lose! Rock smashes Scissors")
        self.assertEqual(scissors_message("Paper"),    "You Win! Scissors cuts Paper")
        self.assertEqual(scissors_message("Scissors"), "You Tie! Scissors equals Scissors")
        self.assertEqual(scissors_message("Lizard"),   "You Win! Scissors decapitates Lizard")
        self.assertEqual(scissors_message("Spock"),    "You Lose! Spock crushes Scissors")

    def test_lizard_message(self):
        """This method tests when a player is Lizard what should happen when the computer is each of the options"""
        self.assertEqual(lizard_message("Rock"),     "You Lose! Rock smashes Lizard")
        self.assertEqual(lizard_message("Paper"),    "You Win! Lizard eats Paper")
        self.assertEqual(lizard_message("Scissors"), "You Lose! Scissors decapitates Lizard")
        self.assertEqual(lizard_message("Lizard"),   "You Tie! Lizard equals Lizard")
        self.assertEqual(lizard_message("Spock"),    "You Win! Lizard poisons Spock")

    def test_spock_message(self):
        """This method tests when a player is Lizard what should happen when the computer is each of the options"""
        self.assertEqual(spock_message("Rock"),     "You Win! Spock vaporizes Rock")
        self.assertEqual(spock_message("Paper"),    "You Lose! Paper covers Spock")
        self.assertEqual(spock_message("Scissors"), "You Win! Spock vaporizes Scissors")
        self.assertEqual(spock_message("Lizard"),   "You Lose! Lizard poisons Spock")
        self.assertEqual(spock_message("Spock"),    "You Tie! Spock equals Spock")

if __name__ == "__main__":
    unittest.main()
