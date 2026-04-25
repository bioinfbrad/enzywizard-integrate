from __future__ import annotations
from argparse import Namespace, ArgumentParser
from ..services.integrate_service import run_integrate_service

def add_integrate_parser(parser: ArgumentParser) -> None:
    parser.add_argument("-i", "--input_dir",required=True,help="Path to a directory containing JSON reports to integrate.")
    parser.add_argument("-o", "--output_dir",required=True,help="Directory to save integrated JSON outputs.")
    parser.add_argument("--strict", dest="strict", action="store_true",help="Enable strict mode requiring all 12 report types and all node fields (default: Disabled).")
    parser.set_defaults(strict=False)
    parser.set_defaults(func=run_integrate)

def run_integrate(args: Namespace) -> None:
    run_integrate_service(input_dir=args.input_dir, output_dir=args.output_dir, strict=args.strict)


# ==============================
# Command: enzywizard-integrate
# ==============================

# brief introduction:
'''
EnzyWizard-Integrate is a command-line tool for integrating multiple EnzyWizard
JSON reports and constructing a protein / protein-substrate graph representation.
It takes a directory containing EnzyWizard JSON reports as input and merges
information from supported report types into a structured graph dataset,
where nodes represent amino acids or substrates, and edges represent
relationships such as interactions.
The input directory must contain exactly one enzywizard_clean report, which is
used as the anchor for residue indexing and protein identity. Additional reports
provide complementary features. The tool integrates the graph data
, enabling direct downstream use in graph-based analysis, machine
learning models, and enzyme function studies.
'''

# example usage:
'''
Example command:

enzywizard-integrate -i examples/input/ -o examples/output/
'''

# input parameters:
'''
-i, --input_dir
Required.
Path to a directory containing JSON reports to integrate.

The directory must contain exactly one enzywizard_clean report.

Supported report types include:
- enzywizard_clean
- enzywizard_aaprops
- enzywizard_hydrocluster
- enzywizard_energy
- enzywizard_flexibility
- enzywizard_disorder
- enzywizard_conservation
- enzywizard_embedding
- enzywizard_pocket
- enzywizard_substrate
- enzywizard_dock
- enzywizard_interaction

Duplicate report types are not allowed.

-o, --output_dir
Required.
Directory to save integrated JSON outputs.

--strict
Optional.
Enable strict mode requiring all 12 report types and all node fields.

'''

# output content:
'''
The program outputs the following files into the output directory:

1. An integrated JSON report
   - integrate_report_{protein_name}.json

   The JSON report contains:

   - "output_type"
     A string identifying the report type:
     "enzywizard_integrate"

   - "integrated_graph"
     A list describing the integrated graph entries.

     Each entry is stored in one of the following formats:

     Node entry:
     - "node_1"
       A single integrated node record representing:
       - an amino acid (protein node)
       - or a substrate (ligand node)

     Edge entry:
     - "node_1"
       Information of the first node

     - "edge"
       Information of the relationship between nodes

     - "node_2"
       Information of the second node

   The integrated graph represents:
   - protein-only / protein-substrate residue interaction networks
   - structural and functional relationships merged into one graph

2. A node-only JSON file
   - integrate_nodes_{protein_name}.json

   Contains all node records extracted from the integrated graph.

3. An edge-only JSON file
   - integrate_edges_{protein_name}.json

   Contains all edge records extracted from the integrated graph.
'''

# Process:
'''
This command processes the input JSON reports as follows:

1. Validate input directory
   - Check that input_dir exists and is a valid directory.
   - Create output_dir if needed.

2. List JSON files
   - Search input_dir for JSON files.
   - Collect all candidate EnzyWizard report files.

3. Identify clean report
   - Locate exactly one enzywizard_clean report in input_dir.
   - Reject the input if no clean report or multiple clean reports are found.

4. Resolve protein name
   - Extract the protein name from the clean report filename.
   - Use this protein name for output file naming.

5. Validate report count
   - Ensure the total number of JSON files does not exceed the maximum number of supported report types.
   - In strict mode, require exactly 12 report types.

6. Load and validate reports
   - Read each JSON report.
   - Validate each report using output_type-specific schema checks.
   - Reject unsupported report types.
   - Reject duplicated report types.

7. Build report dictionary
   - Organize all validated reports into a report_dict keyed by output_type.
   - Use enzywizard_clean as the anchor report.

8. Integrate reports
   - Pass report_dict into the integration algorithm.
   - Merge residue-level, substrate-level, and interaction-level information
     into a unified graph representation.

9. Save integrated report
   - Write the full integrated graph as integrate_report_{protein_name}.json.

10. Split integrated graph
   - Parse integrated_graph entries into:
     - node list
     - edge list

11. Save node and edge outputs
   - Write node list into integrate_nodes_{protein_name}.json.
   - Write edge list into integrate_edges_{protein_name}.json.

12. Finish integration
   - Complete the integration workflow and finalize outputs.
'''

# dependencies:
'''
- Biopython
- NumPy
- JSON
'''

# references:
'''
- Biopython:
  https://biopython.org/

- JSON:
  https://www.json.org/
'''