import pandas as pd
import numpy as np
import geopandas as gpd
import rasterio
import shapely
import pyproj
import xarray as xr
import fiona
import pyogrio
import matplotlib as plt
import geodatasets
import folium
from shapely.geometry import Polygon
from shapely.geometry import box
import matplotlib.cm as cm
import matplotlib.colors as colors
import branca.colormap as bc
import ast

grid_overall_biodiversity = gpd.read_file('overall_species_grid_005_pixels.gpkg').to_crs(epsg='4326')

#Explode species lists
species_long = grid_overall_biodiversity[["grid", "species"]].explode("species")
#Remove empty values
species_long = species_long.dropna(subset=["species"])

#Presence-abscence matrix
presence_abscence = pd.crosstab(species_long["grid"], species_long["species"])

# Convert counts to presence/absence
presence_abscence = (presence_abscence > 0).astype(int)
presence_abscence.to_csv('presence_abscence_matrix.csv')
