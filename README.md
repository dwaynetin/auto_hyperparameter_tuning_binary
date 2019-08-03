# auto_hyperparameter_tuning_binary

Dwayne's personal journey to creating an auto-tuning hyper parameter binary classifier identifier...

Or in non-nerd speak...

What is the best guesser (model) that will help me know if:
- Win or not
- Win a date based on guys vital statistics versus woman's vital statistics
- Identify if your expected baby is a boy or girl based on your demographics


This is my personal journey to automating classifiers, and creating models that are self-tuning.

Code is still in progress.

My sample data is 700 games from Dota 2 7.19 patch.
"Based on the heroes that both teams picked, will radiant or dire win?"

To self, please run this so that the env will be deployed quickly:
virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt 

To run this code:
python src\main.py <sample dataset> <sample configuration> <name of the result column>
python src\main.py datasets\dota\games_718.csv datasets\dota\classifiers.conf Table1.WinningTeam