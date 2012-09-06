#!/usr/bin/python
import simplekml
import simplejson
f=open("combined.json")
d=simplejson.load(f)
import simplejson
f=open("planb_data.json")
d=simplejson.load(f)
fg=open("plankgeo_data.json")
dg=simplejson.load(fg)
geo={}
for g in dg:
  geo[g['id']] = g
stat=[]
for s in d:
  if s['IBNR'] < 8100000 and s['IBNR'] > 7999999:
    s['lon']=geo[s['b1_id']]['lon']
    s['lat']=geo[s['b1_id']]['lat']
    stat.append(s)
kml=simplekml.Kml()
kml=simplekml.Kml()
for s in stat:
 kml.newpoint(name=
 s['name']+" ("+(", ".join(s['synonyms']))+")",
 coords=[(s['lon'],s['lat'])])
kml.save('stations.kml')
