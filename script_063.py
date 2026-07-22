from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from datasets import Dataset
 
ds = Dataset.from_list(eval_data)
report = evaluate(ds, metrics=[faithfulness, answer_relevancy, context_precision, context_recall])
print(report)   # per-metric scores between 0 and 1
