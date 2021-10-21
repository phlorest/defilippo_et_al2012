import pathlib

from tqdm import tqdm
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "defilippo_et_al2012"

    def cmd_makecldf(self, args):
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'bantu_lexico_bin_M1P_cov2_burn40_all.mcct.trees',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.read_gzipped_text(self.raw_dir / 'bantu_lexico_bin_M1P_cov2_burn40_all.trees.gz'),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in tqdm(enumerate(posterior.trees.trees, start=1), total=1000):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'deFelippo_et_al-Bantu.nex')
