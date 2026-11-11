# CausalRL

Code for **Rule Learning with Causal Intervention for Knowledge Graph Reasoning**.

## Installation

Use Python 3.10 or later. Install PyTorch for your CUDA version, then install the remaining dependencies:

```bash
pip install -r requirements.txt
```

## Datasets

The `datasets/` directory contains Family, Kinship, UMLS, WN18RR (`wn-18rr`), and FB15K-237 (`fb15k-237`). Each dataset includes entities, relations, facts, inverse facts, training, validation, and test splits.

## Training and evaluation

Run commands from `code/`:

```bash
cd code
python main.py --datasets family --model CausalRL \
  --epochs 500 --alpha 0.6 --anchor 500 \
  --sample_max_path_len 2 --embedding_size 512 \
  --learning_rate 0.00005 --batch_size 1000 \
  --get_top_k 140 --embedding_use causal \
  --rule_len_low 2 --rule_len_high 2 --seed 2
```

The command trains the model, generates rules, and evaluates knowledge graph completion. Checkpoints, learned rules, and evaluation output are written to `results/`, `rules/`, and `evaluate/` under the repository root. An existing checkpoint with matching filename parameters is loaded for rule generation and evaluation.

Select another dataset with `--datasets kinship`, `--datasets umls`, `--datasets wn-18rr`, or `--datasets fb15k-237`. Use `--gpu` to select a visible CUDA device; `--parallel` enables multiple visible GPUs. CPU execution is available when CUDA is disabled.

The evaluator propagates rules on facts, training, and validation triples, and filters other known true answers when ranking test queries. It reports TOP MRR, expectation MRR, and Hits@1/3/10.
