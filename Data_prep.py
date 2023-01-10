def Data_prep():
    import zipfile
    with zipfile.ZipFile('Music_InCarMusic.zip','r') as zip_ref:
        zip_ref.extractall('data')
    import numpy as np
    import pandas as pd
    file =('data/Music_InCarMusic/Data_InCarMusic.xlsx')
    newData = pd.read_excel(file)
    ContextualRating = pd.read_excel(file, sheet_name = 0, names=['UserID', 'ItemID','Rating','DrivingStyle','landscape',
                                                                  'mood','naturalphenomena','RoadType','sleepiness',
                                                                  'trafficConditions','weather'])
    #ContextFactor = pd.read_excel(file, sheet_name = 1, index_col = 0)
    #
    #MusicCategory = pd.read_excel(file, sheet_name = 3, names=['CategoryId', 'MusicCategory'],header = None,index_col = 0)

    #data for post-filtering 2D recommendation
    ContextualRating_overallrating = ContextualRating
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["DrivingStyle"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["mood"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["landscape"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["naturalphenomena"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["RoadType"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["sleepiness"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["trafficConditions"].isna()]
    ContextualRating_overallrating = ContextualRating_overallrating[ContextualRating_overallrating["weather"].isna()]

    #data for filtering
    ContextualRating_context = ContextualRating[~ContextualRating.index.isin(ContextualRating_overallrating.index)]

    # preparing categories
    # Driving Style
    DrivingStyle = ContextualRating_context[['UserID','ItemID','Rating','DrivingStyle']]
    # landscape
    landscape = ContextualRating_context[['UserID','ItemID','Rating','landscape']]
    # mood
    mood = ContextualRating_context[['UserID','ItemID','Rating','mood']]
    # naturalphenomena
    naturalphenomena  = ContextualRating_context[['UserID','ItemID','Rating','naturalphenomena']]
    # RoadType
    RoadType = ContextualRating_context[['UserID','ItemID','Rating','RoadType']]
    # sleepiness
    sleepiness  = ContextualRating_context[['UserID','ItemID','Rating','sleepiness']]
    # trafficConditions
    trafficConditions  = ContextualRating_context[['UserID','ItemID','Rating','trafficConditions']]
    # weather
    weather = ContextualRating_context[['UserID','ItemID','Rating','weather']]

    # modifing ratings
    DrivingStyle_clean = DrivingStyle.pivot_table(index = ['UserID','ItemID'],columns = 'DrivingStyle', values = 'Rating',aggfunc=max)
    landscape_clean = landscape.pivot_table(index = ['UserID','ItemID'],columns = 'landscape', values = 'Rating',aggfunc=max)
    mood_clean = mood.pivot_table(index = ['UserID','ItemID'],columns = 'mood', values = 'Rating',aggfunc=max)
    naturalphenomena_clean = naturalphenomena.pivot_table(index = ['UserID','ItemID'],columns = 'naturalphenomena', values = 'Rating',aggfunc=max)
    RoadType_clean = RoadType.pivot_table(index = ['UserID','ItemID'],columns = 'RoadType', values = 'Rating',aggfunc=max)
    sleepiness_clean = sleepiness.pivot_table(index = ['UserID','ItemID'],columns = 'sleepiness', values = 'Rating',aggfunc=max)
    trafficConditions_clean = trafficConditions.pivot_table(index = ['UserID','ItemID'],columns = 'trafficConditions', values = 'Rating',aggfunc=max)
    weather_clean = weather.pivot_table(index = ['UserID','ItemID'],columns = 'weather', values = 'Rating',aggfunc=max)

    ############################################
    # megrging data
    # 1.
    merged_data = pd.merge(landscape_clean, DrivingStyle_clean,how='left', left_index=True, right_index=True, sort=True)
    # 2.
    merged_data = pd.merge(merged_data, mood_clean,how='left', left_index=True, right_index=True, sort=True)
    # 3.
    merged_data = pd.merge(merged_data, naturalphenomena_clean,how='left', left_index=True, right_index=True, sort=True)
    # 5.
    merged_data = pd.merge(merged_data, RoadType_clean,how='left', left_index=True, right_index=True, sort=True)
    # 6.
    merged_data = pd.merge(merged_data, sleepiness_clean,how='left', left_index=True, right_index=True, sort=True)
    # 7.
    merged_data = pd.merge(merged_data, trafficConditions_clean,how='left', left_index=True, right_index=True, sort=True)
    # 8.
    merged_data = pd.merge(merged_data, weather_clean,how='left', left_index=True, right_index=True, sort=True)
    #merged_data = merged_data.reset_index()
    #content_table.append('UserID')
    #content_table.append('ItemID')

    #for col in merged_data.columns:
       # if col not in content_table:
            #merged_data = merged_data.drop(col,axis = 1)

    merged_data = merged_data.groupby('ItemID').agg('mean')

    ContextualRating_overallrating = ContextualRating_overallrating[['ItemID','Rating']]
    ContextualRating_overallrating = ContextualRating_overallrating.groupby('ItemID').agg('mean')
    ContextualRating_overallrating = ContextualRating_overallrating.reset_index()
    data_for = merged_data
    data_for = pd.merge(data_for,ContextualRating_overallrating,on = 'ItemID',how='left')
    data_for = data_for.fillna(0)
    data_for = data_for.astype("int")
    #preparing data
    merged_data = merged_data.reset_index()
    merged_data = merged_data.fillna(0)
    merged_data = merged_data.astype("int")

    context = merged_data.drop(columns ="ItemID",axis = 0)
    return context,data_for