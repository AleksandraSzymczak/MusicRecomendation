def reasult_euclidean_distances(context,data_for,a):
    import pandas as pd
    import numpy as np
    from sklearn.metrics.pairwise import euclidean_distances
    import Data_prep

    #context,data_for = Data_prep.Data_prep()
    file = ('data/Music_InCarMusic/Data_InCarMusic.xlsx')
    MusicTrack = pd.read_excel(file, sheet_name=2,
                               names=["id", "album", "artist", "title", "mp3url", "description", "imageurl",
                                      "category_id"], index_col=0)
    #if a == 1:
        #context_1 = context.drop(['sport driving'],axis=1)
    context_1 = context[a]
    array = context_1.to_numpy()

    points1 = np.asarray(array)
    point2 =[]
    temp = []
    for item in range(0,np.size(a)):
        temp.append(5)
    point2.append(temp)
    test = euclidean_distances(points1,point2)

    df = pd.DataFrame(test,columns=['Distance'])
    data_for['Distance'] = df
    data_for = pd.merge(data_for, MusicTrack, how='left', left_on=['ItemID'], right_on=['id'])
    data_for = data_for.sort_values(by=['Distance','Rating'],ascending=[True,False])
    data = data_for.to_numpy()
    return data
def reasult_Manhattan_distance(context,data_for,a):
    import pandas as pd
    import numpy as np
    from sklearn.metrics.pairwise import manhattan_distances
    from itertools import count
    import Data_prep

    #context,data_for = Data_prep.Data_prep()
    file = ('data/Music_InCarMusic/Data_InCarMusic.xlsx')
    MusicTrack = pd.read_excel(file, sheet_name=2,
                               names=["id", "album", "artist", "title", "mp3url", "description", "imageurl",
                                      "category_id"], index_col=0)
    #if a == 1:
        #context_1 = context.drop(['sport driving'],axis=1)
    context_1 = context[a]
    array = context_1.to_numpy()

    points1 = np.asarray(array)
    point2 = []
    temp = []
    for item in range(0, np.size(a)):
        temp.append(5)
    point2.append(temp)
    test = manhattan_distances(points1, point2)

    df = pd.DataFrame(test, columns=['Distance'])
    data_for['Distance'] = df
    data_for = pd.merge(data_for, MusicTrack, how='left', left_on=['ItemID'], right_on=['id'])
    data_for = data_for.sort_values(by=['Distance', 'Rating'], ascending=[True, False])
    data = data_for.to_numpy()
    return data
