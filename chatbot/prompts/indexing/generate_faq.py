FAQ_GENERATION_PROMPT_TEMPLATE = """
# TÁSK: Vietnamese FAQ Generation

## ROLE
You are an expert in generating frequently asked questions (FAQ) pairs that capture the key insights from provided texts.

---
## GOAL
Your task is to extract and generate up to {max_faq_pairs} FAQ pairs from the provided Vietnamese text chunk. Each FAQ pair should consist of a clear question and a concise answer, both written in Vietnamese, derived directly from the text.

---
## GUIDELINES
1. **Extraction of Key Information:**
   * Analyze the given text chunk and identify critical points, details, or common inquiries that can naturally form FAQ pairs.
2. **Language Requirement:**
   * The input text chunk is in Vietnamese, and your output must also be entirely in Vietnamese.
3. **Output Structure:**
   * Return the final output in strict JSON format as an array of objects. Each object must include two keys: "question" and "answer". For example:
    [
        {{
            "question": "Question in Vietnamese?",
            "answer": "Answer in Vietnamese."
        }},
        ...
    ]
4. **Limit on FAQ Pairs:**
   * Generate at most {max_faq_pairs} FAQ pairs. If the text provides fewer points, then output only the relevant pairs.
5. **Clarity and Relevance:**
   * Ensure that each question is clear, directly derived from the text, and that its corresponding answer is succinct and accurately reflects the content.
6. **Internal Reasoning Process:**
   * Use a step-by-step internal reasoning process (chain-of-thought) to determine the most relevant FAQ pairs.
   * **Important:** Do not include any internal chain-of-thought or reasoning steps in your final output.

---
## EXAMPLE
Text Chunk (in Vietnamese):
"Neli Armstrong là người đầu tiên đặt chân lên mặt trăng vào năm 1969. Ông là một phi hành gia nổi tiếng với những đóng góp quan trọng cho ngành hàng không vũ trụ."
Expected Output:
[
    {{
        "question": "Ai là người đầu tiên đặt chân lên mặt trăng?",
        "answer": "Neli Armstrong là người đầu tiên đặt chân lên mặt trăng vào năm 1969."
    }},
    {{
        "question": "Những đóng góp của Neli Armstrong cho ngành hàng không vũ trụ là gì?",
        "answer": "Neli Armstrong là một phi hành gia nổi tiếng với những đóng góp quan trọng cho ngành hàng không vũ trụ."
    }}
]

---
## ADDITIONAL INSTRUCTIONS
* Remember to keep your output within the limit of **{max_faq_pairs} FAQ pairs**.
* Do not include any internal chain-of-thought or reasoning steps in your final output.

---------------------
##### REAL DATA #####
---------------------
REAL DATA:
Text Chunk: {text_chunk}
Output:
"""
