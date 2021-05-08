"""
Set of utils methods.
"""
import re

from util.constants import C

import Stemmer


class Utils:

    @staticmethod
    def getFile(inputFile:str) -> str:
        data = ''
        try:
            with open(inputFile, 'r') as f: 
                data = f.read() 
                f.close()
        except Exception as e:
            print(f'Error detected during opening the file: {str(e)}')

        return data

    @staticmethod
    def composeText(docs:list) -> list:
        """
        This method will compose a structure to use texts in a simpler way.

        [ 'TEXT ...' ] -> [ {body, text, date, page} ]
        """
        out = []

        for doc in docs:
            tempText = {}

            header = re.findall(r'(\*TEXT \d{3}\s+(\d+/\d+/? ?\d+)+\s+PAGE\s+\d+\s+)', doc) # list | list tuple
            body = re.findall(r'.*\s\s((.+\s+)+).*\s\s', doc) # list | list tuple

            if len(body):
                if type(body[0]) == tuple:
                    if len(body[0]):
                        tempText = {'body' : body[0][0] }

                if tempText != {} and len(header):
                    if type(header[0]) == tuple:
                        header = header[0][0].split(' ')
                        tempText.update({
                            'text': header[1],
                            'date': header[2],
                            'page': header[4].replace('\n\n', '')
                        })

            if len( list(tempText.keys()) ) == 4:
                out.append(tempText)
            else:
                print(f'header: {header}')
                print(f'doc: {doc[:32]}\n\n')


        return out

    @staticmethod
    def composeQuery(queries:list) -> list:
        """
        [ '*FIND      1 ...' ] -> {query, body}
        """
        out = []
        for query in queries:
            tempQuery = {}
            header = re.findall(r'(\*FIND\s+(\d+)\s+)', query) # list | list tuple
            body = re.findall(r'.*\s\s((.+\s+)+).*\s\s', query) # list | list tuple

            if len(body):
                if type(body[0]) == tuple:
                    tempQuery.update({
                        'body': str(body[0][0])
                    })

                if tempQuery != {} and header:
                    if type(header[0]) == tuple:
                        tempQuery.update({
                            'query': int(header[0][1]) # Got the number of the query
                        })

            if len( list(tempQuery.keys()) ) == 2:
                out.append(tempQuery)
            else:
                print(f'header: {header}')
                print(f'query: {query[:32]}\n\n')

        return out

    @staticmethod
    def getEachDocument() -> list:
        data = Utils.getFile(C.DOCS)
        docs = re.findall(r'(\*TEXT [^*]+)', data)

        return docs

    @staticmethod
    def getEachQuery() -> list:
        data = Utils.getFile(C.QUERY)
        docs = re.findall(r'(\*FIND [^*]+)', data)

        return docs

    @staticmethod
    def getEmptyWords() -> list:
        data = Utils.getFile(C.EMPTY_WORDS)
        return re.findall(r'\w+', data)

        # emptyWords = re.findall(r'\w+', data)
        # return [ word for word in emptyWords if len(word) > 1 ]

    @staticmethod
    def replaceOnString(pattern, string:str, repl:str='') -> str:
        """
        Given a pattern, replace every pattern matching on "string" with
        "replace" string.

        :param pattern str | list.
            str: String to replace.
            list: List of strings to replace into the "param" string.
        """
        if type(pattern) == list:
            pattern = [f'\s+{str(word)}\s+|' for word in pattern]
            pattern = ''.join(pattern)[:-1]

        elif type(pattern) != str:
            print('[ERROR] "pattern" data type need to be str or list or strings.')
            return ''

        return re.sub(pattern, repl, string)

    @staticmethod
    def truncateOnPorterAlgorithm(data:str) -> str:
        # Instatiating the Stemming class using the Porter algorithim
        stemmer = Stemmer.Stemmer('porter')

        splitData = re.findall(r'\w+', data)
        splitData = list(set(splitData))

        porterTruncate = stemmer.stemWords(splitData)

        if len(splitData) != len(porterTruncate):
            print('[ERROR] Length of splitData and porterTruncate are diff.\n')
            return data

        out = str(data)
        n = len(porterTruncate)
        for i in range(0, n):
            pattern, replace = f'\s+{splitData[i]}\s+', f' {porterTruncate[i]} '

            # Applying the truncate (reduction)
            out = re.sub(pattern, replace, out)
        
        return out

    @staticmethod
    def termFrecuency(data:str) -> dict:
        """
        'three, two, one one one, launching' -> {"three": 1, ... "one": 3}
        """
        out = {}

        splitData = re.findall(r'\w+', data)
        splitData = list(set(splitData))

        for word in splitData:
            out[word] = len(re.findall(word, data))

        return out

    @staticmethod
    def saveTermFrecuency(data:list, outFileName:str, possitionKey:str):
        """
        :param possitionKey str. Name of the key that posses the number 
        of the Text | Query.
        """
        outFileName = f'out/{outFileName}'

        preffix = 'Query' if possitionKey == 'query' else 'Doc'

        try:
            with open(outFileName, 'w') as f:
                for text in data:
                    line = f'{preffix} {text[possitionKey]}' # Number of the Text | Query
                    for key, value in text['termFrecuency'].items():
                        line += (f' {key} {value}')

                    f.write(f'{line}\n\n')
                f.close()
        except Exception as e:
            print(f'[ERROR] saveTermFrecuency "{outFileName}" Some exception detected: {str(e)}')
            return 

