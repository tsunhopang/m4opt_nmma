# m4opt_nmma

This repository contains the files and scripts required for conducting the projection studies after the study in [Singer et al.](https://arxiv.org/abs/2502.17560).

## Content structure
### Injection creation `create_injection/`
Given the binary source parameter table `events.ecsv` at https://zenodo.org/records/14825979, using the priors on additional parameters, the full kilonova injection parameters are created, as in `data_BNS.json` and `data_NSBH.json`.

See `run.sh` for the exact command used.

### Kilonova detectability `calculate_peak_brightness/`
To estimate the detectability of the kilonova, we first calculate the peak brightness for each of the simulated kilonova signals.

- `sanity_check/` to compare the light curve estimated with the light curve shown in Fig. 8 of [Hotokezaka et al.](https://iopscience.iop.org/article/10.3847/1538-4357/ab6a98/pdf)
- `run.sh` Script to i) generate the lightcurves and ii) make a diagnosis histogram

### Parameter estimation `injection_analysis/`
The `run.sh` conducts a parameter estimation condition on the depth of the search. The parameters of interest are
- `prior`: Prior file used for this analysis
- `photometric-error-budget`: Statistical uncertainty for the simulated event
- `dt-inj`: Spacing between subsequent simulated observations in days
- `error-budget`: Underlying systematic uncertainty. Since we are using the same model for both injection and recovery, this can be set to a very small number, but DO NOT set it to zero.
- `sampler`: Sampler used for the analysis. Pymultinest is faster but might be harder to install on older systems.
- `nlive`: Number of live points, should use at least 1024 points.
- `ra, dec`: True sky location of the event in degrees.
- `injection-num`: `Simulation_id` as in the injection json file

Handy tools:
- `find_radec_point_of_depth.py`: Given a desired depth, find the location closest to it.
- `fits_map_vis.py`: Visualization of the depth skymap


### What is missing?
The actual connection between the detected kilonova and the associated parameter estimation requires the limiting magnitude calculated for all of the skymap, as in https://github.com/m4opt/m4opt/pull/309. Moreover, the indexing of the fits file, true sky location, and the run script depend on the job scheduler that it will be running with.
