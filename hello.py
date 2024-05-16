print('Hello World')

#import py_eddy_tracker_sample

from py_eddy_tracker.data import get_demo_path
from py_eddy_tracker.observations.network import NetworkObservations
from py_eddy_tracker.observations.observation import EddiesObservations, Table
from py_eddy_tracker.observations.tracking import TrackEddiesObservations  

eddies_collections = EddiesObservations.load_file(get_demo_path("Cyclonic_20160515.nc"))
eddies_collections.field_table()

eddies_collections.amplitude

# To access only a specific part of the field
eddies_collections.amplitude[4:15]

eddies_collections.obs
