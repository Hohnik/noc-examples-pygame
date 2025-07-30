# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# An LSystem has a starting sentence
# An a ruleset
# Each generation recursively replaces characters in the sentence
# Based on the ruleset

# Construct an LSystem with a starting sentence and a ruleset
class LSystem:
    def __init__(self, axiom, rules):
        self.sentence = axiom  # The sentence (a Sting)
        self.rules = rules  # The ruleset (an array of Rule objects)

    # Generate the next generation
    def generate(self):
        # An empty string that we will fill
        next_gen = ""

        # What is the character
        for c in self.sentence:
            # Replace it with itself unless it matches one of our rules
            next_gen += self.rules.get(c, c)

        # Replace sentence
        self.sentence = next_gen
