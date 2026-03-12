import tkinter as tk
try:
    import matplotlib as mtpl
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    import matplotlib.patches as patches
except ImportError:
    print("Matplotlib not installed.\nRun:")
    print("pip install matplotlib")
    exit(1)  # exit dans la class ?
from data_models import Graph, Connection, Hub


class Simulation:
    def __init__(self, graph: Graph):
        self.connections: dict[str, Connection] = graph.connections
        self.start_name: str = ''
        self.end_name: str = ''
        self.hubs: dict[str, Hub] = graph.hubs
        self.drones_state: list[list[dict[str, str]]] = []
        self.fig = Figure(figsize=(6, 6))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_aspect('equal')  # Pour que les ronds restent des ronds

    def crer_fenetre():
        # 1. Créer la fenêtre principale
        app = tk.Tk()
        app.title("Fly-in Simulation")
        app.geometry("300x200")  # Taille optionnelle

        # 2. Ajouter un widget (Label) - gère les textes et images
        label = tk.Label(app, text="Bonjour le monde !")
        label.pack(pady=50)  # Placement du widget

    def draw_map(self) -> None:
        self.ax.clear()
        for hub_name, hub in self.hubs.items():
            x, y = hub.coord
            match hub.zone_type:
                case 'normal':
                    marker_style = 'o'
                case 'restricted':
                    marker_style = '^'
                case 'priority':
                    marker_style = 's'
                case 'blocked':
                    marker_style = 'X'
            self.ax.plot(x, y, marker=marker_style, markersize=50,
                         color=hub.color, linestyle='None')
            self.ax.text(x, y, hub_name, fontsize=8, ha='center')

        x_max = max(self.hubs.values(), key=lambda h: h.coord[0])
        y_max = max(self.hubs.values(), key=lambda h: h.coord[1])
        x_min = min(self.hubs.values(), key=lambda h: h.coord[0])
        y_min = min(self.hubs.values(), key=lambda h: h.coord[1])
        self.ax.set_xlim(x_min.coord[0]-0.5, x_max.coord[0] + 0.5)
        self.ax.set_ylim(y_min.coord[1]-0.5, y_max.coord[1] + 0.5)

    def lancer_interface(self):
        root = tk.Tk()
        root.title("Fly-in Simulation")

        # --- Intégration de Matplotlib dans Tkinter ---
        self.draw_map()  # On prépare le dessin
        canvas = FigureCanvasTkAgg(self.fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        root.mainloop()

    def main(self) -> None:
        self.lancer_interface()


if __name__ == "__main__":
    """ xpoints = (0, 6)
    ypoints = (0, 250) """
    """ ypoints = np.array([0, 250])

    plt.plot(0, 0, marker='o', ms=20, mec='r', mfc='r')
    plt.plot(0, 250, 'x')
    plt.plot(ypoints)
    plt.show() """
