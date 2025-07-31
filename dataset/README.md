# QA Dataset Collection for Benchmarking Answerability and Ambiguity

This repository contains a curated collection of question answering (QA) datasets used for evaluating model performance under various conditions, including answerability, ambiguity, and multi-hop reasoning. The datasets span both English and Vietnamese and are standardized for comparative benchmarking.

To support reproducible research, each dataset follows a consistent format and is released in two variants: full QA sets (`*_1000.csv`) and ambiguity-focused subsets (`*_ambious.csv`).

## Dataset Descriptions

- **SQuAD 2.0**[1]  
  An English QA dataset combining 100,000+ answerable questions with over 50,000 unanswerable ones. The benchmark challenges models to identify when no answer is available in the context.

- **UIT-ViQuAD 2.0**[2]  
  A Vietnamese adaptation of SQuAD 2.0, released in the VLSP 2021 Challenge. It includes both answerable and unanswerable questions, with careful linguistic alignment to Vietnamese syntax and semantics.

- **HotpotQA**[3]  
  A large-scale English multi-hop QA dataset requiring reasoning across multiple supporting passages. Designed to test explainability and fact synthesis in open-domain QA.

- **VIMQA**[4]  
  A Vietnamese dataset focused on advanced reasoning and explainable multi-hop QA, presented at LREC 2022. It supports complex reasoning chains and document-level context linking.

- **UniQA**  
  A proprietary, institution-specific QA dataset comprising both answerable and unanswerable questions derived from domain-specific sources (e.g., university-related FAQs). To preserve anonymity during peer review, only a 2-question preview is publicly available. Full release will follow paper acceptance.

## Dataset Variants and Format

Each dataset is provided in two variants:

| Variant         | File Pattern           | Fields                                                       |
|-----------------|------------------------|--------------------------------------------------------------|
| Standard        | `*_1000.csv`           | `question`, `answer`, `paragraph`                           |
| Ambiguous       | `*_ambious.csv`        | `question`, `answer`, `paragraph`, `info`                   |
| UniQA (hidden)  | `UniQA_*.csv`          | - `1000`: `question`, `answer`<br>- `ambious`: `question`, `answer`, `info` (only 2 visible examples) |

> In UniQA files, remaining rows beyond the first 2 are replaced with an anonymization notice.

## Dataset Statistics

| Dataset            | Answerable Questions | Unanswerable Questions | Ambiguous Questions |
|--------------------|----------------------|------------------------|---------------------|
| SQuAD 2.0          | 508                  | 492                    | 418                 |
| UIT-ViQuAD 2.0     | 800                  | 200                    | 731                 |
| HotpotQA           | 1000                 | 0                      | 0                   |
| VIMQA              | 1000                 | 0                      | 0                   |
| UniQA              | 500                  | 500                    | 314                 |

## File List

- `Hotpot_1000.csv`
- `Squad2_1000.csv`
- `Squad2_ambious.csv`
- `Viquad2_1000.csv`
- `Viquad2_ambious.csv`
- `VimQA_1000.csv`
- `UniQA_1000_anonymous.csv`
- `UniQA_ambious_anonymous.csv`

## Field Definitions

- `question`: The input query posed to the QA system.
- `answer`: Ground truth answer string.
- `paragraph`: Source context that supports or fails to support the answer.
- `info`: (In ambiguous files) Explanation of ambiguity or disambiguation rationale.

## Example Usage

```python
import pandas as pd

df = pd.read_csv("Squad2_ambious.csv")
print(df[['question', 'answer', 'info']].head())
```

## License and Release Policy

- Datasets derived from public sources follow their original licenses.
- The UniQA dataset is institution-specific and will be made available for research upon official acceptance of the associated publication.

## References

[1] Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018. Know What You Don’t Know: Unanswerable Questions for SQuAD. In *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*, pages 784–789, Melbourne, Australia. Association for Computational Linguistics.

[2] Kiet Nguyen, Son Quoc Tran, Luan Thanh Nguyen, Tin Van Huynh, Son Thanh Luu, and Ngan Luu-Thuy Nguyen. 2022. VLSP 2021 – ViMRC Challenge: Vietnamese Machine Reading Comprehension. *VNU Journal of Science: Computer Science and Communication Engineering*, 38(2).

[3] Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D. Manning. 2018. HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering. In *Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing*, pages 2369–2380, Brussels, Belgium. Association for Computational Linguistics.

[4] Khang Le, Hien Nguyen, Tung Le Thanh, and Minh Nguyen. 2022. VIMQA: A Vietnamese Dataset for Advanced Reasoning and Explainable Multi-hop Question Answering. In *Proceedings of the Thirteenth Language Resources and Evaluation Conference*, pages 6521–6529, Marseille, France. European Language Resources Association.
