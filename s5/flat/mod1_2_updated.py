import streamlit as st
import graphviz
import json
import copy
from itertools import product

# --- Helper Function to Style Graphs ---
def create_base_graph(title=""):
    """Creates a Digraph with default styling for nodes and edges."""
    dot = graphviz.Digraph(comment=title)
    dot.attr('node', shape='circle', style='filled', fillcolor='lightblue', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica')
    dot.attr(rankdir='LR', label=title, fontsize='20', labelloc='t')
    return dot

# --- Automaton Data Structures ---
class Automaton:
    def __init__(self, states, alphabet, transitions, start_state, final_states, description=""):
        self.states = sorted(list(states))
        self.alphabet = set(alphabet)
        self.transitions = transitions # Dict: {(state, symbol): set_of_states}
        self.start_state = start_state
        self.final_states = set(final_states)
        self.description = description

    def to_dict(self):
        serializable_transitions = {f"{k[0]},{k[1]}": list(v) for k, v in self.transitions.items()}
        return {
            "states": list(self.states), "alphabet": sorted(list(self.alphabet)),
            "transitions": serializable_transitions, "start_state": self.start_state,
            "final_states": list(self.final_states), "description": self.description
        }

def draw_automaton(automaton, title=""):
    """Draws any automaton using Graphviz."""
    dot = create_base_graph(title)
    for state in automaton.final_states:
        dot.node(str(state), shape='doublecircle')
    for state in automaton.states:
        if state not in automaton.final_states:
            dot.node(str(state))
    dot.node('start', shape='point')
    dot.edge('start', str(automaton.start_state))
    for (from_state, symbol), to_states in automaton.transitions.items():
        for to_state in to_states:
            dot.edge(str(from_state), str(to_state), label=str(symbol))
    return dot

# --- Pre-loaded Automata Examples ---
PRELOADED_AUTOMATA = {
    "ε-NFA: Ends with 'ab'": Automaton(
        states={'q0', 'q1', 'q2', 'q3'}, alphabet={'a', 'b', 'ε'},
        transitions={('q0', 'a'): {'q0'}, ('q0', 'b'): {'q0'}, ('q0', 'ε'): {'q1'}, ('q1', 'a'): {'q2'}, ('q2', 'b'): {'q3'}},
        start_state='q0', final_states={'q3'}, description="Accepts strings ending in 'ab'."
    ),
    "NFA: Contains 'aba'": Automaton(
        states={'q0', 'q1', 'q2', 'q3'}, alphabet={'a', 'b'},
        transitions={('q0', 'a'): {'q0', 'q1'}, ('q0', 'b'): {'q0'}, ('q1', 'b'): {'q2'}, ('q2', 'a'): {'q3'}, ('q3', 'a'): {'q3'}, ('q3', 'b'): {'q3'}},
        start_state='q0', final_states={'q3'}, description="Accepts strings containing 'aba'."
    ),
    "DFA: Even number of 'a's": Automaton(
        states={'S0', 'S1'}, alphabet={'a', 'b'},
        transitions={('S0', 'a'): {'S1'}, ('S0', 'b'): {'S0'}, ('S1', 'a'): {'S0'}, ('S1', 'b'): {'S1'}},
        start_state='S0', final_states={'S0'}, description="Accepts strings with an even number of 'a's."
    ),
    "DFA: Not minimal": Automaton(
        states={'A', 'B', 'C', 'D', 'E'}, alphabet={'0', '1'},
        transitions={('A', '0'): {'B'}, ('A', '1'): {'C'}, ('B', '0'): {'B'}, ('B', '1'): {'D'}, ('C', '0'): {'B'}, ('C', '1'): {'C'}, ('D', '0'): {'B'}, ('D', '1'): {'E'}, ('E', '0'): {'B'}, ('E', '1'): {'C'}},
        start_state='A', final_states={'D', 'E'}, description="A non-minimal DFA where C,E and B,D are equivalent."
    )
}

# --- Conversion Algorithms (Existing functions are unchanged) ---
def get_epsilon_closure(automaton, states):
    closure = set(states)
    stack = list(states)
    while stack:
        state = stack.pop()
        epsilon_transitions = automaton.transitions.get((state, 'ε'), set())
        for target_state in epsilon_transitions:
            if target_state not in closure:
                closure.add(target_state)
                stack.append(target_state)
    return frozenset(closure)

def convert_enfa_to_nfa(enfa):
    nfa_transitions = {}
    for state in enfa.states:
        closure = get_epsilon_closure(enfa, {state})
        for symbol in enfa.alphabet - {'ε'}:
            move_on_symbol = set().union(*(enfa.transitions.get((s, symbol), set()) for s in closure))
            if move_on_symbol:
                nfa_transitions[(state, symbol)] = get_epsilon_closure(enfa, move_on_symbol)
    nfa_final_states = {s for s in enfa.states if not enfa.final_states.isdisjoint(get_epsilon_closure(enfa, {s}))}
    return Automaton(set(enfa.states), enfa.alphabet - {'ε'}, nfa_transitions, enfa.start_state, nfa_final_states, "Converted from ε-NFA")

def convert_nfa_to_dfa(nfa):
    steps = []
    dfa_states, dfa_transitions, dfa_final_states = set(), {}, set()
    initial_closure = get_epsilon_closure(nfa, {nfa.start_state})
    q0_dfa = initial_closure
    unprocessed, dfa_states = [q0_dfa], {q0_dfa}
    steps.append(f"Initial DFA state is ε-closure({{{nfa.start_state}}}) = {set(q0_dfa)}")
    while unprocessed:
        current_nfa_states = unprocessed.pop(0)
        if not nfa.final_states.isdisjoint(current_nfa_states):
            dfa_final_states.add(current_nfa_states)
        for symbol in nfa.alphabet - {'ε'}:
            next_nfa_states = set().union(*(nfa.transitions.get((s, symbol), set()) for s in current_nfa_states))
            if not next_nfa_states: continue
            target_dfa_state = get_epsilon_closure(nfa, next_nfa_states)
            dfa_transitions[(current_nfa_states, symbol)] = {target_dfa_state}
            steps.append(f"δ({set(current_nfa_states)}, {symbol}) = ε-closure({next_nfa_states}) = {set(target_dfa_state)}")
            if target_dfa_state not in dfa_states:
                dfa_states.add(target_dfa_state)
                unprocessed.append(target_dfa_state)
    state_map = {s: f"S{i}" for i, s in enumerate(dfa_states)}
    pretty_states = set(state_map.values())
    pretty_start = state_map[q0_dfa]
    pretty_final = {state_map[s] for s in dfa_final_states}
    pretty_transitions = {(state_map[f], sym): {state_map[list(t)[0]]} for (f, sym), t in dfa_transitions.items()}
    return Automaton(pretty_states, nfa.alphabet - {'ε'}, pretty_transitions, pretty_start, pretty_final, "Converted from NFA/ε-NFA"), steps

def minimize_dfa(dfa):
    # (Implementation is unchanged)
    states, alphabet = list(dfa.states), list(dfa.alphabet)
    P = [dfa.final_states, set(states) - dfa.final_states]
    W = [dfa.final_states] if len(dfa.final_states) <= len(states) / 2 else [set(states) - dfa.final_states]
    while W:
        A = W.pop(0)
        for symbol in alphabet:
            X = {s for s in states if dfa.transitions.get((s, symbol)) and list(dfa.transitions.get((s, symbol)))[0] in A}
            new_P = []
            for Y in P:
                intersection, difference = Y.intersection(X), Y.difference(X)
                if intersection and difference:
                    new_P.extend([intersection, difference])
                    if Y in W: W.remove(Y); W.extend([intersection, difference])
                    else: W.append(intersection) if len(intersection) <= len(difference) else W.append(difference)
                else: new_P.append(Y)
            P = new_P
    state_map = {s: f"M{i}" for i, part in enumerate(P) for s in part if part}
    min_states = set(state_map.values())
    min_start = state_map[dfa.start_state]
    min_final = {state_map[s] for s in dfa.final_states}
    min_transitions = {(state_map[f], sym): {state_map[list(t)[0]]} for (f, sym), t in dfa.transitions.items()}
    return Automaton(min_states, set(alphabet), min_transitions, min_start, min_final, "Minimized DFA")

def convert_fa_to_re(automaton):
    # (Implementation is unchanged)
    gnfa = copy.deepcopy(automaton)
    states_to_rip = list(gnfa.states)
    new_start, new_final = 'GS_START', 'GF_FINAL'
    gnfa.states.extend([new_start, new_final])
    gnfa.transitions[(new_start, 'ε')] = {gnfa.start_state}
    for f_state in gnfa.final_states:
        gnfa.transitions[(f_state, 'ε')] = gnfa.transitions.get((f_state, 'ε'), set()) | {new_final}
    gnfa.start_state = new_start
    gnfa.final_states = {new_final}
    def combine_re(r1, r2): return f"({r1}|{r2})" if r1 and r2 else r1 or r2
    for rip in states_to_rip:
        in_edges = {p: sym for (p, sym), t in gnfa.transitions.items() if rip in t and p != rip}
        out_edges = {t: sym for (s, sym), t_set in gnfa.transitions.items() for t in t_set if s == rip and t != rip}
        loops = [sym for (s, sym), t in gnfa.transitions.items() if s == rip and rip in t]
        r_loop = f"({combine_re(*loops)})*" if len(loops) > 1 else f"({loops[0]})*" if loops else ""
        for p_state, r_in in in_edges.items():
            for t_state, r_out in out_edges.items():
                r_in_fmt, r_out_fmt = ("" if r_in == 'ε' else r_in), ("" if r_out == 'ε' else r_out)
                new_re = f"{r_in_fmt}{r_loop}{r_out_fmt}" or 'ε'
                existing_re = [sym for (s, sym), t in gnfa.transitions.items() if s == p_state and t_state in t]
                combined = combine_re(existing_re[0], new_re) if existing_re else new_re
                if existing_re: gnfa.transitions.pop((p_state, existing_re[0]))
                gnfa.transitions[(p_state, combined)] = {t_state}
        gnfa.transitions = {(s, sym): t for (s, sym), t in gnfa.transitions.items() if s != rip and rip not in t}
    final_re = [sym for (s, sym), t in gnfa.transitions.items() if s == new_start and new_final in t]
    return final_re[0] if final_re else ""

def convert_grammar_to_nfa(grammar_str):
    """Parses regular grammar rules and converts them to an NFA."""
    productions = [line.strip() for line in grammar_str.splitlines() if line.strip()]
    non_terminals, terminals, transitions = set(), set(), {}
    start_symbol = None
    
    # First pass to find all non-terminals
    for prod in productions:
        lhs, _ = prod.split("->")
        non_terminals.add(lhs.strip())
        if start_symbol is None: start_symbol = lhs.strip()

    final_state = "GF_Final" # A dedicated final state
    states = non_terminals | {final_state}
    final_states = {final_state}

    for prod in productions:
        lhs, rhs = [p.strip() for p in prod.split("->")]
        
        if len(rhs) == 1: # Rule like A -> a or A -> e
            if rhs in non_terminals: raise ValueError(f"Invalid rule: {prod}. Cannot go to a non-terminal alone.")
            if rhs == 'e' or rhs == 'ε': # Epsilon rule
                final_states.add(lhs)
            else: # Terminal rule
                terminals.add(rhs)
                key = (lhs, rhs)
                if key not in transitions: transitions[key] = set()
                transitions[key].add(final_state)
        elif len(rhs) == 2: # Rule like A -> aB
            terminal, non_terminal = rhs[0], rhs[1]
            if terminal in non_terminals or non_terminal not in non_terminals:
                raise ValueError(f"Invalid rule format: {prod}. Must be 'terminalNonTerminal'.")
            terminals.add(terminal)
            key = (lhs, terminal)
            if key not in transitions: transitions[key] = set()
            transitions[key].add(non_terminal)
        else:
            raise ValueError(f"Invalid rule format: {prod}")
            
    return Automaton(states, terminals, transitions, start_symbol, final_states, "Converted from Regular Grammar")

# --- UI Components ---
st.set_page_config(layout="wide")
st.title("Automata Learning Lab & Creator  Workbench 🎓")

st.sidebar.title("Select Mode")
mode = st.sidebar.radio("Choose your mode:", ("Learning Lab", "Manual Creator"))

automaton = None

if mode == "Learning Lab":
    st.sidebar.header("Select an Example")
    example_choice = st.sidebar.selectbox("Choose an automaton to study:", options=list(PRELOADED_AUTOMATA.keys()))
    automaton = PRELOADED_AUTOMATA[example_choice]
    st.session_state.automaton_display = automaton
else: # Manual Creator Mode
    st.sidebar.header("Create Your Own")
    creator_type = st.sidebar.selectbox("What do you want to create?", ("DFA", "NFA", "ε-NFA", "Regular Grammar"))

    if creator_type != "Regular Grammar":
        states_str = st.sidebar.text_input("States (comma-separated)", "q0,q1,q2")
        alphabet_str = st.sidebar.text_input("Alphabet (comma-separated, use 'e' for ε)", "a,b" if creator_type != "ε-NFA" else "a,b,e")
        states = {s.strip() for s in states_str.split(',') if s.strip()}
        alphabet = {s.strip() for s in alphabet_str.split(',') if s.strip()}
        start_state = st.sidebar.selectbox("Start State", options=sorted(list(states)))
        final_states = st.sidebar.multiselect("Final States", options=sorted(list(states)))
        trans_str = st.sidebar.text_area("Transitions (one per line: from,symbol,to)", "q0,a,q1\nq1,b,q2")
        
        if st.sidebar.button("Create Automaton"):
            try:
                transitions = {}
                for line in trans_str.splitlines():
                    from_s, sym, to_s = [p.strip() for p in line.split(',')]
                    sym = 'ε' if sym == 'e' else sym
                    key = (from_s, sym); transitions.setdefault(key, set()).add(to_s)
                
                # Validation
                if creator_type == "DFA":
                    for s in states:
                        for a in alphabet:
                            if (s, a) not in transitions or len(transitions.get((s, a), set())) != 1:
                                raise ValueError(f"DFA Error: State '{s}' must have exactly one transition for symbol '{a}'.")
                
                automaton = Automaton(states, alphabet, transitions, start_state, final_states, f"Manually Created {creator_type}")
                st.session_state.automaton_display = automaton
                st.sidebar.success("Automaton created!")
            except Exception as e:
                st.sidebar.error(f"Error: {e}")
    else: # Regular Grammar
        grammar_str = st.sidebar.text_area("Production Rules (one per line)", "S -> aA\nA -> bS\nS -> e")
        if st.sidebar.button("Create NFA from Grammar"):
            try:
                automaton = convert_grammar_to_nfa(grammar_str)
                st.session_state.automaton_display = automaton
                st.sidebar.success("NFA created from grammar!")
            except Exception as e:
                st.sidebar.error(f"Grammar Error: {e}")

# --- Main Display Area ---
if 'automaton_display' in st.session_state and st.session_state.automaton_display is not None:
    automaton = st.session_state.automaton_display
    st.header("1. Automaton Explorer")
    st.markdown(f"**Description:** {automaton.description}")
    st.graphviz_chart(draw_automaton(automaton))

    st.header("2. Conversion Hub")
    st.markdown("Select a conversion to perform on the automaton above.")
    
    is_dfa, has_epsilon = True, 'ε' in automaton.alphabet
    if not has_epsilon:
        for s in automaton.states:
            for a in automaton.alphabet:
                if len(automaton.transitions.get((s, a), set())) != 1: is_dfa = False; break
            if not is_dfa: break
    else: is_dfa = False

    col1, col2, col3 = st.columns(3)
    with col1:
        if has_epsilon and st.button("Convert ε-NFA to NFA"):
            result = convert_enfa_to_nfa(automaton); st.session_state.conversion_result = ("NFA from ε-NFA", result, [])
        if not is_dfa and st.button("Convert NFA/ε-NFA to DFA"):
            result, steps = convert_nfa_to_dfa(automaton); st.session_state.conversion_result = ("DFA from NFA/ε-NFA", result, steps)
    with col2:
        if is_dfa and st.button("Minimize DFA"):
            result = minimize_dfa(automaton); st.session_state.conversion_result = ("Minimized DFA", result, ["..."])
    with col3:
        if st.button("Convert FA to Regular Expression"):
            with st.spinner("..."):
                re_string = convert_fa_to_re(automaton); st.session_state.conversion_result = ("RE from FA", re_string, [f"`{re_string}`"])

    if 'conversion_result' in st.session_state:
        title, result, steps = st.session_state.conversion_result
        st.header("Conversion Result"); st.subheader(title)
        if isinstance(result, Automaton):
            st.graphviz_chart(draw_automaton(result))
            with st.expander("View Details"): st.json(result.to_dict())
        else: st.code(result, language='plaintext')
        if steps:
            with st.expander("View Steps"):
                for step in steps: st.text(step)
else:
    st.info("Select a mode and an example, or create a new automaton to begin.")
