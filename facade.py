from generator import Generator
from splitter import Splitter
from verifier import Verifier


class MagicSquareGenerator:
    def generate(self, size: int):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()

        while True:
            square = []
            for x in range(size):
                square.append(generator.generate(size))
            
            result_split = splitter.split(square)
            
            if (verifier.verify(result_split)):
                break
            else:
                pass
        
        return square
