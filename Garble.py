from googletrans import Translator, constants
import random
import time
import click

languages = list(constants.LANGUAGES.keys())  # Get a list of language codes
translationService = Translator()  # Initialise translator

def garble(text, amount, seed):
    random.seed(seed)
    history = [text]
    for i in range(amount):
        history.append(translationService.translate(history[i-1], random.choice(languages)).text)  # Translate to random language
        print(history[i])

    result = translationService.translate(history[len(history) - 1], "en").text
    original = text
    return result, original, history

@click.command()
@click.option('--text', default = False)
@click.option('--amount', default = 20)
@click.option('--seed', default = time.time())
@click.option('--infile', default = False)
@click.option('--outfile', default = False)
def main(text, amount, seed, infile, outfile):
    if infile:
        try:
            text = open(infile).read()
        except:
            print("Couldn\'t open input file")
            exit()
    result, original, history = garble(text, amount, seed)
    if outfile:
        try:
            open(outfile, "w").write(result + "\n")
        except:
            print("Couldn\'t open output file!")
            exit()
    print(result)
if __name__ == "__main__":
    main()
