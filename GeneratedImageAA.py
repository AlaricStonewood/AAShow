import numpy as np
import matplotlib.pyplot as plt

N = 450
x = np.arange(N) / N - 0.5
y = np.arange(N) / N - 0.5
aa = np.ones((N, N))
aa[::2, :] = -1

X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
f0 = 5
k = 100
a = np.sin(np.pi * 2 * (f0 * R + k * R**2 / 2))
# make the left hand side of this
a[:int(N / 2), :][R[:int(N / 2), :] < 0.4] = -1
a[:int(N / 2), :][R[:int(N / 2), :] < 0.3] = 1
aa[:, int(N / 3):] = a[:, int(N / 3):]
a = aa

fig, ax = plt.subplots(figsize=(16, 9))
ax.imshow(a, interpolation='nearest', cmap='RdBu_r')
plt.savefig(f'no_AA.png')
plt.show()

i = 0

fig, axs = plt.subplots(2, 2, figsize=(16, 9), constrained_layout=True)
axs[0, 0].imshow(a, interpolation='nearest', cmap='RdBu_r')
axs[0, 0].set_xlim(100, 200)
axs[0, 0].set_ylim(275, 175)
axs[0, 0].set_title('Zoom')

for ax, interp, space in zip(axs.flat[1:],
                             ['nearest', 'antialiased', 'antialiased'],
                             ['data', 'data', 'rgba']):
    ax.imshow(a, interpolation=interp, interpolation_stage=space,
              cmap='RdBu_r')
    ax.set_title(f"interpolation='{interp}'\nspace='{space}'")
    plt.savefig(f'interp{i}.png')
    i += 1
plt.show()

fig, ax = plt.subplots(figsize=(16, 9))
ax.imshow(a, interpolation='nearest', interpolation_stage='rgba', cmap='RdBu_r')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.savefig(f'nearest.png')
plt.show()

fig, ax = plt.subplots(figsize=(16, 9))
ax.imshow(a, interpolation='antialiased', interpolation_stage='rgba',  cmap='RdBu_r')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.savefig(f'aa.png')
plt.show()

fig, ax = plt.subplots(figsize=(16, 9))
ax.imshow(a, interpolation='nearest', interpolation_stage='rgba', cmap='RdBu_r')
ax.set_xlim(100, 200)
ax.set_ylim(275, 175)
ax.set_title('Zoom - No AA')
plt.savefig(f'zoom_no_aa.png')
plt.show()

fig, ax = plt.subplots(figsize=(16, 9))
ax.imshow(a, interpolation='antialiased', interpolation_stage='rgba',  cmap='RdBu_r')
ax.set_xlim(100, 200)
ax.set_ylim(275, 175)
ax.set_title('Zoom - AA')
plt.savefig(f'zoom_aa.png')
plt.show()

i = 0
fig, axs = plt.subplots(1, 2, figsize=(16, 9), constrained_layout=True)
for ax, interp in zip(axs, ['hanning', 'lanczos']):
    ax.imshow(a, interpolation=interp, cmap='RdBu_r')
    ax.set_title(f"interpolation='{interp}'")
    plt.savefig(f'interp{i}.png')
    i += 1
plt.show()
