# LLM STEM Response Evaluator

## Project Goal

The goal of this project is to develop practical experience systematically evaluating Large Language Model (LLM) responses across STEM disciplines: Computer Science, Mathematics, and Natural Sciences (biology, chemistry, physics). 

This project creates a controlled set of 15 prompts with graduated difficulty, submits them to multiple LLMs, and evaluates their responses using a consistent rubric. When a response contains executable code, quantitative derivations, or scientific answers, solutions are verified against test cases or analytical proofs. 

The project is intended to answer questions such as:

* How accurately do different LLMs solve STEM problems as difficulty increases? 
* How consistently do LLMs follow detailed instructions and constraints?
* What types of errors (logical, conceptual, mathematical, syntax, etc.) do LLMs commonly make across different subjects? 
* Where do different models perform differently across coding, math, and science?

**Target scope**: Approximately 10–20 hours.




## Required Features


**1. Prompt Dataset**

The benchmark contains **15 prompts** organized into three domains, progressing from **Level 1 (Pretty Easy)** to **Level 5 (Very Difficult)**:

* Coding:
  * Level 1 (Easy) — Simple syntax, strings, and list operations
  * Level 2 (Medium-Easy) — Data structures and fundamental iteration
  * Level 3 (Medium) — Algorithmic challenges with boundary cases
  * Level 4 (Hard) — Advanced optimization and graph traversal
  * Level 5 (Very Hard) — Low-level memory and complex concurrency
* Math:
  * Level 1 (Easy) — Algebra I
  * Level 2 (Medium-Easy) — Geometry/Algebra II
  * Level 3 (Medium) — Precalculus/Calculus I
  * Level 4 (Hard) — Calculus II
  * Level 5 (Very Hard) — Calculus III
* Science:
  * Level 1 (Easy) — Mendelian genetics or cellular respiration/photosynthesis
  * Level 2 (Medium-Easy) — Stoichiometry and ideal gas law calculations
  * Level 3 (Medium) — Chemical equilibrium or 2D projectile kinematics
  * Level 4 (Hard) — Rotational dynamics with variable torque or conservation of angular momentum
  * Level 5 (Very Hard) — Rotational inertia via integration or variable work & potential energy


**2. Multiple LLM Responses**

Submit the **same prompts** to three LLMs.

Examples of possible LLMs include, but are not limited to:
* ChatGPT
* Gemini
* Claude
* Copilot
* Grok
* DeepSeek

For each response, record:
* Prompt
* Model used
* Model response
* Date of evaluation
* Evaluation scores
* Evaluator notes

Keep the prompts consistent between models so comparisons are meaningful.


**3. LLM Evaluation Rubric**

Develop a rubric before performing the full evaluation.

Possible criteria:
* **Factual & Technical Correctness**: Does the model arrive at the correct final answer, proof, or execution result? 
* **Instruction & Constraint Following**: Did the model adhere to all output formatting, variable constraints, and negative constraints? 
* **Methodological Soundness**: Are the intermediate steps, derivations, or algorithmic designs logically valid? 
* **Completeness & Clarity**: Does the explanation address all sub-questions with structured, coherent explanations?

Define a consistent scoring scale for each criterion and document what each score means.

**4. Verification & Ground Truth Testing**

* **Coding**: Run generated code against unit test suites covering standard cases and edge cases. 
* **Math & Science**: Validate step-by-step analytical solutions against established theorems, symbolic solvers, or known scientific constants and equations.

**5. Error Classification**

Create categories for recurring LLM failures.

Possible categories could include:
* Coding: Syntax errors, off-by-one errors, infinite loops, memory leaks, unhandled edge cases. 
* Math: Arithmetic mistakes, false algebraic simplifications, invalid domain assumptions, hallucinated theorems. 
* Science: Unit conversion errors, sign errors in vector components, misapplied physical/chemical formulas, conceptual biological confusions.

**6. Results Analysis**

After completing the evaluations, summarize the results.

Potential questions to ask:
* Which model performed best overall?
* Which model followed instructions most consistently?
* Which categories of problems caused the most errors?
* What were the most common failure types?
* Were any responses convincing but incorrect?
* Did manual review and executable testing ever lead to different conclusions?

## Milestones

**Milestone 1 — Design the Experiment**

**Estimated time**: 2–3 hours

**Tasks:**
* Define research questions focused on domain differences (Coding vs. Math vs. Science) and scaling degradation across difficulty levels 1 through 5. 
* Create 15 distinct prompts: 5 coding problems (Python), 5 math problems (Algebra to Calculus), and 5 science problems (Biology, Chemistry, Physics). 
* Write explicit constraints, input/output formats, and ground-truth answer keys for each question. 
* Define the multi-domain evaluation rubric covering technical correctness, constraint adherence, methodological soundness, and clarity.
* Establish the repository layout and tracking schemas (prompts.csv, evaluations.csv).

**What to Learn:**
* How to come up with prompt constraints that minimize ambiguity across different STEM subjects. 
* How to design a standardized difficulty progression path across both qualitative and quantitative disciplines. 
* Why objective grading criteria must be pre-registered before collecting model outputs to prevent bias. 

**Milestone 2 - Collect LLM Responses**

**Estimated time**: 2–3 hours

**Tasks:**
* Select three of the best LLMs to evaluate. 
* Submit the identical set of 15 prompts to each model under consistent testing conditions. 
* Record the raw responses untouched into the “model_responses.csv” file, capturing the timestamp, model version, and generation metadata.
* Document unusual output generation behavior (e.g., token cutoffs, refusals, formatting deviations). 

**What to Learn:**
* How different LLMs and their reasoning behaviors diverge across non-coding vs. coding tasks. 
* The necessity of maintaining strict prompt isolation to ensure a fair comparative benchmark. 
* Practical data hygiene strategies for managing multi-turn or structured raw model outputs. 

**Milestone 3 — Evaluate Responses**

**Estimated time**: 3–5 hours

**Tasks:**
* Grade every response using the predetermined scoring scale. 
* Perform step-by-step verification of mathematical solutions, chemical balances, and biological pathways. 
* Record detailed evaluator rationale for score deductions in “evaluations.csv”.
* Tag candidate failure modes (e.g., arithmetic mistake, hallucinated theorem, syntax error, missing/incorrect unit conversion, etc.). 

**What to Learn:**
* How to maintain uniform grading standards across both deterministic (code output) and conceptual (biological processes, mathematical algorithms, etc.) answers. 
* How to identify subtle, convincing "hallucinations"/errors that appear correct at a surface level. 
* How to separate correctness from communicative style or verbosity. 

**Milestone 4 — Code & Solution Verification**

**Estimated time**: 2-4 hours

**Tasks:**
* Write and run automated test suites for the 5 coding prompts across standard inputs and edge cases. 
* Verify computational math and science solutions against online solvers (e.g., Symbolab, WolframAlpha) or manual multi-step calculations. 
* Record test failures, runtime errors, and discrepancies between manual inspection and execution results. 
* Adjust initial rubric scores where dynamic testing reveals hidden logical or runtime faults.

**What to Learn:**
* The limits of static code inspection compared to the advantages of automated dynamic test execution. 
* How subtle edge cases (e.g., off-by-one errors, zero-division error) frequently bypass visual review. 
* How to integrate human evaluation rubrics with programmatic unit testing. 

**Milestone 5 — Analyze Model Performance**

**Estimated time**: 2–3 hours

**Tasks:**
* Aggregate raw evaluation scores using Python tools such as pandas and numpy.
* Compare overall model performance across subjects (Coding vs. Math vs. Science) and difficulty levels (Level 1 to Level 5). 
* Group failure types into an error taxonomy (e.g., algorithmic logic, incorrect computational math, improper unit conversion, instruction ignoring). 
* Generate charts and comparison tables visualizing changes in scores as difficulty increases. 

**What to Learn:**
* How to translate raw scoring datasets into clear, data-driven analytical analyses of results. 
* How problem complexity impacts an LLM’s reasoning across different academic disciplines. 
* How to distinguish evidence-backed conclusions from speculative evaluator assumptions.

**Milestone 6 — Document the Project**

**Estimated time**: 1–2 hours

**Tasks:**
* Update the project README as a comprehensive final documentation. 
* Write up the evaluation methodology, dataset design rationale, and final scoring rubric. 
* Embed summary performance tables and visual charts into the analysis section. 
* Explain about experimental limitations (e.g., sample size per category, evaluator subjectivity) and lessons learned. 

**What to Learn:**
* How to communicate technical benchmark results clearly and transparently. 
* How to articulate experimental boundaries and the limitations of small-sample LLM evaluation. 
* How to present technical documentation for public code GitHub repositories.


## Deliverables

* Documented prompt dataset (prompts/)
* Raw model responses (responses/)
* Standardized evaluation rubric (evaluations/rubric.md)
* Completed evaluation logs (evaluations/evaluations.csv)
* Verification and test cases (tests/)
* Taxonomy of failure modes
* Comparative analysis & visualizations (analysis/, results/)
* Final project documentation (README.md)
