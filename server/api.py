import sqlalchemy
from fastapi import FastAPI
from sqlalchemy import select, func
from models import Artists,Albums,Tracks
from database import session

app = FastAPI()


#result = session.query(Artists).filter_by(name = 'Calexico').first()

#la route 
@app.get("/read_artist/")
async def read_artist (artist_name: str):

    artist_name = "%" + artist_name + "%"
 # requete pour afficher les artistes comprenant le nom donné,
    artist_res = session.query(Artists).filter(func.lower(Artists.name).like(artist_name.lower())).all()
    return {"Artist": artist_res}


# La route
@app.get("/read_albums/{album_name}")
async def read_albums(artist_id: int):
    #afficher les noms d’albums correspondants
    statement = select(Albums).join(Albums.artists).where(Artists.artistId == artist_id)
    album_res = tuple(session.scalars(statement).all())

    return {"Albums": album_res}
  #La route
@app.get("/read_tracks/{tracks_name}")
async def read_tracks(album_id: int):
  #afficher les noms de pistes correspondants
    statement = select(Tracks).join(Tracks.albums).where(Albums.albumId == album_id)
    tracks_res = tuple(session.scalars(statement).all())

    return {"Tracks ": tracks_res}







