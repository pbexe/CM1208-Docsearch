"""
Student No.: C1769331
"""


def generateDictionary(docs):
    dictionary = []
    for doc in docs:
        for word in doc[0].split():
            dictionary.append(word)
    dictionary = set(dictionary)
    return dictionary


def generateInvertedIndex(dictionary, corpus):
    """
    NEEDS TO BE REWRITTEN TO BE *MUCH* MORE EFFICENT
    """
    index = []
    for word in dictionary:
        index.append([word, []])
    for doc in corpus:
        for word in doc[0].split():
            for entry in index:
                if entry[0] == word and doc[1] not in entry[1]:
                        entry[1].append(doc[1])
    return index

def main():
    # Placeholders for data to be imported/generated
    docs = []
    queries = []

    # Load the corpus
    with open("./corpus/set2/docs.txt") as fp:
        docs = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    # Load the queries
    with open("./corpus/set1/queries.txt") as fp:
        queries = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    dictionary = generateDictionary(docs)
    invertedIndex = generateInvertedIndex(dictionary, docs)
    print(docs)
    print(queries)
    print(dictionary)
    print(invertedIndex)


if __name__ == "__main__":
    main()
