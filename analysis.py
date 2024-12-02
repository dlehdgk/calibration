import os

import getdist
import matplotlib.pyplot as plt
import numpy as np
from getdist import plots

# specify chain file root
# chain_root = "./spt-tau-chains/lcdm_comp"
# chain_root = "./act-tau-chains/lcdm"
chain_root = "./act-wmap-chains/lcdm"

# directory and base name
chain_dir = os.path.dirname(chain_root)
chain_base = os.path.basename(chain_root)

# outputs directory
outputs_dir = os.path.join(chain_dir, "outputs")
os.makedirs(outputs_dir, exist_ok=True)

# load MCMC chains
samples = getdist.loadMCSamples(chain_root, settings={"ignore_rows": 0.3})

# adding Ase2tau derived parameter

# Extract parameter arrays
# As = samples.getParams().As
# tau = samples.getParams().tau

# Calculate the derived parameter: 1e9 * As * exp(-2 * tau)
# derived_param = 1e9 * As * np.exp(-2 * tau)

# Add the derived parameter to the samples
# samples.addDerived(derived_param, name="Ase2tau", label="10^9 A_s e^{-2\\tau}")

# list interested parameters
# spt_tau
# params = ["H0", "ombh2", "omch2", "theta_MC_100", "Ase2tau", "ns"]

# act_tau
params = ["H0", "ombh2", "omch2", "theta_MC_100", "tau", "ns", "logA"]

# act desi pantheon for w0waCDM model
# params = ["omch2", "ombh2", "theta_MC_100", "tau", "ns", "logA", "w", "wa"]
# printing R-1 value
print("R-1 =", samples.getGelmanRubin())

param_latex = {param: samples.getInlineLatex(param, 1) for param in params}
for param in params:
    print(param_latex[param])

# triangle plot
g = getdist.plots.get_subplot_plotter(width_inch=8)
g.triangle_plot(samples, params, filled=True)
fig_path = os.path.join(outputs_dir, chain_base + "_triangle.png")
plt.savefig(fig_path, dpi=300)
print(f"triangle plot saved at {fig_path}")

# Write marginalized parameters with uncertainties to a file
params_path = os.path.join(outputs_dir, chain_base + "_parameters.txt")
with open(params_path, "w") as f:
    f.write("R-1 = {:.5f}\n".format(samples.getGelmanRubin()))
    f.write("\nMarginalized parameters with uncertainties:\n")
    for param in params:
        f.write("{} = {}\n".format(param, param_latex[param]))
print(f"parameters saved at {params_path}")
