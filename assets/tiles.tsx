<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.5" tiledversion="1.7.2" name="Tiles" tilewidth="16" tileheight="32" tilecount="5" columns="0">
 <grid orientation="orthogonal" width="1" height="1"/>
 <tile id="3">
  <image width="16" height="16" source="grass.png"/>
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
 <tile id="11">
  <image width="16" height="16" source="wall.png"/>
 </tile>
 <tile id="12">
  <image width="16" height="32" source="door.png"/>
 </tile>
</tileset>
