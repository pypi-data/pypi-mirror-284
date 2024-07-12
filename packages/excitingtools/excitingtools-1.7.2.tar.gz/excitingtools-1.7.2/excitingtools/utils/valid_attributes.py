""" Automatically generated file with the valid attributes from the schema. 
Do not manually change. Instead, run "utils/schema_parsing.py" to regenerate. """ 

# input information 
input_valid_attributes = ["sharedfs", "xsltpath"] 
input_valid_subtrees = ["title", "structure", "groundstate", "relax", "properties", "phonons", "xs", "gw", "MD", "eph", 
                        "keywords"] 
input_mandatory_attributes = ["groundstate", "structure", "title"] 


# common information 
origin_valid_attributes = ["coord"] 

point_valid_attributes = ["breakafter", "coord", "label"] 
point_mandatory_attributes = ["coord"] 

plot1d_valid_subtrees = ["path"] 
plot1d_mandatory_attributes = ["path"] 

path_valid_attributes = ["outfileprefix", "steps"] 
path_valid_subtrees = ["point"] 
path_mandatory_attributes = ["point", "steps"] 
path_multiple_children = ["point"] 

plot2d_valid_subtrees = ["parallelogram"] 
plot2d_mandatory_attributes = ["parallelogram"] 

parallelogram_valid_attributes = ["grid", "outfileprefix"] 
parallelogram_valid_subtrees = ["origin", "point"] 
parallelogram_mandatory_attributes = ["grid", "origin", "point"] 
parallelogram_multiple_children = ["point"] 

plot3d_valid_attributes = ["usesym"] 
plot3d_valid_subtrees = ["box"] 
plot3d_mandatory_attributes = ["box"] 

box_valid_attributes = ["grid", "outfileprefix"] 
box_valid_subtrees = ["origin", "point"] 
box_mandatory_attributes = ["grid", "origin", "point"] 
box_multiple_children = ["point"] 

kstlist_valid_subtrees = ["pointstatepair"] 
kstlist_mandatory_attributes = ["pointstatepair"] 
kstlist_multiple_children = ["pointstatepair"] 

energywindow_valid_attributes = ["intv", "points"] 

qpointset_valid_subtrees = ["qpoint"] 
qpointset_mandatory_attributes = ["qpoint"] 
qpointset_multiple_children = ["qpoint"] 

parts_valid_subtrees = ["dopart"] 
parts_multiple_children = ["dopart"] 

dopart_valid_attributes = ["id"] 
dopart_mandatory_attributes = ["id"] 

qpoints_valid_attributes = ["qf", "qi"] 

kpoints_valid_attributes = ["kf", "ki"] 


# structure information 
structure_valid_attributes = ["autormt", "autormtscaling", "cartesian", "epslat", "primcell", "speciespath", "tshift"] 
structure_valid_subtrees = ["crystal", "species", "symmetries"] 
structure_mandatory_attributes = ["speciespath"] 
structure_multiple_children = ["species"] 

crystal_valid_attributes = ["scale", "stretch"] 
crystal_valid_subtrees = ["basevect"] 
crystal_multiple_children = ["basevect"] 

species_valid_attributes = ["atomicNumber", "chemicalSymbol", "fixrmt", "rmt", "speciesfile"] 
species_valid_subtrees = ["atom", "LDAplusU", "dfthalfparam"] 
species_mandatory_attributes = ["speciesfile"] 
species_multiple_children = ["atom"] 

atom_valid_attributes = ["bfcmt", "coord", "lockxyz", "mommtfix", "velocity"] 
atom_mandatory_attributes = ["coord"] 

LDAplusU_valid_attributes = ["J", "U", "l"] 

dfthalfparam_valid_attributes = ["ampl", "cut", "exponent"] 
dfthalfparam_valid_subtrees = ["shell"] 
dfthalfparam_mandatory_attributes = ["shell"] 
dfthalfparam_multiple_children = ["shell"] 

shell_valid_attributes = ["ionization", "number"] 


# groundstate information 
groundstate_valid_attributes = ["APWprecision", "CoreRelativity", "ExplicitKineticEnergy", "PrelimLinSteps", 
                                "ValenceRelativity", "autokpt", "beta0", "betadec", "betainc", "cfdamp", "chgexs", 
                                "deband", "dipolecorrection", "dipoleposition", "dlinengyfermi", "do", "energyref", 
                                "epsband", "epschg", "epsengy", "epsforcescf", "epsocc", "epspot", "fermilinengy", 
                                "findlinentype", "fracinr", "frozencore", "gmaxvr", "isgkmax", "ldapu", "lmaxapw", 
                                "lmaxinr", "lmaxmat", "lmaxvr", "lradstep", "maxscl", "mixer", "mixerswitch", 
                                "modifiedsv", "msecStoredSteps", "nempty", "ngridk", "niterconvcheck", "nktot", 
                                "nosource", "nosym", "nprad", "npsden", "nwrite", "outputlevel", "ptnucl", 
                                "radialgridtype", "radkpt", "reducek", "rgkmax", "scfconv", "stype", "swidth", 
                                "symmorph", "tevecsv", "tfibs", "tforce", "tpartcharges", "useAPWprecision", 
                                "useDensityMatrix", "vdWcorrection", "vkloff", "xctype"] 
groundstate_valid_subtrees = ["DFTD2parameters", "TSvdWparameters", "spin", "HartreeFock", "dfthalf", "Hybrid", 
                              "sirius", "solver", "OEP", "RDMFT", "output", "libxc", "xsLO", "lorecommendation"] 

DFTD2parameters_valid_attributes = ["cutoff", "d", "s6", "sr6"] 

TSvdWparameters_valid_attributes = ["cutoff", "d", "nr", "nsph", "s6", "sr6"] 

spin_valid_attributes = ["bfieldc", "fixspin", "momfix", "nosv", "realspace", "reducebf", "spinorb", "spinsprl", "svlo", 
                         "taufsm", "vqlss"] 

dfthalf_valid_attributes = ["printVSfile"] 

Hybrid_valid_attributes = ["BasisBareCoulomb", "HSEsingularity", "eccoeff", "epsmb", "exchangetype", "excoeff", "gmb", 
                           "lmaxmb", "maxscl", "mblksiz", "omega", "updateRadial"] 

sirius_valid_attributes = ["cfun", "density", "densityinit", "eigenstates", "sfacg", "vha", "xc"] 

solver_valid_attributes = ["constructHS", "evaltol", "minenergy", "packedmatrixstorage", "type"] 

OEP_valid_attributes = ["convoep", "maxitoep", "tauoep"] 

RDMFT_valid_attributes = ["maxitc", "maxitn", "rdmalpha", "rdmmaxscl", "rdmtemp", "rdmxctype", "taurdmc", "taurdmn"] 

output_valid_attributes = ["state"] 

libxc_valid_attributes = ["correlation", "exchange", "xc"] 

xsLO_valid_attributes = ["emax", "lmax", "maxnodes"] 

lorecommendation_valid_attributes = ["lmaxlo", "nodesmaxlo"] 


# relax information 
relax_valid_attributes = ["addtohistory", "endbfgs", "epsforce", "history", "historyformat", "maxbfgs", "maxsteps", 
                          "method", "outputlevel", "printtorque", "taubfgs", "taunewton"] 


# phonons information 
phonons_valid_attributes = ["canonical", "delete_eigensystem_response", "deltaph", "do", "drynumprocs", "gamma", 
                            "maxprocsperpart", "method", "minprocsperpart", "ngridq", "polar", "reduceq", "sumrule", 
                            "write_schedule"] 
phonons_valid_subtrees = ["qpointset", "phonondos", "phonondispplot", "reformatdynmat", "interpolate", "parts"] 

phonondos_valid_attributes = ["inttype", "ngrdos", "ngridqint", "nsmdos", "ntemp", "nwdos"] 

phonondispplot_valid_subtrees = ["plot1d"] 
phonondispplot_mandatory_attributes = ["plot1d"] 

interpolate_valid_attributes = ["ngridq", "vqloff", "writeeigenvectors"] 
interpolate_mandatory_attributes = ["ngridq"] 


# properties information 
properties_valid_subtrees = ["spintext", "coreoverlap", "bandstructure", "stm", "wfplot", "dos", "LSJ", "masstensor", 
                             "chargedensityplot", "TSvdW", "DFTD2", "exccplot", "elfplot", "mvecfield", "xcmvecfield", 
                             "electricfield", "gradmvecfield", "fermisurfaceplot", "EFG", "mossbauer", "expiqr", 
                             "elnes", "eliashberg", "momentummatrix", "dielmat", "boltzequ", "raman", "moke", "shg", 
                             "wannier", "wannierplot", "wanniergap", "ldos", "polarization"] 

spintext_valid_attributes = ["bands"] 
spintext_valid_subtrees = ["plot2d"] 
spintext_mandatory_attributes = ["plot2d"] 

coreoverlap_valid_attributes = ["coreatom", "corespecies"] 

bandstructure_valid_attributes = ["character", "deriv", "scissor", "wannier"] 
bandstructure_valid_subtrees = ["plot1d"] 
bandstructure_mandatory_attributes = ["plot1d"] 

stm_valid_attributes = ["bias", "stmmode", "stmtype"] 
stm_valid_subtrees = ["plot2d", "region"] 

region_valid_attributes = ["grid2d", "grid3d", "height", "zrange"] 

wfplot_valid_attributes = ["version"] 
wfplot_valid_subtrees = ["kstlist", "plot1d", "plot2d", "plot3d"] 
wfplot_mandatory_attributes = ["kstlist"] 

dos_valid_attributes = ["inttype", "jdos", "linkpt", "lmirep", "lonly", "ngrdos", "ngridkint", "nsmdos", "nwdos", 
                        "scissor", "sqados", "wannier", "winddos"] 

LSJ_valid_subtrees = ["kstlist"] 

masstensor_valid_attributes = ["deltaem", "ndspem", "vklem"] 

chargedensityplot_valid_attributes = ["nocore"] 
chargedensityplot_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

exccplot_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

elfplot_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

mvecfield_valid_subtrees = ["plot2d", "plot3d"] 

xcmvecfield_valid_subtrees = ["plot2d", "plot3d"] 

electricfield_valid_subtrees = ["plot2d", "plot3d"] 

gradmvecfield_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

fermisurfaceplot_valid_attributes = ["nstfsp"] 
fermisurfaceplot_valid_subtrees = ["plot2d", "plot3d"] 

expiqr_valid_subtrees = ["kstlist"] 

elnes_valid_attributes = ["ngrid", "vecql", "wgrid", "wmax", "wmin"] 

eliashberg_valid_attributes = ["mustar"] 

momentummatrix_valid_attributes = ["fastpmat"] 

dielmat_valid_attributes = ["drude", "intraband", "scissor", "swidth", "tevout", "wgrid", "wmax"] 
dielmat_valid_subtrees = ["epscomp"] 
dielmat_multiple_children = ["epscomp"] 

boltzequ_valid_attributes = ["chemicalPotentialRange", "chemicalPotentialSpacing", "dopingConcentration", 
                             "energyReference", "evOutputEnergies", "siOutputUnits", "temperatureRange", 
                             "temperatureSpacing", "transportDfBroadening", "transportDfRange", "transportDfSpacing", 
                             "useDopingConcentration", "useTransportDf"] 
boltzequ_valid_subtrees = ["etCoeffComponents"] 
boltzequ_multiple_children = ["etCoeffComponents"] 

raman_valid_attributes = ["broad", "degree", "displ", "doequilibrium", "elaser", "elaserunit", "getphonon", "mode", 
                          "molecule", "ninter", "nstate", "nstep", "temp", "useforces", "usesym", "writefunc", "xmax", 
                          "xmin"] 
raman_valid_subtrees = ["eigvec", "energywindow"] 
raman_mandatory_attributes = ["energywindow"] 
raman_multiple_children = ["eigvec"] 

eigvec_valid_attributes = ["comp"] 
eigvec_mandatory_attributes = ["comp"] 

moke_valid_attributes = ["drude", "intraband", "scissor", "swidth", "tevout", "wgrid", "wmax"] 

shg_valid_attributes = ["etol", "scissor", "swidth", "tevout", "wgrid", "wmax"] 
shg_valid_subtrees = ["chicomp"] 
shg_mandatory_attributes = ["chicomp"] 
shg_multiple_children = ["chicomp"] 

wannier_valid_attributes = ["cutshell", "do", "fermizero", "input", "mindist", "minshell", "nbzshell", "printproj"] 
wannier_valid_subtrees = ["projection", "group"] 
wannier_multiple_children = ["group"] 

projection_valid_attributes = ["dordmax", "epsld", "nprojtot", "nunocc"] 

group_valid_attributes = ["epsdis", "epsmax", "epsopf", "epsproj", "fst", "innerwindow", "lst", "maxitdis", "maxitmax", 
                          "maxitopf", "memlendis", "memlenmax", "memlenopf", "method", "minitdis", "minitmax", 
                          "minitopf", "minstepdis", "minstepmax", "minstepopf", "neighcells", "nproj", "nwf", "nwrite", 
                          "optim", "outerwindow", "writeconv"] 
group_valid_subtrees = ["projector"] 
group_multiple_children = ["projector"] 

projector_valid_attributes = ["nr"] 
projector_mandatory_attributes = ["nr"] 

wannierplot_valid_attributes = ["cell", "fst", "lst"] 
wannierplot_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

wanniergap_valid_attributes = ["auto", "ngridkint"] 
wanniergap_valid_subtrees = ["pointband"] 
wanniergap_multiple_children = ["pointband"] 

pointband_valid_attributes = ["band", "extremal", "vkl"] 
pointband_mandatory_attributes = ["band", "vkl"] 

ldos_valid_attributes = ["delta", "grid", "newint", "ngrdos", "nsmdos", "nwdos", "scissor", "tol", "winddos"] 


# xs information 
xs_valid_attributes = ["bfieldc", "broad", "dbglev", "dfoffdiag", "dogroundstate", "emattype", "emaxdf", "epsdfde", 
                       "fastpmat", "gqmax", "gqmaxtype", "h5fname", "h5gname", "lmaxapwwf", "lmaxemat", "maxscl", 
                       "nempty", "ngridk", "ngridq", "nosym", "pwmat", "reducek", "reduceq", "rgkmax", "scissor", 
                       "skipgnd", "swidth", "tappinfo", "tevout", "vkloff", "writexsgrids", "xstype"] 
xs_valid_subtrees = ["storeexcitons", "pwelements", "writeexcitons", "writekpathweights", "excitonPlot", 
                     "realTimeTDDFT", "tddft", "screening", "phonon_screening", "expand_eps", "BSE", "fastBSE", 
                     "transitions", "qpointset", "tetra", "energywindow", "plan"] 
xs_mandatory_attributes = ["xstype"] 

storeexcitons_valid_attributes = ["MaxEnergyExcitons", "MaxNumberExcitons", "MinEnergyExcitons", "MinNumberExcitons", 
                                  "selectenergy", "useev"] 

pwelements_valid_attributes = ["band_combinations"] 
pwelements_mandatory_attributes = ["band_combinations"] 

writeexcitons_valid_attributes = ["MaxEnergyExcitons", "MaxNumberExcitons", "MinEnergyExcitons", "MinNumberExcitons", 
                                  "abscutares", "abscutres", "selectenergy", "useev"] 

writekpathweights_valid_attributes = ["MaxEnergyExcitons", "MaxNumberExcitons", "MinEnergyExcitons", 
                                      "MinNumberExcitons", "intorder", "printgridweights", "selectenergy", "useev"] 

excitonPlot_valid_attributes = ["epstol"] 
excitonPlot_valid_subtrees = ["exciton", "hole", "electron"] 
excitonPlot_mandatory_attributes = ["electron", "hole"] 
excitonPlot_multiple_children = ["exciton"] 

exciton_valid_attributes = ["fix", "lambda"] 

hole_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

electron_valid_subtrees = ["plot1d", "plot2d", "plot3d"] 

realTimeTDDFT_valid_attributes = ["TaylorOrder", "calcNonlocalCurrentDensity", "calculateNExcitedElectrons", 
                                  "calculateTotalEnergy", "endTime", "normalizeWF", "printAfterIterations", 
                                  "printTimingDetailed", "printTimingGeneral", "propagator", "subtractJ0", "timeStep", 
                                  "vectorPotentialSolver"] 
realTimeTDDFT_valid_subtrees = ["predictorCorrector", "screenshots", "laser", "pmat"] 
realTimeTDDFT_mandatory_attributes = ["pmat"] 

predictorCorrector_valid_attributes = ["maxIterations", "tol"] 

screenshots_valid_attributes = ["niter"] 
screenshots_valid_subtrees = ["eigenvalues", "projectionCoefficients", "occupations"] 

eigenvalues_valid_attributes = ["nEigenvalues", "tolerance"] 

projectionCoefficients_valid_attributes = ["format", "printAbsoluteValue"] 

occupations_valid_attributes = ["format"] 

laser_valid_attributes = ["fieldType"] 
laser_valid_subtrees = ["kick", "trapCos", "sinSq"] 
laser_multiple_children = ["kick", "sinSq", "trapCos"] 

kick_valid_attributes = ["amplitude", "direction", "t0", "width"] 

trapCos_valid_attributes = ["amplitude", "direction", "omega", "phase", "riseTime", "t0", "width"] 

sinSq_valid_attributes = ["amplitude", "direction", "omega", "phase", "pulseLength", "t0"] 

pmat_valid_attributes = ["forceHermitian", "readFromFile", "writeToFile"] 

tddft_valid_attributes = ["acont", "ahc", "alphalrc", "alphalrcdyn", "aresdf", "aresfxc", "betalrcdyn", "do", "drude", 
                          "fxcbsesplit", "fxctype", "intraband", "kerndiag", "lindhard", "lmaxalda", "mdfqtype", 
                          "nwacont", "torddf", "tordfxc"] 

screening_valid_attributes = ["do", "intraband", "nempty", "ngridk", "ngridq_interpolation", "nosym", "nqpt_unique", 
                              "qpointsgamma", "quasiparticle_correction", "reducek", "rgkmax", "screentype", "tr", 
                              "vkloff"] 

phonon_screening_valid_attributes = ["alat_qe", "excitation_energy", "file_type", "phonon_file", "zstar_file"] 
phonon_screening_mandatory_attributes = ["alat_qe", "excitation_energy", "phonon_file", "zstar_file"] 

expand_eps_valid_attributes = ["supercell_1", "supercell_2"] 

BSE_valid_attributes = ["aresbse", "blocks", "brixshdf5", "bsedirsing", "bsetype", "checkposdef", "chibar0", 
                        "chibar0comp", "chibarq", "coupling", "cuttype", "dichroism", "distribute", "econv", "eecs", 
                        "efind", "fbzq", "iqmtrange", "lmaxdielt", "measure", "nexc", "ngridksub", "nleblaik", "nosym", 
                        "nosymspec", "nstlbse", "nstlxas", "outputlevel", "readstatetask446", "reducek", "rgkmax", 
                        "sciavbd", "sciavqbd", "sciavqhd", "sciavqwg", "sciavtype", "scrherm", "solver", "vkloff", 
                        "xas", "xasatom", "xasedge", "xasspecies", "xes"] 

fastBSE_valid_attributes = ["clanczos", "cvtsteplim", "cvttol", "ngridr", "nisdf", "nlanczos", "saveQ", "seed"] 

transitions_valid_subtrees = ["individual", "ranges", "lists"] 

individual_valid_subtrees = ["trans"] 
individual_multiple_children = ["trans"] 

trans_valid_attributes = ["action", "final", "initial", "kpointnumber"] 

ranges_valid_subtrees = ["range"] 
ranges_multiple_children = ["range"] 

range_valid_attributes = ["action", "kpointnumber", "start", "statestype", "stop"] 
range_mandatory_attributes = ["statestype"] 

lists_valid_subtrees = ["istate"] 
lists_multiple_children = ["istate"] 

istate_valid_attributes = ["action", "kpointnumber", "state", "statestype"] 
istate_mandatory_attributes = ["statestype"] 

tetra_valid_attributes = ["cw1k", "kordexc", "qweights", "tetradf", "tetraocc"] 

plan_valid_subtrees = ["doonly"] 
plan_multiple_children = ["doonly"] 

doonly_valid_attributes = ["task"] 
doonly_mandatory_attributes = ["task"] 


# gw information 
gw_valid_attributes = ["at1", "at2", "coreflag", "debug", "degeneracyAbsoluteTolerance", "degeneracyRelativeTolerance", 
                       "enforceDegeneracy", "eph", "ibgw", "ibmax", "ibmax2", "ibmin", "ibmin2", "igmax", "igmin", 
                       "iik", "jjk", "mblksiz", "nbgw", "nempty", "ngridq", "printSelfC", "printSpectralFunction", 
                       "qdepw", "reduceq", "rmax", "rpath", "rpmat", "skipgnd", "taskname", "vqloff", "wlo", "wto"] 
gw_valid_subtrees = ["plot1d", "freqgrid", "selfenergy", "mixbasis", "barecoul", "scrcoul", "taskGroup"] 

freqgrid_valid_attributes = ["eta", "fconv", "fgrid", "freqmax", "freqmin", "nomeg"] 

selfenergy_valid_attributes = ["actype", "eqpsolver", "eshift", "method", "nempty", "singularity", "swidth", "tol"] 
selfenergy_valid_subtrees = ["wgrid"] 

wgrid_valid_attributes = ["size", "type", "wmax", "wmin"] 

mixbasis_valid_attributes = ["epsmb", "gmb", "lmaxmb"] 

barecoul_valid_attributes = ["barcevtol", "basis", "cutofftype", "pwm", "stctol"] 

scrcoul_valid_attributes = ["averaging", "omegap", "q0eps", "scrtype", "subgrid_q0"] 

taskGroup_valid_attributes = ["outputFormat"] 
taskGroup_valid_subtrees = ["Coulomb", "epsilon", "invertEpsilon", "sigmac", "sigmax", "vxc"] 

Coulomb_valid_subtrees = ["qpoints"] 
Coulomb_mandatory_attributes = ["qpoints"] 
Coulomb_multiple_children = ["qpoints"] 

epsilon_valid_attributes = ["printPolarizabilityFactor"] 
epsilon_valid_subtrees = ["qpoints"] 
epsilon_mandatory_attributes = ["qpoints"] 
epsilon_multiple_children = ["qpoints"] 

invertEpsilon_valid_subtrees = ["qpoints"] 
invertEpsilon_mandatory_attributes = ["qpoints"] 
invertEpsilon_multiple_children = ["qpoints"] 

sigmac_valid_subtrees = ["kpoints"] 
sigmac_mandatory_attributes = ["kpoints"] 
sigmac_multiple_children = ["kpoints"] 

sigmax_valid_subtrees = ["kpoints"] 
sigmax_mandatory_attributes = ["kpoints"] 
sigmax_multiple_children = ["kpoints"] 

vxc_valid_subtrees = ["kpoints"] 
vxc_mandatory_attributes = ["kpoints"] 
vxc_multiple_children = ["kpoints"] 


# MD information 
MD_valid_attributes = ["basisDerivative", "coreCorrections", "integrationAlgorithm", "printAllForces", "timeStep", 
                       "type", "updateOverlap", "updatePmat", "valenceCorrections"] 


# eph information 
eph_valid_attributes = ["debugeph", "ibeph", "ibsumeph", "nbeph", "nbsumeph", "nemptyeph", "ngridqeph", "tasknameeph", 
                        "vqloffeph"] 
eph_valid_subtrees = ["freqgrideph", "selfenergyeph"] 

freqgrideph_valid_attributes = ["freqmaxeph", "nomegeph"] 

selfenergyeph_valid_subtrees = ["SpectralFunctionPloteph"] 

SpectralFunctionPloteph_valid_attributes = ["axis", "eta", "nwgrid", "wmax", "wmin"] 


# valid entries for the xs subtree 'plan'
valid_plan_entries = ["bse", "bsegenspec", "bsesurvey", "df", "df2", "dielectric", "emattest", "exccoulint", 
                      "excitonWavefunction", "expand_add_eps", "fastBSE_groundstate_properties", 
                      "fastBSE_human_readable_output", "fastBSE_isdf_cvt", "fastBSE_main", "fxc_alda_check", "idf", 
                      "kernxc_bse", "kernxc_bse3", "phonon_screening", "planewave_elements", "pmatxs2orig", 
                      "portstate(-1)", "portstate(-2)", "portstate(1)", "portstate(2)", "scrcoulint", "screen", 
                      "scrgeneigvec", "scrtetcalccw", "scrwritepmat", "testmain", "testxs", "tetcalccw", 
                      "write_dielectric_matrix", "write_pmat_hdf5_xs", "write_screen", "write_screened_coulomb", 
                      "writebandgapgrid", "writebevec", "writeemat", "writeematasc", "writekpathweights", 
                      "writeoverlapxs", "writepmat", "writepmatasc", "writepmatxs", "writepwmat", "x0toasc", "x0tobin", 
                      "xsestimate", "xsgeneigvec"] 
