import pathlib

from tqdm import tqdm
import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "defilippo_et_al2012"

    def add_custom_schema(self, args):
        args.writer.cldf.add_columns(
            'LanguageTable',
            'Guthrie',
            'Hist-Groups',
            'G-code',
            'L-code',
            'Language',
            'missing',
            'orig-Longitude',
            'orig-Latitude',
        )

    @staticmethod
    def language_factory(d, row):
        for k in [
            'Guthrie',
            'Hist-Groups',
            'G-code',
            'L-code',
            'Language',
            'missing',
            'orig-Longitude',
            'orig-Latitude',
        ]:
            d[k] = row[k.replace('orig-', '')]

    def cmd_makecldf(self, args):
        self.init(args, language_factory=self.language_factory)
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
