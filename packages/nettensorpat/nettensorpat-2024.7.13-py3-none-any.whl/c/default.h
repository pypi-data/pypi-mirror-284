#include <stdio.h>
#include "UtilsOfTensor.h"

extern int INIT_XY_BY_ONES, INIT_XY_BY_RAND, INIT_XY_BY_UNIT, INIT_XY_DEFAULT;
extern const int NPATTERN_UNLIMITED, MAXPATTERN_DEFAULT;

extern const unsigned int NITERATION_DEFAULT;
extern const unsigned int NSTAGE_DEFAULT;
extern const unsigned int MINGENE_DEFAULT;
extern const unsigned int MINNET_DEFAULT;
extern const unsigned int MAXGENE;
extern const unsigned int NEDGES_LOAD_DEFAULT;

extern const double MIN_DENSITY_DEFAULT;

extern const char MASK_STRATEGY_NAME_EDGES_PATTERN[MAXCHAR];
extern const char MASK_STRATEGY_NAME_EDGES_ALLNETS[MAXCHAR];
extern const char MASK_STRATEGY_NAME_GENES[MAXCHAR];
extern char MASK_STRATEGY_NAME_DEFAULT[MAXCHAR];

extern const char OVERLAPPATTERNCHOOSE_NONZEROS[MAXCHAR];
extern const char OVERLAPPATTERNCHOOSE_MORE_NETS[MAXCHAR];
extern const char OVERLAPPATTERNCHOOSE_MORE_GENES[MAXCHAR];
extern const char OVERLAPPATTERNCHOOSE_BOTH[MAXCHAR];
extern char OVERLAPPATTERNCHOOSE_DEFAULT[MAXCHAR];

extern const unsigned int NEDGES_LOAD_DEFAULT;
extern unsigned int loadUnweighted;
extern const unsigned int RESUME_LASTRUN_DEFAULT;
extern const unsigned int DEFAULT_INCLUDE_EDGES;

extern const char PREFIX_RESULTFILE_DEFAULT[MAXCHAR];
extern const char PATH_RESULT_DEFAULT[MAXCHAR];
extern const char PATH_DEBUG_DATASETS[MAXCHAR];
extern const char PATH_NETS_DEFAULT[MAXCHAR];
extern const char SUFFIX_DATAFILE[MAXCHAR];

extern unsigned int useGivenResultFilename;
extern int muleInput;
extern int muleOutput;

int initDefaultVariables();