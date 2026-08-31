# LLM Evaluation Rubric

Each response is scored across 4 different criteria on a 0-4 scale (the total max score an LLM response can achieve is 16 points).

---

## 1. Factual & Technical Correctness
* **4 (Perfect):** The solution is fully correct. The generated code passes all test cases. The math/science answers, derivations, values, and units are accurate.
* **3. (Minor Flaw):** The solution is mostly correct. The generated code fails an extreme edge case or or has a minor bug. The math/science has a minor arithmetic or round slip without invalidating the core logic.
* **2. (Major Flaw):** Partially correct. The generated code fails primary test cases or has serious runtime issues. The math/science uses an incorrect equation or yields the wrong final value.
* **1. (Mostly Incorrect):** The solution is fundamentally broken, with severe logic failures, incorrect fundamental principles, or non-functional code.
* **0. (Completely Incorrect/Refusal):** The solution is hallucinated nonsense, completely irrelevant output, or an unprompted refusal to answer.

---

## 2. Instruction & Constraint Following
* **4 (Strict Adherence):** The response follows every positive constraint (e.g., requested language, specified time/space complexity) and negative constraint (e.g., "Do not simplify the answer further").
* **3. (Minor Deviation):** The response satisfies all major instructions, but does not follow one or more minor details (e.g., including a markdown file when asked for raw code only).
* **2. (Partial Adherence):** The response missed one explicit direction/constraint (e.g., used an extra array when O(1) a auxiliary space was required).
* **1. (Poor Adherence):** The response ignored major constraints or prompt requirements.
* **0 (Complete Failure):** The responses disregarded the entire prompt, especially the instructions and constraints.

---

## 3. Methodological Soundness
* **4 (Rigorous and Optimal):** The algorithmic approach is optimal. Mathematical proofs and physical derivations are logically valid from first principles.
* **3 (Valid but Suboptimal):** The approach is correct and valid, but uses a brute-force/suboptimal algorithm or an extremely complicated derivation.
* **2 (Flawed Reasoning):** The core method contains conceptual flaws, false statements of proof, or invalid physical assumptions, even if the final guess appears close to the right answer.
* **1 (Invalid Methodology):** Random heuristics, circular logic, or invalid physical laws have been applied to obtain an answer.
* **0 (No Coherent Method):** No valid step-by-step logic has been provided.

---

## 4. Completeness and Clarity
* **4 (Clear & Thorough):** The response covers all sub-questions and edge cases. It also has a well-structured explanation with clear variable definitions.
* **3 (Good):** The response addresses all parts, but the explanation is slightly verbose or could be better organized.
* **2. (Incomplete)** The response addresses the main question but skips secondary sub-prompts or edge cases.
* **1 (Vague / Disorganized):** The response is difficult to follow, poorly formatted, or missing important components.
* **0 (Unintelligible):** The responses lacks a coherent explanation.