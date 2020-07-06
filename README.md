# addons

Some extra assets for OpenSpace


Included are:

### The Trappist Planetary system

<img src="trappist/screenshots/trappistsystem.jpg" width="40%">

### A model (obj) for the tesla roadster

<img src="teslaroadster/screenshots/teslaroadster.jpg" width="40%">

### A script to import galaxy coordinates from the Millennium Simulation results

<img src="millennium-simulation/screenshots/millenniumsimulation.jpg" width="40%">

### An asset importer for the SgrA* system

<img src="SgrA-star/screenshots/sgrastar.jpg" width="40%">

## Instructions

I put the entire `addons` folder directly under the `data/assets` directory. Then in your `.scene` file, just include the lines:

```
asset.request('addons/millennium-simulation/millennium')
asset.request('addons/SgrA-star/SgrA-star-system')
asset.request('addons/trappist/trappist-system')
asset.request('addons/teslaroadster/tesla_roadster.asset')
```

for each asset you would like to incorporate.
