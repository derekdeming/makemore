"""
    This is going to be a character level language model to understand the nit and grit of the large language models. 
    The idea is to create a model that can generate text from a given text. More specifically we will generate names because 
    we are going to be training on a dataset of names.

    A character level language model is a model that takes in a sequence of characters and outputs a sequence of characters. It treats every line 
    and every individual character as a sequence.

    We are going to use several language model neural network nets such as the following: 
        - Bigram (this is a simple model that takes in two characters and outputs a character)
        - Bag of words (this is a simple model that takes in a sequence of characters and outputs a character)
        - MLP - similar to the following paper - https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf
        - RNN - similar to the following paper - https://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf
        - GRU - similar to the following paper - https://arxiv.org/abs/1409.1259
        - LSTM - similar to the following paper - https://arxiv.org/abs/1308.0850
        - Transformer - similar to the following paper - https://arxiv.org/abs/1706.03762

"""