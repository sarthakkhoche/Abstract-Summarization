# Abstract Summarization

Large numbers of conference papers are accessible today and all of them have some standard features: starting with a short abstract, introduction, related work, main contribution, conclusions/discussion etc. Here we present an approach to get an abstract for a research paper based on its content. We scrape the research papers for their abstract and contents and then train an ‘Abstract Generator’ model for research papers using the scraped data as annotated data for supervised learning. 

The input to our trained model is a research paper that doesn’t have an abstract and the model outputs a concise and accurate abstract for the paper. We have demonstrated two approaches - using LSTM and BiLSTM for abstractive summarization of research papers.
