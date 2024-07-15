import argparse
import pandas as pd
import graphviz
from dfa_gen.dfa_class import Codon, DFA, NodeType
from dfa_gen.dfa_util import utr_to_aa, convert_aa_to_triple
from dfa_gen.generate_lattice import prepare_codon_unit_lattice
from dfa_gen.dfa_to_graph import read_dfa_contents, node_map_to_tsv, generate_graphviz_code

def get_dfa(aa_graphs, aa_seq):
    dfa = DFA()
    newnode = NodeType(3 * len(aa_seq), 0)

    dfa.add_node(newnode)

    for i, aa in enumerate(aa_seq):
        i3 = i * 3
        graph = aa_graphs[aa]

        for pos in range(3):
            for node in graph.nodes[pos]:
                num = node.num
                newnode = NodeType(i3 + pos, num)
                
                dfa.add_node(newnode)
                for edge in graph.right_edges[node]:
                    n2 = edge.node
                    nuc = edge.nuc
                    num = n2.num
                    newn2 = NodeType(i3 + pos + 1, num)
                    dfa.add_edge(newnode, newn2, nuc, edge.weight * 100)
    
    return dfa

def dfa_generator(seq, utr="", lambda_val=0):
    SEQ = seq
    UTR = utr
    LAMBDA_VAL = lambda_val
    DFA_FILE = f"test/dfa_{SEQ}"

    CODON_TABLE = "dfa_gen/data/codon_freq_table.tsv"
    CODING_WHEEL = "dfa_gen/data/coding_wheel.txt"

    codon_table = pd.read_csv(CODON_TABLE, sep='\t')
    utr_trimmed = UTR[:len(UTR) - (len(UTR) % 3)]
    utr_aa = utr_to_aa(utr_trimmed, codon_table)
    

    if UTR != "" and SEQ[-1] != '*':
        SEQ = SEQ + '*'
    aa_seq = SEQ + utr_aa

    codon = Codon(CODON_TABLE)
    aa_graphs_with_ln_weights = prepare_codon_unit_lattice(CODING_WHEEL, codon, lambda_=LAMBDA_VAL)
    
    aa_tri_seq = convert_aa_to_triple(aa_seq)
    protein = aa_tri_seq.split()
    dfa = get_dfa(aa_graphs_with_ln_weights, protein)

    with open(DFA_FILE, 'w') as f:
        f.write(f"# {SEQ}\n")
        f.write(f"# {UTR}\n")
        f.write(f"# {aa_seq}\n")
        dfa.print(f)
        
    with open(DFA_FILE, 'r') as file:
        SEQ = file.readline().strip()[2:]
        UTR = file.readline().strip()[2:]
        dfa_input_seq = file.readline().strip()[2:]
        dfa_contents = file.read()

    node_map = read_dfa_contents(dfa_contents)
    node_map_to_tsv(dfa_input_seq, utr_trimmed, node_map, f"{DFA_FILE}.tsv")

    df = pd.read_csv(f"{DFA_FILE}.tsv", sep='\t')
    graphviz_code = generate_graphviz_code(df)
    dot = graphviz.Source(graphviz_code)
    dot.render(f'{DFA_FILE}_graph', format='png')

def main():
    parser = argparse.ArgumentParser(description="Generate DFA from sequence")
    parser.add_argument("seq", type=str, help="The amino acid sequence")
    parser.add_argument("-u", "--utr", type=str, default="", help="The 3'UTR sequence")
    parser.add_argument("-l", "--lambda_val", type=float, default=0, help="The lambda value for calculating edge weight")

    args = parser.parse_args()
    dfa_generator(args.seq, args.utr, args.lambda_val)

if __name__ == "__main__":
    main()