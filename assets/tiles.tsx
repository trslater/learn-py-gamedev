<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.5" tiledversion="1.7.2" name="Tiles" tilewidth="16" tileheight="32" tilecount="7" columns="0">
 <grid orientation="orthogonal" width="1" height="1"/>
 <tile id="3">
  <image width="16" height="16" source="grass.png"/>
 </tile>
 <tile id="4">
  <image width="16" height="8" source="wall.png"/>
 </tile>
 <tile id="5">
  <image width="8" height="8" source="boundary.png"/>
 </tile>
 <tile id="6">
  <image width="16" height="8" source="stairs.png"/>
 </tile>
 <tile id="7">
  <image width="8" height="8" source="path.png"/>
 </tile>
 <tile id="8">
  <image width="16" height="32" source="crate.png"/>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="8.125" width="16" height="23.875"/>
   <object id="2" x="0" y="10" width="16" height="22"/>
  </objectgroup>
 </tile>
 <tile id="9">
  <image width="16" height="32" source="player.png"/>
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="25.875" width="15.625" height="5.75"/>
  </objectgroup>
 </tile>
</tileset>
