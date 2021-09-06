# Total number of distinct label to keyword mappings

## Before filtering
|    | type   |   size(collect_set(struct(label, keywordId))) |
|---:|:-------|----------------------------------------------:|
|  0 | DS     |                                        147497 |
|  1 | GP     |                                        546131 |
|  2 | CD     |                                         55922 |

## After filtering
|    | type   |   size(collect_set(struct(label, keywordId))) |
|---:|:-------|----------------------------------------------:|
|  0 | DS     |                                        137718 |
|  1 | GP     |                                        456926 |
|  2 | CD     |                                         51687 |



# p55 mapping counts by keyword and distinct PMID

## Before filtering
Total number of distinct PMIDs containing at least one p55 mapping: **2916.**

|    | keywordId       |   size(collect_set(pmid)) |
|---:|:----------------|--------------------------:|
|  0 | ENSG00000226881 |                      2916 |
|  1 | ENSG00000185624 |                      2916 |
|  2 | ENSG00000157554 |                      2916 |
|  3 | ENSG00000256525 |                      2916 |
|  4 | ENSG00000117461 |                      2916 |
|  5 | ENSG00000134460 |                      2916 |
|  6 | ENSG00000197170 |                      2916 |
|  7 | ENSG00000130830 |                      2916 |
|  8 | ENSG00000075618 |                      2916 |
|  9 | ENSG00000067182 |                      2916 |

## After filtering
Total number of distinct PMIDs containing at least one p55 mapping: **699.**

|    | keywordId       |   size(collect_set(pmid)) |
|---:|:----------------|--------------------------:|
|  0 | ENSG00000185624 |                        11 |
|  1 | ENSG00000157554 |                         8 |
|  2 | ENSG00000256525 |                        13 |
|  3 | ENSG00000117461 |                        29 |
|  4 | ENSG00000134460 |                        26 |
|  5 | ENSG00000197170 |                         8 |
|  6 | ENSG00000130830 |                        26 |
|  7 | ENSG00000075618 |                        16 |
|  8 | ENSG00000067182 |                       572 |



# Global list of APP gene synonyms (ENSG00000142192)

## Before filtering
|     | label                                             |
|----:|:--------------------------------------------------|
|   0 | Amyloid-beta protein precursor                    |
|   1 | Beta-amyloid precursor proteins                   |
|   2 | Protease nexin II                                 |
|   3 | protein amyloid precursor protein                 |
|   4 | amyloid-precursor protein                         |
|   5 | Amyloid Precursor Protein*                        |
|   6 | amyloid-beta protein precursor-amyloid-beta       |
|   7 | beta-protein amyloid A4                           |
|   8 | sAPP-alpha                                        |
|   9 | amyloid-beta-precursor protein                    |
|  10 | peptidase Nexin-II                                |
|  11 | APPIs                                             |
|  12 | PN II                                             |
|  13 | beta -amyloid precursor protein                   |
|  14 | amyloid-( precursor protein                       |
|  15 | amyloid-beta A4 protein                           |
|  16 | amyloid beta-precursor protein                    |
|  17 | Vaps C                                            |
|  18 | Amyloid Protein Precursor                         |
|  19 | Alzheimer disease amyloid protein                 |
|  20 | APP                                               |
|  21 | beta-amyloid-precursor proteins                   |
|  22 | amyloid ß precursor protein                       |
|  23 | amyloid-βeta precursor protein                    |
|  24 | Amyloid precursor protein α                       |
|  25 | AßPP                                              |
|  26 | APPI                                              |
|  27 | (PPI) A                                           |
|  28 | Aβpp                                              |
|  29 | appE                                              |
|  30 | Amyloid precursor proteins                        |
|  31 | APPs-I                                            |
|  32 | beta-amyloid-precursor-protein                    |
|  33 | Amyloid-Beta Precursor Protein                    |
|  34 | Amyloid-ß Precursor Protein                       |
|  35 | PreA4                                             |
|  36 | alpha-sAPP                                        |
|  37 | s amyloid precursor protein                       |
|  38 | ad1                                               |
|  39 | (APP)I                                            |
|  40 | σA4                                               |
|  41 | Precursor of amyloid protein                      |
|  42 | beta-amyloid-precursor protein                    |
|  43 | The amyloid precursor protein                     |
|  44 | α4s                                               |
|  45 | amyloid precursor protein a                       |
|  46 | α4,                                               |
|  47 | AβPP                                              |
|  48 | amyloid protein precursor                         |
|  49 | -A4                                               |
|  50 | Amyloid-beta precursor protein                    |
|  51 | α-AβPP                                            |
|  52 | ABPPs                                             |
|  53 | Pn II                                             |
|  54 | AppI                                              |
|  55 | APPe                                              |
|  56 | APPS                                              |
|  57 | α-4                                               |
|  58 | amyloidal precursor protein                       |
|  59 | a4                                                |
|  60 | Beta Amyloid Precursor Protein                    |
|  61 | AMYLOID PRECURSOR PROTEIN                         |
|  62 | [beta]-amyloid precursor protein                  |
|  63 | Amyloidal Precursor Protein                       |
|  64 | amyloid Precursor Protein                         |
|  65 | Beta (A4)-amyloid protein                         |
|  66 | beta-Amyloid protein (beta A4                     |
|  67 | APP) I                                            |
|  68 | AD.1                                              |
|  69 | Amyloid-Precursor Protein                         |
|  70 | )-amyloid precursor protein                       |
|  71 | APp                                               |
|  72 | Amyloidal precursor protein                       |
|  73 | amyloid precursor proteins α                      |
|  74 | Where amyloid beta protein precursor-amyloid beta |
|  75 | Ã4                                                   |
|  76 | amyloid-beta protein precursor                    |
|  77 | cVAP                                              |
|  78 | protein precursor of amyloid                      |
|  79 | beta-amyloid and amyloid precursor protein        |
|  80 | beta-Amyloid Precursor Protein                    |
|  81 | APP-I                                             |
|  82 | amyloid protein (beta A4                          |
|  83 | Vap C                                             |
|  84 | protease nexin-II                                 |
|  85 | Amyloid Precursor-Protein                         |
|  86 | Amyloid precursor proteinE                        |
|  87 | aPP                                               |
|  88 | APPS-I                                            |
|  89 | A4e                                               |
|  90 | amyloidbeta precursor protein                     |
|  91 | amyloid beta protein precursor                    |
|  92 | APP- I                                            |
|  93 | α4                                                |
|  94 | α-amyloid precursor protein                       |
|  95 | amyloid precursors protein                        |
|  96 | Protease Nexin II                                 |
|  97 | BPP-A                                             |
|  98 | AP-P                                              |
|  99 | aD1                                               |
| 100 | beta-amyloid protein precursor                    |
| 101 | α(4                                               |
| 102 | amyloid-beta precursor protein                    |
| 103 | ApP                                               |
| 104 | beta-amyloid precursor proteins                   |
| 105 | aPPs                                              |
| 106 | Amyloid precursor Protein                         |
| 107 | ad-1                                              |
| 108 | amyloid precursor-protein                         |
| 109 | amyloid beta protein A4                           |
| 110 | (APP) I                                           |
| 111 | s Amyloid Precursor Protein                       |
| 112 | beta A4 amyloid protein                           |
| 113 | VAP-C                                             |
| 114 | app                                               |
| 115 | AβPPs                                             |
| 116 | AppY                                              |
| 117 | PPI-A                                             |
| 118 | AD-1                                              |
| 119 | P05067                                            |
| 120 | amyloid-precursor-protein                         |
| 121 | amyloid protein precursor α                       |
| 122 | appe                                              |
| 123 | amyloid beta precursor proteins                   |
| 124 | Amyloid-beta A4 Protein                           |
| 125 | Amyloid-beta Protein Precursor                    |
| 126 | Alzheimer's disease amyloid ß-protein             |
| 127 | AbPP                                              |
| 128 | Amyloid beta Precursor Protein                    |
| 129 | protease nexin II                                 |
| 130 | Beta A4-amyloid protein                           |
| 131 | beta-A4 amyloid protein                           |
| 132 | amyloid precursor protein α                       |
| 133 | Amyloid beta precursor protein                    |
| 134 | Cvap                                              |
| 135 | IPN I                                             |
| 136 | APPy                                              |
| 137 | A4                                                |
| 138 | APP I                                             |
| 139 | Amyloid precursorprotein                          |
| 140 | s-amyloid precursor protein                       |
| 141 | apP                                               |
| 142 | Ap-P                                              |
| 143 | -in amyloid precursor protein                     |
| 144 | preA4                                             |
| 145 | Amyloid Precursor Protein α                       |
| 146 | App I                                             |
| 147 | App                                               |
| 148 | beta-amyloid precursor-protein                    |
| 149 | Amyloid protein precursor                         |
| 150 | PS-Ap                                             |
| 151 | appI                                              |
| 152 | PN-II                                             |
| 153 | Amyloid beta A4 protein                           |
| 154 | s-APP                                             |
| 155 | Beta A4 amyloid protein                           |
| 156 | ̃-amyloid precursor protein                                                   |
| 157 | precursor amyloid protein                         |
| 158 | amyloid precursor protein beta                    |
| 159 | beta-Amyloid precursor protein                    |
| 160 | Amyloid-beta Precursor Protein                    |
| 161 | beta amyloid protein A4                           |
| 162 | APPE                                              |
| 163 | beta amyloid protein precursor                    |
| 164 | amyloid beta-protein precursor                    |
| 165 | APP-                                              |
| 166 | Amyloid Beta Precursor Protein                    |
| 167 | CVAPs                                             |
| 168 | Amyloid Precursor protein                         |
| 169 | amyloid beta protein precursor protein            |
| 170 | amyloid beta A4 protein                           |
| 171 | α-APP                                             |
| 172 | The amyloid beta-precursor protein                |
| 173 | Amyloid Precursor Proteins                        |
| 174 | ApPS                                              |
| 175 | amyloid precursorprotein                          |
| 176 | Beta-amyloid precursor protein                    |
| 177 | APP)                                              |
| 178 | Beta amyloid precursor protein                    |
| 179 | Amyloid beta-protein precursor                    |
| 180 | APPs                                              |
| 181 | Protease nexin-II                                 |
| 182 | amyloid precursor proteins                        |
| 183 | α4-                                               |
| 184 | beta-amyloid precursor protein                    |
| 185 | sAPP alpha                                        |
| 186 | amyloid pre-cursor protein                        |
| 187 | beta/A4 amyloid protein                           |
| 188 | APPY                                              |
| 189 | A-4                                               |
| 190 | Alzheimer's disease amyloid protein               |
| 191 | APP α                                             |
| 192 | α4-α4                                             |
| 193 | Amyloid-beta A4 protein                           |
| 194 | APP-S                                             |
| 195 | beta amyloid A4 protein                           |
| 196 | beta amyloid precursor protein                    |
| 197 | AP PS                                             |
| 198 | Beta-amyloid Precursor Protein                    |
| 199 | protein precursor amyloid                         |
| 200 | amyloid beta a4 protein                           |
| 201 | PPI) A                                            |
| 202 | pp-A                                              |
| 203 | APP-α                                             |
| 204 | Amyloid-precursor protein                         |
| 205 | amyloid beta protein, beta A4                     |
| 206 | amyloid precursor protein-α                       |
| 207 | Ad1                                               |
| 208 | ?-amyloid precursor protein                       |
| 209 | beta-Amyloid protein precursor                    |
| 210 | APPs-α                                            |
| 211 | ABPP                                              |
| 212 | ApPI                                              |
| 213 | APPys                                             |
| 214 | Beta amyloid precursor proteins                   |
| 215 | CVAP                                              |
| 216 | beta A4-amyloid protein                           |
| 217 | Amyloid precursor protein                         |
| 218 | amyloid beta/A4 protein                           |
| 219 | Amyloid-Precursor-Protein                         |
| 220 | -APP                                              |
| 221 | beta protein amyloid A4                           |
| 222 | amy-loid precursor protein                        |
| 223 | amyloid precursor protein                         |
| 224 | Amyloid precursor protein beta                    |
| 225 | peptidase nexin-II                                |
| 226 | appY                                              |
| 227 | protein amyloid-beta precursor protein            |
| 228 | amyloid beta precursor protein                    |
| 229 | " amyloid precursor protein                       |
| 230 | -amyloid precursor protein                        |
| 231 | Amyloid Precursor Protein                         |
| 232 | amyloid- precursor protein                        |
| 233 | AD1                                               |
| 234 | APPÉ                                                   |
| 235 | Beta-Amyloid Precursor Protein                    |
| 236 | ß-amyloid precursor protein                       |
| 237 | Alzheimer disease amyloid proteins                |

## After filtering
|     | label                                             |
|----:|:--------------------------------------------------|
|   0 | Amyloid-beta protein precursor                    |
|   1 | Protease nexin II                                 |
|   2 | Beta-amyloid precursor proteins                   |
|   3 | protein amyloid precursor protein                 |
|   4 | amyloid-precursor protein                         |
|   5 | Amyloid Precursor Protein*                        |
|   6 | beta-protein amyloid A4                           |
|   7 | amyloid-beta protein precursor-amyloid-beta       |
|   8 | amyloid-beta-precursor protein                    |
|   9 | sAPP-alpha                                        |
|  10 | APPIs                                             |
|  11 | peptidase Nexin-II                                |
|  12 | PN II                                             |
|  13 | beta -amyloid precursor protein                   |
|  14 | amyloid-( precursor protein                       |
|  15 | amyloid beta-precursor protein                    |
|  16 | amyloid-beta A4 protein                           |
|  17 | Vaps C                                            |
|  18 | Amyloid Protein Precursor                         |
|  19 | Alzheimer disease amyloid protein                 |
|  20 | APP                                               |
|  21 | amyloid ß precursor protein                       |
|  22 | beta-amyloid-precursor proteins                   |
|  23 | amyloid-βeta precursor protein                    |
|  24 | Amyloid precursor protein α                       |
|  25 | AßPP                                              |
|  26 | APPI                                              |
|  27 | Aβpp                                              |
|  28 | appE                                              |
|  29 | Amyloid precursor proteins                        |
|  30 | APPs-I                                            |
|  31 | beta-amyloid-precursor-protein                    |
|  32 | Amyloid-Beta Precursor Protein                    |
|  33 | Amyloid-ß Precursor Protein                       |
|  34 | PreA4                                             |
|  35 | alpha-sAPP                                        |
|  36 | s amyloid precursor protein                       |
|  37 | ad1                                               |
|  38 | Precursor of amyloid protein                      |
|  39 | (APP)I                                            |
|  40 | beta-amyloid-precursor protein                    |
|  41 | The amyloid precursor protein                     |
|  42 | amyloid precursor protein a                       |
|  43 | AβPP                                              |
|  44 | amyloid protein precursor                         |
|  45 | α-AβPP                                            |
|  46 | Amyloid-beta precursor protein                    |
|  47 | ABPPs                                             |
|  48 | Pn II                                             |
|  49 | AppI                                              |
|  50 | APPe                                              |
|  51 | APPS                                              |
|  52 | amyloidal precursor protein                       |
|  53 | Beta Amyloid Precursor Protein                    |
|  54 | AMYLOID PRECURSOR PROTEIN                         |
|  55 | [beta]-amyloid precursor protein                  |
|  56 | amyloid Precursor Protein                         |
|  57 | beta-Amyloid protein (beta A4                     |
|  58 | Amyloidal Precursor Protein                       |
|  59 | Beta (A4)-amyloid protein                         |
|  60 | APP) I                                            |
|  61 | AD.1                                              |
|  62 | Amyloid-Precursor Protein                         |
|  63 | )-amyloid precursor protein                       |
|  64 | APp                                               |
|  65 | Amyloidal precursor protein                       |
|  66 | amyloid precursor proteins α                      |
|  67 | Where amyloid beta protein precursor-amyloid beta |
|  68 | amyloid-beta protein precursor                    |
|  69 | cVAP                                              |
|  70 | protein precursor of amyloid                      |
|  71 | beta-amyloid and amyloid precursor protein        |
|  72 | beta-Amyloid Precursor Protein                    |
|  73 | APP-I                                             |
|  74 | amyloid protein (beta A4                          |
|  75 | protease nexin-II                                 |
|  76 | Amyloid Precursor-Protein                         |
|  77 | aPP                                               |
|  78 | Amyloid precursor proteinE                        |
|  79 | APPS-I                                            |
|  80 | amyloid beta protein precursor                    |
|  81 | amyloidbeta precursor protein                     |
|  82 | α-amyloid precursor protein                       |
|  83 | APP- I                                            |
|  84 | α4                                                |
|  85 | amyloid precursors protein                        |
|  86 | Protease Nexin II                                 |
|  87 | BPP-A                                             |
|  88 | beta-amyloid protein precursor                    |
|  89 | aD1                                               |
|  90 | AP-P                                              |
|  91 | amyloid-beta precursor protein                    |
|  92 | ApP                                               |
|  93 | beta-amyloid precursor proteins                   |
|  94 | aPPs                                              |
|  95 | Amyloid precursor Protein                         |
|  96 | ad-1                                              |
|  97 | amyloid precursor-protein                         |
|  98 | amyloid beta protein A4                           |
|  99 | (APP) I                                           |
| 100 | beta A4 amyloid protein                           |
| 101 | s Amyloid Precursor Protein                       |
| 102 | VAP-C                                             |
| 103 | app                                               |
| 104 | AβPPs                                             |
| 105 | AppY                                              |
| 106 | AD-1                                              |
| 107 | P05067                                            |
| 108 | amyloid protein precursor α                       |
| 109 | appe                                              |
| 110 | amyloid-precursor-protein                         |
| 111 | Amyloid-beta Protein Precursor                    |
| 112 | Amyloid-beta A4 Protein                           |
| 113 | amyloid beta precursor proteins                   |
| 114 | Alzheimer's disease amyloid ß-protein             |
| 115 | AbPP                                              |
| 116 | Amyloid beta Precursor Protein                    |
| 117 | protease nexin II                                 |
| 118 | Beta A4-amyloid protein                           |
| 119 | beta-A4 amyloid protein                           |
| 120 | amyloid precursor protein α                       |
| 121 | Amyloid beta precursor protein                    |
| 122 | Cvap                                              |
| 123 | APPy                                              |
| 124 | IPN I                                             |
| 125 | APP I                                             |
| 126 | A4                                                |
| 127 | Amyloid precursorprotein                          |
| 128 | s-amyloid precursor protein                       |
| 129 | Ap-P                                              |
| 130 | apP                                               |
| 131 | -in amyloid precursor protein                     |
| 132 | preA4                                             |
| 133 | Amyloid Precursor Protein α                       |
| 134 | App I                                             |
| 135 | App                                               |
| 136 | beta-amyloid precursor-protein                    |
| 137 | Amyloid protein precursor                         |
| 138 | PN-II                                             |
| 139 | appI                                              |
| 140 | Amyloid beta A4 protein                           |
| 141 | s-APP                                             |
| 142 | Beta A4 amyloid protein                           |
| 143 | ̃-amyloid precursor protein                                                   |
| 144 | precursor amyloid protein                         |
| 145 | beta-Amyloid precursor protein                    |
| 146 | amyloid precursor protein beta                    |
| 147 | beta amyloid protein A4                           |
| 148 | Amyloid-beta Precursor Protein                    |
| 149 | APPE                                              |
| 150 | beta amyloid protein precursor                    |
| 151 | amyloid beta-protein precursor                    |
| 152 | APP-                                              |
| 153 | Amyloid Beta Precursor Protein                    |
| 154 | CVAPs                                             |
| 155 | Amyloid Precursor protein                         |
| 156 | amyloid beta protein precursor protein            |
| 157 | amyloid beta A4 protein                           |
| 158 | α-APP                                             |
| 159 | The amyloid beta-precursor protein                |
| 160 | Amyloid Precursor Proteins                        |
| 161 | ApPS                                              |
| 162 | amyloid precursorprotein                          |
| 163 | Beta-amyloid precursor protein                    |
| 164 | Beta amyloid precursor protein                    |
| 165 | Amyloid beta-protein precursor                    |
| 166 | APP)                                              |
| 167 | APPs                                              |
| 168 | Protease nexin-II                                 |
| 169 | amyloid precursor proteins                        |
| 170 | beta-amyloid precursor protein                    |
| 171 | sAPP alpha                                        |
| 172 | beta/A4 amyloid protein                           |
| 173 | amyloid pre-cursor protein                        |
| 174 | APPY                                              |
| 175 | Alzheimer's disease amyloid protein               |
| 176 | APP α                                             |
| 177 | APP-S                                             |
| 178 | Amyloid-beta A4 protein                           |
| 179 | beta amyloid A4 protein                           |
| 180 | beta amyloid precursor protein                    |
| 181 | AP PS                                             |
| 182 | Beta-amyloid Precursor Protein                    |
| 183 | protein precursor amyloid                         |
| 184 | amyloid beta a4 protein                           |
| 185 | pp-A                                              |
| 186 | APP-α                                             |
| 187 | Amyloid-precursor protein                         |
| 188 | amyloid beta protein, beta A4                     |
| 189 | amyloid precursor protein-α                       |
| 190 | Ad1                                               |
| 191 | ?-amyloid precursor protein                       |
| 192 | beta-Amyloid protein precursor                    |
| 193 | APPs-α                                            |
| 194 | ABPP                                              |
| 195 | APPys                                             |
| 196 | ApPI                                              |
| 197 | Beta amyloid precursor proteins                   |
| 198 | CVAP                                              |
| 199 | beta A4-amyloid protein                           |
| 200 | Amyloid precursor protein                         |
| 201 | amyloid beta/A4 protein                           |
| 202 | -APP                                              |
| 203 | Amyloid-Precursor-Protein                         |
| 204 | beta protein amyloid A4                           |
| 205 | amy-loid precursor protein                        |
| 206 | amyloid precursor protein                         |
| 207 | Amyloid precursor protein beta                    |
| 208 | peptidase nexin-II                                |
| 209 | appY                                              |
| 210 | protein amyloid-beta precursor protein            |
| 211 | amyloid beta precursor protein                    |
| 212 | " amyloid precursor protein                       |
| 213 | -amyloid precursor protein                        |
| 214 | Amyloid Precursor Protein                         |
| 215 | amyloid- precursor protein                        |
| 216 | AD1                                               |
| 217 | APPÉ                                                   |
| 218 | Beta-Amyloid Precursor Protein                    |
| 219 | ß-amyloid precursor protein                       |
| 220 | Alzheimer disease amyloid proteins                |
