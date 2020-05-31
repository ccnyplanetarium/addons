# Art for the constellations.

All 88 constellations are included as image textures.

<img src="screenshots/twohemispheres.jpg" width="60%">

This asset reads a csv file to determine the texture and position for each constellation individually.

<img src="screenshots/constellation-art-sample-2.jpg" width="60%">

<img src="screenshots/cepheus.jpg" width="60%">

By default they are off, but can be turned on using the gui or Lua commands.

To turn them all on or off:

```
openspace.setPropertyValue("{ConstellationArtImage}.Renderable.Enabled",true)
openspace.setPropertyValue("{ConstellationArtImage}.Renderable.Enabled",false)
```

The are also tagged to some degree, for example, the zodiac can be added alone.

```
openspace.setPropertyValue("{zodiac}.Renderable.Enabled",true)
```
<img src="screenshots/orion_gemini.jpg" width="60%">
<img src="screenshots/virgo.jpg" width="60%">

<video controls width="512">

    <source src="screenshots/rotate.mp4"
            type="video/mp4">

    Sorry, your browser doesn't support embedded videos.
</video>

TODO:

General improvements of drawings.
