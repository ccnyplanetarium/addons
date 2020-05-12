# constellation art

Art for the constellations.

This asset reads a csv file to determine the texture and position for each constellation individually.

<img src="screenshots/constellation-art-sample-2.jpg" width="60%">

By default they are off, but can be turned on using the gui or Lua commands.

<img src="screenshots/constellation-art-sample-3.jpg" width="60%">

To turn them all on or off:

```
openspace.setPropertyValue("{ConstellationArtImage}.Renderable.Enabled",true)
openspace.setPropertyValue("{ConstellationArtImage}.Renderable.Enabled",false)
```

The are also tagged to some degree, for example, the zodiac can be added alone.

```
openspace.setPropertyValue("{zodiac}.Renderable.Enabled",true)
```
TODO:

* Add more! Only the zodiac and Orion have been created so far
