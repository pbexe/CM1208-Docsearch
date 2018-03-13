"""
Student No.: C1769331
"""
import numpy as np
import math


def generateDictionary(docs):
    dictionary = []
    for doc in docs:
        for word in doc[0].split():
            dictionary.append(word)
    dictionary = list(set(dictionary))
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


def calculateAngle(doc1, doc2, dictionary):
    # Split each document down into individual words
    doc1, doc2 = doc1.split(), doc2.split()

    # Create empty vectors
    doc1_vector = np.zeros(len(dictionary), dtype=np.int32)
    doc2_vector = np.zeros(len(dictionary), dtype=np.int32)

    # Populate them
    for i, word in enumerate(dictionary):
        doc1_vector[i] = doc1.count(word)
    for i, word in enumerate(dictionary):
        doc2_vector[i] = doc2.count(word)

    # Calculate the lengths of the vectors
    doc1_length = np.sqrt(np.dot(doc1_vector, doc1_vector))
    doc2_length = np.sqrt(np.dot(doc2_vector, doc2_vector))

    # And finally calculate the angles between them
    angle = np.degrees(np.arccos(np.dot(doc1_vector, doc2_vector) / (doc1_length * doc2_length)))
    return angle


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

    # Generate the dictionary and inverted index
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
        print("Relevant documents:", " ".join(str(x) for x in related))

        angles = []
        # Calculate the angles between the documents
        # TODO: Optimise this
        for document in docs:
            if document[1] in related:
                angles.append((document[1], calculateAngle(document[0], query[0], dictionary)))
        # Order the angles
        sorted_angles = sorted(angles, key=lambda x: x[1])
        # Print them to 2 ddecimal places keeping trailing 0s
        for angle in sorted_angles:
            print(angle[0], '{:.2f}'.format(round(angle[1], 2)))


if __name__ == "__main__":
    main()
