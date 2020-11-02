import geopandas as gpd

def generator(model_codes):
    usa = gpd.read_file('../zipcodes.shp')
    urls = []
    #only focus in NY right now
    #for z in usa['ZIP_CODE']:
    count = 0
    for model in model_codes:
        for z in usa[usa['STATE'] == 'NY']['ZIP_CODE']:
            #urls.append('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip={}&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=10&entitySelectingHelper.selectedEntity2={}&sortType=DEAL_SCORE&entitySelectingHelper.selectedEntity={}'.format(z, model, model))
            urls.append('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=10001&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=10&entitySelectingHelper.selectedEntity2=c21411&sortType=DEAL_SCORE&entitySelectingHelper.selectedEntity=c21411#listing=281375564')
            #print('https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip={}&showNegotiable=true&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=10&entitySelectingHelper.selectedEntity2={}&sortType=DEAL_SCORE&entitySelectingHelper.selectedEntity={}'.format(z, model, model))
            count += 1
            if count == 5:
                break
    print("All URLs Generated!")
    return urls