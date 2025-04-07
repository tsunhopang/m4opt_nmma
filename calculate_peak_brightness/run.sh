lightcurve-generation \
  --model HoNa2020 \
  --injection ../create_injection/data_BNS.json \
  --tmin 0.5 \
  --tmax 10.0 \
  --dt 0.1 \
  --filters FUV,NUV \
  --outdir ./outdir_bns/ \
  --label lc \

lightcurve-generation \
  --model HoNa2020 \
  --injection ../create_injection/data_NSBH.json \
  --tmin 0.5 \
  --tmax 10.0 \
  --dt 0.1 \
  --filters FUV,NUV \
  --outdir ./outdir_nsbh/ \
  --label lc \

python peak_brightness_dist.py bns 30
python peak_brightness_dist.py nsbh 10
