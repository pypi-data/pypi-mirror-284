import ghog
import os
import numpy as np
import matplotlib.pyplot as plt

# Load
file = "./20240621T222828_groundhog0084.h5"
data = ghog.load(file)

plt.figure()
pclip = 10
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.title("Raw")


# Fast time filter
data = ghog.filt(data, (0.5e6, 4e6), axis=0)

plt.figure()
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.title("FT Filtered")

# NMO
data = ghog.nmo(data, 100)

plt.figure()
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.title("NMO correction")

# Restack
data = ghog.restack(data, 5)

plt.figure()
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.title("Restack")

# Slow time filter
data = ghog.filt(data, (1/1000, 1/50), axis=1)

plt.figure()
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.title("ST Filtered")


# Migrate
data = ghog.stolt(data)

plt.figure()
pclip = 10
plt.imshow(data["rx"], aspect="auto", vmin=np.percentile(data["rx"], pclip), vmax=np.percentile(data["rx"], 100-pclip))
plt.title("Migrated")

plt.show()

# Save
tmpfile = "./ghog84_tmp.h5"
if(os.path.isfile(tmpfile)):
    os.unlink(tmpfile)
#os.system("cp %s %s" % (file, tmpfile))
ghog.save(tmpfile, data)
