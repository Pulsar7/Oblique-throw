"""
Author: Benedikt Fichtner
Python-Version: 3.8.10
The oblique throw - Simulation / Without air resistance 
"""
import sys,math,argparse,numpy as np
import matplotlib.pyplot as plt
from rich import (pretty,console as cons)
from rich.table import Table
from sympy import (symbols,Eq,solve)


class Simulation():
    def __init__(self,console,v_zero:float,g:float,h:float,alpha:float) -> None:
        (self.console,self.v_zero,self.g,self.h,self.alpha) = (console,v_zero,g,h,alpha)

    def simulate(self) -> None:
        (fig, ax) = plt.subplots(2, 2, constrained_layout=True)
        fig.suptitle("The oblique throw - Simulation / Without air resistance")
        fig.set_figwidth(13)
        fig.set_figheight(7)
        (h,g,alpha,v_0) = (self.h,self.g,self.alpha,self.v_zero)

        (x,t) = symbols('x,t')
        eq1 = Eq((((-1/2) * (g/((v_0*math.cos(alpha))**2)) * (x**2)+math.tan(alpha)*x+h)), 0)
        eq2 = Eq(((-1/2) * g * (t**2) + v_0 * math.sin(alpha) * t + h),0)
        solutions = solve((eq1),(x))
        solutions_2 = solve(eq2,(t))
        table = Table(title="The oblique throw - Simulation / Without air resistance")
        table.add_column("Description", justify="left", style="blue", no_wrap=True)
        table.add_column("Information", style="green")
        table.add_row("Gravitational acceleration in m/s²",f"{g} m/s²")
        table.add_row("The initial velocity in m/s",f"{v_0} m/s")
        table.add_row("Initial height in meters",f"{h} m")
        table.add_row("Dropping angle alpha in deg",f"{alpha}°")
        table.add_section()
        table.add_row("zero point: y(x) = 0",f"{solutions[1]} meters")
        table.add_row("zero point: y(t) = 0",f"{solutions_2[1]} seconds")
        self.console.print(table)

        ### y(x)
        x_coordinates:list[float] = []
        y_coordinates:list[float] = []
        coordinates = np.linspace(0,100,100)
        for x in coordinates:
            y:float = ((-1/2) * (g/((v_0*math.cos(alpha))**2)) * (x**2)+math.tan(alpha)*x+h)
            if y < 0:
                break
            else:
                x_coordinates.append(x)
                y_coordinates.append(y)
        ax[0][0].stem(x_coordinates, y_coordinates,linefmt ='grey', markerfmt ='D')
        ax[0][0].plot(x_coordinates, y_coordinates,label = "trajectory "+r'$y(x)$',
            linewidth = 1.5, color = "black", linestyle = "-"
        )
        ax[0][0].fill_between(x_coordinates, y_coordinates, alpha=0.1,color="black")
        ax[0][0].set_xlabel("Distance x (meters)")
        ax[0][0].set_ylabel("Height y (meters)")
        ax[0][0].legend(loc='best')
        ax[0][0].set_yticks(np.arange(0, max(y_coordinates)+5,5))
        ax[0][0].set_xticks(np.arange(0, len(x_coordinates)+1, 1))
        ax[0][0].set_ylim(ymin=0)
        ax[0][0].set_xlim(xmin=0)
        ax[0][0].set_title(r"$y(x)$")
        ax[0][0].grid(True)

        ### y(t)
        t_coordinates:list[float] = []
        y_coordinates:list[float] = []
        times = np.linspace(0,100,500)
        for t in times:
            y:float = ((-1/2) * g * (t**2) + v_0 * math.sin(alpha) * t + h)
            t_coordinates.append(t)
            y_coordinates.append(y)
            if y < 0:
                break
        ax[0][1].plot(t_coordinates, y_coordinates, linewidth = 1.5, linestyle = "-", color = "royalblue", marker = "x",
            label = "trajectory "+r'$y(t)$'
        )
        ax[0][1].set_xlabel("Time t (seconds)")
        ax[0][1].set_ylabel("Height y (meters)")
        ax[0][1].legend(loc='best')
        ax[0][1].set_yticks(np.arange(0, max(y_coordinates)+5,5))
        ax[0][1].set_xticks(np.arange(0, max(t_coordinates), 1))
        ax[0][1].set_ylim(ymin=0)
        ax[0][1].set_xlim(xmin=0)
        ax[0][1].set_title(r"$y(t)$")
        ax[0][1].grid(True)

        ### x(t)
        t_coordinates:list[float] = t_coordinates # from ax[0][1]
        x_coordinates:list[float] = [(v_0*math.cos(alpha)*t) for t in t_coordinates]
        ax[1][0].plot(t_coordinates, x_coordinates, linewidth = 1.5, linestyle = "-", color = "royalblue",
            label = "steady motion "+r'$x(t)$'
        )
        ax[1][0].set_xlabel("Time t (seconds)")
        ax[1][0].set_ylabel("Distance x (meters)")
        ax[1][0].legend(loc='best')
        ax[1][0].set_yticks(np.arange(0, max(x_coordinates)+5,5))
        ax[1][0].set_xticks(np.arange(0, max(t_coordinates)+1, 1))
        ax[1][0].set_ylim(ymin=0)
        ax[1][0].set_xlim(xmin=0)
        ax[1][0].set_title(r"$x(t)$")
        ax[1][0].grid(True)
        
        ### v_y(t)
        t_coordinates:list[float] = t_coordinates # from ax[0][1]
        v_coordinates:list[float] = [(-g * t + v_0 * np.sin(alpha)) for t in t_coordinates]
        ax[1][1].plot(t_coordinates, v_coordinates, linewidth = 1.5, linestyle = "-", color = "royalblue",
            label = "Uniformly accelerates "+r'$v_y (t)$'
        )
        ax[1][1].plot(t_coordinates, [0 for t in t_coordinates], linewidth = 2, linestyle = "-", color = "red",
            label = r"$v_y (t) = 0$"
        )
        ax[1][1].set_xlabel("Time t (seconds)")
        ax[1][1].set_ylabel("Acceleration v ("+r'$\frac{m}{s}$'+")")
        ax[1][1].legend(loc='best')
        ax[1][1].set_yticks(np.arange(min(v_coordinates),max(v_coordinates)+5,1))
        ax[1][1].set_xticks(np.arange(0, max(t_coordinates), 1))
        ax[1][1].set_ylim(ymin=min(v_coordinates)-2)
        ax[1][1].set_xlim(xmin=0)
        ax[1][1].set_title(r'$v_y (t)$')
        ax[1][1].grid(True)
        
        plt.show()

#
pretty.install()
console = cons.Console()

default_initial_velocity:float = 10.0 # m/s
default_g_acceleration:float = 9.81 # m/s²
default_initial_height:float = 20.0 # m
#
parser = argparse.ArgumentParser("The oblique throw - Simulation")
parser.add_argument('-i','--initial_velocity',
    help=f"The initial velocity in m/s (default = {default_initial_velocity} m/s²",
    type = float, default = default_initial_velocity
)
parser.add_argument('-a','--alpha',help="Dropping angle alpha in deg",type = float)
parser.add_argument('-g','--g_acceleration',    
    help=f"Gravitational acceleration in m/s (default = {default_g_acceleration} m/s", type = float,
    default = default_g_acceleration
)
parser.add_argument('-y','--initial_height',help=f"Initial height in m (default = {default_initial_height} m)",
    type = float, default = default_initial_height
)
args = parser.parse_args()

if args.alpha == None:
    parser.print_help()
    sys.exit()
#

if __name__ == '__main__':
    Simulation(console = console,g = args.g_acceleration, 
        v_zero = args.initial_velocity, h = args.initial_height,
        alpha = args.alpha
    ).simulate()
