# Rebuild the index under a new setting, re-evaluate, and compare the deltas:
for setting in [{"chunk": 256, "rerank": False},
                {"chunk": 512, "rerank": False},
                {"chunk": 512, "rerank": True}]:
    rebuild_index(**setting)                     # re-chunk / re-embed as needed
    rows = [{**r, "contexts": retrieve(r["question"]),
             "answer": rag_answer(r["question"])} for r in eval_data]
    rep = evaluate(Dataset.from_list(rows),
                   metrics=[faithfulness, context_recall])
    print(setting, "-> faithfulness", round(rep["faithfulness"], 2),
          "context_recall", round(rep["context_recall"], 2))
