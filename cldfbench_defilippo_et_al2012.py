import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "defilippo_et_al2012"

    def cmd_makecldf(self, args):
        self.init(args)
        
        # Add summary tree (e.g. MCCT or Consensus)
        summary = self.raw_dir.read_tree(
            'bantu_lexico_bin_M1P_cov2_burn40_all.mcct.trees', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)

        # Add posterior tree distribution
        posterior = self.raw_dir.read_trees(
            'bantu_lexico_bin_M1P_cov2_burn40_all.trees.gz',
            burnin=4001, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        # Add nexus data
        data = self.raw_dir.read_nexus('deFelippo_et_al-Bantu.nex')
        args.writer.add_data(data, self.characters, args.log)
