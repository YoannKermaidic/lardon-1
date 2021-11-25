import json as json

class params:
    def __init__(self):
       self.ped_amp_sig_fst = 1          # default amplitude trigger threshold for 1st pass signal mask - in RMS 
       self.ped_amp_sig_oth = 1          # default amplitude trigger threshold for other pass signal mask - in RMS 
       self.hit_amp_sig     = [3,6,2]    # default amplitude trigger threshold for hit search - in RMS
       self.hit_dt_min      = [10,10,10] # minimal delta t for hit search - in bins

    def read(self,config="1"):
       try:
          with open('settings/analysis_parameters.json','r') as f:
             data = json.load(f)
             if(config not in data):
                print("WARNING: Thresholds configuration ",config," not found.")
                print("         Default thresholds will be applied.")
             else:
                self.ped_amp_sig_fst = data[config]['pedestal']['first_pass_thrs']
                self.ped_amp_sig_oth = data[config]['pedestal']['other_pass_thrs']
                self.hit_amp_sig     = data[config]['hit_finder']['amp_sig_thrs']
                self.hit_dt_min      = data[config]['hit_finder']['dt_min']
       except:
            print("WARNING: Thresholds setting file (./settings/analysis_parameters.json) not found.")
            print("         Default thresholds will be applied.")

    def set_fst_thrs(self,value):
      self.amp_sig_fst = values 

    def set_oth_thrs(self,value):
      self.amp_sig_oth = values 

    def get_fst_thrs(self):
      return self.amp_sig_fst 

    def get_oth_thrs(self):
      return self.amp_oth_fst 

    def set_amp_sig_thrs(self,values):
      self.amp_sig = values

    def set_dt_min_thrs(self,values):
      self.dt_min = values
    
    def get_amp_sig_thrs(self):
      return self.amp_sig  
    
    def get_dt_min_thrs(self):
      return self.dt_min


