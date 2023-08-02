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

    simulation.plt_abs(outline=False, cbar=True);
    simulation.plt_re(outline=False, cbar=True);

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    dipole()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
