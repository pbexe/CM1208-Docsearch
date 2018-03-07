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
    index = {}
    for word in dictionary:
        index[word] = []
    for doc in corpus:
        for word in doc[0].split():
            if word in index and doc[1] not in index[word]:
                index[word].append(doc[1])
    return index


def main():
    # Placeholders for data to be imported/generated
    docs = []
    queries = []

    # Load the corpus
    with open("./corpus/set2/docs.txt") as fp:
        docs = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    # Load the queries
    with open("./corpus/set2/queries.txt") as fp:
        queries = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    dictionary = generateDictionary(docs)
    invertedIndex = generateInvertedIndex(dictionary, docs)

    print("Words in dictionary:", len(dictionary))

    # Iterate through queries
    for query in queries:
        print("Query:", query[0])
        word_documents = []
        # Iterate through each word in the query
        for word in query[0].split():
            if word in invertedIndex:
                # Convert the array to a set so an intersection can be found
                word_documents.append(set(invertedIndex[word]))
        # Calculate the intersection
        related = set.intersection(*word_documents)
        print("Related:", " ".join(str(x) for x in set(related)))


if __name__ == "__main__":
    main()
