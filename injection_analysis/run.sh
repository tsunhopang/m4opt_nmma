# for the given test.fits.gz
# the testing sky locations are
# ra = 217.64423076923077, dec = 51.25580694880489, limit_mag = 26.3788730071021
# ra = 211.54205607476635, dec = 50.091456801832585, limit_mag = 24.96083280769723
# simulation id 5282 has a peak brigtness of 22.67 in FUV band

mpiexec -np 4 lightcurve-analysis \
  --model HoNa2020 \
  --label m4opt_test \
  --prior ./KN.prior \
  --tmin 0.5 \
  --tmax 10.0 \
  --dt 0.1 \
  --dt-inj 1.0 \
  --filters FUV,NUV \
  --photometric-error-budget 0.1 \
  --error-budget 0.01 \
  --soft-init \
  --sampler ultranest \
  --nlive 512 \
  --seed 42 \
  --injection ../create_injection/data_BNS.json\
  --injection-num 5282 \
  --plot \
  --local-only \
  --detection-limit-fits-file ./test.fits.gz \
  --ra 217.644\
  --dec 51.236\
  --outdir outdir/ \
  --ylim 28,21 \
  --xlim 0.5,10 \
