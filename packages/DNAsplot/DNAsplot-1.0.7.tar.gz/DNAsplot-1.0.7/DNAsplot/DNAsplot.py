#!/usr/bin/env python
import os
import sys, getopt
import os.path
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

dir = os.path.dirname(os.path.abspath(__file__))
version_py = os.path.join(dir, "_version.py")
exec(open(version_py).read())

def DNAsplot(inputpath,input,outpath,outfile):
    os.chdir(inputpath)
    DNA = pd.read_csv(input,sep="\t",header=0,names=['label','seq'])
    # Define colors for each nucleotide
    nucleotide_colors = {'A': 'green','T': 'red','G': 'blue','C': 'orange'}
    original = DNA.iloc[0]['seq']
    #mutations = DNA.iloc[1:]['seq']
    fig, ax = plt.subplots(len(DNA), 1)
    for i,(index,row) in enumerate(DNA.iterrows()):
        # Plot the label
        label = row['label']
        seq = row['seq']
        ax[i].text(-0.05, 0.6, label, horizontalalignment='right',
            verticalalignment='center', fontsize=10, transform=ax[i].transAxes)
        # Plot the sequence
        for j, nucleotide in enumerate(seq):
            ax[i].text(j, 0.5, nucleotide, horizontalalignment='center', 
                verticalalignment='center', fontsize=10, family='monospace', 
                color=nucleotide_colors.get(nucleotide, 'black'))
            # Highlight the mutation if not the original sequence
            if i > 0 and nucleotide != original[j]:
                rect = Rectangle((j - 0.5, 0.25), 1, 0.6, fill=None, edgecolor='red', linewidth=1)
                ax[i].add_patch(rect)
        # Set the y-axis limits and remove ticks
        ax[i].set_xlim(-1, len(seq))
        ax[i].set_ylim(0, 1)
        ax[i].axis('off')
    plt.subplots_adjust(left=0.3, right=0.6, top=0.3, bottom=0.1)
    plt.savefig(outpath+'/'+outfile+'.pdf')
    del DNA

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--inputpath', dest='inputpath',
                        required=True,
                        help='path of input file')
    parser.add_argument('-f', '--filename', dest='filename',
                        required=True,
                        help='name of input file')
    parser.add_argument('-O', '--outpath', dest='outpath',
                        required=True,
                        help='path of output file')
    parser.add_argument('-o', '--outfile', dest='outfile',
                        required=True,
                        help='name of output file')
    parser.add_argument("-V", "--version", action="version",version="DNAsplot {}".format(__version__)\
                      ,help="Print version and exit")
    args = parser.parse_args()
    print('###Parameters:')
    print(args)
    print('###Parameters')
    DNAsplot(args.inputpath,args.filename,args.outpath,args.outfile)

if __name__ == '__main__':
    main()


