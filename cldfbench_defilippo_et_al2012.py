import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "defilippo_et_al2012"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'bantu_lexico_bin_M1P_cov2_burn40_all.mcct.trees',
                detranslate=True),
            self.metadata,
            args.log)
        posterior = self.sample(
            self.raw_dir.read('bantu_lexico_bin_M1P_cov2_burn40_all.trees.gz'),
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log,
            verbose=True)
        args.writer.add_data(
            self.raw_dir.read_nexus('deFelippo_et_al-Bantu.nex'),
            self.characters,
            args.log)
