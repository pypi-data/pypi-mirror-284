import getopt, sys
from .nc_base import nc_base
from .dictarray import fetch_score_dict_flatfile
from . import __version__

class nc_standalone( nc_base):
    """Neighborhood Correlation calculation using pure Python from BLAST scores"""

    def __init__(self, nc_thresh, smin_factor,
                 flatfile_name, num_residues):
        nc_base.__init__( self)
        
        self.new_run( 0, None, nc_thresh, smin_factor,
                      0, num_residues)

        (self.score_dict, self.seq_id_map
         ) = fetch_score_dict_flatfile( flatfile_name)

        # provide information about the blast run. Used to calculate
        # SMIN. If not specified, use the average number of residues
        # from human and mouse
        self.blast_info['num_sequences'] = len(self.score_dict)
        if not 'num_residues' in self.blast_info:
            self.blast_info['num_residues'] = int(537.2148 * len(self.score_dict))
        self.blast_info['params'] = {'expectation': 10 * len(self.score_dict)}


def usage():
    s = f"""Neighborhood Correlation {__version__}.

    This implementation depends upon the Numpy numerical package, and
    uses a compiled C helper to for memory and calculation efficiency.

    If the helper module is not available and cannot be compiled, this
    implementation will still run, but use a slower python
    implementation of the helper.

    For details of Neighborhood Correlation please refer to
    http://www.neighborhoodcorrelation.org/ or the publication:

    Sequence Similarity Network Reveals Common Ancestry of Multidomain
    Proteins
    Song N, Joseph JM, Davis GB, Durand D
    PLoS Computational Biology 4(5): e1000063
    doi:10.1371/journal.pcbi.1000063

    (C) 2011 Jacob Joseph <jmjoseph@andrew.cmu.edu>
    and Carnegie Mellon University
    
    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 3
    of the License, or (at your option) any later version.

Usage:

    NC_standalone -f <flatfile> [options]

    Output of Neighborhood Correlation scores will be printed to
    stdout in the same three-column format as used for input.

Options:

     -f, --flatfile <filename>   (required)
          A white-space delimited file of BIT-scores from BLAST.  Three
          columns are expected, of the format:

          --------------------------------------
          seq_id_0   seq_id_1   bit_score
          seq_id_2   seq_id_3   bit_score
          ....
          --------------------------------------
          
          No column heading should be provided.  Please refer to
          http://www.ncbi.nlm.nih.gov/books/bv.fcgi?rid=handbook.section.614
          for an explanation of BIT-score.

     -o, --output <filename>
          Write score output to a file.  If omitted, the score list is
          printed to stdout.
     
     -h, --help
          Print this help message.

     --num_residues <integer>
          Number of residues in the sequence database.  Used to
          calculate SMIN, the lowest expected bit_score.  If
          unspecified, an estimate of 537 residues per sequence will
          be used, which is an average of mouse and human SwissProt
          sequences.

     --nc_thresh <float>
          NC reporting threshold.  Calculated values below this
          threshold will not be reported.  Conservatively defaults to
          0.05.

     --smin_factor <0.95>
          SMIN factor.  Calculate SMIN from the expected random
          BIT-score scaled by this factor. Defaults to 0.95.
          """
    return s


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:o:",
                                   ["help", "nc_thresh=", "smin_factor=",
                                    "flatfile=", "output=",
                                    "num_residues="])
        
    except getopt.GetoptError:
        # print help information and exit:
        print(usage())
        raise

    printhelp = False
    nc_thresh = 0.05
    smin_factor = 0.95
    flatfile_name = None
    output_name = None
    num_residues = None
    for o, a in opts:
        if o in ("-h", "--help"):
            printhelp=True
        if o == '--nc_thresh': nc_thresh = float(a)
        if o == '--smin_factor' : smin_factor = float(a)
        if o in ( '-f', '--flatfile'): flatfile_name = a
        if o in ( '-o', '--output'): output_name = a
        if o == "--num_residues": num_residues = int(a)
        
    if printhelp or flatfile_name is None:
        print(usage())
        sys.exit()

    ncrun = nc_standalone(nc_thresh, smin_factor,
                         flatfile_name, num_residues)

    if output_name is not None:
        fd_out = open(output_name, 'w')
    else:
        fd_out = sys.stdout

    ncrun.calculate_nc( ncrun.score_dict, fd_out = fd_out,
                        seq_id_map = ncrun.seq_id_map)

    if fd_out != sys.stdout: fd_out.close()


if __name__ == "__main__":
    main()





