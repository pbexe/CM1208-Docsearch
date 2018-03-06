"""
Student No.: C1769331
"""


def generateDictionary(docs):
    dictionary = []
    for doc in docs:
        for word in doc.split():
            dictionary.append(word)
    dictionary = set(dictionary)
    return dictionary


def main():
    # Placeholders for data to be imported/generated
    docs = []
    queries = []

    # Load the corpus
    with open("./corpus/set1/docs.txt") as fp:
        docs = [x.strip('\n') for x in fp.readlines()]

    # Load the queries
    with open("./corpus/set1/queries.txt") as fp:
        queries = [x.strip('\n') for x in fp.readlines()]

    dictionary = generateDictionary(docs)

    print(docs)
    print(queries)
    print(dictionary)


if __name__ == "__main__":
    main()
