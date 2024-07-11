import ghog
import os
import numpy as np
import matplotlib.pyplot as plt

# Load
file = "./20240621T222828_groundhog0084.h5"
data = ghog.load(file)

# Fast time filter
data = ghog.filt(data, (0.5e6, 4e6), axis=0)

# NMO
data = ghog.nmo(data, 100)

# Restack
data = ghog.restack(data, 5)

# Slow time filter (wavenumber)
data = ghog.filt(data, (1/1000, 1/200), axis=1)

# Migrate
data = ghog.stolt(data, ntaper=16)

plt.figure()
pclip=20
gain = np.arange(data["rx"].shape[0])**3
data["rx"] = data["rx"]*gain[:, np.newaxis]
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.show()

# Save
ghog.save(file, data, group="restack")
