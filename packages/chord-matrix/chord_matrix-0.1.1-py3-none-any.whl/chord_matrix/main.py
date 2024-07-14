import pandas as pd
import numpy as np
import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert the data files into co-occurence matrix required for chord diagrams", 
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # mandatory arguments
    parser.add_argument("--path", required=True, help="Path to the main data file in TSV format")
    parser.add_argument("--outputPath", required=True, help="Path to download the output matrix file.")

    return parser.parse_args()

def check_directories(target_dir, output_dir):
    if not target_dir.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)


def make_matrix(target_dir, output_dir):
    df = pd.read_csv(target_dir, sep='\t', low_memory=False)

    # Filter the data for specific status. It helps to filter data. You can remove this line per your requirement.
    df = df[df['status'] == 'RMG_53']
    
    # Select and drop duplicates based on UPN and SYMBOL columns. UPN = Unique Patient Number, SYMBOL = Gene symbol
    filtered_df = df[["UPN", "AF", "SYMBOL"]]
    filtered_df = filtered_df.drop_duplicates(subset=['UPN', 'SYMBOL'], keep='first')

    # Get the total number of unique patients
    total_patients = filtered_df['UPN'].unique().size

    # Create a pivot table with gene symbols as rows and patients as columns
    pivot_df = filtered_df.pivot(index='SYMBOL', columns='UPN', values='AF')
    pivot_df = (pivot_df > 0).astype(int)

    # Transpose the pivot table for matrix multiplication
    transpose_df = pivot_df.transpose()
    transpose_df = (transpose_df>0).astype(int)

    # Reverse the transposition
    reverse_transposed_df = transpose_df.transpose()

    # Calculate the co-occurrence matrix using dot product
    cooccurence_matrix = reverse_transposed_df.dot(transpose_df)

    # Calculate the count of patients with only one gene mutation
    single_gene_count = (transpose_df.sum(axis=1) == 1).astype(int)
    single_gene_df = transpose_df[single_gene_count == 1].sum(axis=0)

    # Uncomment this if you want the [genex,genex] to be for patients that ONLY had genex and no other gene.
    # Otherwise [genex, genex] will be the total number of patients gene x occured in. 

    # for gene in single_gene_df.index:
    #     cooccurence_matrix.loc[gene, gene] = single_gene_df[gene]

    # Getting the details of the data
    details_df = getDetails(cooccurence_matrix, total_patients)

     # Write the co-occurrence matrix and details to the output file with appropriate line separators
    with open(output_dir, 'w') as f:
        f.write('# Co-occurence matrix \n')
        cooccurence_matrix.to_csv(f, sep='\t', index=False, header=True)
        f.write('\n#Details \n')
        details_df.to_csv(f, sep='\t', index=False)


def getDetails(matrix, total_patients):
    details = []
    genes = matrix.index

    # Calculate statistics for each pair of genes
    for i in range(genes.size):
        for j in range(genes.size):
            if (i != j):
                totalA = matrix.iloc[i, i]
                totalB = matrix.iloc[j, j]
                totalAB = matrix.iloc[i, j]

                AnotB = totalA - totalAB
                BnotA = totalB - totalAB
                neither = total_patients - totalAB - AnotB - BnotA

                oddsRatio = 1
                if (AnotB * BnotA != 0):
                    oddsRatio = (neither * totalAB) / (AnotB * BnotA)
                
                oddsRatio = np.log2(oddsRatio)


                tendency = "Mutual exclusivity"
                if (oddsRatio > 0):
                    tendency = "Co-occurence"

                # Append details to the list
                details.append({
                    'geneA':  genes[i],
                    'geneB': genes[j],
                    'Both': totalAB, 
                    'A Not B': AnotB,
                    'B Not A': BnotA,
                    'Neither': neither,
                    'Log2 Odds Ratio': oddsRatio,
                    'Tendency': tendency
                })

    # Convert details list to DataFrame
    details_df = pd.DataFrame(details)
    return details_df

def main():
    # Parse command line arguments
    args = parse_arguments()
    target_dir = Path(args.path)
    output_dir = Path(args.outputPath)
    
    # Check if directories exist
    check_directories(target_dir, output_dir)

    # Create the co-occurrence matrix
    make_matrix(target_dir, output_dir)

if __name__ == "__main__":
    main()