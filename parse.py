""" parse the text file into because statements """
import nltk
nltk.download('punkt')

def main():
    """ make the because file """
    with open('why.txt', 'r', encoding='latin-1') as whyfile:
        why = whyfile.read()

    output = []

    string_why = why.replace('\n', ' ')
    tok = nltk.sent_tokenize(string_why)
    for sentence in tok:
        spl = sentence.split('because')
        try:
            because = 'because' + spl[1]
            if because.count('"') % 2 != 0:
                if because[-1] == '"':
                    because = because[:-1]
            if because.count('"') % 2 != 0:
                pass
            else:
                output.append(because)
        except:
            pass

    output = set(output)

    with open('output.txt', 'w') as outfile:
        for item in output:
            outfile.write(f'{item}\n')

if __name__ == '__main__':
    main()
