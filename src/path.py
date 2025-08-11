import os

#Find absolute path for current py-file
abs_path_current_file=os.path.abspath(__file__)

#Get the root directory
root_dir = os.path.dirname(os.path.dirname(abs_path_current_file))

#Get project directory
project_dir=os.path.dirname(os.path.dirname(root_dir))

#DATA
#Path to data directory
data_dir=os.path.join(root_dir, "data")

#Specifie files
csv_file=os.path.join(data_dir, "dirty_video_games_data.csv")