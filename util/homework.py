"""
Composittion from every home work to complete.

Ref: https://ccc.inaoep.mx/~mmontesg/pmwiki.php/Main/RecuperacionDeInformacion
"""
from util.utils import Utils


class Homework:

    @staticmethod
    def homeWork1():
        print('Homework #1 - Start\n')

        docs = Utils.getEachDocument()
        print(f'Length of documents to process: {len(docs)}')

        docsDataStructure = Utils.composeText(docs)
        print(f'Length of documents processed: {len(docsDataStructure)}')

        queryDocs = Utils.getEachQuery()
        print(f'Length of queries to process: {len(queryDocs)}')

        queryDocsDataStructure = Utils.composeQuery(queryDocs)
        print(f'Length of queries processed: {len(queryDocsDataStructure)}')

        emptyWords = Utils.getEmptyWords()
        print(f'Length of empty words to use: {len(emptyWords)}\n')

        # Looping on every Text | Document
        i = 1
        for doc in docsDataStructure:
            # 1.a - Delete empty words
            doc['cleanBody'] = Utils.replaceOnString(emptyWords, doc['body'], ' ')
            print(f'Reduction text           #{i}: { 1 - (len(doc["cleanBody"]) / len(doc["body"])) }')

            # 1-b - Truncating using Porter Algorithm    
            doc['cleanBodyPorter'] = Utils.truncateOnPorterAlgorithm(doc['body'])
            print(f'Reduction text (Porter)  #{i}: { 1 - (len(doc["cleanBodyPorter"]) / len(doc["body"])) }')

            # 2 Term frecuency
            doc['termFrecuency'] = Utils.termFrecuency(doc['body'])
            print(f'Length of the vocabulary #{i}: { len(doc["termFrecuency"].keys()) }\n')
            i += 1

        # Looping on every Query
        i = 1
        for query in queryDocsDataStructure:
            query['cleanBody'] = Utils.replaceOnString(emptyWords, query['body'], ' ')
            print(f'Reduction query          #{i}: { 1 - (len(query["cleanBody"]) / len(query["body"])) }')

            # 1-b - Truncating using Porter Algorithm    
            query['cleanBodyPorter'] = Utils.truncateOnPorterAlgorithm(query['body'])
            print(f'Reduction query (Porter) #{i}: { 1 - (len(query["cleanBodyPorter"]) / len(query["body"])) }')

            # 2 Term frecuency
            query['termFrecuency'] = Utils.termFrecuency(query['body'])
            print(f'Length of the vocabulary #{i}: { len(query["termFrecuency"].keys()) }\n')
            i += 1

        Utils.saveTermFrecuency(docsDataStructure,'tf-text.out', 'text')
        Utils.saveTermFrecuency(queryDocsDataStructure, 'tf-query.out', 'query')

    @staticmethod
    def homeWork2():
        pass
