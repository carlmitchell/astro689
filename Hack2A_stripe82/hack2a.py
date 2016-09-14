from astroML.datasets import fetch_sdss_S82standards
import matplotlib.pyplot as plt

data_unmatched = fetch_sdss_S82standards()
g_u = data_unmatched['mmu_g']
r_u = data_unmatched['mmu_r']
i_u = data_unmatched['mmu_i']

data_matched = fetch_sdss_S82standards(crossmatch_2mass=True)
g_m = data_matched['mmu_g']
r_m = data_matched['mmu_r']
i_m = data_matched['mmu_i']

# Plot of the unmatched (all) stars
plt.figure(figsize=[16, 9])
plt.scatter(g_u-r_u, r_u-i_u, s=4, c='black')
plt.xlabel('g-r color')
plt.ylabel('r-i color')
plt.xlim(-2, 4)
plt.ylim(-2, 4)
plt.title('Non-crossmatched SDSS Data')
plt.savefig('unmatched.png')
plt.close()

# Plot of the matched stars
fig = plt.figure(figsize=[16, 9])
plt.scatter(g_m-r_m, r_m-i_m, s=4, c='black')
plt.xlabel('g-r color')
plt.ylabel('r-i color')
plt.xlim(-2, 4)
plt.ylim(-2, 4)
plt.title('SDSS crossmatched with 2MASS')
plt.savefig('matched.png')
plt.close()

# Overlay matched on unmatched
fig = plt.figure(figsize=[16, 9])
plt.scatter(g_u-r_u, r_u-i_u, s=4, c='black', label='unmatched')
plt.scatter(g_m-r_m, r_m-i_m, s=4, c='red', label='matched')
plt.xlabel('g-r color')
plt.ylabel('r-i color')
plt.legend(loc='best')
plt.savefig('both_overlay.png')
plt.close()

# Both side by side
fig, axs = plt.subplots(1, 2, sharey=True, sharex=True, figsize=[16, 9])
axs[0].scatter(g_u-r_u, r_u-i_u, s=4, c='black')
axs[1].scatter(g_m-r_m, r_m-i_m, s=4, c='black')
axs[0].set_xlabel('g-r color')
axs[1].set_xlabel('g-r color')
axs[0].set_ylabel('r-i color')
plt.subplots_adjust(wspace=0)
plt.savefig('both_sidebyside.png')
plt.close()
