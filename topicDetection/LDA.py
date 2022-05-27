import gensim.corpora as corpora
import gensim
from pprint import pprint


def generateLDA(allTokens):
    id2word = corpora.Dictionary(allTokens)# Create Corpus
    texts = allTokens# Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]# View



    # number of topics
    num_topics = 10 # Build LDA model

    lda_model = gensim.models.ldamulticore.LdaMulticore(corpus=corpus,
                                                       id2word=id2word,
                                                       num_topics=num_topics,
                                                       random_state=100,
                                                       chunksize=10,
                                                       eval_every=1,
                                                       passes=10,
                                                       alpha='symmetric',
                                                       iterations=100,
                                                       per_word_topics=True)

    # lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
    #                                            id2word=id2word,
    #                                            num_topics=num_topics,
    #                                            update_every=1,
    #                                            alpha='symmetric',
    #                                            per_word_topics=True)

    pprint(lda_model.print_topics(num_topics=10,num_words=10))

    doc_lda = lda_model[corpus]

    return lda_model, corpus
