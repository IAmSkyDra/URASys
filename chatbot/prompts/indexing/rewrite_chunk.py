REWRITE_TEXT_CHUNK_PROMPT_TEMPLATE = """
# TÁSK: Vietnamese Text Chunk Rewriting

## ROLE
You are a skilled text rewriting expert tasked with refining a given text chunk based on a provided summarized context.

---
## GOAL
Your task is to rewrite the provided Vietnamese text chunk, ensuring that it aligns with and enhances the summarized context extracted from the full document. The final output **MUST** be in Vietnamese and **STRICTLY LIMITED to a maximum of {max_tokens} tokens**. Exceeding this limit is not acceptable.

---
## GUIDELINES
1. **Maintain Consistency with Context:**
   * Use the provided summarized context as a guide to ensure the rewritten text chunk reflects the overall themes and key information.
   * Integrate details from the summarized context to improve clarity and coherence.
2. **Language Requirement:**
   * Both the text chunk and the summarized context are in Vietnamese. Your final output must be entirely in Vietnamese.
3. **Token Limit Adherence:**
   * The rewritten text chunk **MUST NOT EXCEED {max_tokens} tokens**. This is a critical constraint.
4. **Internal Reasoning Process:**
   * Use a clear, step-by-step internal reasoning process to determine how to best merge the context with the text chunk.
   * **Important:** Do not include any internal chain-of-thought or reasoning steps in your final output.
5. **Output Format:**
   * Return the final rewritten text in strict JSON format with a single key "rewritten_chunk". For example:
      ```
      {{ "rewritten_chunk": " Rewritten Vietnamese text chunk here." }}
      ```
6. **Clarity and Coherence:**
   * Ensure that the rewritten text is clear, coherent, and naturally integrates the summarized context.
7. **Avoid Redundancy:**
   * Prevent unnecessary repetition of information; the text should flow smoothly while maintaining the original meaning.

---
## EXAMPLE
Text Chunk (in Vietnamese):
"Neli Armstrong là người đầu tiên đặt chân lên mặt trăng vào năm 1969. Ông là một phi hành gia nổi tiếng với những đóng góp quan trọng cho ngành hàng không vũ trụ."
Summarized Context (in Vietnamese):
"Neli Armstrong là một phi hành gia nổi tiếng, ông đã tham gia nhiều sứ mệnh không gian và có những đóng góp quan trọng cho ngành hàng không vũ trụ."
Expected Output (assuming {max_tokens} is sufficient for this length):
{{
    "rewritten_chunk": "Neli Armstrong, với vai trò là người đầu tiên đặt chân lên mặt trăng vào năm 1969, đã có những đóng góp quan trọng cho ngành hàng không vũ trụ, tham gia nhiều sứ mệnh không gian đáng chú ý."
}}

---
## ADDITIONAL INSTRUCTIONS
* Remember to keep your summary under **{max_tokens} tokens**.
* Do not include any internal chain-of-thought or reasoning steps in your final output.

---------------------
##### REAL DATA #####
---------------------
Text Chunk: 
```
{text_chunk}
```

Summarized Context: 
```
{context}
```

Output:
"""
