# Compiler Design Study Plan Checklist

Study window: May 12, 2026, 1:00 PM to May 13, 2026 night

Goal: cover all compiler design modules using repeated-question mastery, with emphasis on recurring exam patterns and full-answer practice.

## How to use this plan

1. Read the linked skill file for the question.
2. Answer the question once without notes.
3. Check the practice-question section in the same skill file.
4. Repeat the answer after correcting mistakes.
5. Keep one error log for formulas, grammar rules, tables, and diagrams.

## Day 1: May 12

### 1:00 PM - 1:45 PM
- [ ] Q11: Explain the working of different phases of a compiler and illustrate with a source language statement.
- Skill: [skill](skills/compiler_design/module_1_-_introduction_to_compilers_and_lexical_analysis/introduction-to-compilers-skill/SKILL.md)
- Focus: compiler phases, output of each phase, one worked example.

### 1:45 PM - 2:30 PM
- [ ] Q12: Explain bootstrapping with an example.
- [ ] Q12: Explain different compiler construction tools.
- Skill: [skill](skills/compiler_design/module_1_-_introduction_to_compilers_and_lexical_analysis/introduction-to-compilers-skill/SKILL.md)
- Focus: T-diagram, compiler tools, concise comparison answers.

### 2:45 PM - 3:30 PM
- [ ] Q1: What is the relevance of input buffering in lexical analysis?
- Skill: [skill](skills/compiler_design/module_1_-_introduction_to_compilers_and_lexical_analysis/lexical-analysis-skill/SKILL.md)
- Focus: tokenization, lexer role, input buffering purpose.

### 3:30 PM - 4:15 PM
- [ ] Q2: Draw a transition diagram to represent relational operators.
- Skill: [skill](skills/compiler_design/module_1_-_introduction_to_compilers_and_lexical_analysis/draw-transition-diagram-relational-operators-skill/SKILL.md)
- Focus: single-character and multi-character operators, clean state transitions.

### 4:30 PM - 5:15 PM
- [ ] Q12: Explain in detail about buffer pairs and sentinels.
- Skill: [skill](skills/compiler_design/module_1_-_introduction_to_compilers_and_lexical_analysis/buffer-pairs-and-sentinels-in-lexical-analysis-skill/SKILL.md)
- Focus: two-buffer system, sentinels, advantages, pointer movement.

### 5:15 PM - 6:00 PM
- [ ] Module 1 recap from memory
- Skill: all Module 1 skills above
- Focus: rewrite Q11, Q12, Q1, Q2 answers without notes.

### 7:00 PM - 7:45 PM
- [ ] Q3: With an example write the steps to remove left recursion.
- Skill: [skill](skills/compiler_design/module_2_-_introduction_to_syntax_analysis/basic-parsing-approaches-skill/SKILL.md)
- Focus: immediate and indirect left recursion, transformation rule.

### 7:45 PM - 8:30 PM
- [ ] Q4: What is left factoring? Left factor the given grammar.
- Skill: [skill](skills/compiler_design/module_2_-_introduction_to_syntax_analysis/basic-parsing-approaches-skill/SKILL.md)
- Focus: common prefixes, transformed grammar.

### 8:45 PM - 9:30 PM
- [ ] Q13: Construct a recursive descent parser for handling arithmetic expressions.
- Skill: [skill](skills/compiler_design/module_2_-_introduction_to_syntax_analysis/construct-a-recursive-descent-parser-for-handling-arithme-skill/SKILL.md)
- Focus: parser procedure structure, grammar cleanup first.

### 9:30 PM - 10:15 PM
- [ ] Q14: Write all the moves by the LL(1) parser for parsing the input string.
- Skill: [skill](skills/compiler_design/module_2_-_introduction_to_syntax_analysis/top-down-parsing-skill/SKILL.md)
- Focus: predictive parsing table, stack/input trace.

### 10:15 PM - 10:45 PM
- [ ] Module 2 recap from memory
- Skill: all Module 2 skills above
- Focus: left recursion rule, left factoring rule, LL(1) checklist, parser moves.

## Day 2: May 13

### 9:00 AM - 9:45 AM
- [ ] Q5: Find FIRST set and FOLLOW set of each nonterminal.
- Skill: [skill](skills/compiler_design/module_3_-_bottom-up_parsing/find-first-set-and-follow-set-of-each-nonterminal-in-the-skill/SKILL.md)
- Focus: step-by-step derivation, epsilon handling, follow propagation.

### 9:45 AM - 10:30 AM
- [ ] Q6: What are viable prefixes?
- Skill: [skill](skills/compiler_design/module_3_-_bottom-up_parsing/shift-reduce-parsing-skill/SKILL.md)
- Focus: shift-reduce actions, handle concept, viable prefix definition.

### 10:45 AM - 11:30 AM
- [ ] Q15: What is a shift-reduce parser? Explain the conflicts during shift-reduce parsing.
- Skill: [skill](skills/compiler_design/module_3_-_bottom-up_parsing/shift-reduce-parsing-skill/SKILL.md)
- Focus: shift-reduce conflict, reduce-reduce conflict, examples.

### 11:30 AM - 12:15 PM
- [ ] Q16: Construct SLR, LALR, or CLR parsing ideas and explain conflicts.
- Skill: [skill](skills/compiler_design/module_3_-_bottom-up_parsing/lr-parsing-skill/SKILL.md)
- Focus: LR item sets, table construction, grammar classification.

### 1:15 PM - 2:00 PM
- [ ] Q15: Construct SLR parsing table for the given grammar.
- Skill: [skill](skills/compiler_design/module_3_-_bottom-up_parsing/lr-parsing-skill/SKILL.md)
- Focus: canonical collection, action/goto table, SLR validation.

### 2:00 PM - 2:45 PM
- [ ] Q16: Construct CLR or LALR parsing table for the given grammar.
- Skill: [skill](skills/compiler_design/module_3_-_bottom-up_parsing/lr-parsing-skill/SKILL.md)
- Focus: table construction and justification.

### 3:00 PM - 3:45 PM
- [ ] Q8: What are L-attributed definitions and S-attributed definitions?
- Skill: [skill](skills/compiler_design/module_4_-_syntax-directed_translation_and_intermediate_code_generation/syntax-directed-translation-skill/SKILL.md)
- Focus: differences, examples, evaluation rules.

### 3:45 PM - 4:30 PM
- [ ] Q17: Explain bottom-up evaluation of S-attributed definitions.
- Skill: [skill](skills/compiler_design/module_4_-_syntax-directed_translation_and_intermediate_code_generation/syntax-directed-translation-skill/SKILL.md)
- Focus: translation scheme and evaluation order.

### 4:45 PM - 5:30 PM
- [ ] Q18: Construct the syntax tree and three-address code for assignment statements.
- Skill: [skill](skills/compiler_design/module_4_-_syntax-directed_translation_and_intermediate_code_generation/intermediate-code-generation-skill/SKILL.md)
- Focus: syntax tree, TAC, SDD, worked example.

### 5:30 PM - 6:15 PM
- [ ] Q7: Explain quadruples, triples, and indirect triples with examples.
- Skill: [skill](skills/compiler_design/module_4_-_syntax-directed_translation_and_intermediate_code_generation/intermediate-code-generation-skill/SKILL.md)
- Focus: representations, table format, comparison.

### 6:30 PM - 7:15 PM
- [ ] Q7: Explain the structure of activation record.
- Skill: [skill](skills/compiler_design/module_4_-_syntax-directed_translation_and_intermediate_code_generation/the-structure-of-activation-record-skill/SKILL.md)
- Focus: stack frame parts, runtime stack, storage allocation.

### 7:15 PM - 8:00 PM
- [ ] Q9: Differentiate local and global optimizations.
- Skill: [skill](skills/compiler_design/module_5_-_code_optimization_and_generation/code-optimization-skill/SKILL.md)
- Focus: optimization scope and examples.

### 8:00 PM - 8:45 PM
- [ ] Q19: Explain basic blocks and code optimization techniques.
- Skill: [skill](skills/compiler_design/module_5_-_code_optimization_and_generation/code-optimization-skill/SKILL.md)
- Focus: basic blocks, loop optimizations, peephole optimization.

### 9:00 PM - 9:45 PM
- [ ] Q20: Explain the code generation algorithm and getreg function.
- Skill: [skill](skills/compiler_design/module_5_-_code_optimization_and_generation/code-generation-skill/SKILL.md)
- Focus: register descriptors, code generation flow.

### 9:45 PM - 10:30 PM
- [ ] Q20: Use Sethi-Ullman or convert TAC to machine code for the given statement.
- Skill: [skill](skills/compiler_design/module_5_-_code_optimization_and_generation/code-generation-skill/SKILL.md)
- Focus: code sequence, register use, machine-code conversion.

### 10:30 PM onward
- [ ] Full mock revision
- Focus: one question from Module 1, one from Module 3, and one from Module 5 under timed conditions.

## Priority order if time gets short

1. Module 3: FIRST/FOLLOW, shift-reduce, LR, SLR, LALR, CLR.
2. Module 2: left recursion, left factoring, recursive descent, LL(1).
3. Module 5: code optimization and code generation.
4. Module 4: TAC, syntax-directed translation, activation records.
5. Module 1: phases, bootstrapping, lexical analysis, buffering.

## Exam answer pattern

- Define the concept first.
- State the rule or algorithm.
- Show the worked example or diagram.
- Finish with a short conclusion or comparison.

## Repeated-question clusters to master

- Module 1: Q1, Q2, Q11, Q12.
- Module 2: Q3, Q4, Q13, Q14.
- Module 3: Q5, Q6, Q15, Q16.
- Module 4: Q7, Q8, Q17, Q18.
- Module 5: Q9, Q10, Q19, Q20.

## Bonus questions if time remains

### Module 1 extras
- [ ] Q12: Explain the role of transition diagrams in recognition of tokens.
- [ ] Q11: Write code for the lexical analyser for the above design.
- [ ] Q1: What is the relation between input buffering and lexical analysis performance?

### Module 2 extras
- [ ] Q13: Explain the error recovery strategies in parsing.
- [ ] Q14: Write and explain the algorithm for constructing LL(1) predictive parsing table.
- [ ] Q13: Explain any two drawbacks of recursive descent parser and its solutions.
- [ ] Q4: Write the algorithm of left factoring.

### Module 3 extras
- [ ] Q6: What is handle pruning?
- [ ] Q5: Explain synthesized attributes and inherited attributes.
- [ ] Q15: Construct canonical LR(0) collection of items for a grammar.
- [ ] Q16: Explain different parsing conflicts in the SLR parsing table.
- [ ] Q16: Differentiate CLR and LALR parsers.
- [ ] Q33-style practice: operator precedence parsing or viable-prefix tracing if your notes include it.

### Module 4 extras
- [ ] Q7: Define three-address code, triples, and quadruples.
- [ ] Q8: Generate intermediate code for an if-else statement.
- [ ] Q8: Write three-address code for a while loop by choosing a suitable example.
- [ ] Q18: Write syntax directed definition to construct syntax tree and three-address code for assignment statements.
- [ ] Q18: Explain static allocation and heap allocation strategies.
- [ ] Q18: Explain run-time environments or storage allocation strategies.

### Module 5 extras
- [ ] Q19: Explain the optimization of basic blocks.
- [ ] Q19: Explain different code optimization techniques.
- [ ] Q19: Explain any three code optimization transformations.
- [ ] Q19: Explain any four principal sources of optimization.
- [ ] Q10: Explain any three issues in the design of a code generator.
- [ ] Q20: Illustrate the role of register descriptor and address descriptor in code generation phase.
- [ ] Q20: Convert to three-address code and write machine code for a given statement.
