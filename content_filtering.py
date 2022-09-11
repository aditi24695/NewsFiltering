from __future__ import division
import math
import numpy as np
import nltk
import sqlite3
result = []

nltk.download('stopwords')
nltk.download('punkt')
import itertools
from nltk import word_tokenize
from nltk.corpus import stopwords

########################Initialization###########################################
#news = ({"index": 1, "heading":" Sehwag: Dhoni has to score from ball one, should realise his role in T20s", "description":"Legendary action note opener Virender Sehwag on Monday advised Mahendra Singh Dhoni to get going from ball one while chasing big totals and asked the Indian team management to brief the under-pressure player about his role in the T20 team.", "link": "https://timesofindia.indiatimes.com/sports/cricket/new-zealand-in-india/team-management-must-brief-dhoni-about-his-role-in-t20s-sehwag/articleshow/61534388.cms", "date": "Mon, 06 Nov 2017 15:21:35 GMT", "type": " Top Stories " },{"index": 2, "heading": "A year on, bankers say note ban has been good", "description": "A couple of days ahead of the first anniversary of demonetisation, bankers said on Monday that the move was good for them as it resulted in higher deposits and pushed digitisation at a faster pace. Deposits, which came into the bankers note action banking sector, left banks with trillions of rupees in surplus funds, leading to action taxman officer taxman an overall decline in money market rates.", "link": "https://timesofindia.indiatimes.com/india/a-year-on-bankers-say-note-ban-has-been-good-for-them/articleshow/61533298.cms", "date": "Mon, 06 Nov 2017 13:45:22 GMT", "type":  "Top Stories" },{"index": 3, "heading": "Over 20,000 I-T returns picked for detailed probe", "description":" A scrutiny procedure in the I-T department parlance denotes submission of a volume of records action action entities and testimonials, after which the taxman or the assessing officer makes sure that the return filed is correct and the filer has opener not evaded any tax.", "link": "https://timesofindia.indiatimes.com/business/india-business/note-ban-over-20000-i-t-returns-picked-for-detailed-probe/articleshow/61532527.cms", "date": "Mon, 06 Nov 2017 12:32:34 GMT", "type":  "Top Stories" },{"index": 4, "heading":"Multi-agency group to probe Paradise Papers", "description": "The panel will first go through the details of income tax returns filed by the 714 Indian individuals and entities named in the Paradise Papers and subsequently take action, in a case-to-case basis, the sources said.", "link": "https://timesofindia.indiatimes.com/business/india-business/multi-agency-group-on-panama-leak-to-probe-paradise-papers/articleshow/61532075.cms", "date": "Mon, 06 Nov 2017 12:17:15 GMT", "type":  "Top Stories" },{"index": 5, "heading": "Exclusive: Nadella on Digital India and future", "description": "", "link": "https://timesofindia.indiatimes.com/videos/tech/Exclusive-Microsoft-CEO-Satya-Nadella-on-Digital-India-Google-Apple-and-the-future/videoshow/61530698.cms", "date":"Mon, 06 Nov 2017 11:45:04 GMT", "type":"Top Stories"})

bag_of_words = ['crime','toxic','riots','disaster','Bail','Ballistics','Battery','Beat','Behavior','Behindbars','Belligerence','Bighouse','Blackmail','Damage','Danger','entrepreneur','Failure','Fingerprint','Firebombing','Gory','Government','Grief','Grievance','Illegal','Immoral','Immunity','Impression','Imprison','capitalist','Incarceration','Judicial','Judiciary','Jurisdiction','','Revenge','Rights','Robbery','Rogue','Suppress','Surveillance','Survivor','Suspect','Suspected','Suspicion','Victim','Victory','Vigilance','Vigilante','Violate','Vagrancy','inflation','Viable','Transfer','Trauma','Quarrel','aerobics','badminton','ballbase','baseball','tabletennis','game','goldmedal','scuba','score','WorldCup','WorldSeries','wrestler','champion','competition','boxing','biking','billiards','monument','history','impact','personality','business','personality','ransomware','catastrophic','pristine','fired','mindfullness','cosmetics','artifacts','euphoria','persecuted','executiveorder','politics','parties','speculation','inequality','president','elect','burgeoning','construction','allegations',' blackout',' Government','singer']


total = []
status = 1
filterdocs = [];
array_position = 0;
tokenized_doc = []
w, h = 100, 100
result = []
########################dot product and cosine similiarity##################################
def getUserDocs(newNews, filterdocs):
    for i in range(1, 20):
        result.append(cosine_similiarity(newNews(i), filterdocs))

class getCosine(object):
    def __init__(self):
        pass

    def dot_product(self, v1, v2):
        a = len(v1)
        b =len(v2)
        return np.dot(v1, v2);


    def cosine_similiarity(self, v1, v2):
        prod = self.dot_product(v1, v2)
        len1 = math.sqrt(self.dot_product(v1, v1));
        len2 = math.sqrt(self.dot_product(v2, v2));
        if not len1:
            return 0
        if not len2:
            return 0
        return prod / (len1 * len2)


########################################tokenize document####################################################

class preProcessing(object):
    stopword = set(stopwords.words('english'))
    tokenize = lambda doc: doc.lower().split(" ")

    def __init__(self):
       pass

    def tokenize_documents(self, news):
        tokenize = lambda doc: doc.lower().split(" ")
        for d in news:
            tokenized_doc.append(tokenize(d.desc))
        return tokenized_doc
    #####################stop word removal#######################
    def remove_stop_word(self, tokenized_doc):
        for i in tokenized_doc:
            filtered_docs = []
            stem_document = []
            for j in i:
                if j not in self.stopword:
                    filtered_docs.append(j)
            stem_document = ' '.join(filtered_docs)
            filterdocs.append(stem_document)
        return filterdocs

#############################query command for news################################
# def getNews():
#     conn = sqlite3.connect('news.db')
#     cursor = conn.cursor;
#     cursor.execute("SELECT TOP 20 FROM news order by date ASC");
#     news = cursor.fetchone()
#     tokenize_documents(news)
#
####################################################################
# def add_word(word):
#     bag_of_words[array_position % 5] = word
#     while True:
#         for tag in bag_of_words:
#             if tag in bag_of_words:
#                 matrix[0][0] += 1
#             else:
#                 add_word(tag)
#         break

###############################calculating tfidf############################################

class tfidf(object):
    def __init__(self):
        pass
    def termfrequency(self, documents):
        w, h= 100, 100
        matrix = [[0 for x in range(w)] for y in range(h)]
        for i in range(0, len(documents)):
            for term in range(0, len(bag_of_words)):
                matrix[i][term]= documents[i].count(bag_of_words[term].lower())
        return matrix


    def log_term_frequency(self, matrix):
        for i in range(1, w):
            for j in range(1, h):
                if matrix[i][j]:
                    matrix[i][j] = 1+math.log(matrix[i][j], 10)
        return matrix

    def inversedocfrequency(self, matrix):
        total = self.calculate_col_sum(matrix)
        for i in range(w):
            if total[i] and w:
                total[i] = math.log(w/total[i], 10)
        return total


    def calculate_col_sum(self, matrix):
        total = [np.count_nonzero(x) for x in zip(*matrix)]
        return total

    def tf_idf(self, matrix,total):
        document = np.asarray(matrix)
        for i in range(0, h):
            for j in range(0, w):
                document[i,j] = total[j]*document[i,j]
        return document
#######################user update#####################################


#####################calculate Top documents################################

class getResults(object):
    def __init__(self):
        pass
    def calculate_top_documents(self, newNews, news):
        preProc = preProcessing()
        calcTfidf = tfidf()
        CSScore = getCosine()
        tokenized_doc = preProc.tokenize_documents(news)
        documents = preProc.remove_stop_word(tokenized_doc)
        matrix = calcTfidf.termfrequency(documents)
        matrix = calcTfidf.log_term_frequency(matrix)
        total = calcTfidf.inversedocfrequency(matrix)
        documents = calcTfidf.tf_idf(matrix, total)
        for j in range(0, len(newNews)):
            cosine_result = []
            for i in range(0, len(news)):
                if news[i].status == 1:
                    cosine_result.append(CSScore.cosine_similiarity(documents[i], self.getVectorTerm(newNews[j].desc)))
                else:
                    cosine_result.append(0)
            result.append( np.average(cosine_result))
        indexNews = []
        for j in range(0, len(newNews)):
            indexNews.append(newNews[j].news_id)
        sortedResult = [indexNews for _, indexNews in sorted(zip(result, indexNews))]
        displayNewsOrder = sortedResult[::-1]
        return displayNewsOrder

    def getVectorTerm(self, newNews):
        stopword = set(stopwords.words('english'))
        filterNews= []
        termVector = [0]*100
        tokenize_news = word_tokenize(newNews)
        for j in tokenize_news:
            if j not in stopword:
                filterNews.append(j)
                stemNews = ' '.join(filterNews)
        for term in range(0, len(bag_of_words)):
            termVector[term] = (stemNews.count(bag_of_words[term]))
        return termVector
