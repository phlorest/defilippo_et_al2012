<a name="ds-genericmetadatajson"> </a>

# Generic Generic

**CLDF Metadata**: [Generic-metadata.json](./Generic-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | De Filippo, C., Bostoen, K., Stoneking, M., & Pakendorf, B. (2012). Bringing together linguistic and genetic evidence to test the Bantu expansion. Proceedings of the Royal Society B: Biological Sciences, 279(1741), 3256–3263. doi:10.1098/rspb.2012.0318
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:hasPart](http://purl.org/dc/terms/hasPart) | <dl><dt><a href="http://purl.org/dc/terms/relation">dc:relation</a></dt><dd>data.nex</dd><dt><a href="http://purl.org/dc/terms/description">dc:description</a></dt><dd>The data underlying the analysis which created the phylogeny</dd><dt><a href="http://purl.org/dc/terms/format">dc:format</a></dt><dd>https://en.wikipedia.org/wiki/Nexus_file</dd></dl>
[dc:identifier](http://purl.org/dc/terms/identifier) | https://dx.doi.org/10.1098/rspb.2012.0318
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/D-PLACE/dplace-tree-defilippo_et_al2012
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/D-PLACE/dplace-tree-defilippo_et_al2012/tree/lottolog-v4.2">D-PLACE/dplace-tree-defilippo_et_al2012 with-glottolog-v4.2</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.4">Glottolog v4.4</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | defilippo_et_al2012
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

The LanguageTable lists the taxa, i.e. the leafs of the phylogeny, mapped to languoids.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 412


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
`Guthrie` | `string` | 
`Hist-Groups` | `string` | 
`G-code` | `string` | 
`L-code` | `string` | 
`Language` | `string` | 
`missing` | `string` | 
`orig-Longitude` | `string` | 
`orig-Latitude` | `string` | 
`Glottolog_Name` | `string` | 

## <a name="table-treescsv"></a>Table [trees.csv](./trees.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 1001


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Nexus_File](http://purl.org/dc/terms/relation) | `string` | The newick representation of the tree, labeled with identifiers as described in LanguageTable, is stored in the TREES block of the Nexus file specified here. (See https://en.wikipedia.org/wiki/Nexus_file)
`rooted` | `boolean` | Whether the tree is rooted (true) or unrooted (false) (or no info is available (null))
`type` | `string` | Whether the tree is a summary (or consensus) tree, i.e. can be analysed in isolation, or whether it is a sample, resulting from a method that creates multiple trees
`method` | `string` | Specifies the method that was used to create the tree
`scaling` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

The ParameterTable lists characters (a.k.a. sites), i.e. the (often binary) variables used as data basis to compute the phylogeny from.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 2832


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Sequence index of the site in the corresponding Nexus file.<br>Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Nexus_File](http://purl.org/dc/terms/relation) | `string` | The data for this parameter is stored at 1-based index {ID} of the sequences in the DATA block of the Nexus file specified here. (See https://en.wikipedia.org/wiki/Nexus_file)

