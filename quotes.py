import argparse
import pickle
import sys
import os.path
import random
from collections import defaultdict
filename = 'quotedict'
def display_quote(args, quotedict):
    user = args.user
    rand = args.random
    # Display random quote for user
    if rand:
        if not user:
            user = random.choice(list(quotedict.keys()))
        quote = random.choice(quotedict[user])
        print('{}: {}'.format(user, quote))
        return
    # Display all quotes for specified user
    if user:
        for quote in quotedict[user]:
            print(quote)
        return
    else:
        for user, quotes in quotedict.items():
            for quote in quotes:
                print('{}: {}'.format(user, quote))

def add_quote(args, quotedict):
    user = args.user
    quote = args.quote
    quotedict[user].append(quote)
    print('{}: {}'.format(user, quote))

def search_quote(args, quotedict):
    phrase = args.phrase
    user = args.user
    if user:
        matches = [quote for quote in quotedict[user] if phrase in quote]
        for match in matches:
            print('{}: {}'.format(user, match))
    else:
        all_quotes = quotedict.values()
        for user, quotes in quotedict.items():
            matches = [quote for quote in quotes if phrase in quote]
            for match in matches:
                print('{}: {}'.format(user, match))
        

def main(argv=None):
    # Set up arguments
    parser = argparse.ArgumentParser(description='Save and view quotes.')
    subparsers = parser.add_subparsers(dest='command', help='command to run')
    subparsers.required = True
    parser_display = subparsers.add_parser('display', help='display a quote')
    parser_display.add_argument('--user', help='choose user to display')
    parser_display.add_argument('--random', action='store_true', help='pick a random quote')

    parser_add = subparsers.add_parser('add', help='add a quote')
    parser_add.add_argument('user', help='specify quote speaker')
    parser_add.add_argument('quote', help='quote to add')

    parser_search = subparsers.add_parser('search', help='search for a quote')
    parser_search.add_argument('phrase', help='search for phrase in quotes')
    parser_search.add_argument('--user', help='limit search to user')

    parser_display.set_defaults(func=display_quote)
    parser_add.set_defaults(func=add_quote)
    parser_search.set_defaults(func=search_quote)
    args = parser.parse_args()
    # Check if quotes file exists, if not then make new
    if os.path.exists(filename):
        quotefile = open(filename,'rb')
        quotedict = pickle.load(quotefile)
        quotefile.close()
    else:
        quotedict = defaultdict(list)

    args.func(args, quotedict)

    # Pickle and finish
    outfile = open(filename,'wb')
    pickle.dump(quotedict,outfile)
    outfile.close()
    return

if __name__ == '__main__':
        sys.exit(main())
