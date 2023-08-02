import matplotlib.pyplot as plt
import numpy as np

from DiffractiX import Simulation


def dipole():
    omega = 2*np.pi*200e12
    dl = 0.02 # grid size (units of L0, which defaults to 1e-6)
    eps_r = np.ones((200, 200)) # relative permittivity
    NPML = [15, 15] # number of pml grid points on x and y borders

    simulation = Simulation(omega, eps_r, dl, NPML, 'Ez')
    simulation.src[100, 100] = 1
    simulation.solve_fields()

    fig1 = simulation.plt_abs(outline=False, cbar=True)
    fig2 = simulation.plt_re(outline=False, cbar=True)

    return fig1, fig2

def ridge_waveguide():
    omega = 2 * np.pi * 200e12
    dl = 0.01  # grid size (units of L0, which defaults to 1e-6)
    eps_r = np.ones((600, 200))  # relative permittivity
    eps_r[:, 90:110] = 12.25  # set waveguide region
    NPML = [15, 15]  # number of pml grid points on x and y borders

    simulation = Simulation(omega, eps_r, dl, NPML, 'Ez')
    simulation.add_mode(3.5, 'x', [20, 100], 60, scale=10)
    simulation.setup_modes()
    simulation.solve_fields()
    print('input power of {} in W/L0'.format(simulation.W_in))

    fig1 = simulation.plt_re(outline=True, cbar=False)
    fig2 = simulation.plt_abs(outline=True, cbar=False)

    return fig1, fig2


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    ridge_waveguide()
    plt.show()
