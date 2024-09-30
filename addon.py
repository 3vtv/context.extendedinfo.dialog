# -*- coding: utf-8 -*-
import xbmc

def main():
    if xbmc.getCondVisibility('String.IsEqual(ListItem.DBType,movie) + !String.IsEmpty(ListItem.DBID)'):
        xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedinfo,dbid=%s,id=%s)' % (xbmc.getInfoLabel('ListItem.DBID'),xbmc.getInfoLabel('ListItem.IMDBNumber')))

    elif xbmc.getCondVisibility('String.IsEqual(ListItem.DBType,movie)'):
        xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedinfo,name=\'"%s"\',name=\'"%s"\',year=%s)' % (xbmc.getInfoLabel('ListItem.Title'),xbmc.getInfoLabel('OriginalTitle'),xbmc.getInfoLabel('ListItem.Year')))

    elif xbmc.getCondVisibility('String.IsEqual(ListItem.DBType,tvshow)'):
        xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedtvinfo,name=\'"%s"\',name=\'"%s"\',year=%s)' % (xbmc.getInfoLabel('ListItem.TVShowTitle'),xbmc.getInfoLabel('ListItem.OriginalTitle'),xbmc.getInfoLabel('ListItem.Year')))

    elif xbmc.getCondVisibility('String.IsEqual(ListItem.DBType,season)'):
        xbmc.executebuiltin('RunScript(script.extendedinfo,info=seasoninfo,dbid=%s,tvshow=\'"%s"\',season=%s)' % (xbmc.getInfoLabel('ListItem.DBID'),xbmc.getInfoLabel('ListItem.TVShowTitle'),xbmc.getInfoLabel('ListItem.Season')))

    elif xbmc.getCondVisibility('String.IsEqual(ListItem.DBType,episode)'):
        xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedepisodeinfo,dbid=%s,tvshow=\'"%s"\',season=%s,episode=%s)' % (xbmc.getInfoLabel('ListItem.DBID'),xbmc.getInfoLabel('ListItem.TVShowTitle'),xbmc.getInfoLabel('ListItem.Season'),xbmc.getInfoLabel('ListItem.Episode')))

    elif xbmc.getCondVisibility('String.IsEqual(ListItem.DBType,actor) | String.IsEqual(ListItem.DBType,director)'):
        xbmc.executebuiltin('RunScript(script.extendedinfo,info=extendedactorinfo,name=\'"%s"\')' % xbmc.getInfoLabel('ListItem.Label'))

if __name__ == '__main__':
    main()
