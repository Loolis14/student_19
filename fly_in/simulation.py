import tkinter as tk
from collections import Counter
from graph import Graph
from connection import Connection
from hub import Hub
from drone import Drone
from typing import Optional
import sys

try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    from matplotlib.lines import Line2D
    from matplotlib.offsetbox import OffsetImage, AnnotationBbox
    from matplotlib.text import Text
    from matplotlib.collections import PathCollection
    from matplotlib.backend_bases import MouseEvent
    import matplotlib.image as mpimg
    from PIL import Image, ImageTk
    import numpy as np
except ImportError:
    print("A dependency is missing.\nRun:")
    print("make install")
    sys.exit(1)


class Simulation:
    """Graphical simulation of drones moving across a network.

    This class handles:
        - Rendering of hubs and connections
        - Animation of drone movements over time
        - User interactions (click, navigation, play/pause)

    Attributes:
        connections (dict[str, Connection]): All connections in the graph.
        drones (list[Drone]): List of drones in the simulation.
        hubs (dict[str, Hub]): All hubs in the graph.
        connections_used (list[Connection | Hub]): Connections used during
        simulation.

        turn_total (int): Total number of turns in the simulation.
        current_turn (int): Current turn displayed.

        is_playing (bool): Whether the animation is running.
    """

    def __init__(self, graph: Graph) -> None:
        """Initialize the simulation from a graph.

        Args:
            graph (Graph): Graph containing hubs, connections, and drones.
        """
        self.connections: dict[str, Connection] = graph.connections
        self.drones: list[Drone] = [d for d in graph.drones.values()]
        self.start_name: str = ''
        self.end_name: str = ''
        self.hubs: dict[str, Hub] = graph.hubs
        self.connections_used: list[Connection | Hub] = []

        self.turn_total: int = 0
        self.current_turn: int = 0
        self.turn_entry: tk.Entry
        self.drone_scatter: Optional[PathCollection] = None
        self.drone_nbr_labels: list[Text] = []
        self.is_playing: bool = False
        self.after_id: str = ""
        self.selection: Optional[PathCollection] = None
        self.fig = Figure(figsize=(6, 6))
        self.root = tk.Tk()
        self.img = mpimg.imread('assets/drone.png')
        self.ax = self.fig.add_subplot(111)

    def _draw_map(self) -> None:
        """Draw hubs and connections on the matplotlib canvas."""
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
            self.ax.text(x, y - 0.30, hub_id, fontsize=7, ha='center')

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
                x_h: float = (hub_a.coord[0] + hub_b.coord[0]) / 2
                y_h: float = (hub_a.coord[1] + hub_b.coord[1]) / 2
                self.ax.text(x_h, y_h - 0.15, co_id,
                             fontsize=8, ha='center')

        self.ax.set_axis_off()
        x_max: Hub = max(self.hubs.values(), key=lambda h: h.coord[0])
        y_max: Hub = max(self.hubs.values(), key=lambda h: h.coord[1])
        x_min: Hub = min(self.hubs.values(), key=lambda h: h.coord[0])
        y_min: Hub = min(self.hubs.values(), key=lambda h: h.coord[1])
        self.ax.set_xlim(x_min.coord[0]-0.5, x_max.coord[0] + 0.5)
        self.ax.set_ylim(y_min.coord[1]-0.5, y_max.coord[1] + 0.5)
        self.fig.subplots_adjust(left=0.05, bottom=0.15, right=0.95, top=0.95)

    def _add_caption(self) -> None:
        """Add a legend describing hubs and connection types."""
        legend_elements: list[Line2D] = [
            Line2D([0], [0], marker='o', color='w', label='Normal Zone',
                   markerfacecolor='gray', markersize=10),
            Line2D([0], [0], marker='s', color='w', label='Priority Zone',
                   markerfacecolor='gray', markersize=10),
            Line2D([0], [0], marker='^', color='w', label='Restricted Zone',
                   markerfacecolor='gray', markersize=10),
            Line2D([0], [0], marker='X', color='w', label='Blocked Zone',
                   markerfacecolor='gray', markersize=10),
            Line2D([0], [0], color='gray', linestyle='-', linewidth=1,
                   label='Standard Connection'),
            Line2D([0], [0], color='gray', linestyle=':', linewidth=2,
                   label='Connection occupied one turn during transit'),
        ]

        self.ax.legend(
            handles=legend_elements,
            loc='upper center',
            bbox_to_anchor=(0.5, -0.05),
            ncol=3,
            fontsize=8,
            frameon=False)

    def _update_drones(self) -> None:
        """Update drone positions for the current turn.

        This method:
            - Computes drone coordinates
            - Updates scatter plot positions
            - Displays drone icons and counts at each position
            - Refreshes the canvas
        """
        imagebox = OffsetImage(self.img, zoom=0.04)
        for txt in self.drone_nbr_labels:
            txt.remove()
        self.drone_nbr_labels.clear()
        for artist in self.ax.artists:
            if isinstance(artist, AnnotationBbox):
                artist.remove()

        x_s: list[int | float] = []
        y_s: list[int | float] = []
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
            self.drone_scatter = self.ax.scatter(
                x_s, y_s,
                s=400,
                alpha=0,
                picker=True,
                label='_nolegend_',
                zorder=4)
        else:
            self.drone_scatter.set_offsets(np.c_[x_s, y_s])
        positions: list[tuple[int | float, int | float]] = list(zip(x_s, y_s))
        count: Counter[tuple[int | float, int | float]] = Counter(positions)
        already_done = []
        for (x, y), total in count.items():
            if (x, y) in already_done:
                continue
            ab = AnnotationBbox(imagebox, (x, y), frameon=False)
            ab.set_picker(True)
            self.ax.add_artist(ab)
            t: Text = self.ax.text(x, y, str(total), color='white',
                                   va='center', ha='center', zorder=7)
            self.drone_nbr_labels.append(t)
            already_done.append((x, y))
        self.ax.set_title(f"Turn: {self.current_turn}")
        self.canvas.draw_idle()

    def _remove_selection(self) -> None:
        """Remove the current selection highlight from the plot.

        Also resets the information label.
        """
        if self.selection is not None:
            self.selection.remove()
            self.selection = None
            self.info_label.config(
                text="Clic on drones representation to see drones details",
                fg="#050505"
            )
            if self.canvas:
                self.canvas.draw_idle()

    def play_pause(self) -> None:
        """Toggle the simulation animation state.

        Starts or pauses the drone animation.
        """
        self._remove_selection()
        if self.is_playing:
            self.is_playing = False
            if self.after_id:
                self.root.after_cancel(self.after_id)
        else:
            self.is_playing = True
            self._run_drones_animation()

    def _run_drones_animation(self) -> None:
        """Run the animation loop for drone movements."""
        self._remove_selection()
        if self.is_playing and self.current_turn < self.turn_total:
            self._next_turn()
            self.after_id = self.root.after(500, self._run_drones_animation)

    def _prev_turn(self) -> None:
        """Go back one turn in the simulation."""
        self._remove_selection()
        if self.current_turn > 0:
            self.current_turn -= 1
            self._update_drones()

    def _next_turn(self) -> None:
        """Advance to the next turn in the simulation."""
        self._remove_selection()
        if self.current_turn < self.turn_total:
            self.current_turn += 1
            self._update_drones()

    def _reset_simulation(self) -> None:
        """Reset the simulation to the initial state (turn 0)."""
        self._remove_selection()
        self.current_turn = 0
        self._update_drones()

    def _on_click(self, event: MouseEvent) -> None:
        """Handle click events on the plot.

        If a drone is clicked:
            - Displays drone IDs at that position
            - Highlights the selected position

        Otherwise:
            - Displays a message indicating no drones are present

        Args:
            event (MouseEvent): Matplotlib mouse event.
        """
        self._remove_selection()
        if event.xdata is None or event.ydata is None:
            return
        self._remove_selection()
        if self.drone_scatter is None:
            return
        cont, ind = self.drone_scatter.contains(event)
        if cont:
            drones_i = ind['ind']
            drones: list[str] = []
            for i in drones_i:
                drones.append(self.drones[i].id)
                state = self.drones[i].state[self.current_turn]
                connection: bool = any(
                    state == c.id for c in self.connections_used)
            self.info_label.config(
                text=f"Drones on this position: {', '.join(drones)}",
                fg="#050505"
            )
            if not connection:
                self.selection = self.ax.scatter(
                    [round(event.xdata)], [round(event.ydata)],
                    s=300,
                    facecolors='none',
                    edgecolors='red',
                    linewidths=2,
                    zorder=10
                    )
            else:
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
        """Jump to a specific turn entered by the user.

        Invalid input is highlighted in red.
        """
        value = self.turn_entry.get()
        if not value.isdigit() or int(value) > self.turn_total:
            self.turn_entry.config(bg="red")
            self.turn_entry.after(1000,
                                  lambda: self.turn_entry.config(bg="#FFFFFF"))
            return
        self._remove_selection()
        self.current_turn = int(value)
        self.turn_entry.config(bg="#FFFFFF")
        self._update_drones()

    def _on_click_wrapper(self, event: object) -> None:
        """Wrapper to ensure the event is a valid MouseEvent.

        Args:
            event (object): Event triggered by matplotlib.
        """
        if isinstance(event, MouseEvent):
            self._on_click(event)

    def interface_control(self) -> None:
        """Initialize and launch the graphical user interface.

        This method sets up:
            - The matplotlib canvas
            - Control buttons (play, next, previous, reset)
            - Turn navigation input
            - Click interaction handling

        Starts the Tkinter main loop.
        """
        self.root.title("Fly-in Simulation")

        # Graphique part
        self.canvas = FigureCanvasTkAgg(
            self.fig,
            master=self.root)
        self.fig.tight_layout()
        self._draw_map()
        self._add_caption()
        self._update_drones()
        widget = self.canvas.get_tk_widget()
        widget.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1,
            pady=0,
        )

        # Informations on click
        img = Image.open('assets/drone.png').resize((25, 25))
        icon = ImageTk.PhotoImage(img)
        self.info_label: tk.Label = tk.Label(
            self.root,
            text='Click on drones representation to see details',
            image=icon,  # type: ignore[arg-type]
            compound='left',
            fg="#000000",
            padx=10,
            )
        setattr(self.info_label, "image", icon)
        self.info_label.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.fig.canvas.mpl_connect('button_press_event',
                                    self._on_click_wrapper)

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
