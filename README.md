Practise with autotests

## prepare venv  
python -m venv .venv  
.venv/Scripts/activate  
pip install -r requirements.txt  

## start tests  
python -m pytest  

## launch with different browsers  
pytest --browser=chrome   
pytest --browser=firefox   