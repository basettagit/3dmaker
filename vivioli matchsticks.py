from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display

# Inizializza il display
display, start_display, add_menu, add_function_to_menu = init_display()

# Dimensioni della scatola esterna (cover)
outer_length = 56  # Lunghezza esterna
outer_width = 24   # Larghezza esterna
outer_height = 24  # Altezza esterna
wall_thickness = 2  # Spessore della parete

# Dimensioni del cassetto interno
drawer_length = outer_length - 2 * wall_thickness  # Lunghezza del cassetto
drawer_width = outer_width - 2 * wall_thickness    # Larghezza del cassetto
drawer_height = outer_height - wall_thickness      # Altezza del cassetto
drawer_wall_thickness = 1                          # Spessore del cassetto

# 1. Creare la scatola esterna (cover)
outer_box = BRepPrimAPI_MakeBox(gp_Pnt(0, 0, 0), outer_length, outer_width, outer_height).Shape()
inner_cut = BRepPrimAPI_MakeBox(
    gp_Pnt(wall_thickness, wall_thickness, wall_thickness),
    outer_length - wall_thickness,
    outer_width - wall_thickness,
    outer_height
).Shape()
cover = BRepAlgoAPI_Cut(outer_box, inner_cut).Shape()

# 2. Creare il cassetto interno (drawer)
drawer_outer = BRepPrimAPI_MakeBox(gp_Pnt(5, 5, 5), drawer_length, drawer_width, drawer_height).Shape()
drawer_inner_cut = BRepPrimAPI_MakeBox(
    gp_Pnt(5 + drawer_wall_thickness, 5 + drawer_wall_thickness, 5 + drawer_wall_thickness),
    drawer_length - drawer_wall_thickness,
    drawer_width - drawer_wall_thickness,
    drawer_height - drawer_wall_thickness
).Shape()
drawer = BRepAlgoAPI_Cut(drawer_outer, drawer_inner_cut).Shape()

# Aggiungi la scatola e il cassetto al display
display.DisplayShape(cover, update=True, color="red")  # Scatola esterna
display.DisplayShape(drawer, update=True, color="blue")  # Cassetto interno

# Avvia la visualizzazione
start_display()
