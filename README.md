# 5102_innovation_challenge
### File Description
1. get_location.py
   - Use LLM to extract the location from user's input.
   - return search_location
2. get_real_time_data.py
   - Get real-time traffic data
   - Using Lat&lng to get place name by Google Map and split the first part of place（****改完了！！！！****） 
   - return camera_data, camera_location_list, camera_location_split
3. predict_imgae.py
   - match the location（****改完了！！！！****） 
   - get image link
   - predict imgae
   - return string

This is a demo for OurApp

Please first create a conda environment using the following command
`conda create --name venv python=3.9.6` 

### 1. Install Flask Back End
Requirement: Please have Python3 installed.
1. `conda activate venv`
2. `cd backend`
3. `pip install -r requirements.txt` 
4. `python app.py`
The flask back end will be running on http://localhost:5000/

### 2. Install React Front End
Requirement: Please have npm and yarn installed.
1. open another separate terminal window
2. `conda activate venv`
2. `cd OurApp`
3. `rm -rf package-lock.json` 
4. `npm install react-scripts` 
5. `npm install`
6. `npm run start`
The front end will be running on http://localhost:3000/
or
1. `cd OurApp`
2. `yarn start`
3. The app will be running on http://localhost:3000/
