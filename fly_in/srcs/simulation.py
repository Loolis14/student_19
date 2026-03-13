import tkinter as tk
from collections import Counter
try:
    import matplotlib as mtpl
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    from matplotlib.patches import ConnectionPatch
    import numpy as np
except ImportError:
    print("Matplotlib not installed.\nRun:")
    print("pip install matplotlib")
from data_models import Graph, Connection, Hub, Drone


class Simulation:
    def __init__(self, graph: Graph):
        self.connections: dict[str, Connection] = graph.connections
        self.drones: list[Drone] = [d for d in graph.drones.values()]
        self.start_name: str = ''
        self.end_name: str = ''
        self.hubs: dict[str, Hub] = graph.hubs
        self.connections_used: list = []

        self.turn_total: int = 0
        self.current_turn: int = 0
        self.turn_entry: int = 0
        self.drone_scatter = None
        self.drone__nbr_labels: list[int] = []
        self.is_playing = False
        self.after_id = None
        self.selection = None
        self.fig = Figure(figsize=(6, 6))
        self.root = None
        self.canvas: FigureCanvasTkAgg = None
        self.ax = self.fig.add_subplot(111)
        self.ax.set_aspect('equal')  # Pour que les ronds restent des ronds

    def _draw_map(self) -> None:
        for hub_id, hub in self.hubs.items():
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
                         color='white', alpha=1, zorder=2)
            self.ax.plot(x, y, marker=marker_style, markersize=50,
                         color=hub.color, alpha=0.7, zorder=3)
            self.ax.text(x, y - 0.40, hub_id, fontsize=8, ha='center')

        for co_id, co in self.connections.items():
            hub_a, hub_b = co.hubs
            x_coords = [hub_a.coord[0], hub_b.coord[0]]
            y_coords = [hub_a.coord[1], hub_b.coord[1]]
            if co not in self.connections_used:
                self.ax.plot(x_coords, y_coords, color='gray', alpha=0.7,
                             linestyle='-', linewidth=1, zorder=1)
            else:
                self.ax.plot(x_coords, y_coords, color='gray', alpha=0.9,
                             linestyle=':', linewidth=1, zorder=1)
                x = (hub_a.coord[0] + hub_b.coord[0]) / 2
                y = (hub_a.coord[1] + hub_b.coord[1]) / 2
                self.ax.text(x + 0.05, y + 0.05, co_id,
                             fontsize=8, ha='center')

        x_max = max(self.hubs.values(), key=lambda h: h.coord[0])
        y_max = max(self.hubs.values(), key=lambda h: h.coord[1])
        x_min = min(self.hubs.values(), key=lambda h: h.coord[0])
        y_min = min(self.hubs.values(), key=lambda h: h.coord[1])
        self.ax.set_xlim(x_min.coord[0]-0.5, x_max.coord[0] + 0.5)
        self.ax.set_ylim(y_min.coord[1]-0.5, y_max.coord[1] + 0.5)

    def _update_drones(self) -> None:
        """Update drones positions."""
        for txt in self.drone__nbr_labels:
            txt.remove()
        self.drone__nbr_labels.clear()

        x_s: list = []
        y_s: list = []
        for drone in self.drones:
            pos: str = drone.state[self.current_turn]
            if pos in self.hubs.keys():
                pos_obj_u: Hub = self.hubs[pos]
                x_s.append(pos_obj_u.coord[0])
                y_s.append(pos_obj_u.coord[1])
            else:
                pos_obj_c: Connection = self.connections[pos]
                hub_a, hub_b = pos_obj_c.hubs
                x = (hub_a.coord[0] + hub_b.coord[0]) / 2
                y = (hub_a.coord[1] + hub_b.coord[1]) / 2
                x_s.append(x)
                y_s.append(y)
        if not self.drone_scatter:
            self.drone_scatter = self.ax.scatter(x_s, y_s,
                                                 color='#413c54',
                                                 marker='o',
                                                 s=150,
                                                 zorder=5,
                                                 picker=2)
        else:
            self.drone_scatter.set_offsets(np.c_[x_s, y_s])
        positions = list(zip(x_s, y_s))
        count = Counter(positions)
        for (x, y), total in count.items():
            t = self.ax.text(x, y, str(total), color='white',
                             va='center', ha='center', zorder=6)
            self.drone__nbr_labels.append(t)
        self.ax.set_title(f"Turn: {self.current_turn}")
        self.canvas.draw_idle()

    def _remove_selection(self) -> None:
        if self.selection:
            self.selection.remove()
            self.selection = None
            self.info_label.config(
                text="Click on drones representation to see details",
                fg="#050505"
            )
            if self.canvas:
                self.canvas.draw_idle()

    def play_pause(self) -> None:
        self._remove_selection()
        if self.is_playing:
            self.is_playing = False
            if self.after_id:
                self.root.after_cancel(self.after_id)
        else:
            self.is_playing = True
            self._run_drones_animation()

    def _run_drones_animation(self) -> None:
        self._remove_selection()
        if self.is_playing and self.current_turn < self.turn_total:
            self._next_turn()
            self.after_id = self.root.after(500, self._run_drones_animation)

    def _prev_turn(self) -> None:
        self._remove_selection()
        if self.current_turn > 0:
            self.current_turn -= 1
            self._update_drones()

    def _next_turn(self) -> None:
        self._remove_selection()
        if self.current_turn < self.turn_total:
            self.current_turn += 1
            self._update_drones()

    def _reset_simulation(self) -> None:
        self._remove_selection()
        self.current_turn = 0
        self._update_drones()

    def _on_click(self, event) -> None:
        if not event.xdata or not event.ydata:
            return
        self._remove_selection()
        cont, ind = self.drone_scatter.contains(event)
        if cont:
            drones_i = ind['ind']
            drones: list[str] = []
            for i in drones_i:
                drones.append(self.drones[i].id)
            self.info_label.config(
                text=f"Drones on this position: {', '.join(drones)}",
                fg="#050505"
            )
            self.selection = self.ax.scatter(
                [event.xdata], [event.ydata],
                s=300,
                facecolors='none',
                edgecolors='red',
                linewidths=2,
                zorder=10
                )
        else:
            self.info_label.config(
                text="No drones here. "
                "Click on drones representation to see details",
                fg="#050505"
            )
        self.canvas.draw_idle()

    def _jump_to(self) -> None:
        value = self.turn_entry.get()
        if not value.isdigit():
            self.turn_entry.delete(0, tk.END)
        else:
            if int(value) > self.turn_total:
                self.turn_entry.delete(0, tk.END)
            else:
                self._remove_selection()
                self.current_turn = int(value)
                self._update_drones()

    def _interface_control(self):
        self.root.title("Fly-in Simulation")

        # Graphique part
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.fig.tight_layout()
        self._draw_map()
        self._update_drones()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Informations on click
        self.info_label = tk.Label(
            self.root,
            text='Click on drones representation to see details',
            fg="#000000"
            )
        self.info_label.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.fig.canvas.mpl_connect('button_press_event', self._on_click)

        # Toolbar
        toolbar = tk.Frame(self.root, bg="#c6c5cc")
        toolbar.pack(side=tk.TOP, pady=5)

        tk.Button(toolbar,
                  text="Previous",
                  command=self._prev_turn).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar,
                  text="▶ Play/Pause",
                  command=self.play_pause).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar,
                  text='Next',
                  command=self._next_turn).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar,
                  text="Reset",
                  command=self._reset_simulation).pack(side=tk.LEFT, padx=10)
        tk.Label(toolbar,
                 text='Jump on turn').pack(side=tk.LEFT, padx=10)
        self.turn_entry = tk.Entry(toolbar, width=5)
        self.turn_entry.insert(0, "0")
        self.turn_entry.pack(side=tk.LEFT, padx=2)
        self.turn_entry.bind('<Return>', lambda e: self._jump_to())
        tk.Label(toolbar,
                 text=f'(max {self.turn_total})').pack(side=tk.LEFT, padx=2)

        self.root.mainloop()

    def main(self) -> None:
        self.root = tk.Tk()
        self._interface_control()
