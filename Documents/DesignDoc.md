Project Idea
============
The idea for this project is to create a sandbox in the cloud where I can send a file. The OS will then run various tests on this file and send the results via telegram to me.

Research
--------------------------------------

- Which OS?
  - There are many types of systems out there, I prefer Linux due to its accessablitiy and ease of use, I might run into problems if I want to use windows specific libraries though.
  - I considered useing Rocky 9 because I love it for some reason but I'll start out using a simple ubuntu server, due to how widley known and used it is.
- Language?
  - Python: I know it well and telegram intergration is easy. 
- Cloud platform?
  - Digital Ocean: I have 200$ free from Github education but the problem is if I turn a cloud server off it keeps eating from the money so after a while it can get very expensive.
  - AWS: Currently learning.
  - Azure: I was dumb and left a vm on for months so all my money is used up.
- Tests to run?
  - Security scans
  - File integrity checks
  - Code analyse
  - Performace tests
  - Compatabitiy checks
  - Content analsye op patterns, keyworks, attributes
  - Complience check (GDPR, HIPAA,..)
  - Custom tests
  - EXPERIMENT: Machine leaning models -> train a model to detect anomolies 
- ...

Tests in Python
---------------------------------------
1. Clamav: antivirus scanning https://docs.clamav.net/
2. Pytestseract: OCR based security checks (extract text, logos, and other identifiable objects from images) 
3. Checksums maken en vergelijken voor en na processing - haslib
4. Pylint, flake8 or bandit for code analyse.
5. Time, timeit for execution time and performace can be done with psutil.
6. Conditonal statements or compatability libraries te handle different information.
7. Regular expressions to analyze for specific patterns,... - re can be used
8. compience check for GDPR

For each test I can write scripts and organize them into framworks like unittest, pytest or nose2.

Framework choice
---------------------------------------
Pytest is my first choice due to its east of use, powerful features and its integration into the Python ecosystem that I'll be using]


Tasks
---------------------------------------
1. Develop the clamav tests in an ubuntu vm, because its mafe for linux not windows
2. check for other tests
3. ...
4. last step will be deploying to cloud

