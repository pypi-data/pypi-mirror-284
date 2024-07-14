# Code Arena Python SDK

```python
import codearena

# Initilize CodeArena Client
client = CodeArena(url_root='https://codellm.club', token='<codellm.club token>')

# Get Problem List
problems = client.get_problems()

# Get Problem Details
problem = client.get_problem(problem_id='<problem_id>')

# Get Submission List
submissions = client.get_submissions()

# Get Submission Details
submission = client.get_submission(<submission_id>)

# Submit Solution
submission_result = client.post_submission(problem_code="<problem_id>", language="<language>", source="<source_code>")
```

More details can be found [Here](https://codellm.club/about/). Should you have any problem with this library, feel free to email [Mingzhe Du](mailto:mingzhe@nus.edu.sg).