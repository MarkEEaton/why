""" parse the text file into because statements """
import nltk
nltk.download('punkt')

def main():
    """ make the because file """
    with open('why.txt', 'r', encoding='latin-1') as whyfile:
        why = whyfile.read()

    output = []

    # remove line breaks, replace with spaces
    string_why = why.replace('\n', ' ')
    # parse into sentences
    tok = nltk.sent_tokenize(string_why)
    for sentence in tok:
        # remove series of multiple spaces
        sentence = ' '.join(sentence.split())        
        # split on 'because'
        spl = sentence.split('because')
        try:
            # grab the half of the sentence after because
            because = 'because' + spl[1]
            # try to find if there is a second because
            # and include the bit after it if it exists
            try:
                because = because + 'because' + spl[2]
            except:
                pass
            # if there's an odd number of quotes
            # and the last character is a quote
            # remove the last character
            if because.count('"') % 2 != 0:
                if because[-1] == '"':
                    because = because[:-1]
            # if there's still an odd number of quotes, skip it
            if because.count('"') % 2 != 0:
                pass
            # append that parsed sentence!
            else:
                output.append(because)
        except:
            pass

    # remove duplicates
    output = set(output)

    with open('output.txt', 'w') as outfile:
        for item in output:
            outfile.write(f'{item}\n')

if __name__ == '__main__':
    main()
