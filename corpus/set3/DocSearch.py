"""
Student No.: C1769331
"""
import sys
import math
import numpy as np


def generate_dictionary(docs):
    """Generates a dictionary of all of the words that occur in `docs`

    Args:
        docs (list): A list of the documents in the corpus

    Returns:
        list: A list of all of the words that occur in `docs`
    """

    dictionary = []
    for doc in docs:
        for word in doc[0].split():
            dictionary.append(word)
    dictionary = list(set(dictionary))
    return dictionary


def generate_inverted_index(dictionary, corpus):
    """Generates an inverted index of all of the words in `dictionary` that
    occur in the corpus

    Args:
        dictionary (list): A dictionary of all words in the whole corpus
        corpus (list): The text that the inverted index shall be generated from

    Returns:
        dict: A dictionary representing the inverted index
    """

    index = {}
    for word in dictionary:
        index[word] = []
    for doc in corpus:
        for word in doc[0].split():
            if word in index and doc[1] not in index[word]:
                index[word].append(doc[1])
    return index


def calculate_angle(doc1, doc2, dictionary):
    """Calculates the angle between two documents

    Args:
        doc1 (str): The first document
        doc2 (str): The second document
        dictionary (list): A dictionary of all words in the whole corpus

    Returns:
        float: The angle between the two documents
    """

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
    doc1_length = np.linalg.norm(doc1_vector)
    doc2_length = np.linalg.norm(doc2_vector)

    # And finally calculate the angles between them
    angle = np.degrees(
        np.arccos(
            np.dot(doc1_vector, doc2_vector) / (doc1_length * doc2_length)
        )
    )
    return angle


def main():
    """The main procedure
    """

    # Placeholders for data to be imported/generated
    docs = []
    queries = []

    # Load the corpus
    with open('docs.txt') as fp:
        docs = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    # Load the queries
    with open('queries.txt') as fp:
        queries = [x.strip('\n') for x in fp.readlines()]

    # Generate the dictionary and inverted index
    dictionary = generate_dictionary(docs)
    inverted_index = generate_inverted_index(dictionary, docs)
    print("Words in dictionary:", len(dictionary))

    # Iterate through queries
    for query in queries:
        print("Query:", query)
        word_documents = []
        # Iterate through each word in the query
        for word in query.split():
            if word in inverted_index:
                # Convert the array to a set so an intersection can be found
                word_documents.append(set(inverted_index[word]))

        # Calculate the intersection
        related = set.intersection(*word_documents)
        print("Relevant documents:", " ".join(str(x) for x in related))

        angles = []
        # Calculate the angles between the documents
        for document in docs:
            if document[1] in related:
                dictionary = generate_dictionary(
                    [
                        [document[0], None],
                        [query, None]
                    ]
                )
                # Order the angles
                angles.append(
                    (
                     document[1],
                     calculate_angle(document[0], query, dictionary)
                    )
                )
        sorted_angles = sorted(angles, key=lambda x: x[1])
        # Print them to 2 ddecimal places keeping trailing 0s
        for angle in sorted_angles:
            print(angle[0], '{:.5f}'.format(round(angle[1], 5)))


if __name__ == "__main__":
    main()
