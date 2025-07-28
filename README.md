# Football-predicition-model
This is a summertime project that aims to predict the result of matches between teams in the top 5 European leagues in football

xG = expected goals
xGA = expected goals allowed

### Initial Plan
- Create a prediction model using a Poisson simulation based on xG values. Each team would be assigned a lambda value, and the model would estimate the number of goals each team scores in each simulation, assigning wins, draws, and losses to each team based on the simulation results. The respective lambda values were to be calculated based on xG that the team has generated at home, away, over the past 6 games (form), and head-to-head with the opposition. The model also looks at xGA, to increase or decrease the xG of the opposing team.
- To scrape this data, you need to build a URL for each team. That requires an FBref ID and slug, but there are no available files/overview containing this information. 
- Idea: Use Gemini AI to interpret user input and dynamically fetch the correct FBref team ID and slug.
- Allow user input with minor spelling errors, handled by the AI.
- Support multiple leagues (Premier League, La Liga, Serie A, Bundesliga)
- Create GUI using AnimationWindow from TDT4102, combining C++ and Python

### Challenges Encountered
- FBref URLs are structured using team-specific IDs and slugs, which are not easy to generate without accurate data.
- Gemini AI produced hallucinations when asked to provide precise FBref IDs from names, making it unreliable for URL construction.
- 
### Revised Plan
- Limit the model to the Premier League for now.
- Pre-scrape all team IDs and slugs and store them in a local CSV file or a simple dictionary in one of the py files.
- Use AI only for fuzzy matching/correcting user input, not for fetching IDs.

### Future Considerations
- Incorporate an OpenAI API instead, and hope that one is more accurate and less prone to hallucinations. Drawback: Costs money

### Comments
-The model is mostly complete, I just haven't made my mind up on which way to go. The GUI and AI bit is not finished, but I won't upload files until the project is done since I don't know how to use GitHub.
