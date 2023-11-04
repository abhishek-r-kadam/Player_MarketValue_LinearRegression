import pandas as pd
import numpy as np
import config
import pickle



class MarketValuePredict():
    def __init__(self,club, position, page_views, fpl_value, fpl_sel, fpl_points, region, new_foreign, age_cat, big_club, new_signing):
        self.club = club
        self.position = position
        self.page_views = page_views
        self.fpl_value = fpl_value
        self.fpl_sel = fpl_sel
        self.fpl_points = fpl_points
        self.region = region
        self.new_foreign = new_foreign
        self.age_cat = age_cat
        self.big_club = big_club
        self.new_signing = new_signing
        
    def load_model(self):
        
        with open(config.MODEL_PATH,"rb") as f:
            self.model = pickle.load(f)
        
        
    def predict_mv(self):
        
        self.load_model()
        
        input_data = [self.club, self.position, self.page_views, self.fpl_value, self.fpl_sel, self.fpl_points, self.region, self.new_foreign, self.age_cat, self.big_club, self.new_signing] 
        
        prediction = self.model.predict([input_data])[0]
        
        return prediction