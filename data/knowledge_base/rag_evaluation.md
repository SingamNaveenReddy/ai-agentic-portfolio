# RAG Evaluation

A retrieval augmented generation system should be evaluated with grounded answers, citation coverage, retrieval quality, and regression tests. Grounded answers make claims that are supported by retrieved context instead of relying only on model memory.

Citation coverage helps reviewers see whether each answer can be traced back to a source. Regression tests are useful because prompt and retrieval changes can silently break previously working behavior.

Strong RAG projects usually include a small evaluation set, examples of good and bad answers, and clear notes about chunking, ranking, and answer synthesis.
