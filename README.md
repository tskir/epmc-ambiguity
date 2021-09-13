# Total number of distinct label to keyword mappings

## Before filtering
|    | type   |   size(collect_set(struct(label, keywordId))) |
|---:|:-------|----------------------------------------------:|
|  0 | DS     |                                        158015 |
|  1 | GP     |                                        650358 |
|  2 | CD     |                                         60022 |

## After filtering
|    | type   |   size(collect_set(struct(label, keywordId))) |
|---:|:-------|----------------------------------------------:|
|  0 | GP     |                                        564846 |



# p55 mapping counts

## Before filtering
Total number of distinct PMIDs containing at least one p55 mapping: **3555.**

|    | keywordId       |   size(collect_set(pmid)) |
|---:|:----------------|--------------------------:|
|  0 | ENSG00000226881 |                      3555 |
|  1 | ENSG00000157554 |                      3555 |
|  2 | ENSG00000117461 |                      3555 |
|  3 | ENSG00000197170 |                      3555 |
|  4 | ENSG00000075618 |                      3555 |

## After filtering
Total number of distinct PMIDs containing at least one p55 mapping: **71.**

|    | keywordId       |   size(collect_set(pmid)) |
|---:|:----------------|--------------------------:|
|  0 | ENSG00000157554 |                         9 |
|  1 | ENSG00000117461 |                        39 |
|  2 | ENSG00000197170 |                         8 |
|  3 | ENSG00000075618 |                        19 |



# Global list of APP gene synonyms (ENSG00000142192)

## Before filtering
|     | label                                             |
|----:|:--------------------------------------------------|
|   0 | beta amyloid-peptide                              |
|   1 | Amyloid-beta protein precursor                    |
|   2 | Beta-amyloid precursor proteins                   |
|   3 | amyloid beta-Protein Precursor                    |
|   4 | Protease nexin II                                 |
|   5 | amyloid beta/A4 precursor protein                 |
|   6 | AAAs                                              |
|   7 | protein amyloid precursor protein                 |
|   8 | amyloid precursor's protein                       |
|   9 | amyloid-precursor protein                         |
|  10 | AAA+:                                             |
|  11 | Amyloid Precursor Protein*                        |
|  12 | beta-protein amyloid A4                           |
|  13 | amyloid-beta protein precursor-amyloid-beta       |
|  14 | sAPP-alpha                                        |
|  15 | amyloid-beta-precursor protein                    |
|  16 | peptidase Nexin-II                                |
|  17 | APPIs                                             |
|  18 | Amyloid beta-Peptides                             |
|  19 | AAAS                                              |
|  20 | PN II                                             |
|  21 | beta -amyloid precursor protein                   |
|  22 | peptide amyloid-beta                              |
|  23 | amyloid-( precursor protein                       |
|  24 | amyloid-beta A4 protein                           |
|  25 | amyloid beta-precursor protein                    |
|  26 | Vaps C                                            |
|  27 | beta-amyloid-peptide                              |
|  28 | Amyloid Protein Precursor                         |
|  29 | Pn-2                                              |
|  30 | Alzheimer disease amyloid protein                 |
|  31 | Amyloid-Beta Peptide                              |
|  32 | Amyloid beta peptides                             |
|  33 | APP                                               |
|  34 | Pn2s                                              |
|  35 | beta-amyloid-precursor proteins                   |
|  36 | amyloid ß precursor protein                       |
|  37 | amyloid-βeta precursor protein                    |
|  38 | Amyloid precursor protein α                       |
|  39 | AßPP                                              |
|  40 | APPI                                              |
|  41 | (PPI) A                                           |
|  42 | Aβpp                                              |
|  43 | appE                                              |
|  44 | Amyloid precursor proteins                        |
|  45 | beta-amyloid-precursor-protein                    |
|  46 | AAA-                                              |
|  47 | P340                                              |
|  48 | APPs-I                                            |
|  49 | PP-A                                              |
|  50 | beta/A4 amyloid precursor protein                 |
|  51 | amyloide beta (A4) precursor protein              |
|  52 | Amyloid-Beta Precursor Protein                    |
|  53 | Amyloid-ß Precursor Protein                       |
|  54 | PreA4                                             |
|  55 | AaA                                               |
|  56 | alpha-sAPP                                        |
|  57 | ααα                                               |
|  58 | and amyloid protein precursor                     |
|  59 | ETA-Ab                                            |
|  60 | s amyloid precursor protein                       |
|  61 | ad1                                               |
|  62 | (APP)I                                            |
|  63 | Precursor of amyloid protein                      |
|  64 | Aaa                                               |
|  65 | beta-amyloid-precursor protein                    |
|  66 | The amyloid precursor protein                     |
|  67 | Amyloid-beta peptide                              |
|  68 | Amyloid-beta peptides                             |
|  69 | amyloid precursor protein a                       |
|  70 | Amyloid Beta Peptide                              |
|  71 | AβPP                                              |
|  72 | p342                                              |
|  73 | amyloid protein precursor                         |
|  74 | Amyloid-beta precursor protein                    |
|  75 | α-AβPP                                            |
|  76 | ABPPs                                             |
|  77 | beta-amyloide peptide                             |
|  78 | aaa                                               |
|  79 | Pn II                                             |
|  80 | AppI                                              |
|  81 | AAA+(                                             |
|  82 | Amyloid Beta (A4) Precursor Protein               |
|  83 | APPe                                              |
|  84 | Amyloid Beta-Peptide                              |
|  85 | aPP-N                                             |
|  86 | beta-AS                                           |
|  87 | A-beta                                            |
|  88 | APPS                                              |
|  89 | AAa                                               |
|  90 | Gamma-secretase C-terminal fragment 59            |
|  91 | beta Amyloid peptide                              |
|  92 | C83                                               |
|  93 | Amyloid Beta-peptides                             |
|  94 | amyloidal precursor protein                       |
|  95 | Beta Amyloid Precursor Protein                    |
|  96 | Beta Amyloid Peptide                              |
|  97 | AMYLOID PRECURSOR PROTEIN                         |
|  98 | beta A4-amyloid precursor protein                 |
|  99 | [beta]-amyloid precursor protein                  |
| 100 | A-Beta                                            |
| 101 | Amyloidal Precursor Protein                       |
| 102 | amyloid Precursor Protein                         |
| 103 | Beta (A4)-amyloid protein                         |
| 104 | beta-Amyloid protein (beta A4                     |
| 105 | APP) I                                            |
| 106 | AD.1                                              |
| 107 | beta-A                                            |
| 108 | C8.0                                              |
| 109 | Amyloid-Precursor Protein                         |
| 110 | Amyloid beta-precursor protein                    |
| 111 | )-amyloid precursor protein                       |
| 112 | beta-Amyloid Peptide                              |
| 113 | APp                                               |
| 114 | Amyloidal precursor protein                       |
| 115 | amyloid precursor proteins α                      |
| 116 | beta amyloid peptide                              |
| 117 | Where amyloid beta protein precursor-amyloid beta |
| 118 | C8-3                                              |
| 119 | amyloid beta A4 precursor protein                 |
| 120 | beta-amyloid protein 42                           |
| 121 | amyloid-beta protein precursor                    |
| 122 | cVAP                                              |
| 123 | AαA                                               |
| 124 | Aaas                                              |
| 125 | Beta-Amyloid Peptides                             |
| 126 | protein precursor of amyloid                      |
| 127 | beta-amyloid and amyloid precursor protein        |
| 128 | beta-Amyloid Precursor Protein                    |
| 129 | amyloid beta precursor-protein                    |
| 130 | APP-I                                             |
| 131 | amyloid protein (beta A4                          |
| 132 | amyloid beta peptides                             |
| 133 | Vap C                                             |
| 134 | aaA                                               |
| 135 | protease nexin-II                                 |
| 136 | amyloid beta-protein 42                           |
| 137 | amyloid-beta 42 protein                           |
| 138 | Amyloid Precursor-Protein                         |
| 139 | ̃-Amyloid precursor-protein                                                   |
| 140 | beta-amyloid peptides                             |
| 141 | Amyloid precursor proteinE                        |
| 142 | aPP                                               |
| 143 | APPS-I                                            |
| 144 | Beta-A                                            |
| 145 | amyloidbeta precursor protein                     |
| 146 | amyloid beta protein precursor                    |
| 147 | AAA(+)                                            |
| 148 | Beta-amyloid peptide                              |
| 149 | APP- I                                            |
| 150 | α-amyloid precursor protein                       |
| 151 | beta A4-amyloid protein precursor                 |
| 152 | A beta                                            |
| 153 | PN-2                                              |
| 154 | amyloid precursors protein                        |
| 155 | aAAS                                              |
| 156 | Protease Nexin II                                 |
| 157 | Beta Amyloid Peptides                             |
| 158 | BPP-A                                             |
| 159 | aD1                                               |
| 160 | beta-amyloid protein precursor                    |
| 161 | AP-P                                              |
| 162 | CTF gamma                                         |
| 163 | amyloid-beta protein precursor/amyloid-beta       |
| 164 | amyloid-beta precursor protein                    |
| 165 | ApP                                               |
| 166 | beta- amyloid peptide                             |
| 167 | beta amyloid precursor proteins                   |
| 168 | Amyloid-beta-peptide                              |
| 169 | beta-amyloid precursor proteins                   |
| 170 | aPPs                                              |
| 171 | Amyloid beta/A4 protein                           |
| 172 | Amyloid beta Peptide                              |
| 173 | ad-1                                              |
| 174 | amyloid precursor-protein                         |
| 175 | amyloid beta protein A4                           |
| 176 | beta A4 amyloid precursor protein                 |
| 177 | Amyloid beta/A4 precursor protein                 |
| 178 | (APP) I                                           |
| 179 | Pn2                                               |
| 180 | APPN                                              |
| 181 | s Amyloid Precursor Protein                       |
| 182 | beta A4 amyloid protein                           |
| 183 | beta/A4-amyloid protein                           |
| 184 | VAP-C                                             |
| 185 | Amyloid beta-peptides                             |
| 186 | ß-Amyloid precursor protein                       |
| 187 | AAA+                                              |
| 188 | peptide beta-amyloid                              |
| 189 | app                                               |
| 190 | Amyloid beta protein 40                           |
| 191 | AβPPs                                             |
| 192 | AppY                                              |
| 193 | PPI-A                                             |
| 194 | Abetas                                            |
| 195 | AD-1                                              |
| 196 | amyloid beta-peptide                              |
| 197 | P05067                                            |
| 198 | (Abeta)                                           |
| 199 | AAA+-                                             |
| 200 | amyloid-precursor-protein                         |
| 201 | Amyloid-beta Peptide                              |
| 202 | appe                                              |
| 203 | amyloid protein precursor α                       |
| 204 | ABETA                                             |
| 205 | amyloid beta precursor proteins                   |
| 206 | Beta amyloid peptides                             |
| 207 | APPi                                              |
| 208 | Amyloid-beta A4 Protein                           |
| 209 | beta A                                            |
| 210 | Amyloid-beta Protein Precursor                    |
| 211 | beta-amyloid peptide                              |
| 212 | Beta amyloid peptide                              |
| 213 | Alzheimer's disease amyloid ß-protein             |
| 214 | beta-amyloid protein-42                           |
| 215 | AbPP                                              |
| 216 | protease nexin II                                 |
| 217 | Amyloid beta Precursor Protein                    |
| 218 | p3 40                                             |
| 219 | abeta                                             |
| 220 | Beta A4-amyloid protein                           |
| 221 | beta-A4 amyloid protein                           |
| 222 | beta amyloid peptides                             |
| 223 | Beta-Amyloid Peptide                              |
| 224 | C-99                                              |
| 225 | AAA/                                              |
| 226 | amyloid precursor protein α                       |
| 227 | Amyloid beta precursor protein                    |
| 228 | Amyloid beta A4 precursor protein                 |
| 229 | Cvap                                              |
| 230 | amyloid beta-protein 40                           |
| 231 | IPN I                                             |
| 232 | APPy                                              |
| 233 | Amyloid Beta Peptides                             |
| 234 | amyloid beta-protein-42                           |
| 235 | APP I                                             |
| 236 | Amyloid precursorprotein                          |
| 237 | beta -amyloid peptide                             |
| 238 | s-amyloid precursor protein                       |
| 239 | amyloid-beta-amyloid peptide                      |
| 240 | IPN-I                                             |
| 241 | apP                                               |
| 242 | Ap-P                                              |
| 243 | CTfgamma                                          |
| 244 | -in amyloid precursor protein                     |
| 245 | preA4                                             |
| 246 | AMYLOID BETA A4 PRECURSOR PROTEIN                 |
| 247 | Amyloid Precursor Protein α                       |
| 248 | App I                                             |
| 249 | CTFgamma                                          |
| 250 | App                                               |
| 251 | Amyloid beta (A4) precursor protein               |
| 252 | ETA Ab                                            |
| 253 | amyloid Beta Peptide                              |
| 254 | beta-amyloid precursor-protein                    |
| 255 | Amyloid protein precursor                         |
| 256 | PS-Ap                                             |
| 257 | beta-Amyloid peptide                              |
| 258 | PN-II                                             |
| 259 | appI                                              |
| 260 | Amyloid beta A4 protein                           |
| 261 | s-APP                                             |
| 262 | Amyloid beta-peptide                              |
| 263 | Beta A4 amyloid protein                           |
| 264 | beta/A4 amyloid protein precursor                 |
| 265 | ̃-amyloid precursor protein                                                   |
| 266 | precursor amyloid protein                         |
| 267 | beta-amyloid (A4 protein                          |
| 268 | AAA+,                                             |
| 269 | amyloid precursor protein beta                    |
| 270 | Amyloid-beta Precursor Protein                    |
| 271 | beta-Amyloid precursor protein                    |
| 272 | AAA+/                                             |
| 273 | beta amyloid protein A4                           |
| 274 | APPE                                              |
| 275 | beta amyloid protein precursor                    |
| 276 | amyloid beta protein 42                           |
| 277 | Amyloid-beta A4 precursor protein                 |
| 278 | amyloid beta-protein precursor                    |
| 279 | APP-                                              |
| 280 | Amyloid Beta Precursor Protein                    |
| 281 | beta amyloid protein 40                           |
| 282 | Beta-amyloid peptides                             |
| 283 | CVAPs                                             |
| 284 | amyloid beta peptide                              |
| 285 | Amyloid Precursor protein                         |
| 286 | P34-2                                             |
| 287 | amyloid beta protein precursor protein            |
| 288 | amyloid beta A4 protein                           |
| 289 | α-APP                                             |
| 290 | amyloid betapeptide                               |
| 291 | The amyloid beta-precursor protein                |
| 292 | Amyloid Precursor Proteins                        |
| 293 | ApPS                                              |
| 294 | amyloid precursorprotein                          |
| 295 | Beta-amyloid precursor protein                    |
| 296 | Beta amyloid precursor protein                    |
| 297 | [amyloid precursor protein                        |
| 298 | APP)                                              |
| 299 | Amyloid beta-protein precursor                    |
| 300 | APPs                                              |
| 301 | c99                                               |
| 302 | Protease nexin-II                                 |
| 303 | i-AAA                                             |
| 304 | amyloid precursor proteins                        |
| 305 | pn2                                               |
| 306 | C99                                               |
| 307 | beta-amyloid precursor protein                    |
| 308 | AAA +                                             |
| 309 | Amyloid Precursor Protein a                       |
| 310 | sAPP alpha                                        |
| 311 | amyloid pre-cursor protein                        |
| 312 | Beta-amyloid protein 42                           |
| 313 | beta/A4 amyloid protein                           |
| 314 | APPY                                              |
| 315 | Alzheimer's disease amyloid protein               |
| 316 | amyloid peptide beta                              |
| 317 | APP α                                             |
| 318 | APP-S                                             |
| 319 | Amyloid-beta A4 protein                           |
| 320 | beta amyloid A4 protein                           |
| 321 | beta amyloid precursor protein                    |
| 322 | AP PS                                             |
| 323 | AbetaS                                            |
| 324 | amyloid-beta peptides                             |
| 325 | Amyloid beta protein 42                           |
| 326 | Beta-amyloid Precursor Protein                    |
| 327 | beta-Amyloid peptides                             |
| 328 | amyloid- beta peptide                             |
| 329 | Abeta                                             |
| 330 | amyloid beta a4 protein                           |
| 331 | protein precursor amyloid                         |
| 332 | PPI) A                                            |
| 333 | AaaS                                              |
| 334 | CTF-gamma                                         |
| 335 | PN2                                               |
| 336 | pp-A                                              |
| 337 | C80                                               |
| 338 | ABeta                                             |
| 339 | APP-α                                             |
| 340 | peptide amyloid beta                              |
| 341 | Amyloid-precursor protein                         |
| 342 | amyloid beta protein, beta A4                     |
| 343 | amyloid Beta peptide                              |
| 344 | amyloid-beta-peptide                              |
| 345 | amyloid precursor protein-α                       |
| 346 | Ad1                                               |
| 347 | p34-2                                             |
| 348 | ?-amyloid precursor protein                       |
| 349 | beta-Amyloid protein precursor                    |
| 350 | Abeta)                                            |
| 351 | beta -Amyloid peptide                             |
| 352 | beta-amyloid 42 protein                           |
| 353 | APPs-α                                            |
| 354 | amyloid beta-proteins 42                          |
| 355 | ABPP                                              |
| 356 | APPys                                             |
| 357 | ApPI                                              |
| 358 | Beta amyloid precursor proteins                   |
| 359 | Beta amyloid Peptide                              |
| 360 | beta A beta A                                     |
| 361 | CVAP                                              |
| 362 | APP-N                                             |
| 363 | beta A4-amyloid protein                           |
| 364 | Amyloid precursor protein                         |
| 365 | AAA+)                                             |
| 366 | amyloid beta/A4 protein                           |
| 367 | aaas                                              |
| 368 | AAA                                               |
| 369 | Amyloid-Precursor-Protein                         |
| 370 | amyloid-protein precursor                         |
| 371 | beta protein amyloid A4                           |
| 372 | -APP                                              |
| 373 | α-AA                                              |
| 374 | Amyloid beta peptide                              |
| 375 | amy-loid precursor protein                        |
| 376 | amyloid precursor protein                         |
| 377 | Amyloid precursor protein beta                    |
| 378 | p340                                              |
| 379 | Amyloid beta-protein 42                           |
| 380 | peptidase nexin-II                                |
| 381 | amyloid-beta peptide                              |
| 382 | beta AS                                           |
| 383 | appY                                              |
| 384 | protein amyloid-beta precursor protein            |
| 385 | amyloid beta precursor protein                    |
| 386 | Beta-amyloid Peptide                              |
| 387 | " amyloid precursor protein                       |
| 388 | n-APP                                             |
| 389 | Beta-Amyloid peptide                              |
| 390 | -amyloid precursor protein                        |
| 391 | Amyloid Precursor Protein                         |
| 392 | amyloid- precursor protein                        |
| 393 | AD1                                               |
| 394 | AppN                                              |
| 395 | APPÉ                                                   |
| 396 | N-APP                                             |
| 397 | Beta-Amyloid Precursor Protein                    |
| 398 | Amyloid beta A4 protein precursor                 |
| 399 | ß-amyloid precursor protein                       |
| 400 | amyloid beta (A4) precursor protein               |
| 401 | amyloid beta-peptides                             |
| 402 | Alzheimer disease amyloid proteins                |

## After filtering
|     | label                                             |
|----:|:--------------------------------------------------|
|   0 | Amyloid-beta protein precursor                    |
|   1 | beta amyloid-peptide                              |
|   2 | amyloid beta-Protein Precursor                    |
|   3 | Protease nexin II                                 |
|   4 | amyloid beta/A4 precursor protein                 |
|   5 | Beta-amyloid precursor proteins                   |
|   6 | AAAs                                              |
|   7 | protein amyloid precursor protein                 |
|   8 | amyloid precursor's protein                       |
|   9 | amyloid-precursor protein                         |
|  10 | Amyloid Precursor Protein*                        |
|  11 | beta-protein amyloid A4                           |
|  12 | amyloid-beta protein precursor-amyloid-beta       |
|  13 | amyloid-beta-precursor protein                    |
|  14 | sAPP-alpha                                        |
|  15 | APPIs                                             |
|  16 | peptidase Nexin-II                                |
|  17 | Amyloid beta-Peptides                             |
|  18 | PN II                                             |
|  19 | AAAS                                              |
|  20 | beta -amyloid precursor protein                   |
|  21 | peptide amyloid-beta                              |
|  22 | amyloid-( precursor protein                       |
|  23 | amyloid beta-precursor protein                    |
|  24 | beta-amyloid-peptide                              |
|  25 | amyloid-beta A4 protein                           |
|  26 | Amyloid Protein Precursor                         |
|  27 | Amyloid-Beta Peptide                              |
|  28 | Alzheimer disease amyloid protein                 |
|  29 | Pn-2                                              |
|  30 | Amyloid beta peptides                             |
|  31 | APP                                               |
|  32 | amyloid ß precursor protein                       |
|  33 | Pn2s                                              |
|  34 | beta-amyloid-precursor proteins                   |
|  35 | amyloid-βeta precursor protein                    |
|  36 | Amyloid precursor protein α                       |
|  37 | AßPP                                              |
|  38 | APPI                                              |
|  39 | Aβpp                                              |
|  40 | appE                                              |
|  41 | Amyloid precursor proteins                        |
|  42 | beta/A4 amyloid precursor protein                 |
|  43 | APPs-I                                            |
|  44 | beta-amyloid-precursor-protein                    |
|  45 | P340                                              |
|  46 | PP-A                                              |
|  47 | Amyloid-Beta Precursor Protein                    |
|  48 | amyloide beta (A4) precursor protein              |
|  49 | Amyloid-ß Precursor Protein                       |
|  50 | PreA4                                             |
|  51 | alpha-sAPP                                        |
|  52 | and amyloid protein precursor                     |
|  53 | s amyloid precursor protein                       |
|  54 | ad1                                               |
|  55 | Precursor of amyloid protein                      |
|  56 | (APP)I                                            |
|  57 | beta-amyloid-precursor protein                    |
|  58 | Amyloid-beta peptide                              |
|  59 | The amyloid precursor protein                     |
|  60 | Amyloid-beta peptides                             |
|  61 | amyloid precursor protein a                       |
|  62 | AβPP                                              |
|  63 | Amyloid Beta Peptide                              |
|  64 | p342                                              |
|  65 | amyloid protein precursor                         |
|  66 | α-AβPP                                            |
|  67 | Amyloid-beta precursor protein                    |
|  68 | ABPPs                                             |
|  69 | beta-amyloide peptide                             |
|  70 | AppI                                              |
|  71 | Amyloid Beta-Peptide                              |
|  72 | APPe                                              |
|  73 | Amyloid Beta (A4) Precursor Protein               |
|  74 | aPP-N                                             |
|  75 | A-beta                                            |
|  76 | APPS                                              |
|  77 | Gamma-secretase C-terminal fragment 59            |
|  78 | beta Amyloid peptide                              |
|  79 | C83                                               |
|  80 | Amyloid Beta-peptides                             |
|  81 | amyloidal precursor protein                       |
|  82 | Beta Amyloid Precursor Protein                    |
|  83 | Beta Amyloid Peptide                              |
|  84 | beta A4-amyloid precursor protein                 |
|  85 | AMYLOID PRECURSOR PROTEIN                         |
|  86 | [beta]-amyloid precursor protein                  |
|  87 | amyloid Precursor Protein                         |
|  88 | beta-Amyloid protein (beta A4                     |
|  89 | Amyloidal Precursor Protein                       |
|  90 | Beta (A4)-amyloid protein                         |
|  91 | APP) I                                            |
|  92 | AD.1                                              |
|  93 | C8.0                                              |
|  94 | Amyloid-Precursor Protein                         |
|  95 | )-amyloid precursor protein                       |
|  96 | Amyloid beta-precursor protein                    |
|  97 | APp                                               |
|  98 | beta-Amyloid Peptide                              |
|  99 | Amyloidal precursor protein                       |
| 100 | amyloid precursor proteins α                      |
| 101 | beta amyloid peptide                              |
| 102 | C8-3                                              |
| 103 | Where amyloid beta protein precursor-amyloid beta |
| 104 | amyloid beta A4 precursor protein                 |
| 105 | beta-amyloid protein 42                           |
| 106 | amyloid-beta protein precursor                    |
| 107 | Beta-Amyloid Peptides                             |
| 108 | protein precursor of amyloid                      |
| 109 | beta-amyloid and amyloid precursor protein        |
| 110 | beta-Amyloid Precursor Protein                    |
| 111 | amyloid beta precursor-protein                    |
| 112 | APP-I                                             |
| 113 | amyloid protein (beta A4                          |
| 114 | amyloid beta-protein 42                           |
| 115 | amyloid beta peptides                             |
| 116 | protease nexin-II                                 |
| 117 | ̃-Amyloid precursor-protein                                                   |
| 118 | Amyloid Precursor-Protein                         |
| 119 | amyloid-beta 42 protein                           |
| 120 | beta-amyloid peptides                             |
| 121 | aPP                                               |
| 122 | Amyloid precursor proteinE                        |
| 123 | APPS-I                                            |
| 124 | amyloid beta protein precursor                    |
| 125 | amyloidbeta precursor protein                     |
| 126 | Beta-amyloid peptide                              |
| 127 | beta A4-amyloid protein precursor                 |
| 128 | α-amyloid precursor protein                       |
| 129 | APP- I                                            |
| 130 | PN-2                                              |
| 131 | A beta                                            |
| 132 | amyloid precursors protein                        |
| 133 | Protease Nexin II                                 |
| 134 | Beta Amyloid Peptides                             |
| 135 | BPP-A                                             |
| 136 | beta-amyloid protein precursor                    |
| 137 | aD1                                               |
| 138 | AP-P                                              |
| 139 | CTF gamma                                         |
| 140 | amyloid-beta protein precursor/amyloid-beta       |
| 141 | amyloid-beta precursor protein                    |
| 142 | beta- amyloid peptide                             |
| 143 | ApP                                               |
| 144 | beta amyloid precursor proteins                   |
| 145 | Amyloid-beta-peptide                              |
| 146 | beta-amyloid precursor proteins                   |
| 147 | aPPs                                              |
| 148 | Amyloid beta/A4 protein                           |
| 149 | Amyloid beta Peptide                              |
| 150 | ad-1                                              |
| 151 | amyloid precursor-protein                         |
| 152 | Amyloid beta/A4 precursor protein                 |
| 153 | beta A4 amyloid precursor protein                 |
| 154 | amyloid beta protein A4                           |
| 155 | (APP) I                                           |
| 156 | APPN                                              |
| 157 | beta A4 amyloid protein                           |
| 158 | Pn2                                               |
| 159 | beta/A4-amyloid protein                           |
| 160 | s Amyloid Precursor Protein                       |
| 161 | Amyloid beta-peptides                             |
| 162 | ß-Amyloid precursor protein                       |
| 163 | peptide beta-amyloid                              |
| 164 | AAA+                                              |
| 165 | app                                               |
| 166 | AβPPs                                             |
| 167 | Amyloid beta protein 40                           |
| 168 | AppY                                              |
| 169 | Abetas                                            |
| 170 | amyloid beta-peptide                              |
| 171 | AD-1                                              |
| 172 | P05067                                            |
| 173 | amyloid-precursor-protein                         |
| 174 | amyloid protein precursor α                       |
| 175 | appe                                              |
| 176 | Amyloid-beta Peptide                              |
| 177 | Beta amyloid peptides                             |
| 178 | beta A                                            |
| 179 | Amyloid-beta Protein Precursor                    |
| 180 | Amyloid-beta A4 Protein                           |
| 181 | ABETA                                             |
| 182 | amyloid beta precursor proteins                   |
| 183 | APPi                                              |
| 184 | beta-amyloid peptide                              |
| 185 | Beta amyloid peptide                              |
| 186 | Alzheimer's disease amyloid ß-protein             |
| 187 | beta-amyloid protein-42                           |
| 188 | AbPP                                              |
| 189 | Amyloid beta Precursor Protein                    |
| 190 | protease nexin II                                 |
| 191 | p3 40                                             |
| 192 | Beta A4-amyloid protein                           |
| 193 | beta-A4 amyloid protein                           |
| 194 | beta amyloid peptides                             |
| 195 | Beta-Amyloid Peptide                              |
| 196 | C-99                                              |
| 197 | amyloid precursor protein α                       |
| 198 | Amyloid beta precursor protein                    |
| 199 | Amyloid beta A4 precursor protein                 |
| 200 | amyloid beta-protein 40                           |
| 201 | APPy                                              |
| 202 | Amyloid Beta Peptides                             |
| 203 | amyloid beta-protein-42                           |
| 204 | APP I                                             |
| 205 | Amyloid precursorprotein                          |
| 206 | beta -amyloid peptide                             |
| 207 | s-amyloid precursor protein                       |
| 208 | amyloid-beta-amyloid peptide                      |
| 209 | Ap-P                                              |
| 210 | apP                                               |
| 211 | CTfgamma                                          |
| 212 | -in amyloid precursor protein                     |
| 213 | preA4                                             |
| 214 | AMYLOID BETA A4 PRECURSOR PROTEIN                 |
| 215 | Amyloid Precursor Protein α                       |
| 216 | App I                                             |
| 217 | CTFgamma                                          |
| 218 | App                                               |
| 219 | Amyloid beta (A4) precursor protein               |
| 220 | amyloid Beta Peptide                              |
| 221 | beta-amyloid precursor-protein                    |
| 222 | beta-Amyloid peptide                              |
| 223 | Amyloid protein precursor                         |
| 224 | appI                                              |
| 225 | PN-II                                             |
| 226 | Amyloid beta A4 protein                           |
| 227 | s-APP                                             |
| 228 | Amyloid beta-peptide                              |
| 229 | Beta A4 amyloid protein                           |
| 230 | beta/A4 amyloid protein precursor                 |
| 231 | ̃-amyloid precursor protein                                                   |
| 232 | beta-amyloid (A4 protein                          |
| 233 | precursor amyloid protein                         |
| 234 | beta-Amyloid precursor protein                    |
| 235 | amyloid precursor protein beta                    |
| 236 | beta amyloid protein A4                           |
| 237 | Amyloid-beta Precursor Protein                    |
| 238 | APPE                                              |
| 239 | beta amyloid protein precursor                    |
| 240 | amyloid beta-protein precursor                    |
| 241 | amyloid beta protein 42                           |
| 242 | Amyloid-beta A4 precursor protein                 |
| 243 | APP-                                              |
| 244 | Amyloid Beta Precursor Protein                    |
| 245 | beta amyloid protein 40                           |
| 246 | Beta-amyloid peptides                             |
| 247 | amyloid beta peptide                              |
| 248 | Amyloid Precursor protein                         |
| 249 | P34-2                                             |
| 250 | amyloid beta protein precursor protein            |
| 251 | amyloid beta A4 protein                           |
| 252 | α-APP                                             |
| 253 | amyloid betapeptide                               |
| 254 | The amyloid beta-precursor protein                |
| 255 | Amyloid Precursor Proteins                        |
| 256 | ApPS                                              |
| 257 | amyloid precursorprotein                          |
| 258 | Beta-amyloid precursor protein                    |
| 259 | Beta amyloid precursor protein                    |
| 260 | Amyloid beta-protein precursor                    |
| 261 | [amyloid precursor protein                        |
| 262 | APP)                                              |
| 263 | APPs                                              |
| 264 | Protease nexin-II                                 |
| 265 | c99                                               |
| 266 | i-AAA                                             |
| 267 | amyloid precursor proteins                        |
| 268 | pn2                                               |
| 269 | C99                                               |
| 270 | beta-amyloid precursor protein                    |
| 271 | Amyloid Precursor Protein a                       |
| 272 | sAPP alpha                                        |
| 273 | beta/A4 amyloid protein                           |
| 274 | amyloid pre-cursor protein                        |
| 275 | Beta-amyloid protein 42                           |
| 276 | APPY                                              |
| 277 | Alzheimer's disease amyloid protein               |
| 278 | amyloid peptide beta                              |
| 279 | APP α                                             |
| 280 | APP-S                                             |
| 281 | Amyloid-beta A4 protein                           |
| 282 | beta amyloid A4 protein                           |
| 283 | beta amyloid precursor protein                    |
| 284 | AP PS                                             |
| 285 | amyloid-beta peptides                             |
| 286 | Amyloid beta protein 42                           |
| 287 | Beta-amyloid Precursor Protein                    |
| 288 | beta-Amyloid peptides                             |
| 289 | amyloid- beta peptide                             |
| 290 | Abeta                                             |
| 291 | protein precursor amyloid                         |
| 292 | CTF-gamma                                         |
| 293 | amyloid beta a4 protein                           |
| 294 | PN2                                               |
| 295 | pp-A                                              |
| 296 | C80                                               |
| 297 | APP-α                                             |
| 298 | ABeta                                             |
| 299 | peptide amyloid beta                              |
| 300 | Amyloid-precursor protein                         |
| 301 | amyloid Beta peptide                              |
| 302 | amyloid beta protein, beta A4                     |
| 303 | amyloid-beta-peptide                              |
| 304 | amyloid precursor protein-α                       |
| 305 | Ad1                                               |
| 306 | p34-2                                             |
| 307 | ?-amyloid precursor protein                       |
| 308 | beta-Amyloid protein precursor                    |
| 309 | beta -Amyloid peptide                             |
| 310 | beta-amyloid 42 protein                           |
| 311 | amyloid beta-proteins 42                          |
| 312 | APPs-α                                            |
| 313 | ABPP                                              |
| 314 | APPys                                             |
| 315 | Beta amyloid Peptide                              |
| 316 | ApPI                                              |
| 317 | Beta amyloid precursor proteins                   |
| 318 | CVAP                                              |
| 319 | beta A4-amyloid protein                           |
| 320 | APP-N                                             |
| 321 | Amyloid precursor protein                         |
| 322 | amyloid beta/A4 protein                           |
| 323 | -APP                                              |
| 324 | AAA                                               |
| 325 | amyloid-protein precursor                         |
| 326 | Amyloid-Precursor-Protein                         |
| 327 | beta protein amyloid A4                           |
| 328 | Amyloid beta peptide                              |
| 329 | amy-loid precursor protein                        |
| 330 | amyloid precursor protein                         |
| 331 | p340                                              |
| 332 | Amyloid beta-protein 42                           |
| 333 | Amyloid precursor protein beta                    |
| 334 | amyloid-beta peptide                              |
| 335 | peptidase nexin-II                                |
| 336 | appY                                              |
| 337 | protein amyloid-beta precursor protein            |
| 338 | amyloid beta precursor protein                    |
| 339 | Beta-amyloid Peptide                              |
| 340 | " amyloid precursor protein                       |
| 341 | n-APP                                             |
| 342 | Beta-Amyloid peptide                              |
| 343 | -amyloid precursor protein                        |
| 344 | Amyloid Precursor Protein                         |
| 345 | amyloid- precursor protein                        |
| 346 | AD1                                               |
| 347 | AppN                                              |
| 348 | N-APP                                             |
| 349 | APPÉ                                                   |
| 350 | Beta-Amyloid Precursor Protein                    |
| 351 | ß-amyloid precursor protein                       |
| 352 | Amyloid beta A4 protein precursor                 |
| 353 | amyloid beta (A4) precursor protein               |
| 354 | amyloid beta-peptides                             |
| 355 | Alzheimer disease amyloid proteins                |
